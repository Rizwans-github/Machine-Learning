# Missing Indicator Imputation in Univariate Imputation

## 1. Introduction to Missing Indicator Imputation

### Definition:
- The Missing Indicator Method (MIM) involves adding an indicator variable to denote the presence of missing values. This helps improve model performance by capturing missing data patterns.

### Benefits:
- Enhances model accuracy and efficiency.
- Useful when missing data is not random and carries information.

### Example:
- A dataset with columns `Age` and `Fare`. If `Age` has missing values, create `Age_Indicator`, where `True` denotes missing values and `False` otherwise.

---

## Conclusion
- Missing Indicator Imputation helps models capture missing data patterns.
- It improves model performance compared to simple mean imputation.
- KNN Imputation relies on distance calculations for estimating missing values.

                                                    
