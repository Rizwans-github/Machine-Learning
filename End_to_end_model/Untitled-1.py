# %%
!pip install pandas numpy scikit-learn xgboost matplotlib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor, callback
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error
import matplotlib.pyplot as plt

# %%
'''
Setting up Kaggle to load data
  28 cp kaggle.json ~/.kaggle/kaggle.json
  29 & C:/Users/rizwa/anaconda3/envs/Machine_learning/python.exe c:/Users/rizwa/Tech/Github/Data/Machine-Learning/Regres... 
  30 kaggle competitions download -c home-data-for-ml-course
  31 cd ../tech/github/data/machine-learning/
  32 kaggle competitions download -c home-data-for-ml-course
  33 mkdir End_to_end_model
  34 mv Regressor.py End_to_end_model/
  35 rmv home-data-for-ml-course.zip
  36 rm home-data-for-ml-course.zip
  37 cd end_to_end_model
  38 kaggle competitions download -c home-data-for-ml-course
  39 unzip home-data-for-ml-course.zip
  40 Expand-Archive home-data-for-ml-course.zip .
  '''


# %%
#loading data
df = pd.read_csv(r'C:\Users\rizwa\Tech\Github\Data\Machine-Learning\End_to_end_model\train.csv')
df.shape                

# %%
df.info()

# %%
df.describe()

# %%
null_cols = df.isnull().sum()[df.isnull().sum() > 0]
null_cols

# %%
null_cols_perc = (df.isnull().mean() * 100)[df.isnull().mean() * 100 > 0]
null_cols_perc

# %%

## Dropping columns with null values exceeding 30%
df = df.loc[:, df.isnull().mean() < 0.3]


# %%
null_cols = df.isnull().sum()[df.isnull().sum() > 0]
null_cols

# %%
null_cols_perc = (df.isnull().mean() * 100)[df.isnull().mean() * 100 > 0]
null_cols_perc

# %%
# Find duplicate rows
duplicates = df[df.duplicated()]
duplicates

# %%
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# %%
X.shape, y.shape

# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size =0.2, random_state=2)

# %%
categorical_cols = X_train.select_dtypes(include='object').columns
numerical_cols = X_train.select_dtypes(exclude='object').columns

# %%
categorical = Pipeline(steps=[('impute', SimpleImputer(strategy='constant')),
                              ('OHE', OneHotEncoder(handle_unknown='ignore'))])
numerical = Pipeline(steps=[('impute', SimpleImputer(strategy='median')),
                            ('Scaler', StandardScaler())])

# %%
Preprocessor = ColumnTransformer(transformers=[('categorical', categorical, categorical_cols),
                                             ('numerical', numerical, numerical_cols)])

# %%
Rf_model = RandomForestRegressor(n_estimators= 300, max_depth= 5, random_state = 2, max_leaf_nodes= 5)

# %%
Rf_pipeline = Pipeline(steps = [('Preprocessing', Preprocessor),
                       ('RfR', Rf_model)])

# %%
Rf_pipeline.fit(X_train, y_train)

# %%
Rf_predictions = Rf_pipeline.predict(X_test)
Rf_mae = mean_absolute_error(Rf_predictions, y_test)
Rf_r2_score = r2_score(Rf_predictions, y_test)
Rf_rmse = np.sqrt(mean_squared_error(y_test, Rf_predictions))
print(f'RandomForestRegressor: MAE is {round(Rf_mae, 2)} and R2 score is {round(Rf_r2_score, 3)} and RMSE is {round(Rf_rmse, 2)}')

# %%
XG_model = XGBRegressor(n_estimators=300, max_depth=5, learning_rate=0.05, random_state=2)

# %%
XG_pipeline = Pipeline(steps= [('Preprocessing', Preprocessor),
                               ('model', XG_model)])

# %%
XG_pipeline.fit(X_train, y_train)

# %%
XG_predictions = XG_pipeline.predict(X_test)


# %%
XG_predictions = XG_pipeline.predict(X_test)
XG_mae = mean_absolute_error(XG_predictions, y_test)
XG_r2_score = r2_score(XG_predictions, y_test)
XG_rmse = np.sqrt(mean_squared_error(y_test, XG_predictions))
print(f'RandomForestRegressor: MAE is {round(XG_mae, 2)} and R2 score is {round(XG_r2_score, 3)} and RMSE is {round(XG_rmse, 2)}')

# %%
models= ['RandRandomForest', 'XGBoost']
mae_scores= [Rf_mae, XG_mae]
R2_scores = [Rf_r2_score, XG_r2_score]
rmse_scores =[Rf_rmse,XG_rmse]

fig, ax = plt.subplots(1, 3, figsize = (10,5))

bars_mae = ax[0].bar(models, mae_scores, color = ['orange', 'green'], )
ax[0].set_title('MAE Performance Comparison')
ax[0].set_ylabel('Mean Absolute Error')
for i in range(len(bars_mae)):
    ax[0].text(i, mae_scores[i], f'{mae_scores[i]:.0f}', ha= 'center', va = 'bottom')

bars_rmse = ax[1].bar(models, rmse_scores, color = ['orange', 'green'])
ax[1].set_title('RMSE Performance Comparison')
ax[1].set_ylabel('Root Mean Squared Error')
for i in range(len(bars_rmse)):
    ax[1].text(i, rmse_scores[i], f'{rmse_scores[i]:.0f}', ha= 'center', va = 'bottom')

bars_r2 = plt.bar(models, r2_scores, color=['orange', 'green'])
ax[2].set_title('R2 Performance Comparison')
ax[2].set_ylabel('R2 Score')
for i in range(len(bars_r2)):
    ax[2].text(i, r2_scores[i], f'{R2_scores[i]:.2f}', ha='center', va= 'bottom')
plt.tight_layout()
plt.show()

# %%
# Fine tuning the performance

def eval(max_depth: int, n_estimators: int, learning_rate: float, cv_folds: int=10)-> float:
    XG_model_2 = XGBRegressor(max_depth=max_depth,n_estimators=n_estimators, learning_rate=learning_rate, random_state = 2) 
    XG_pipe = Pipeline(steps=[('Preprocessing', Preprocessor),
                              ('model', XG_model_2)])    
    cv_scores = cross_val_score(XG_pipe,
                                X, y,
                                scoring= 'neg_mean_absolute_error',
                                cv = cv_folds,
                                n_jobs=-1)
    avg_mae = cv_scores.mean() * -1
    return avg_mae

# %%
max_depth= [3, 5, 7]
n_estimators = [100, 200, 300, 400, 500]
learning_rate = [0.01, 0.05, 0.1]
best_param = {}
best_mae = float('inf')
for depth in max_depth:
    for estimator in n_estimators:
        for rate in learning_rate:
            avg_mae = eval(depth, estimator, rate)
            if avg_mae < best_mae:
                best_mae = avg_mae
                best_param = {'max_depth': {depth}, 'n_estimators': {estimator}, 'learning_rate': {rate}}


# %%
finalized_model = XGBRegressor(max_depth=best_param['max_depth'],
                                n_estimators=best_param['n_estimators'],
                                learning_rate=best_param['learning_rate'],
                                random_state=2)

# %%
final_pipe = Pipeline(steps=[('Preprocessing', Preprocessor),
                              ('model', finalized_model)])

# %%
finalized_model.fit(X_train, y_train)

# %%
final_pipe.fit(X_train, y_train)


