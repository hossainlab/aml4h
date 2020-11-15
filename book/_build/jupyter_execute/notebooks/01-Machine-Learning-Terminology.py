#!/usr/bin/env python
# coding: utf-8

# # Machine Learning Terminology

# ![Iris](../img/03_iris.png)

# - 50 samples of 3 different species of iris (150 samples total)
# - Measurements: sepal length, sepal width, petal length, petal width

# ## Machine learning on the iris dataset
# 
# - Framed as a **supervised learning** problem: Predict the species of an iris using the measurements
# - Famous dataset for machine learning because prediction is **easy**
# - Learn more about the iris dataset: [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/datasets/Iris)

# ## Loading the iris dataset into scikit-learn

# In[3]:


# import load_iris function from datasets module
from sklearn.datasets import load_iris


# In[4]:


# save "bunch" object containing iris dataset and its attributes
iris = load_iris()
type(iris)


# In[5]:


# print the iris data
print(iris.data)


# In[6]:


# print the names of the four features
print(iris.feature_names)


# In[7]:


# print integers representing the species of each observation
print(iris.target)


# In[8]:


# print the encoding scheme for species: 0 = setosa, 1 = versicolor, 2 = virginica
print(iris.target_names)


# ## Requirements for working with data in scikit-learn
# 
# 1. Features and response are **separate objects**
# 2. Features and response should be **numeric**
# 3. Features and response should be **NumPy arrays**
# 4. Features and response should have **specific shapes**

# In[9]:


# check the types of the features and response
print(type(iris.data))
print(type(iris.target))


# In[10]:


# check the shape of the features (first dimension = number of observations, second dimensions = number of features)
print(iris.data.shape)


# In[11]:


# check the shape of the response (single dimension matching the number of observations)
print(iris.target.shape)


# In[12]:


# store feature matrix in "X"
X = iris.data

# store response vector in "y"
y = iris.target

