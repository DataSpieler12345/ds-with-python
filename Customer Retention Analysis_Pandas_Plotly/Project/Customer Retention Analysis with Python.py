#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go # for data visualization


# ### Registered Users table 

# In[2]:


users = pd.read_excel('user_purchase_data.xlsx', sheet_name='user_registration')
users.sample(15)


# In[3]:


users.shape


# In[4]:


users.isna().sum()


# In[5]:


users['userID'].nunique() == users.shape[0]


# In[6]:


users[users['userID'].duplicated()].shape[0]


# In[7]:


users['is_subscriber'].value_counts(dropna=False, normalize=True).plot(kind='bar')


# ### Mobile Orders table

# In[8]:


mobile = pd.read_excel('user_purchase_data.xlsx', sheet_name='mobile_orders')
mobile.sample(15)


# In[9]:


mobile.shape


# In[10]:


mobile.isna().sum()


# In[11]:


mobile[mobile['user_id'].duplicated()].shape[0]


# In[12]:


mobile.dtypes


# In[13]:


mobile['user_id'] = mobile['user_id'].astype('object')


# In[14]:


mobile.dtypes


# In[15]:


mobile['mobile_orders'].describe()


# In[16]:


mobile['mobile_orders'].plot(kind='hist', bins=130, range=[0,50])


# In[17]:


mobile[~mobile['user_id'].isin(users['userID'])].shape[0]


# In[18]:


mobile.loc[~mobile['user_id'].isin(users['userID']), 'user_id'].tolist()


# ### In-store Orders table 

# In[19]:


store = pd.read_excel('user_purchase_data.xlsx', sheet_name='in_store_orders')
store.sample(15)


# In[20]:


store.shape


# In[21]:


store.isna().sum()


# In[22]:


store['user_id'].nunique() == store.shape[0]


# In[23]:


store.dtypes


# In[24]:


store['user_id'] = store['user_id'].astype('object')


# In[25]:


store.dtypes


# In[26]:


store['in_store_orders'].describe()


# In[27]:


store['in_store_orders'].plot(kind='hist', bins=130, range=[0,200])


# In[28]:


store.loc[~mobile['user_id'].isin(users['userID']), 'user_id'].tolist()


# In[29]:


len(store.loc[~mobile['user_id'].isin(users['userID']), 'user_id'].tolist())


# ### DataFrame Manipulation

# In[30]:


users.rename(columns={'userID':'user_id'}, inplace=True)


# In[31]:


users


# In[32]:


users['user_category'] = ['Premium'if i=='Yes' else 'Free' for i in users['is_subscriber'].values]
users.drop(columns='is_subscriber', inplace=True)
users


# In[33]:


users['user_category'].value_counts()


# In[34]:


orders = pd.merge(users, mobile, how='left', on='user_id').merge(store, how='left', on='user_id')


# In[35]:


orders


# In[36]:


orders.isna().sum()


# In[37]:


for col in orders.columns[2:]:
    orders[col] = orders[col].fillna(0)
orders.head()


# In[38]:


orders.dtypes


# In[39]:


orders['total_orders'] = orders['mobile_orders'] + orders['in_store_orders']
orders['total_orders'] = orders['total_orders'].astype(int)
orders


# In[40]:


orders.drop(columns=['mobile_orders','in_store_orders'], inplace=True)


# In[41]:


orders


# In[42]:


orders.total_orders.describe()


# In[43]:


orders


# In[44]:


cat='Free'
min_orders=100

100*orders[(orders['user_category']==cat) & (orders['total_orders']>=min_orders)].shape[0]/\
(orders['user_category']==cat).sum()


# In[45]:


cat='Premium'
min_orders=1000

100*orders[(orders['user_category']==cat) & (orders['total_orders']>=min_orders)].shape[0]/\
(orders['user_category']==cat).sum()


# In[46]:


orders_bins = [0,1,2,3,4,5,6,7,8,10,12,15,20,25,30,35,40,45,50,55,60,70,80,90,100,120,
               140,160,180,200,250,300,350,400,450,500,550,600,700,800,900,1000,1100]


# In[47]:


len(orders_bins) #newcolumns


# In[48]:


for order_bin in orders_bins:
    orders['orders >= '+str(order_bin)] = [1 if i>=order_bin else 0 for 
                                           i in orders['total_orders'].values]
orders


# In[49]:


pd.set_option('display.max_columns', None)
orders.head(10)


# In[50]:


totals = orders.drop(columns=['user_id','total_orders'])
totals.head()


# In[51]:


totals.columns[1:]


# In[52]:


totals = totals.groupby('user_category')[totals.columns[1:]].sum().reset_index()


# In[53]:


totals


# In[54]:


pd.melt(totals, id_vars='user_category', value_vars=totals.columns[1:], var_name='orders_bins', value_name='registered_users')


# In[55]:


graph_df = pd.melt(totals, id_vars='user_category', value_vars=totals.columns[1:], var_name='orders_bins', value_name='registered_users')


# In[56]:


graph_df


# In[57]:


graph_df['min_orders'] = [int(i.split('>= ')[1]) for i in graph_df['orders_bins'].values]
graph_df.drop(columns='orders_bins', inplace=True)
graph_df


# In[58]:


baseline = 0
grouped_df = graph_df.loc[graph_df['min_orders'] == baseline].groupby('user_category')
graph_df['category_totals'] = grouped_df['registered_users'].max().loc[graph_df['user_category']].values


# In[59]:


graph_df


# In[60]:


graph_df['%_registered_users'] = graph_df['registered_users']/graph_df['category_totals']


# In[61]:


graph_df


# In[62]:


graph_df = graph_df.drop(columns=['registered_users','category_totals'])


# In[63]:


graph_df


# ### Data Visualization

# In[65]:


# Using Plotly
fig = go.Figure()

fig.add_trace(go.Scatter(x=graph_df.loc[graph_df['user_category']=='Free', 'min_orders'],
                         y=graph_df.loc[graph_df['user_category']=='Free', '%_registered_users'],
                             name= 'Free Customers'))


fig.show()


# In[67]:


baseline = 0 # Definir el valor de baseline
fig = go.Figure()

for i in graph_df['user_category'].unique():
    fig.add_trace(go.Scatter(x=graph_df.loc[graph_df['user_category']==i, 'min_orders'],
                             y=graph_df.loc[graph_df['user_category']==i, '%_registered_users'],
                             name= i+' Users',
                             hovertemplate='<b>%{y:.2%}</b>'))
    
fig.update_traces(mode='markers+lines')
fig.update_layout(hovermode='x unified', xaxis_title='Minimum Total Orders', 
                  yaxis={'title': '% of registered users who ordered '+str(baseline)+' + times',
                        'tickformat':',.0%'})

fig.show()


# In[74]:


baseline = 0 # Definir el valor de baseline
fig = go.Figure()

for i in graph_df['user_category'].unique():
    fig.add_trace(go.Scatter(x=graph_df.loc[graph_df['user_category']==i, 'min_orders'],
                             y=graph_df.loc[graph_df['user_category']==i, '%_registered_users'],
                             name= i+' Users',
                             hovertemplate='<b>%{y:.2%}</b>'))
    
fig.update_traces(mode='markers+lines')
fig.update_layout(hovermode='x unified', xaxis_title='Minimum Total Orders', 
                  yaxis={'title': '% of registered users who ordered '+str(baseline)+' + times',
                        'tickformat':',.0%'},
                  title={'text':'Retention Curve for Free vs. Premium Customers',
                         'y':0.85, 'x':0.465, 'xanchor':'center', 'yanchor':'middle'})

fig.show()


# In[75]:


baseline = 0 # Definir el valor de baseline
fig = go.Figure()

for i in graph_df['user_category'].unique():
    fig.add_trace(go.Scatter(x=graph_df.loc[graph_df['user_category']==i, 'min_orders'],
                             y=graph_df.loc[graph_df['user_category']==i, '%_registered_users'],
                             name= i+' Users',
                             hovertemplate='<b>%{y:.2%}</b>'))
    
fig.update_traces(mode='markers+lines')
fig.update_layout(hovermode='x unified', xaxis_title='Minimum Total Orders', 
                  yaxis={'title': '% of registered users who ordered '+str(baseline)+' + times',
                        'tickformat':',.0%'},
                  title={'text':'Retention Curve for Free vs. Premium Customers',
                         'y':0.85, 'x':0.465, 'xanchor':'center', 'yanchor':'middle'})

fig.update_xaxes(range=[baseline, 200])

fig.show()


# In[76]:


baseline = 0 # define the value of baseline
max_x_val = 200

fig = go.Figure()

for i in graph_df['user_category'].unique():
    fig.add_trace(go.Scatter(x=graph_df.loc[graph_df['user_category']==i, 'min_orders'],
                             y=graph_df.loc[graph_df['user_category']==i, '%_registered_users'],
                             name= i+' Users',
                             hovertemplate='<b>%{y:.2%}</b>'))
    
fig.update_traces(mode='markers+lines')
fig.update_layout(hovermode='x unified', xaxis_title='Minimum Total Orders', 
                  yaxis={'title': '% of registered users who ordered '+str(baseline)+' + times',
                        'tickformat':',.0%'},
                  title={'text':'Retention Curve for Free vs. Premium Customers',
                         'y':0.85, 'x':0.465, 'xanchor':'center', 'yanchor':'middle'})

fig.update_xaxes(range=[baseline, max_x_val])

fig.show()


# In[80]:


baseline = 0 # define the value of baseline
max_x_val = 50 # to 50

fig = go.Figure()

for i in graph_df['user_category'].unique():
    fig.add_trace(go.Scatter(x=graph_df.loc[graph_df['user_category']==i, 'min_orders'],
                             y=graph_df.loc[graph_df['user_category']==i, '%_registered_users'],
                             name= i+' Users',
                             hovertemplate='<b>%{y:.2%}</b>'))
    
fig.update_traces(mode='markers+lines')
fig.update_layout(hovermode='x unified', xaxis_title='Minimum Total Orders', 
                  yaxis={'title': '% of registered users who ordered '+str(baseline)+' + times',
                        'tickformat':',.0%'},
                  title={'text':'Retention Curve for Free vs. Premium Customers',
                         'y':0.85, 'x':0.465, 'xanchor':'center', 'yanchor':'middle'})

fig.update_xaxes(range=[baseline, max_x_val])
fig.update_yaxes(range=[-0.01, 1.01])

fig.show()


# In[82]:


baseline = 0 # define the value of baseline
max_x_val = 200

fig = go.Figure()

for i in graph_df['user_category'].unique():
    fig.add_trace(go.Scatter(x=graph_df.loc[graph_df['user_category']==i, 'min_orders'],
                             y=graph_df.loc[graph_df['user_category']==i, '%_registered_users'],
                             name= i+' Users',
                             hovertemplate='<b>%{y:.2%}</b>'))
    
fig.update_traces(mode='markers+lines')
fig.update_layout(hovermode='x unified', xaxis_title='Minimum Total Orders', 
                  yaxis={'title': '% of registered users who ordered '+str(baseline)+' + times',
                        'tickformat':',.0%'},
                  title={'text':'Retention Curve for Free vs. Premium Customers',
                         'y':0.85, 'x':0.465, 'xanchor':'center', 'yanchor':'middle'})

fig.update_xaxes(range=[baseline, max_x_val])
fig.update_yaxes(range=[-0.01, 1.01])

fig.write_html('E:\PYTHON\PYDASHBOARDS\Data Analyst Python Project Demo_Curstomer Retention Analysis_Pandas_Plotly\Plotly_graph')

fig.show()


# **made by** | **DataSpieler12345**

# In[ ]:




