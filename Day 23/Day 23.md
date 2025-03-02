# Machine Learning - Linear Regression

## Types of Machine Learning
1. **Supervised Learning**
   - Algorithms learn from labeled data.
   - Example: Linear Regression, Classification.
   
2. **Unsupervised Learning**
   - Algorithms find patterns in unlabeled data.
   
3. **Semi-Supervised Learning**
   - Combines both supervised and unsupervised learning techniques.

4. **Reinforcement Learning**
   - Algorithms learn by interacting with an environment to maximize rewards.

## What is Linear Regression?
- **Definition**: A statistical method used for predictive analysis.
- **Purpose**: To find a linear relationship between independent (input) and dependent (output) variables.
- **Example**: Predicting salary based on years of experience or predicting temperature based on pollution levels.

### Key Concepts:
- **Dependent Variable**: The output variable that depends on other factors.
- **Independent Variable**: The input variable that influences the dependent variable.
- **Best Fit Line**: The line that best represents the relationship between variables.
<br></br>
<img height= 400 src ='https://github.com/user-attachments/assets/b44c4429-4cfd-4e6a-ab5f-267605d8de78'>

## Types of Linear Regression
1. **Simple Linear Regression**
   - Involves one independent variable and one dependent variable.
   - Example: Predicting package (salary) based on CGPA.

2. **Multiple Linear Regression**
   - Involves two or more independent variables and one dependent variable.
   - Example: Predicting blood pressure based on height, weight, and amount of exercise.

### Differences Between Simple and Multiple Linear Regression
- **Simple Linear Regression** works with only two columns of data (one independent and one dependent).
- **Multiple Linear Regression** works with multiple columns of data (multiple independent variables).

## Benefits of Linear Regression
- **Easy Implementation**: Simple to understand and implement.
- **Scalability**: Works well with increasing data volumes.
- **Interpretability**: Provides clear insights into how inputs affect outputs.

## Practical Example
- **Scenario**: Predicting student packages (salaries) based on their CGPA.
- **Data Points**:
  - Student A: High CGPA but low package.
  - Student B: Moderate CGPA but higher package than expected.
  
- **Visualization**: Use scatter plots to visualize data points and draw the best fit line.

## Steps in Implementing Linear Regression
1. **Understand the Data**: Identify independent and dependent variables.
2. **Visualize the Data**: Plot the data points to observe trends.
3. **Draw the Best Fit Line**: Use algorithms to find the line that minimizes prediction errors.
4. **Predict Future Outcomes**: Use the model to predict outcomes for new data points.

## Mathematical Formulation
- **Equation**: \( y = mx + c \)
  - \( y \): Dependent variable (output).
  - \( x \): Independent variable (input).
  - \( m \): Slope of the line.
  - \( c \): Intercept of the line.

## Coding Example
- **Tools**: Python libraries like NumPy, Pandas, Matplotlib, and Scikit-learn.
- **Process**:
  1. Import necessary libraries.
  2. Load and explore the dataset.
  3. Visualize the data using scatter plots.
  4. Fit a linear regression model to the data.
  5. Evaluate the model’s performance.
  6. Make predictions on new data.

## Conclusion
- Linear regression is a fundamental algorithm in machine learning.
- Understanding its principles and applications lays the groundwork for more complex models.
- Practice and patience are key to mastering this concept.
