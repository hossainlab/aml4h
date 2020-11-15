#!/usr/bin/env python
# coding: utf-8

# # Exploring Data with Descriptive Statistics

# You must understand your data in order to get better results. In this notebook I'll explain you that you can use Python to better understand your data. There is no substitute for looking at the raw data. Looking at the raw data can reveal **insights** that you cannot get any other way.

# ## Import Libraries 

# In[1]:


import pandas as pd # for data manipulation
import numpy as np # for linear algebra 

# set options 
pd.set_option('display.width', 100)
pd.set_option('precision', 3)


# ## Load Dataset 
# - In this example, I'll use heart disease dataset
# - Data Source - [Kaggle](https://www.kaggle.com/ronitf/heart-disease-uci)

# In[2]:


# load data 
df = pd.read_csv('../data/heart.csv')


# ## Peek at Your Data 

# In[3]:


# examine first few rows 
df.head() 


# In[4]:


# examine last few rows 
df.tail() 


# In[5]:


# examine specific number of rows 
df.head(10)


# ## Dimensions
# - Too many rows and algorithms may take too long to train. Too few and perhaps you do
#   not have enough data to train the algorithms.
# - Too many features and some algorithms can be distracted or suffer poor performance due
#   to the curse of dimensionality.

# In[6]:


# check shape of data 
df.shape


# In[7]:


# no. of rows 
df.shape[0]


# In[8]:


# no. of columns 
df.shape[1]


# ## Data Type For Each Attribute

# In[9]:


# dtypes 
df.dtypes


# ## Descriptive Statistics
# - Count 
# - Mean 
# - Median 
# - Standard Deviation
# - Five Number Summary
#     - Minimum 
#     - 25th Percentile 
#     - 50th Percentile 
#     - 75th Percentile 
#     - Maximum 
# 

# In[10]:


# summary stats 
df.describe() 


# In[11]:


# transpose summary stats 
df.describe().T


# ## Class Distribution(Classification Only) 

# In[12]:


# class distribution 
df['target'].value_counts() 


# In[13]:


# class distribution 
df['target'].value_counts(normalize=True) 


# In[14]:


# class distribution using group by 
df.groupby('target').size() 


# ## Correlations Between Attributes
# - Correlation refers to the relationship between two variables and how they may or may not
#   change together.
# - The most common method for calculating correlation is **Pearson’s** Correlation
#   Coefficient, that assumes a normal distribution of the attributes involved. 
# - A correlation of -1 or 1 shows a full negative or positive correlation respectively.
# - Whereas a value of 0 shows no correlation at all.
# - Some machine learning algorithms like linear and logistic regression can suffer
#   **poor** performance if there are **highly** correlated attributes in your dataset.

# In[15]:


# correlation: Pearson’s by default 
df.corr(method='pearson')


# ## Skewness
# - Skew refers to a distribution that is assumed **Gaussian** (normal or bell curve) that is shifted or
#   squashed in one direction or another.
# - Many machine learning algorithms assume a **Gaussian or normal** distribution.
# - Knowing that an attribute has a skew may allow you to perform data preparation to correct the skew and later improve the accuracy of your models.
# - The skew result show a positive (right) or negative (left) skew. Values closer to zero show less skew

# In[16]:


# skew 
df.skew() 

