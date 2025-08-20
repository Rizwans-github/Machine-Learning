import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, r2_score
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
#loading data
df = pd.read_csv(r'C:\Users\rizwa\Tech\Github\Data\Machine-Learning\End_to_end_model\train.csv')
print(df.shape)
print(df.head()) 