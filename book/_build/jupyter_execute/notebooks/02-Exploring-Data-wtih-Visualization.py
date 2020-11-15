#!/usr/bin/env python
# coding: utf-8

# # Exploring Data with Visualization

# In[2]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
sns.set_style('whitegrid')
pd.set_option('display.width', 100)
pd.set_option('precision', 3)
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df = pd.read_csv('../data/diabetes.csv')


# In[4]:


df.head() 


# ## Univariate Plot 
# - Histograms 
# - Density Plot 
# - Box and Whisker Plots 

# In[8]:


df.hist(figsize=(20,10))
plt.show() 


# In[16]:


df.plot(kind='density', subplots=True, sharex=False, figsize=(20,10), layout=(3,3))
plt.show() 


# In[17]:


df.plot(kind='box', subplots=True, sharex=False, figsize=(20,10), layout=(3,3))
plt.show() 


# In[26]:


plt.figure(figsize=(8,6))
corr = df.corr() 
sns.heatmap(corr, annot=True)
plt.show()

