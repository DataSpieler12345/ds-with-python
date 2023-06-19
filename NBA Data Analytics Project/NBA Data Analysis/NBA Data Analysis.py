#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
pd.set_option('display.max_columns', None)

data = pd.read_excel('nba_player_data_cleaned.xlsx')


# In[3]:


data.sample(20)


# In[4]:


data.shape


# # Data cleaning & analysis preparation

# In[6]:


data.isna().sum() # there is no null values in the dataset 


# In[ ]:


# Drop the unusel columns = RANK, EFF


# In[7]:


data.drop(columns=['RANK','EFF'], inplace=True)


# In[8]:


data


# In[29]:


# Year Column 4 digits astype int, to identify the year
data['season_start_year'] = data['Year'].str[:4].astype(int)


# In[11]:


# teams , figure out: NOH | NOP
data.TEAM.unique()


# In[13]:


# teams = 30 and not 31
data.TEAM.nunique()


# In[14]:


data['TEAM'].replace(to_replace=['NOP','NOH'], value='NO', inplace=True)


# In[15]:


# check again | NO
data.TEAM.unique()


# In[18]:


# clean the Season_type column

data['Season_Type'].replace('Regular%20Season','RS', inplace=True)


# In[19]:


data


# In[22]:


# filter dataset with RS first
rs_df = data[data['Season_Type']=='RS']
rs_df


# In[23]:


# same with playoffs
playoffs_df = data[data['Season_Type']=='Playoffs']
playoffs_df


# In[40]:


#check the columns of the data DF
data.columns


# In[25]:


#Select the columns 
total_cols = ['MIN','FGM','FGA','FG3M','FG3A','FTM','FTA',
              'OREB','DREB','REB','AST','STL','BLK','TOV','PF','PTS']


# ### Wich player stats are correlated with each other?

# In[42]:


# Select only the numeric columns
data_numeric = data.select_dtypes(include='number')

# Calculating the correlation matrix
correlation_matrix = data_numeric.corr()
correlation_matrix


# In[64]:


data_per_min = data.groupby(['PLAYER_ID','PLAYER','Year'])[total_cols].sum().reset_index()
for col in data_per_min.columns[4:]:
    data_per_min[col] =  data_per_min[col]/data_per_min['MIN']

data_per_min['FG%'] =  data_per_min['FGM']/data_per_min['FGA']
data_per_min['3PT%'] =  data_per_min['FG3M']/data_per_min['FG3A']
data_per_min['FT%'] =  data_per_min['FTM']/data_per_min['FTA']
data_per_min['FG3A%'] =  data_per_min['FG3A']/data_per_min['FGA']
data_per_min['PTS/FGA'] =  data_per_min['PTS']/data_per_min['FGA']
data_per_min['FG3M/FGM'] =  data_per_min['FG3M']/data_per_min['FGM']
data_per_min['FTA/FGA'] =  data_per_min['FTA']/data_per_min['FGA']
data_per_min['TRU%'] = 0.5*data_per_min['PTS']/(data_per_min['FGA']+0.475*data_per_min['FTA'])
data_per_min['AST_TOV'] =  data_per_min['AST']/data_per_min['TOV']

data_per_min = data_per_min[data_per_min['MIN']>=50]
data_per_min.drop(columns='PLAYER_ID', inplace=True)

data_per_min


# In[68]:


fig = px.imshow(data_numeric.corr())
fig.show()


# In[57]:


(data_per_min['MIN']>=500).mean()


# ### How are minutes played distributed?

# In[73]:


fig = px.histogram(x=rs_df['MIN'], histnorm='percent')
fig.show()


# In[72]:


fig = px.histogram(x=playoffs_df['MIN'], histnorm='percent')
fig.show()


# In[89]:


def hist_data(df=rs_df, min_MIN=0, min_GP=0):
    return df.loc[(df['MIN']>=min_MIN) & (df['GP']>=min_GP), 'MIN']/\
    df.loc[(df['MIN']>=min_MIN) & (df['GP']>=min_GP), 'GP']


# In[90]:


fig = go.Figure()
fig.add_trace(go.Histogram(x=hist_data(rs_df,50,5), histnorm='percent', name='RS', xbins={'start':0,'end':45,'size':1}))
fig.add_trace(go.Histogram(x=hist_data(playoffs_df,5,1), histnorm='percent', name='Playoffs', xbins={'start':0,'end':45,'size':1}))

fig.update_layout(barmode='overlay')
fig.update_traces(opacity=0.5)
fig.show()


# In[85]:


# 75 % same values 
((hist_data(rs_df,50,5)>=12)&(hist_data(rs_df,50,5)<=34)).mean()


# ### has the game changed over the past 10 years?

# In[105]:


change_df = data.groupby('season_start_year')[total_cols].sum().reset_index()
change_df['POSS_est'] = change_df['FGA']-change_df['OREB']+change_df['TOV']+0.44*change_df['FTA']
change_df = change_df[list(change_df.columns[0:2])+['POSS_est']+list(change_df.columns[2:-1])]


change_df['FG%'] = change_df['FGM']/change_df['FGA']
change_df['3PT%'] = change_df['FG3M']/change_df['FG3A']
change_df['FT%'] = change_df['FTM']/change_df['FTA']
change_df['FG3A%'] = change_df['FG3A']/change_df['FGA']
change_df['PTS/FGA'] = change_df['PTS']/change_df['FGA']
change_df['FG3M/FGM'] = change_df['FG3M']/change_df['FGM']
change_df['FTA/FGA'] = change_df['FTA']/change_df['FGA']
change_df['TRU%'] = 0.5*change_df['PTS']/(change_df['FGA']+0.475*change_df['FTA'])
change_df['AST_TOV'] =  change_df['AST']/change_df['TOV']

change_df


# In[100]:


change_per48_df = change_df.copy()
for col in change_per48_df.columns[2:18]:
    change_per48_df[col] = (change_per48_df[col]/change_per48_df['MIN'])*48*5
    
change_per48_df.drop(columns='MIN', inplace=True)

fig = go.Figure()
for col in change_per48_df.columns[1:]:
    fig.add_trace(go.Scatter(x=change_per48_df['season_start_year'],
                             y=change_per48_df[col], name=col))

fig.show()


# In[103]:


change_per100_df = change_df.copy()


for col in change_per100_df.columns[3:18]:
    change_per100_df[col] = (change_per100_df[col]/change_per100_df['POSS_est'])*100
    
change_per100_df.drop(columns=['MIN','POSS_est'], inplace=True)
change_per100_df

fig = go.Figure()

for col in change_per100_df.columns[1:]:
    fig.add_trace(go.Scatter(x=change_per100_df['season_start_year'],
                             y=change_per100_df[col], name=col))

fig.show()


# ### Comparte RS to Playoffs

# In[109]:


rs_change_df = rs_df.groupby('season_start_year')[total_cols].sum().reset_index()
playoffs_change_df = playoffs_df.groupby('season_start_year')[total_cols].sum().reset_index()

for i in [rs_change_df, playoffs_change_df]:
    i['POSS_est'] = i['FGA']-i['OREB']+i['TOV']+0.44*i['FTA']
    i['POSS_per_48'] = (i['POSS_est']/i['MIN'])*48*5
    
    i['FG%'] = i['FGM']/i['FGA']
    i['3PT%'] = i['FG3M']/i['FG3A']
    i['FT%'] = i['FTM']/i['FTA']
    i['FG3A%'] = i['FG3A']/i['FGA']
    i['PTS/FGA'] = i['PTS']/i['FGA']
    i['FG3M/FGM'] = i['FG3M']/i['FGM']
    i['FTA/FGA'] = i['FTA']/i['FGA']
    i['TRU%'] = 0.5*i['PTS']/(i['FGA']+0.475*i['FTA'])
    i['AST_TOV'] =  i['AST']/i['TOV']
    for col in total_cols:
        i[col] = 100*i[col]/i['POSS_est']
    i.drop(columns=['MIN','POSS_est'], inplace=True)

rs_change_df


# In[115]:


comp_change_df = round(100*(playoffs_change_df-rs_change_df)/rs_change_df,2)
comp_change_df['season_start_year'] = list(range(2012,2022))
comp_change_df


# In[117]:


fig = go.Figure()
for col in comp_change_df.columns[1:]:
    fig.add_trace(go.Scatter(x=comp_change_df['season_start_year'],
                             y=comp_change_df[col], name=col))
    
fig.show()


# **Made by** | **DataSpieler12345**
