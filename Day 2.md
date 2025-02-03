<img height="200" src="https://github.com/user-attachments/assets/4fd761d1-6a1b-4de2-8d93-fddb67e50591">

## Batch Machine Learning (Offline ML):
In batch learning, data is accumulated overa period of time. The machine learning model is
then trained with this accumulated data from time to time in batches. It is the direct
opposite of online learning because the model is unable to learn incrementally from a
stream of live data. In batch learning, the machine learning algorithm updates its
parameters only after consuming batches of new data.
The fact that models are trained with large batches of accumulated data means that more
time and resources such as CPU, memory space, and disk input/output are needed.
<br></br>
<img height="200" src="https://github.com/user-attachments/assets/c42255b4-07e6-4fc1-be81-ed6a8252d19b">
#### Batch size (machine learning)
Batch size is a term used in machine learning and refers to the number of training examples
utilized in one iteration. The batch size can be one of three options:
- Batch mode: where the batch size is equal to the total dataset thus making the iteration
and epoch values equivalent
- Mini-batch mode: where the batch size is greater than one but less than the total dataset
size. Usually, a number that can be divided into the total dataset size.
- Stochastic mode: where the batch size is equal to one. Therefore, the gradient and the
neural network parameters are updated after each sample.

#### Advantages: (When we use?)
- Lower production costs
- Flexibility
- Better quality control
- Increased efficiency
#### Disadvantages:
- Large-scale failures
- They are monolithic in nature
- Complex to manage
- Require very expensive

### Online Machine Learning:
Online machine learning is a method of machine learning where the model incrementally
learns from a stream of data points in real time. It's a dynamic process that adapts its
predictive algorithm over time, allowing the model to change as new data arrives. This
method is incredibly significant in today's rapidly evolving data-rich environments because
it can provide timely and accurate predictions.
Real time example: Chat Bot, YouTube or OTT Recommended, Stock, Fraud Detection

#### Advantages:(What are the Benefits of Online Machine Learning?)
- Adaptability: Just like the cyclists learning as they go, online machine learning can adapt to
new patterns in the data, improving its performance over time.
- Scalability: Since online learning processes data one at a time, it doesn't require the storage
capacity that batch learning does. This makes it scalable to big data applications.
- Real-time predictions: Unlike batch learning which might be outdated by the time it's
implemented, online learning provides real-time insights, which can be critical in many
applications like stock trading and health monitoring.
- Efficiency: As online machine learning allows for continuous learning and updating of
models, this can lead to faster and more cost-efficient decision-making processes.

#### Disadvantages:(What are the Limitations of Online Machine Learning?)
- Sensitive to sequence or Tricky to Use: The order in which the data is presented can impact
the learning process. An unusual data point can significantly alter the model's parameters, decreasing accuracy.
- Less control over training or risk: Unlike batch learning, where you can control the
training process, online learning is always on. An unexpected influx of bad-quality data can
lead to poor predictions.
- Lack of interpretability: Online learning algorithms, especially those based on deep learning
or neural networks, can be highly complex and difficult to interpret. This lack of
interpretability can make it challenging to understand and explain the model's decisions.

If we face problems in an online learning system real-time technique, we use: We use
anomaly detection system to switch the system to Offline Mode or rollback the system
online to offline batch learning.

#### Difference Between Online Vs Offline Machine Learning?
<br></br>
<img height="400" src="https://github.com/user-attachments/assets/9eef397d-fb35-4f0b-b9e7-f665be10c9ad">

Think about how humans learn, the answer is memorised or generalized
Learning -> Memorising (Example of Instanced-Based ML)
Learning -> Generalized (Example of Model-Based ML)
 
### Instance-Based Machine Learning:
The Machine Learning systems which are categorized as instance-based learning are the
systems that learn the training examples by heart and then generalize to new instances
based on some similarity measures. It is called instance-based because it builds the
hypotheses from the training instances. It is also known as memory-based learning or lazy-
learning (because they delay processing until a new instance must be classified). 
The time complexity of this algorithm depends upon the size of the training data. Each time
whenever a new query is encountered, its previously stored data is examined. And assign to
a target function value for the new instance.
<br></br>
<img height="200" src="https://github.com/user-attachments/assets/3dc99317-08c6-4947-b30d-f18ff4e44456">
<img height="200" src="https://github.com/user-attachments/assets/e1e90761-9746-46af-959d-ae6b6f5bcf7b">
<img height="200" src="https://github.com/user-attachments/assets/77f4bdc6-6675-4a32-ba2f-88c8dbdbb6b8">

### Model-Based Machine Learning:
Model-based learning (also known as structure-based or eager learning) takes a different
approach by constructing models from the training data that can generalize better than
instance-based methods. This involves using algorithms like linear regression, logistic
regression, random forest, trees etc. to create an underlying model from which predictions
can be made for new data points. The picture below represents how the prediction about
the class is decided based on the boundary learned from training data rather than comparing
with the learned data set based on similarity measures.
<br></br>
![image](https://github.com/user-attachments/assets/a3a18ca8-1522-4ed4-b965-ea7843920a30)

The model-based learning approach has several benefits over instance-based
methods, such as faster processing speeds and better generalization capabilities due to its
use of an underlying model rather than relying solely on memorized examples. However,
his approach requires more time and effort to develop and tune the model for optimal
performance on unseen data sets.

#### Instance-Based Vs Model-Based Machine Learning
<img height="500" src="https://github.com/user-attachments/assets/c89fc446-16cb-461f-a558-228a64fa07e3">

### Challenges in Machine Learning:
- Data Collection
- Insufficient Data
- Non Reprehensive Data (Sampling Noise, Sampling Bias)
- Poor Quality Data
- Irrelevant Features
- Overfitting & Under fitting
- Software Integration
- Deployment & Cost Involved

#### Application of Machine Learning:
1. Retail / E-Commerce Sector
2. Banking and Finance Sector
3. Logistics and Transportation Sector
4. Manufacturing Sector
5. Social Networking Sector
6. Many More Sector

#### Machine Learning Development Life Cycle (MLDLC/MLDC):

1. Frame the problem
1. Gathering data
1. Data preprocessing
1. Exploratory data analysis
1. Feature engineering & selection
1. Model training, evaluation and selection
1. Model deployment
1. Testing
1. Optimize
