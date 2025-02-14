# Machine Learning Day 13 Notes: Feature Engineering & Random Sampling Imputation

## Feature Engineering: Missing Value Imputation
### Techniques Covered So Far
1. **Removing Data**
2. **Mean/Median Imputation** (Numerical Data)
3. **Mode Imputation** (Categorical Data)
4. **Arbitrary Value Imputation**
5. **End of Distribution Imputation**

---

## Random Sampling Imputation
### What is Random Sampling Imputation?
- **Definition**: Replace missing values with **random observations** from the same variable's available data pool.
- **Applicability**: Works for **both numerical and categorical data**.
- **Advantages**:
  - Preserves original data distribution.
  - Easy implementation using Pandas (no Scikit-learn required).
  - Suitable for linear models.
- **Disadvantages**:
  - Complex deployment in live systems.
  - Not ideal for tree-based algorithms.

---

## Data Storytelling: Travel Industry Use Cases
1. **Recommendation Engines**: Suggest flights/hotels based on user behavior.
2. **Price Forecasting**: Predict flight/hotel prices using historical trends.
3. **Customer Support Automation**: AI chatbots for instant query resolution.
4. **Case Study - OYO**: 
   - Used data analytics to identify top spiritual destinations (e.g., Varanasi, Tirupati) driving revenue.
   - Insights helped optimize marketing strategies and resource allocation.

---

## Summary
- **Random Sampling Imputation** replaces missing values with random samples from the same feature, preserving data distribution.
- **Implementation**:
  - Use Pandas for simple numerical/categorical imputation.
  - Visualize distributions to validate results.
- **Real-World Impact**: Data science drives decisions in industries like travel (e.g., OYO’s success with regional analytics).
