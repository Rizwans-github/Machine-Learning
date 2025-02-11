## Handling Missing Data

### Problems with Missing Data  
Real-world data often contains missing values due to data corruption or recording failures. Handling missing data is crucial, as many ML algorithms do not support missing values.  

### Methods to Handle Missing Data  
1. **Removing Missing Values** (Complete Case Analysis - CCA)  
2. **Imputing Missing Values**  
   - **Univariate:** Mean/Median (Numerical), Mode (Categorical)  
   - **Multivariate:** KNN Imputer, Iterative Imputer  

### Complete Case Analysis (CCA)  
CCA removes any observation with missing values, analyzing only complete records.  

#### When to Use CCA?  
- Data is **Missing Completely at Random (MCAR)**  
- Small dataset with few missing values  
- Simplicity is preferred over accuracy  

#### Pros & Cons of CCA  
✅ Easy to implement  
✅ Preserves relationships in complete data  
❌ Reduces dataset size  
❌ Introduces bias if data isn’t MCAR  

Handling missing data correctly improves model performance and ensures meaningful analysis. 🚀
