#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd


# In[6]:


pwd


# In[8]:


df_monthly = pd.read_csv("monthly.csv")
df_gold_advanced_features = pd.read_csv("gold_advanced_features.csv")


# In[9]:


df_monthly.head()


# In[10]:


df_gold_advanced_features.head()


# In[14]:


df_monthly['Price'].max()


# In[15]:


df_gold_advanced_features['price'].max()


# In[20]:


df_monthly['Price'].min()


# In[16]:


df_monthly.count()


# In[22]:


df_gold_advanced_features['price'].min()


# In[17]:


df_gold_advanced_features.count()


# In[19]:


df_gold_advanced_features[df_gold_advanced_features['price']==5019.97]


# In[23]:


df_gold_advanced_features[df_gold_advanced_features['price']==17.06]


# In[24]:


df_gold_advanced_features['volatility_3'].max()


# In[25]:


df_gold_advanced_features[df_gold_advanced_features['volatility_3']==358.9957906902974]


# In[26]:


df_gold_advanced_features['volatality_rounded'] = df_gold_advanced_features['volatility_3'].round(3)
df_gold_advanced_features.tail()


# In[ ]:





# In[ ]:




