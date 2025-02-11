## Difference Between Univariate and Multivariate Imputation  
- **Univariate Imputation**: Uses only the values of a single column to fill in missing values.  
- **Multivariate Imputation**: Considers multiple features in the dataset for more informed imputation.  

### Mean or Median Imputation  
- Replaces missing values with the **mean** or **median** of the observed values in that column.  
- Simple but may not capture data variability.  

<img height='200' src='https://github.com/user-attachments/assets/8b89b165-4038-4dfc-8ce5-923455bb8e13'>  
<img height='200' src='https://github.com/user-attachments/assets/1e91ea64-1e4e-4d93-a457-a03df5e69ebe'>  
<img height='300' src='https://github.com/user-attachments/assets/5b8fe0c8-5c36-4368-bfe9-7747a3f2bf68'>  

### Arbitrary Value Imputation  
- Replaces missing values with a **fixed arbitrary value** (e.g., -999 or 0).  
- Useful when missing values have special meaning (e.g., "not recorded").  
- Can distort data distribution if not used carefully.  

<img height='200' src='https://github.com/user-attachments/assets/00081c43-f5bd-4777-ac3f-d1931b704c7a'>  
<img height='300' src='https://github.com/user-attachments/assets/05fd74e2-9c5a-42c8-a80e-3fdbe664c8f6'>  
