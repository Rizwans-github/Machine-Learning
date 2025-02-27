# Machine Learning: Outlier Detection using IQR Technique (Day 19)

## Introduction to Outlier Detection
- Essential for feature engineering and data preprocessing
- Helps identify anomalies in data distribution
- Used in fraud detection, anomaly analysis, and data science

## Box Plot and IQR Fundamentals
### Box Plot Components
| Component | Description |
|-----------|-------------|
| Q1 (First Quartile) | 25th Percentile |
| Q2 (Median) | 50th Percentile |
| Q3 (Third Quartile) | 75th Percentile |

![Box Plot](https://github.com/user-attachments/assets/cf7d9b79-1e9c-4bbb-81aa-af823761a2cb)

### Interquartile Range (IQR) Calculation
- **IQR = Q3 - Q1**
- Outlier Boundaries:
  - **Lower Limit**: `Q1 - 1.5 * IQR`
  - **Upper Limit**: `Q3 + 1.5 * IQR`

![Five Number Summary](https://github.com/user-attachments/assets/9324eecb-46d4-4f18-a0ca-8ea0805a6eb3)

## Skewed Distributions
- **Positive Skew**: Mean > Median > Mode (Tail extends right)
- **Negative Skew**: Mode > Median > Mean (Tail extends left)

![Skewed Distributions](https://github.com/user-attachments/assets/a4d74fe2-b624-48db-a4ec-be401a3faf3f)

## Outlier Treatment Strategies
| Method | Data Impact | Use Case |
|--------|------------|----------|
| **Trimming** | Removes outliers | Small datasets, clear errors |
| **Capping** | Replaces outliers with limits | Large datasets, preserves size |

## Practical Implementation
- Used Python to analyze a placement exam dataset (1000 entries)
- Identified 15 outliers using IQR
- Visualized data distribution for better insights

## Key Takeaways
- **Z-Score** is suitable for normal distributions
- **IQR** works better for skewed distributions
- Always visualize and validate before applying outlier treatment
- 
## Performance Metrics Table
| Method | Data Preservation | Complexity | Recommended Use |
|--------|------------------|------------|----------------|
| Z-Score | Moderate | Low | Normal Distribution |
| IQR | High | Medium | Skewed Data |
| Percentile | High | Medium-High | Robust Datasets |

## Common Challenges
- Balancing data integrity with outlier removal
- Ensuring domain relevance of outliers
- Avoiding excessive data loss
