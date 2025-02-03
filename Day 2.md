<img height="200" src="https://github.com/user-attachments/assets/4fd761d1-6a1b-4de2-8d93-fddb67e50591">

## Batch Machine Learning (Offline ML)
Batch learning gathers data over time and trains models in batches rather than learning continuously. This approach requires more CPU, memory, and disk I/O due to processing large, accumulated datasets.

<br></br>
<img height="200" src="https://github.com/user-attachments/assets/c42255b4-07e6-4fc1-be81-ed6a8252d19b">

#### Batch Size
- **Batch Mode**: Uses the entire dataset.
- **Mini-batch Mode**: Uses smaller subsets.
- **Stochastic Mode**: Processes one sample at a time.

#### Advantages
- Lower production costs  
- Flexibility  
- Better quality control  
- Increased efficiency  

#### Disadvantages
- Prone to large-scale failures  
- Monolithic structure  
- Complex management  
- Expensive requirements  

---

### Online Machine Learning
Online ML updates models in real time from a continuous data stream, allowing immediate adjustments and predictions.

**Examples**: Chatbots, YouTube/OTT recommendations, stock analysis, fraud detection.

#### Advantages
- **Adaptability**: Adjusts to new patterns.  
- **Scalability**: Minimal storage needs.  
- **Real-time predictions**: Immediate insights.  
- **Efficiency**: Continuous learning for quick decision-making.

#### Disadvantages
- Sensitive to data order  
- Less control over training  
- Lower interpretability

If issues occur, anomaly detection can trigger a switch from online to offline batch learning.

---

#### Difference Between Online vs. Offline ML
<br></br>
<img height="400" src="https://github.com/user-attachments/assets/9eef397d-fb35-4f0b-b9e7-f665be10c9ad">

Learning approaches include:
- **Instance-Based Learning**: Memorizes examples and classifies based on similarity.
- **Model-Based Learning**: Builds predictive models for generalization.

---

### Instance-Based Machine Learning
Instance-based methods memorize training examples and classify new data based on similarity. Also known as memory-based or lazy learning, they delay processing until a new instance needs classification.

<br></br>
<img height="200" src="https://github.com/user-attachments/assets/3dc99317-08c6-4947-b30d-f18ff4e44456">
<img height="200" src="https://github.com/user-attachments/assets/e1e90761-9746-46af-959d-ae6b6f5bcf7b">
<img height="200" src="https://github.com/user-attachments/assets/77f4bdc6-6675-4a32-ba2f-88c8dbdbb6b8">

---

### Model-Based Machine Learning
Model-based learning builds a predictive model from the training data using algorithms like linear regression, logistic regression, or random forests. This approach generally offers faster processing and better generalization but requires more effort to develop and fine-tune.

<br></br>
<img height="200" src="https://github.com/user-attachments/assets/a3a18ca8-1522-4ed4-b965-ea7843920a30">

#### Instance-Based vs. Model-Based ML
<img height="300" src="https://github.com/user-attachments/assets/c89fc446-16cb-461f-a558-228a64fa07e3">

---

### Challenges in Machine Learning
- Data Collection  
- Insufficient Data  
- Non-representative Data (Sampling Noise, Bias)  
- Poor Quality Data  
- Irrelevant Features  
- Overfitting & Underfitting  
- Software Integration  
- Deployment & Cost

---

#### Applications of Machine Learning
1. Retail / E-Commerce  
2. Banking and Finance  
3. Logistics and Transportation  
4. Manufacturing  
5. Social Networking  
6. And more...

---

#### Machine Learning Development Life Cycle (MLDLC/MLDC)
1. Frame the problem  
1. Gather data  
1. Data preprocessing  
1. Exploratory data analysis  
1. Feature engineering & selection  
1. Model training, evaluation, and selection  
1. Model deployment  
1. Testing  
1. Optimization
