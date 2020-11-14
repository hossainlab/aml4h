#!/usr/bin/env python
# coding: utf-8

# # Understand Data with Descriptive Statistics

# ## Import Libraries 

# In[10]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
pd.set_option('display.width', 100)
pd.set_option('precision', 3)
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Load Dataset 

# In[11]:


df = pd.read_csv('../data/diabetes.csv')


# ## Exploring Data 

# In[12]:


df.head() 


# In[13]:


# shape 
df.shape


# In[14]:


# dtypes 
df.dtypes


# In[15]:


# summary 
df.describe() 


# In[18]:


# class distribution 
df['Outcome'].value_counts() 


# In[19]:


# correlation 
df.corr(method='pearson')


# In[20]:


# skew 
df.skew() 

