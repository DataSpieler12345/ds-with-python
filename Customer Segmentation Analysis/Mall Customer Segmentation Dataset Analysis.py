#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import all the required libraries
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings('ignore')


# In[2]:


#import the data
data = pd.read_csv("E:/DATA SETS/Mall_Customers.csv")
print("Data Loaded")


# In[3]:


data.head()


# # Univariate Analysis 
# 

# In[4]:


data.describe()


# In[5]:


sns.displot(data['Annual Income (k$)']);


# In[6]:


data.columns


# In[7]:


#another way to create it 
columns = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']

for i in columns:
    plt.figure()
    sns.displot(data[i])


# In[8]:


sns.kdeplot(data['Annual Income (k$)'], shade=True,hue=data['Gender']);


# In[9]:


columns = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']

for i in columns:
    plt.figure()
    sns.kdeplot(data[i], shade=True,hue=data['Gender']);


# In[10]:


columns = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']

for i in columns:
    plt.figure()
    sns.boxplot(data=data,x='Gender',y=data[i]);


# In[11]:


# Number of Males and Females
data['Gender'].value_counts()


# In[12]:


data['Gender'].value_counts(normalize = True)


# # Bivariate Analysis

# In[13]:


sns.scatterplot(data=data, x = 'Annual Income (k$)', y = 'Spending Score (1-100)' )


# In[14]:


#data=data.drop('CustomerID', axis=1)
sns.pairplot(data,hue = 'Gender')


# In[15]:


#groupby the data set by......
data.groupby(['Gender'])['Age', 'Annual Income (k$)', 'Spending Score (1-100)'].mean()


# In[16]:


#test the correlation
data.corr()


# In[17]:


#heatmap to see the correlation
sns.heatmap(data.corr(),annot=True,cmap='coolwarm')


# # Clustering - Univariate, Bivariate, Multivariate

# In[32]:


#KMean Algorithm
clustering1 = KMeans(n_clusters=3)


# In[33]:


clustering1.fit(data[['Annual Income (k$)']])


# In[34]:


# labels 0 to 7 
clustering1.labels_


# In[35]:


# add labels to the data frame to compare it
data['Income Cluster'] = clustering1.labels_
data.head()


# In[36]:


#how many are in the cluster Income? 
data['Income Cluster'].value_counts()


# In[37]:


#inertia distance
clustering1.inertia_


# In[38]:


intertia_scores=[]

for i in range(1,11):
    kmeans=KMeans(n_clusters=i)
    kmeans.fit(data[['Annual Income (k$)']])
    intertia_scores.append(kmeans.inertia_)
   


# In[39]:


# call all the scores
intertia_scores


# In[40]:


#plot it 
plt.plot(range(1,11),intertia_scores)


# In[41]:


data.columns


# In[42]:


#Group the data by
data.groupby('Income Cluster')['Age', 'Annual Income (k$)','Spending Score (1-100)'].mean()


# # Bivariate Clustering

# In[44]:


data.columns


# In[48]:


# KMeans Algorithm
clustering2 = KMeans(n_clusters = 5)
X = data[['Annual Income (k$)', 'Spending Score (1-100)']]
clustering2.fit(X)
data['Spending and Income Cluster'] = clustering2.labels_
data.head()


# In[49]:


intertia_scores2=[]

for i in range(1,11):
    kmeans2=KMeans(n_clusters=i)
    kmeans2.fit(data[['Annual Income (k$)', 'Spending Score (1-100)']])
    intertia_scores2.append(kmeans2.inertia_)
plt.plot(range(1,11),intertia_scores2)


# In[59]:



centers = pd.DataFrame(clustering2.cluster_centers_)
centers.columns = ['x','y']


# In[78]:


# scatterplot
plt.figure(figsize=(10,8))
plt.scatter(x = centers['x'], y = centers['y'],s=100,c='black',marker='*')
sns.scatterplot(data=data, x='Annual Income (k$)', y='Spending Score (1-100)', hue='Spending and Income Cluster', palette='tab10')
plt.savefig('clustering_bivariate.png')


# In[62]:


#cluster information %
pd.crosstab(data['Spending and Income Cluster'],data['Gender'],normalize='index')


# In[63]:


#cluster 4
data.groupby('Spending and Income Cluster')['Age', 'Annual Income (k$)','Spending Score (1-100)'].mean()


# # Multivariate clustering 

# In[64]:


from sklearn.preprocessing import StandardScaler


# In[65]:


scale = StandardScaler()


# In[66]:


data.head()


# In[68]:


#dummie DF
dff =pd.get_dummies(data,drop_first=True)
dff.head()


# In[69]:


dff.columns


# In[70]:


#the new DF
dff = dff[['Age', 'Annual Income (k$)', 'Spending Score (1-100)', 'Gender_Male']]
dff.head()


# In[73]:


dff = scale.fit_transform(dff)


# In[74]:


dff = pd.DataFrame(scale.fit_transform(dff))
dff.head()


# In[76]:


intertia_scores3=[]

for i in range(1,11):
    kmeans3=KMeans(n_clusters=i)
    kmeans3.fit(data[['Annual Income (k$)', 'Spending Score (1-100)']])
    intertia_scores3.append(kmeans3.inertia_)
plt.plot(range(1,11),intertia_scores3)


# In[77]:


data


# In[80]:


#clustering to CSV 
data.to_csv('Clustering.csv')
print('clustering csv file created')


# **By:** **DataSpieler12345**

# In[ ]:




