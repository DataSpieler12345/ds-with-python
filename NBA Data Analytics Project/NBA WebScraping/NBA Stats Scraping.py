#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
pd.set_option('display.max.columns', None) # so we can see all columns in a wide DataFrame 
import time 
import numpy as np


# In[2]:


test_url = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=Totals&Scope=S&Season=2012-13&SeasonType=Regular%20Season&StatCategory=PTS'


# In[3]:


r = requests.get(url=test_url).json()


# In[4]:


table_headers = r['resultSet']['headers']


# In[5]:


table_headers


# In[6]:


pd.DataFrame(r['resultSet']['rowSet'], columns=table_headers)


# In[7]:


temp_df1 = pd.DataFrame(r['resultSet']['rowSet'], columns=table_headers)
temp_df2 = pd.DataFrame({'Year':['2012-13' for i in range(len(temp_df1))],
                         'Season_type':['Regular%20Season' for i in range(len(temp_df1))]})

temp_df3 = pd.concat([temp_df2, temp_df1], axis=1)
temp_df3


# In[ ]:


del temp_df1, temp_df2, temp_df3


# In[8]:


df_cols = ['Year','Season_Type'] + table_headers


# In[10]:


df_cols


# In[12]:


pd.DataFrame(columns=df_cols)


# In[14]:


headers1 = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8,de;q=0.7',
    'Connection': 'keep-alive',
    'Host': 'stats.nba.com',
    'Origin': 'https://www.nba.com',
    'Referer': 'https://www.nba.com/',
    'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': 'Windows',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}


# In[16]:


df = pd.DataFrame(columns=df_cols)
season_types = ['Regular%20Season', 'Playoffs']
years = ['2012-13','2013-14','2014-15','2015-16','2016-17','2017-18','2018-19','2019-20','2020-21','2021-22']

begin_loop = time.time()

for y in years:
    for s in season_types:
        api_url = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=Totals&Scope=S&Season='+y+'&SeasonType='+s+'&StatCategory=PTS'
        r = requests.get(url=api_url, headers=headers1).json()
        temp_df1 = pd.DataFrame(r['resultSet']['rowSet'], columns=table_headers)
        temp_df2 = pd.DataFrame({'Year':[y for i in range(len(temp_df1))],
                                 'Season_type':[s for i in range(len(temp_df1))]})
        temp_df3 = pd.concat([temp_df2, temp_df1], axis=1)
        df = pd.concat([df, temp_df3], axis=0)
        print(f'Finished scraping data for the {y} {s}.')
        lag = np.random.uniform(low=5,high=40)
        print(f'...waiting {round(lag,1)} seconds')
        time.sleep(lag)

print(f'Process completed! Total run time: {round((time.time()-begin_loop)/60,2)}')
                                            
df.to_excel('nba_player_data.xlsx', index=False)


# In[17]:


df

