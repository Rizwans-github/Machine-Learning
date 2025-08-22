import streamlit as st
import pandas as pd
import pickle
import os

path = os.path.join(os.path.dirname(__file__), "final_model.sav")
model = pickle.load(open(path, "rb"))

st.title("House Price Prediction App")

st.subheader("Upload CSV for Prediction")
uploaded_file = st.file_uploader("Upload a CSV file with house data", type=["csv"])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
    st.write("Uploaded Data Preview:", input_df.head())

    predictions = model.predict(input_df)
    st.write("Predictions:", predictions)

st.subheader("Enter Key Features Manually")


GrLivArea = st.number_input("Above grade living area (sq ft):", min_value=300, max_value=6000, value=1500)
GarageCars = st.number_input("Garage capacity:", min_value=0, max_value=5, value=2)
TotalBsmtSF = st.number_input("Total Basement Area (sq ft):", min_value=0, max_value=3000, value=800)

#MSZoning = st.selectbox("Zoning Class:", ["RL", "RM", "FV", "RH", "C (all)"])
#Neighborhood = st.selectbox("Neighborhood:", ["CollgCr", "Veenker", "Crawfor", "NoRidge", "Mitchel", "Somerst", "Other"])
#HouseStyle = st.selectbox("House Style:", ["1Story", "2Story", "1.5Fin", "SLvl", "SFoyer", "Other"])
#SaleCondition = st.selectbox("Sale Condition:", ["Normal", "Abnorml", "Partial", "Family", "Alloca", "AdjLand"])


# MSZoning
zoning_options = {
    "big houses, large lots": "RL",
    "smaller lots, townhouses": "RM",
    "apartments, multi-family": "RH",
    "waterfront homes": "FV",
    "commercial area": "C (all)"
}
zoning_display = st.selectbox("Zoning Class:", list(zoning_options.keys()))
MSZoning = zoning_options[zoning_display]

# Neighborhood
neighborhood_options = {
    "College Creek area": "CollgCr",
    "Crawford area": "Crawfor",
    "Northridge": "NoRidge",
    "Mitchell": "Mitchel",
    "Somerest": "Somerst",
    "Veenker": "Veenker",
    "Other": "Other"
}
neighborhood_display = st.selectbox("Neighborhood:", list(neighborhood_options.keys()))
Neighborhood = neighborhood_options[neighborhood_display]

# House Style
housestyle_options = {
    "1 story house": "1Story",
    "2 story house": "2Story",
    "1.5 story finished": "1.5Fin",
    "split level": "SLvl",
    "split foyer": "SFoyer",
    "other style": "Other"
}
housestyle_display = st.selectbox("House Style:", list(housestyle_options.keys()))
HouseStyle = housestyle_options[housestyle_display]



if st.button("Predict from Manual Input"):
    preprocessor = model.named_steps['Preprocessing']
    cat_cols = preprocessor.transformers_[0][2]   
    num_cols = preprocessor.transformers_[1][2]   

    input_data = pd.DataFrame({col: [0] for col in num_cols})        
    for col in cat_cols:
        input_data[col] = "missing"                                  

    if "GrLivArea" in input_data.columns:
        input_data.at[0, "GrLivArea"] = GrLivArea
    if "GarageCars" in input_data.columns:
        input_data.at[0, "GarageCars"] = GarageCars
    if "TotalBsmtSF" in input_data.columns:
        input_data.at[0, "TotalBsmtSF"] = TotalBsmtSF
    if "MSZoning" in input_data.columns:
        input_data.at[0, "MSZoning"] = MSZoning
    if "Neighborhood" in input_data.columns:
        input_data.at[0, "Neighborhood"] = Neighborhood
    if "HouseStyle" in input_data.columns:
        input_data.at[0, "HouseStyle"] = HouseStyle

    prediction = model.predict(input_data)
    st.success(f"Predicted House Price: ${prediction[0]:,.2f}")


import matplotlib.pyplot as plt

st.subheader("Model Performance Comparison")

models = ['RandomForest', 'XGBoost', 'Final XGBoost']
cross_val_mae = [29219.75, 16545.21, 16525.77]
r2_scores = [0.548, 0.892, 0.892]

fig, ax = plt.subplots(1, 2, figsize=(10, 6))

# MAE
mae_bars = ax[0].bar(models, cross_val_mae, color=['orange', 'green', 'blue'])
ax[0].set_title("Cross-Validated MAE Comparison")
ax[0].set_ylabel("Mean Absolute Error")
for i in range(len(cross_val_mae)):
    ax[0].text(i, cross_val_mae[i], f'{cross_val_mae[i]:,.2f}', ha='center', va='bottom')

# R2
r2_bars = ax[1].bar(models, r2_scores, color=['orange', 'green', 'blue'])
ax[1].set_title("R2 Comparison")
ax[1].set_ylabel("R2 Score")
for i in range(len(r2_scores)):
    ax[1].text(i, r2_scores[i], f'{r2_scores[i]:.2f}', ha='center', va='bottom')

fig.tight_layout()
st.pyplot(fig)

