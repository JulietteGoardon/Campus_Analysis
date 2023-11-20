#!/usr/bin/env python
# coding: utf-8

# In[44]:


import pandas as pd


# In[45]:


import numpy as np 


# In[46]:


population = pd.read_csv("/Users/juliettegoardon/Desktop/SQL Project/population_by_age_group.csv")
""" https://www.kaggle.com/datasets/elmoallistair/population-by-age-group-2021/ """


# In[47]:


population


# In[48]:


population_EU = population.loc[population["Country"].isin(['Germany','Austria', "Spain", "Finland","Romania", "Sweden", "Latvia", "Estonia", "France", "Czechia", "Belgium", "Denmark", "Greece", "Bulgaria", "Luxembourg", "Lithuania", "Hungary", "Italy", "Netherlands", "Poland", "Croatia", "Slovenia", "Portugal", "Slovakia","Cyprus", "Ireland", "Malta"])]
population_EU


# In[49]:


population_EU = population_EU.sort_values(by='Country').reset_index(drop=True)
population_EU


# In[50]:


population_EU.columns


# In[51]:


population_EU = population_EU[["Country",'15-24 years','25-64 years']]
population_EU


# In[52]:


import os  
os.makedirs('/Users/juliettegoardon/Desktop/SQL-Project/Created_CSV', exist_ok=True)  
population_EU.to_csv('/Users/juliettegoardon/Desktop/SQL-Project/Created_CSV/population_EU.csv')


# In[53]:


""" MOVING ON TO: THE GDP """


# In[54]:


GDP = pd.read_csv("/Users/juliettegoardon/Desktop/SQL-Project/Countries_GDP.csv")

""" https://www.kaggle.com/datasets/rajkumarpandey02/gdp-in-usd-per-capita-income-by-country """


# In[55]:


GDP


# In[56]:


GDP.columns


# In[57]:


GDP = GDP.rename(columns={'Country/Territory': 'Country'})


# In[67]:


GDP_EU = GDP.loc[GDP["Country"].isin(['Germany','Austria', "Spain", "Finland","Romania", "Sweden", "Latvia", "Estonia", "France", "Czechia", "Belgium", "Denmark", "Greece", "Bulgaria", "Luxembourg", "Lithuania", "Hungary", "Italy", "Netherlands", "Poland", "Croatia", "Slovenia", "Portugal", "Slovakia", "Czech Republic", "Cyprus", "Malta", "Ireland"])]
GDP_EU


# In[68]:


GDP_EU.shape


# In[69]:


GDP_EU = GDP_EU.sort_values(by='Country').reset_index(drop=True)
GDP_EU


# In[70]:


GDP_EU = GDP_EU[['Country', 'IMF']]


# In[71]:


GDP_EU


# In[72]:


import os  
os.makedirs('/Users/juliettegoardon/Desktop/SQL-Project/Created_CSV', exist_ok=True)  
GDP_EU.to_csv('/Users/juliettegoardon/Desktop/SQL-Project/Created_CSV/GDP_EU.csv')


# In[64]:


""" MOVING ON TO: FUTURE EMPLOYMENT GROWTH IN HIGH TECH """


# In[65]:


Growth = pd.read_csv("/Users/juliettegoardon/Desktop/SQL-Project/Employment growth in Whole high-tech economy in 2022-2035.csv")

""" https://www.cedefop.europa.eu/en/tools/skills-intelligence/employment-growth-high-tech-economy?country=EU27&year=2022-2035#2 """


# In[66]:


Growth


# In[76]:


Growth_EU = Growth[Growth['Countries'] != 'EU27'].reset_index(drop=True)
Growth_EU


# In[77]:


Growth_EU = Growth_EU.rename(columns={'Countries': 'Country'})
Growth_EU


# In[80]:


Growth_EU = Growth_EU.sort_values(by='Country').reset_index(drop=True)
Growth_EU


# In[81]:


Growth_EU = Growth_EU[["Country", "Value"]]
Growth_EU


# In[82]:


import os  
os.makedirs('/Users/juliettegoardon/Desktop/SQL-Project/Created_CSV', exist_ok=True)  
Growth_EU.to_csv('/Users/juliettegoardon/Desktop/SQL-Project/Created_CSV/Growth_EU.csv')


# In[83]:


""" MOVING ON TO: EMPLOYMENT WITH BASIC IT SKILLS """


# In[84]:


Skills = pd.read_csv("/Users/juliettegoardon/Desktop/SQL-Project/Share of All in employment in 2021 with above basic digital skills across European countries.csv")

"""https://www.cedefop.europa.eu/en/tools/skills-intelligence/digital-skills-level?year=2021"""


# In[85]:


Skills


# In[86]:


Skills_EU = Skills[Skills['Countries'] != 'EU27'].reset_index(drop=True)
Skills_EU


# In[87]:


Skills_EU = Skills_EU.rename(columns={'Countries': 'Country'})
Skills_EU


# In[88]:


Skills_EU = Skills_EU.sort_values(by='Country').reset_index(drop=True)
Skills_EU


# In[89]:


Skills_EU = Skills_EU[["Indicator","Country", "Value"]]
Skills_EU


# In[90]:


import os  
os.makedirs('/Users/juliettegoardon/Desktop/SQL-Project/Created_CSV', exist_ok=True)  
Growth_EU.to_csv('/Users/juliettegoardon/Desktop/SQL-Project/Created_CSV/Skills_EU.csv')


# In[ ]:




