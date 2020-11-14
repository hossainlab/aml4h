#!/usr/bin/env python
# coding: utf-8

# # Introduction to Machine Learning

# ## What machine learning?
# One definition: "Machine learning is the semi-automated extraction of knowledge from data"
# 
# - **Knowledge from data**: Starts with a question that might be answerable using data
# - **Automated extraction**: A computer provides the insight
# - **Semi-automated**: Requires many smart decisions by a human

# ## How does machine learning "work"?
# 
# High-level steps of supervised learning:
# 
# 1. First, train a **machine learning model** using **labeled data**
# 
#     - "Labeled data" has been labeled with the outcome
#     - "Machine learning model" learns the relationship between the attributes of the data and its outcome
# 
# 2. Then, make **predictions** on **new data** for which the label is unknown
# 
# ![](../img/ml_workflow.png)

# ![Supervised learning](../img/01_supervised_learning.png)

# ## Types of Machine Learning Algorithms?
# - Supervised Learning
# - Unsupervised Learning 
# - Reinforcement Learning
# ![](../img/mlalgo.png)

# ## How does Supervised Learning Works?

# ## How Unsupervised Learning Works?
# ![](../img/unsupervised_learning.png)

# ## How Reinforcement Learning Works?
# ![](../img/reinforcement_learning.png)

# ## Example of Supervised Learning 
# Making predictions using data
# - Example: Is a given email "spam" or "ham"?
# - There is an outcome we are trying to predict

# ![Spam filter](../img/01_spam_filter.png)

# ## Example of Unsupervised Learning 
# Extracting structure from data
# 
# - Example: Segment grocery store shoppers into clusters that exhibit similar behaviors
# - There is no "right answer"

# ![Clustering](../img/01_clustering.png)

# The primary goal of supervised learning is to build a model that "generalizes": It accurately predicts the **future** rather than the **past**!

# ## Machine learning terminology
# 
# - Each row is an **observation** (also known as: sample, example, instance, record)
# - Each column is a **feature** (also known as: predictor, attribute, independent variable, input, regressor, covariate)

# - Each value we are predicting is the **response** (also known as: target, outcome, label, dependent variable)
# - **Classification** is supervised learning in which the response is categorical
# - **Regression** is supervised learning in which the response is ordered and continuous

# ![](../img/datatypes.png)

# ## Questions about machine learning
# 
# - How do I choose **which attributes** of my data to include in the model?
# - How do I choose **which model** to use?
# - How do I **optimize** this model for best performance?
# - How do I ensure that I'm building a model that will **generalize** to unseen data?
# - Can I **estimate** how well my model is likely to perform on unseen data?
