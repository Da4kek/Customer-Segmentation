# Customer-Segmentation
---
>Customer Segmentation is the subdivision of a market into discrete customer groups that share similar characteristics. Customer Segmentation can be a powerful means to identify unsatisfied customer needs. Using the above data companies can then outperform the competition by developing uniquely appealing products and services.

**The most common ways in which businesses segment their customer base are:**

* __Demographic information__: such as gender, age, familial and marital status, income, education, and occupation.

* __Geographical information__: which differs depending on the scope of the company. For localized businesses, this info might pertain to specific towns or counties. For larger companies, it might mean a customer’s city, state, or even country of residence.

* __Psychographics__: such as social class, lifestyle, and personality traits.
Behavioral data, such as spending and consumption habits, product/service usage, and desired benefits.

# Problem Statement:
---
```
Develop a machine-learning solution that can segment
customers into different groups based on their demographics, behavior, or preferences.
The solution should be able to provide insights into customer behavior and preferences
and help businesses develop targeted marketing campaigns or personalized
experiences for their customers. 
```
## Dataset used:
---
[instacart Market Basket Analysis](https://www.kaggle.com/competitions/instacart-market-basket-analysis) The dataset is anonymized and contains a sample of over 3 million grocery orders from more than 200,000 Instacart users. For each user, They've provide between 4 and 100 of their orders, with the sequence of products purchased in each order.

Each entity (customer, product, order, aisle, etc.) has an associated unique id. Most of the files and variable names should be self-explanatory.

## Approach:
---
I have decided to build a machine learning model which will be an Unsupervised learning model that shall cluster different user groups based on their preferences and later show the recommended product for each group of users.

**Algorithms used:**
* TruncatedSVD (singular value decomposition)
* IsolationForest
* KMeans clustering

**Files:**

 The Data Folder contains the required data for the task (I cannot add the entire dataset as the size of certain csv files were more than 100MB).

 The Models Folder contains KMeans function that I used to test prior the submission(which was a disaster).

 The data_init.py file was used to get the data as zip format and then unzip them.

 The EDA.ipynb file is the jupyter notebook containing code that will give basic understanding of the data, give insights about the data by graphical approach.

 The Customer_segmentation.ipynb is the jupyter notebook containing project code that contains process like feature extraction, data preprocessing, clustering and then plotting.

 ## Terminologies
 ---

 1. EDA(exploratory data analysis):
    * EDA is applied to investigate the data and summarize the key insights.
    It will give you the basic understanding of your data, it’s distribution, null values and much more.
    You can either explore data using graphs or through some python functions.
    There will be two type of analysis. Univariate and Bivariate. In the univariate, you will be analyzing a single attribute. But in the bivariate, you will be analyzing an attribute with the target attribute.
    In the non-graphical approach, you will be using functions such as shape, summary, describe, isnull, info, datatypes and more.
    In the graphical approach, you will be using plots such as scatter, box, bar, density and correlation plots.

2. KMeans clustering:
    * K means is one of the most popular Unsupervised Machine Learning Algorithms Used for Solving Classification Problems. K Means segregates the unlabeled data into various groups, called clusters, based on having similar features, common patterns.
    * The technique to segregate Datasets into various groups, on basis of having similar features and characteristics, is being called Clustering.

3. Dimensionality Reduction:
    * Dimensionality reduction is a machine learning (ML) or statistical technique of reducing the amount of random variables in a problem by obtaining a set of principal variables.
    * In short, Reduce the size of data (specially means attributes or columns in tabular data).

4. SVD(Singular value decomposition):
    * Singular Value Decomposition (SVD) is a widely used technique to decompose a matrix into several component matrices, exposing many of the useful and interesting properties of the original matrix.
    * Unlike regular SVDs, truncated SVD produces a factorization where the number of columns can be specified for a number of truncation. For example, given an n x n matrix, truncated SVD generates the matrices with the specified number of columns, whereas SVD outputs n columns of matrices.

5. CSR(compressed sparse row matrix):
    * Ideally, the entries are sorted first by row index and then by column index, to improve random access times. This is another format that is good for incremental matrix construction.
    * In short, represents a matrix M by three (one-dimensional) arrays, that respectively contain nonzero values, the extents of rows, and column indices. It is similar to COO, but compresses the row indices, hence the name.

6. IsolationForest:
    * The IsolationForest ‘isolates’ observations by randomly selecting a feature and then randomly selecting a split value between the maximum and minimum values of the selected feature.

7. Data anomaly detection: 
    * Anomaly detection is the process of finding the outliers in the data, i.e. points that are significantly different from the majority of the other data points.

8. Outliers:
    * An outlier is nothing but a data point that differs significantly from other data points in the given dataset.


## Conclusion & Future works:
---

Further the model can be used in real world with higher data insights and building a robust model involving high computational cost.

Further the model can be tuned with XGboost and providing more data insights.
Since I'm restricted with computational resources I could only perform with less than 20% of the data.

Machine learning isn't always about creating complex statistical models to predict desired label, sometimes Machine learning can be a part of analysing complex data, creating structures, insights and creating inovating ideas.

Thank you.

Cheers! 

Dark.