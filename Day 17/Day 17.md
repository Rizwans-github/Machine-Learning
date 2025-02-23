# Introduction to Outliers in Machine Learning


## Agenda
1. Recap of Previous Class (Day 16)
2. Introduction to Outliers
3. Importance of Outliers in Machine Learning
4. Types of Data Distributions
5. Techniques to Handle Outliers
6. Impact of Outliers on Machine Learning Models
7. Practical Example of Outliers
8. Conclusion and Next Steps

## 1. Recap of Previous Class (Day 16)
- **Topic Covered:** Handling Missing Values in Feature Engineering
- **Key Points:**
  - Techniques for handling missing values were discussed.
  - Importance of data cleaning and preprocessing was emphasized.

## 2. Introduction to Outliers
- **Definition:** Outliers are data points that are significantly different from the rest of the dataset.
  - Example: Heights ranging from 4.5 to 6 feet, but a value of 10 feet is an outlier.

![image](https://github.com/user-attachments/assets/940736ee-e03d-4837-a885-9fe63f02920d)

## 3. Importance of Outliers in Machine Learning
- **Potential Issues:**
  - Can distort statistical measures.
  - Lead to incorrect conclusions.
  - Impact the efficiency and accuracy of machine learning models.
- **Example:** Incorrect data entry (80 instead of 6) can severely impact model performance.

## 4. Types of Data Distributions
- **Normal Distribution:**
  - Data is symmetrically distributed around the mean.
  - Example: Heights of students in a class.

![image](https://github.com/user-attachments/assets/b56b1b4b-843b-4233-af94-d70b62b1cc95)

- **Skewed Distribution:**
  - Data is asymmetrically distributed.
  - **Positive Skew:** Tail on the right side (e.g., income distribution).
  - **Negative Skew:** Tail on the left side (e.g., exam scores).

![image](https://github.com/user-attachments/assets/3d5c9a98-8352-472d-ad76-59b440e7ec70)

- **Other distributions (percentile-based approach):**
    - Identifies outliers by comparing the observations to specific percentiles.
If an observation is greater than the 97.5th percentile or less than the 2.5th
percentile, it is considered an outlier.

![image](https://github.com/user-attachments/assets/687172b8-6306-49c2-b22c-25237727006a)
![image](https://github.com/user-attachments/assets/0da59c33-4f7b-493a-b43f-7b3fb0b6c0cc)

- **Uniform Distribution:**
  - Data is evenly distributed across the range.
  - Example: Rolling a fair die.

## 5. Techniques to Handle Outliers
- **Four Main Techniques:**
  1. **Z-Score Treatment:** Suitable for normally distributed data.
     - Formula: \( Z = \frac{(X - \mu)}{\sigma} \)
     - Values outside the range of -3 to 3 are considered outliers.
  2. **IQR (Interquartile Range):** Suitable for skewed distributions.
     - Formula: \( IQR = Q3 - Q1 \)
     - Outliers are values below \( Q1 - 1.5 \times IQR \) or above \( Q3 + 1.5 \times IQR \).
  3. **Percentile Method:** General outlier detection.
     - Values below the 2.5th percentile or above the 97.5th percentile are considered outliers.
  4. **Winsorization:** Replacing outliers with specific percentile values.
     - Example: Replace values below the 5th percentile with the 5th percentile value and values above the 95th percentile with the 95th percentile value.

## 6. Impact of Outliers on Machine Learning Models
- **Weight-Based Algorithms:**
  - Linear Regression
  - Logistic Regression
  - AdaBoost
  - Deep Learning
- **Objective:** Minimize error and maximize output efficiency.
- **Example:** Outliers can skew the prediction line in linear regression, leading to incorrect predictions.

## 7. Practical Example of Outliers
- **Scenario:** Student marks ranging from 40 to 60, with a few students having marks around 98.
- **Analysis:** Including outliers can skew the model. Detecting and handling outliers improves model accuracy.

## 8. Conclusion and Next Steps
- **Summary:** Understanding and handling outliers is crucial for feature engineering and improving machine learning model efficiency.
