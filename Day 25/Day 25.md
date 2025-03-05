# Regression Metrics Summary


### Key Points Covered:
1. **Mean Absolute Error (MAE)**
2. **Mean Squared Error (MSE)**
3. **Root Mean Squared Error (RMSE)**
4. **R-squared (R²)**
5. **Adjusted R-squared**
6. **Mean Absolute Percentage Error (MAPE)**
7. **Mean Bias Deviation (MBD)**

### 1. Mean Absolute Error (MAE)
- **Definition**: The average of the absolute errors between the predicted values and the actual values.
- **Formula**:
  $$\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|$$
- **Advantages**: Easy to understand and interpret.
- **Disadvantages**: Does not penalize larger errors more than smaller ones.

### 2. Mean Squared Error (MSE)
- **Definition**: The average of the squared differences between the predicted values and the actual values.
- **Formula**:
  $$\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$
- **Advantages**: Penalizes larger errors more than smaller ones.
- **Disadvantages**: Sensitive to outliers.

### 3. Root Mean Squared Error (RMSE)
- **Definition**: The square root of the mean squared error.
- **Formula**:
  $$\text{RMSE} = \sqrt{\text{MSE}}$$
- **Advantages**: Provides a measure of the average error in the same units as the target variable.
- **Disadvantages**: Still sensitive to outliers.

### 4. R-squared (R²)
- **Definition**: The proportion of the variance in the dependent variable that is predictable from the independent variable.
- **Formula**:
  $$R^2 = 1 - \frac{\text{SSR}}{\text{SST}}$$
  where:  
  $$\text{SSR} = \sum\limits_{i=1}^{n} (y_i - \hat{y}_i)^2$$
  
  SSR or SSE measures the total deviation of the observed values from the values predicted by the regression model.
  
  $$\text{SST} = \sum\limits_{i=1}^{n} (y_i - \bar{y})^2$$

  SST measures the total deviation of the observed values from the mean of the observed values.
- **Advantages**: Provides a measure of how well the independent variable explains the dependent variable.
- **Disadvantages**: Can be misleading if the model is overfitted.

### 5. Adjusted R-squared
- **Definition**: Adjusts the R-squared value based on the number of predictors in the model.
- **Formula**:
  $$\text{Adjusted } R^2 = 1 - \frac{(1 - R^2)(n - 1)}{n - p - 1}$$
  where \( p \) is the number of predictors.
- **Advantages**: Penalizes the model for adding unnecessary predictors.
- **Disadvantages**: Can be complex to interpret.

### 6. Mean Absolute Percentage Error (MAPE)
- **Definition**: Measures the percentage error between actual and predicted values.
- **Formula**:
  $$\text{MAPE} = \frac{100}{n} \sum_{i=1}^{n} \left| \frac{y_i - \hat{y}_i}{y_i} \right|$$
- **Advantages**: Expresses error as a percentage, making it easy to interpret.
- **Disadvantages**: Not reliable when actual values are close to zero.

### 7. Mean Bias Deviation (MBD)
- **Definition**: Measures the bias in the predictions by taking the average difference between actual and predicted values.
- **Formula**:
  $$\text{MBD} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)$$
- **Advantages**: Helps understand whether the model systematically overestimates or underestimates.
- **Disadvantages**: Does not provide a measure of overall accuracy, only bias.

### Practical Example
Let's consider a simple linear regression model where we predict the salary (\( y \)) based on the years of experience (\( x \)).

1. **MAE Calculation**:
   $$\text{MAE} = \frac{1}{n} \sum\limits_{i=1}^{n} |y_i - \hat{y}_i|$$
   Suppose the actual salaries are \([50, 55, 60]\) and the predicted salaries are \([48, 57, 59]\).

$$\text{MAE} = \frac{1}{3} (|50 - 48| + |55 - 57| + |60 - 59|) = \frac{1}{3} (2 + 2 + 1) = 1.67$$

3. **MSE Calculation**:
   $$\text{MSE} = \frac{1}{n} \sum\limits_{i=1}^{n} (y_i - \hat{y}_i)^2$$
   
   Using the same values:
   $$\text{MSE} = \frac{1}{3} ((50 - 48)^2 + (55 - 57)^2 + (60 - 59)^2)
   = \frac{1}{3} (4 + 4 + 1) = 3$$

4. **RMSE Calculation**:
   $$\text{RMSE} = \sqrt{\text{MSE}}
   = \sqrt{3} \approx 1.73$$

6. **R-squared Calculation**:
      $$R^2 = 1 - \frac{\text{SSR}}{\text{SST}}$$
   where:
   
$$
\text{SSR} = \sum\limits_{i=1}^{n} (y_i - \hat{y}_i)^2 = 3
$$

$$
\text{SST} = (50 - 55)^2 + (55 - 55)^2 + (60 - 55)^2 = 50
$$
$$
R^2 = 1 - \frac{3}{50} = 0.94
$$

