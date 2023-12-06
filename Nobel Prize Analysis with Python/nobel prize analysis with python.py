#!/usr/bin/env python
# coding: utf-8

# <center><h1><b><font size="6">Nobel Prize Analysis with Python</font></b></h1></center>

# #### Packages

# In[24]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 


# ##### Load the data 

# In[3]:


url = "https://raw.githubusercontent.com/Adrian-Cancino/DataScience/main/Data/nobel.csv"
data = pd.read_csv(url)
data.head()


# #### overview of the data set 

# In[4]:


data.info()
#NaN values


# #### NaN values

# In[57]:


data.isnull().sum()


# In[59]:


data.dropna(axis=0, inplace=True)


# In[61]:


data.head()


# ### General knowledge of the set

# #### Total registered awards?

# In[62]:


display(len(data))


# #### How many awards have been won by men and how many by women?

# In[63]:


display(data['sex'].value_counts())


#  #### Which countries have won the most awards?

# In[64]:


display(data['birth_country'].value_counts().head(10))


# #### Wich category has the most awards?

# In[65]:


display(data['category'].value_counts().head(10))


# #### percentage of U.S. winners per decade?

# In[66]:


# add new column = usa_born_winner
data['usa_born_winner'] = data['birth_country'] == "United States of America"
data.head()


# In[67]:


# add another column called = decade
# np.floor = rounded to the nearest whole number
data['decade'] = (np.floor(data['year'] / 10) *10).astype(int)
data.head()


# #### Group the data

# In[68]:


prop_usa_winners = data.groupby('decade', as_index=False)['usa_born_winner'].mean()


# In[69]:


prop_usa_winners
# usa accumulates more awards over time


# #### Graphic the result

# In[70]:


from matplotlib.ticker import PercentFormatter

plt.rcParams['figure.figsize'] = [11, 7]
ax = sns.lineplot(x='decade', y='usa_born_winner', data=prop_usa_winners)
ax.yaxis.set_major_formatter(PercentFormatter())


# #### winning percentage between men and women in the different categories

# In[71]:


data['female_winner'] = data['sex'] == "Female"
print(data.head())


# #### Group the data

# #### the percentage / decade

# In[72]:


prop_female_winners = data.groupby(['decade', 'category'], as_index=False)['female_winner'].mean()


# In[73]:


prop_female_winners


# In[74]:


print(data['female_winner'].unique())


# In[75]:


import matplotlib.pyplot as plt

plt.hist(data['female_winner'])
plt.xlabel('Female Winner')
plt.ylabel('Count')
plt.title('Distribution of Female Winner')
plt.show()

import warnings

# Ignore all warnings
warnings.filterwarnings("ignore")


# In[76]:


ax = sns.lineplot(x='decade',
                  y='female_winner', 
                  data=data, 
                  hue='category')

ax.yaxis.set_major_formatter(PercentFormatter())


# #### winners by age

# In[78]:


data['birth_date'] = pd.to_datetime(data['birth_date'])

data['age'] = data['year'] - data['birth_date'].dt.year

data.head()


# #### Graphic Result

# In[80]:


ax = sns.lmplot(x='year',
                  y='age', 
                  data=data, 
                  lowess=True,
                 aspect=2,
                 line_kws={'color': 'black'})


# #### Age range of the winners in the different categories 

# In[81]:


ax = sns.lmplot(x='year',
                  y='age', 
                  data=data, 
                  lowess=True,
                 aspect=2,
                 line_kws={'color': 'black'},
               	 row='category')


# #### who is the oldest person to win the nobel prize and the youngest person to win the nobel prize

# In[83]:


display(data.nlargest(1, 'age'))

data.nsmallest(1, 'age')

