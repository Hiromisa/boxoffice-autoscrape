#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[26]:


url = 'https://www.boxofficemojo.com/weekly/?ref_=bo_nb_ml_secondarytab'
df = pd.io.html.read_html(url)


# In[27]:


df = df[0]


# In[36]:


df = df.drop(columns=['Genre','Budget','Running Time']).rename(columns={'%± LW' : 'Top10 Gross Change','%± LW.1' : 'Overall Grross Change'}) 


# In[38]:


df.to_csv('WeeklyBoxoffice.csv', index=False)


# In[ ]:





# In[ ]:




