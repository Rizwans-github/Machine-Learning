# Software Development Lifecycle (SDLC)
The Software Development Lifecycle (SDLC) is a structured approach to building high-quality software efficiently. It helps minimize risks, ensures clear planning, and meets customer expectations by breaking development into measurable tasks.
[Learn More](https://aws.amazon.com/what-is/sdlc/)

<br></br>
<img height="300" src="https://github.com/user-attachments/assets/1b5f65ae-61ac-42d5-8762-e22e2bd405d6">

# Machine Learning Development Lifecycle (MLDLC)
<img height="300" src="https://github.com/user-attachments/assets/27b5547d-8357-4103-89ac-397d459a9d9a">

## 1. Frame the Problem
Define objectives, estimate costs, and establish clear project requirements before starting development.

## 2. Data Collection
Gather relevant data from multiple sources—online, offline, or scraped. Large-scale data collection is critical for machine learning projects.

## 3. Data Pre-processing
Clean and organize raw data to make it suitable for training machine learning models.

<img height="200" src="https://github.com/user-attachments/assets/3527dfac-fedb-4ffc-9774-c4acd6b454db">

## 4. Exploratory Data Analysis (EDA)
Analyze and visualize datasets to understand key characteristics before model development.

## 5. Feature Engineering & Selection
Transform raw data into meaningful features through creation, transformation, extraction, selection, and scaling. Experimentation is required to find the best features for a given problem.

<img height="200" src="https://github.com/user-attachments/assets/3b3ca451-d449-40fe-9d69-4226146effe4">

## 6. Model Training, Evaluation, and Selection
Train models and assess their performance using evaluation metrics to ensure they generalize well for future predictions.

<img height="200" src="https://github.com/user-attachments/assets/504b7e86-d9a8-403b-8ef5-463e7742b9bc">

## 7. Model Deployment
Integrate the trained model into a production environment for real-world applications.

## 8. Testing
Evaluate the trained model's performance on a separate testing dataset to ensure reliability and accuracy.

## 9. Optimization
Refine the model iteratively to improve accuracy and reduce errors.

<img height="300" src="https://github.com/user-attachments/assets/330cf998-52e9-436e-ad68-41c4212c8814">
<img height="300" src="https://github.com/user-attachments/assets/0d490ef4-6c75-43fe-a40b-bebed7acf990">
<img height="200" src="https://github.com/user-attachments/assets/95cdb883-de40-45f0-ab45-05d23d7c6678">

# Data Handling & Preparation
## Importing and Uploading Data

### Reading CSV Files
```python
import pandas as pd
df = pd.read_csv('hotel_bookings.csv')
```

### Reading CSV from a URL
```python
import requests
from io import StringIO

url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
req = requests.get(url)
data = StringIO(req.text)
df = pd.read_csv(data)
```

### Reading CSV with Different Parameters
- **Separator (`sep`)**: Specifies a custom delimiter.
- **Index Column (`index_col`)**: Sets a specific column as index.
- **Header (`header`)**: Defines header row.
- **Use Columns (`usecols`)**: Selects specific columns.
- **Skip Rows (`skiprows`)**: Skips initial rows.
- **Read Limited Rows (`nrows`)**: Loads only a subset of data.
- **Encoding (`encoding`)**: Handles character encoding issues.

```python
pd.read_csv('movie_titles_metadata.tsv', sep='\t', index_col=0)
pd.read_csv('aug_train.csv', usecols=['enrollee_id', 'gender'])
pd.read_csv('zomato.csv', encoding='latin-1')
```

## Handling Missing Data
```python
df.fillna(value, inplace=True)  # Fills missing values
df.dropna(inplace=True)  # Drops missing values
```

## Handling Large Datasets
```python
dfs = pd.read_csv('aug_train.csv', chunksize=5000)
for chunk in dfs:
    print(chunk.shape)
```

## Working with JSON Data
```python
df_json = pd.read_json('train.json')
```

## Working with SQL Databases
```python
import mysql.connector
conn = mysql.connector.connect(host='localhost', user='root', password='', database='world')
df_sql = pd.read_sql_query("SELECT * FROM countrylanguage", conn)
```

## Handling Dates
```python
df = pd.read_csv('IPL Matches 2008-2020.csv', parse_dates=['date'])
```
