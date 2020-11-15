#!/usr/bin/env python
# coding: utf-8

# # Exploring Data with Visualization
# The fastest way to learn more about your data is to use data visualization.
# > “A picture is worth a thousand words” Because of the way the human brain processes information, using charts or graphs to visualize large amounts of complex data is easier than poring over spreadsheets or reports. Data visualization is a quick, easy way to convey concepts in a universal manner – and you can experiment with different scenarios by making slight adjustments.
# 
# In this notebook, You'll learn data visualization technique using Pandas and Matplotlib

# In[14]:


import pandas as pd 
from pandas.plotting import scatter_matrix
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

# set options 
sns.set_style('whitegrid')
pd.set_option('display.width', 100)
pd.set_option('precision', 3)
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Dataset
# - Pima Indians Diabetes Database
# - Data Source - [Kaggle](https://www.kaggle.com/uciml/pima-indians-diabetes-database)

# In[2]:


# read data 
df = pd.read_csv('../data/diabetes.csv')


# In[3]:


# examine first few rows 
df.head() 


# ## Univariate Plots
# - Histograms 
# - Density Plot 
# - Box and Whisker Plots 

# ### Histograms
# 4 Main Aspects
# - **Shape**: Overall appearance of histogram. Can be symmetric, bell-shaped, left skewed, right skewed, etc. 
# - **Center**: Mean or Median
# - **Spread**: How far our data spreads. Range, Interquartile Range (IQR),standard deviation, variance.
# - **Outliers**: Data points that fall far from the bulk of the data

# In[6]:


df.hist(figsize=(20,10), edgecolor='black')
plt.show() 


# ### Density Plots 
# - Density plots are another way of getting a quick idea of the distribution of each attribute.
# - The plots look like an abstracted histogram with a smooth curve drawn through the top of each bin,much like your eye tried to do with the histograms.

# In[7]:


df.plot(kind='density', subplots=True, sharex=False, figsize=(20,10), layout=(3,3))
plt.show() 


# ### Boxplots 
# - Boxplots provide a graphical picture of the five-number summary: showing center (median), spread (IQR and range), and identifies potential outliers.
# - Boxplots can hide some shape aspects(histograms do better job at displaying shape)
# - Side-by-Side Boxplots are useful for comparing two or more sets of observations.

# In[8]:


df.plot(kind='box', subplots=True, sharex=False, figsize=(20,10), layout=(3,3))
plt.show() 


# ## Multivariate Plots
# - Correlation Matrix Plot 
# - Scatter Plot 

# ### Correlation Matrix Plot 
# - Correlation gives an indication of how related the changes are between two variables.
# - If two variables change in the same direction they are positively correlated.
# - If they change in opposite directions together (one goes up, one goes down), then they are negatively correlated.
# - This is useful to know, because some machine learning algorithms like linear and logistic regression can have poor performance if there are highly correlated input variables in your data.

# In[11]:


plt.figure(figsize=(10,6))
corr = df.corr() 
sns.heatmap(corr, annot=True)
plt.show()


# ### Scatter Plot 
# - A scatter plot shows the relationship between two variables as dots in two dimensions, one axis for each attribute.

# In[ ]:


df.plot(kind='scatter', x="BMI", y="BloodPressu", alpha=0.3); 


# ## Pair Plot
# - Plot pairwise relationships in a dataset.
# - By default, this function will create a grid of Axes such that each numeric variable in data will by shared across the y-axes across a single row and the x-axes across a single column. The diagonal plots are treated differently: a univariate distribution plot is drawn to show the marginal distribution of the data in each column.
# - It is also possible to show a subset of variables or plot different variables on the rows and columns.
# [__See More__](https://seaborn.pydata.org/generated/seaborn.pairplot.html)

# In[20]:


sns.pairplot(df)


# In[22]:


sns.pairplot(df, hue='Outcome')

