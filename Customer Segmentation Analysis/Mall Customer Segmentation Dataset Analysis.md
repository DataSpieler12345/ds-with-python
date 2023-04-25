```python
# import all the required libraries
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings('ignore')
```


```python
#import the data
data = pd.read_csv("E:/DATA SETS/Mall_Customers.csv")
print("Data Loaded")
```

    Data Loaded
    


```python
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CustomerID</th>
      <th>Gender</th>
      <th>Age</th>
      <th>Annual Income (k$)</th>
      <th>Spending Score (1-100)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Male</td>
      <td>19</td>
      <td>15</td>
      <td>39</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Male</td>
      <td>21</td>
      <td>15</td>
      <td>81</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Female</td>
      <td>20</td>
      <td>16</td>
      <td>6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Female</td>
      <td>23</td>
      <td>16</td>
      <td>77</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Female</td>
      <td>31</td>
      <td>17</td>
      <td>40</td>
    </tr>
  </tbody>
</table>
</div>



# Univariate Analysis 



```python
data.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CustomerID</th>
      <th>Age</th>
      <th>Annual Income (k$)</th>
      <th>Spending Score (1-100)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>200.000000</td>
      <td>200.000000</td>
      <td>200.000000</td>
      <td>200.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>100.500000</td>
      <td>38.850000</td>
      <td>60.560000</td>
      <td>50.200000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>57.879185</td>
      <td>13.969007</td>
      <td>26.264721</td>
      <td>25.823522</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>18.000000</td>
      <td>15.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>50.750000</td>
      <td>28.750000</td>
      <td>41.500000</td>
      <td>34.750000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>100.500000</td>
      <td>36.000000</td>
      <td>61.500000</td>
      <td>50.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>150.250000</td>
      <td>49.000000</td>
      <td>78.000000</td>
      <td>73.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>200.000000</td>
      <td>70.000000</td>
      <td>137.000000</td>
      <td>99.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
sns.displot(data['Annual Income (k$)']);
```


    
![png](output_5_0.png)
    



```python
data.columns
```




    Index(['CustomerID', 'Gender', 'Age', 'Annual Income (k$)',
           'Spending Score (1-100)'],
          dtype='object')




```python
#another way to create it 
columns = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']

for i in columns:
    plt.figure()
    sns.displot(data[i])
```


    <Figure size 432x288 with 0 Axes>



    
![png](output_7_1.png)
    



    <Figure size 432x288 with 0 Axes>



    
![png](output_7_3.png)
    



    <Figure size 432x288 with 0 Axes>



    
![png](output_7_5.png)
    



```python
sns.kdeplot(data['Annual Income (k$)'], shade=True,hue=data['Gender']);
```


    
![png](output_8_0.png)
    



```python
columns = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']

for i in columns:
    plt.figure()
    sns.kdeplot(data[i], shade=True,hue=data['Gender']);
```


    
![png](output_9_0.png)
    



    
![png](output_9_1.png)
    



    
![png](output_9_2.png)
    



```python
columns = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']

for i in columns:
    plt.figure()
    sns.boxplot(data=data,x='Gender',y=data[i]);
```


    
![png](output_10_0.png)
    



    
![png](output_10_1.png)
    



    
![png](output_10_2.png)
    



```python
# Number of Males and Females
data['Gender'].value_counts()
```




    Female    112
    Male       88
    Name: Gender, dtype: int64




```python
data['Gender'].value_counts(normalize = True)
```




    Female    0.56
    Male      0.44
    Name: Gender, dtype: float64



# Bivariate Analysis


```python
sns.scatterplot(data=data, x = 'Annual Income (k$)', y = 'Spending Score (1-100)' )
```




    <AxesSubplot:xlabel='Annual Income (k$)', ylabel='Spending Score (1-100)'>




    
![png](output_14_1.png)
    



```python
#data=data.drop('CustomerID', axis=1)
sns.pairplot(data,hue = 'Gender')
```




    <seaborn.axisgrid.PairGrid at 0x1d73b69f940>




    
![png](output_15_1.png)
    



```python
#groupby the data set by......
data.groupby(['Gender'])['Age', 'Annual Income (k$)', 'Spending Score (1-100)'].mean()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Annual Income (k$)</th>
      <th>Spending Score (1-100)</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>38.098214</td>
      <td>59.250000</td>
      <td>51.526786</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>39.806818</td>
      <td>62.227273</td>
      <td>48.511364</td>
    </tr>
  </tbody>
</table>
</div>




```python
#test the correlation
data.corr()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CustomerID</th>
      <th>Age</th>
      <th>Annual Income (k$)</th>
      <th>Spending Score (1-100)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>CustomerID</th>
      <td>1.000000</td>
      <td>-0.026763</td>
      <td>0.977548</td>
      <td>0.013835</td>
    </tr>
    <tr>
      <th>Age</th>
      <td>-0.026763</td>
      <td>1.000000</td>
      <td>-0.012398</td>
      <td>-0.327227</td>
    </tr>
    <tr>
      <th>Annual Income (k$)</th>
      <td>0.977548</td>
      <td>-0.012398</td>
      <td>1.000000</td>
      <td>0.009903</td>
    </tr>
    <tr>
      <th>Spending Score (1-100)</th>
      <td>0.013835</td>
      <td>-0.327227</td>
      <td>0.009903</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
#heatmap to see the correlation
sns.heatmap(data.corr(),annot=True,cmap='coolwarm')
```




    <AxesSubplot:>




    
![png](output_18_1.png)
    


# Clustering - Univariate, Bivariate, Multivariate


```python
#KMean Algorithm
clustering1 = KMeans(n_clusters=3)
```


```python
clustering1.fit(data[['Annual Income (k$)']])
```




    KMeans(n_clusters=3)




```python
# labels 0 to 7 
clustering1.labels_
```




    array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
           2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
           2, 2])




```python
# add labels to the data frame to compare it
data['Income Cluster'] = clustering1.labels_
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CustomerID</th>
      <th>Gender</th>
      <th>Age</th>
      <th>Annual Income (k$)</th>
      <th>Spending Score (1-100)</th>
      <th>Income Cluster</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Male</td>
      <td>19</td>
      <td>15</td>
      <td>39</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Male</td>
      <td>21</td>
      <td>15</td>
      <td>81</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Female</td>
      <td>20</td>
      <td>16</td>
      <td>6</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Female</td>
      <td>23</td>
      <td>16</td>
      <td>77</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Female</td>
      <td>31</td>
      <td>17</td>
      <td>40</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
#how many are in the cluster Income? 
data['Income Cluster'].value_counts()
```




    0    90
    1    74
    2    36
    Name: Income Cluster, dtype: int64




```python
#inertia distance
clustering1.inertia_
```




    23517.330930930926




```python
intertia_scores=[]

for i in range(1,11):
    kmeans=KMeans(n_clusters=i)
    kmeans.fit(data[['Annual Income (k$)']])
    intertia_scores.append(kmeans.inertia_)
   
```


```python
# call all the scores
intertia_scores
```




    [137277.28000000003,
     48660.88888888889,
     23517.330930930926,
     13278.112713472487,
     8481.496190476191,
     5050.904761904763,
     3949.2756132756135,
     2827.308424908425,
     2388.1887279387283,
     1778.9230380730387]




```python
#plot it 
plt.plot(range(1,11),intertia_scores)
```




    [<matplotlib.lines.Line2D at 0x1d73d0246a0>]




    
![png](output_28_1.png)
    



```python
data.columns
```




    Index(['CustomerID', 'Gender', 'Age', 'Annual Income (k$)',
           'Spending Score (1-100)', 'Income Cluster'],
          dtype='object')




```python
#Group the data by
data.groupby('Income Cluster')['Age', 'Annual Income (k$)','Spending Score (1-100)'].mean()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Annual Income (k$)</th>
      <th>Spending Score (1-100)</th>
    </tr>
    <tr>
      <th>Income Cluster</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38.722222</td>
      <td>67.088889</td>
      <td>50.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>39.500000</td>
      <td>33.486486</td>
      <td>50.229730</td>
    </tr>
    <tr>
      <th>2</th>
      <td>37.833333</td>
      <td>99.888889</td>
      <td>50.638889</td>
    </tr>
  </tbody>
</table>
</div>



# Bivariate Clustering


```python
data.columns
```




    Index(['CustomerID', 'Gender', 'Age', 'Annual Income (k$)',
           'Spending Score (1-100)', 'Income Cluster'],
          dtype='object')




```python
# KMeans Algorithm
clustering2 = KMeans(n_clusters = 5)
X = data[['Annual Income (k$)', 'Spending Score (1-100)']]
clustering2.fit(X)
data['Spending and Income Cluster'] = clustering2.labels_
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CustomerID</th>
      <th>Gender</th>
      <th>Age</th>
      <th>Annual Income (k$)</th>
      <th>Spending Score (1-100)</th>
      <th>Income Cluster</th>
      <th>Spending and Income Cluster</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Male</td>
      <td>19</td>
      <td>15</td>
      <td>39</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Male</td>
      <td>21</td>
      <td>15</td>
      <td>81</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Female</td>
      <td>20</td>
      <td>16</td>
      <td>6</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Female</td>
      <td>23</td>
      <td>16</td>
      <td>77</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Female</td>
      <td>31</td>
      <td>17</td>
      <td>40</td>
      <td>1</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
intertia_scores2=[]

for i in range(1,11):
    kmeans2=KMeans(n_clusters=i)
    kmeans2.fit(data[['Annual Income (k$)', 'Spending Score (1-100)']])
    intertia_scores2.append(kmeans2.inertia_)
plt.plot(range(1,11),intertia_scores2)
```




    [<matplotlib.lines.Line2D at 0x1d740752af0>]




    
![png](output_34_1.png)
    



```python

centers = pd.DataFrame(clustering2.cluster_centers_)
centers.columns = ['x','y']
```


```python
# scatterplot
plt.figure(figsize=(10,8))
plt.scatter(x = centers['x'], y = centers['y'],s=100,c='black',marker='*')
sns.scatterplot(data=data, x='Annual Income (k$)', y='Spending Score (1-100)', hue='Spending and Income Cluster', palette='tab10')
plt.savefig('clustering_bivariate.png')
```


    
![png](output_36_0.png)
    



```python
#cluster information %
pd.crosstab(data['Spending and Income Cluster'],data['Gender'],normalize='index')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Gender</th>
      <th>Female</th>
      <th>Male</th>
    </tr>
    <tr>
      <th>Spending and Income Cluster</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.590909</td>
      <td>0.409091</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.592593</td>
      <td>0.407407</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.457143</td>
      <td>0.542857</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.538462</td>
      <td>0.461538</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.608696</td>
      <td>0.391304</td>
    </tr>
  </tbody>
</table>
</div>




```python
#cluster 4
data.groupby('Spending and Income Cluster')['Age', 'Annual Income (k$)','Spending Score (1-100)'].mean()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Annual Income (k$)</th>
      <th>Spending Score (1-100)</th>
    </tr>
    <tr>
      <th>Spending and Income Cluster</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>25.272727</td>
      <td>25.727273</td>
      <td>79.363636</td>
    </tr>
    <tr>
      <th>1</th>
      <td>42.716049</td>
      <td>55.296296</td>
      <td>49.518519</td>
    </tr>
    <tr>
      <th>2</th>
      <td>41.114286</td>
      <td>88.200000</td>
      <td>17.114286</td>
    </tr>
    <tr>
      <th>3</th>
      <td>32.692308</td>
      <td>86.538462</td>
      <td>82.128205</td>
    </tr>
    <tr>
      <th>4</th>
      <td>45.217391</td>
      <td>26.304348</td>
      <td>20.913043</td>
    </tr>
  </tbody>
</table>
</div>



# Multivariate clustering 


```python
from sklearn.preprocessing import StandardScaler
```


```python
scale = StandardScaler()
```


```python
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CustomerID</th>
      <th>Gender</th>
      <th>Age</th>
      <th>Annual Income (k$)</th>
      <th>Spending Score (1-100)</th>
      <th>Income Cluster</th>
      <th>Spending and Income Cluster</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Male</td>
      <td>19</td>
      <td>15</td>
      <td>39</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Male</td>
      <td>21</td>
      <td>15</td>
      <td>81</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Female</td>
      <td>20</td>
      <td>16</td>
      <td>6</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Female</td>
      <td>23</td>
      <td>16</td>
      <td>77</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Female</td>
      <td>31</td>
      <td>17</td>
      <td>40</td>
      <td>1</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
#dummie DF
dff =pd.get_dummies(data,drop_first=True)
dff.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CustomerID</th>
      <th>Age</th>
      <th>Annual Income (k$)</th>
      <th>Spending Score (1-100)</th>
      <th>Income Cluster</th>
      <th>Spending and Income Cluster</th>
      <th>Gender_Male</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>19</td>
      <td>15</td>
      <td>39</td>
      <td>1</td>
      <td>4</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>21</td>
      <td>15</td>
      <td>81</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>20</td>
      <td>16</td>
      <td>6</td>
      <td>1</td>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>23</td>
      <td>16</td>
      <td>77</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>31</td>
      <td>17</td>
      <td>40</td>
      <td>1</td>
      <td>4</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
dff.columns
```




    Index(['CustomerID', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)',
           'Income Cluster', 'Spending and Income Cluster', 'Gender_Male'],
          dtype='object')




```python
#the new DF
dff = dff[['Age', 'Annual Income (k$)', 'Spending Score (1-100)', 'Gender_Male']]
dff.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Annual Income (k$)</th>
      <th>Spending Score (1-100)</th>
      <th>Gender_Male</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>19</td>
      <td>15</td>
      <td>39</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>15</td>
      <td>81</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>20</td>
      <td>16</td>
      <td>6</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23</td>
      <td>16</td>
      <td>77</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>31</td>
      <td>17</td>
      <td>40</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
dff = scale.fit_transform(dff)
```


```python
dff = pd.DataFrame(scale.fit_transform(dff))
dff.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-1.424569</td>
      <td>-1.738999</td>
      <td>-0.434801</td>
      <td>1.128152</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-1.281035</td>
      <td>-1.738999</td>
      <td>1.195704</td>
      <td>1.128152</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-1.352802</td>
      <td>-1.700830</td>
      <td>-1.715913</td>
      <td>-0.886405</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-1.137502</td>
      <td>-1.700830</td>
      <td>1.040418</td>
      <td>-0.886405</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.563369</td>
      <td>-1.662660</td>
      <td>-0.395980</td>
      <td>-0.886405</td>
    </tr>
  </tbody>
</table>
</div>




```python
intertia_scores3=[]

for i in range(1,11):
    kmeans3=KMeans(n_clusters=i)
    kmeans3.fit(data[['Annual Income (k$)', 'Spending Score (1-100)']])
    intertia_scores3.append(kmeans3.inertia_)
plt.plot(range(1,11),intertia_scores3)
```




    [<matplotlib.lines.Line2D at 0x1d7439ec430>]




    
![png](output_48_1.png)
    



```python
data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CustomerID</th>
      <th>Gender</th>
      <th>Age</th>
      <th>Annual Income (k$)</th>
      <th>Spending Score (1-100)</th>
      <th>Income Cluster</th>
      <th>Spending and Income Cluster</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Male</td>
      <td>19</td>
      <td>15</td>
      <td>39</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Male</td>
      <td>21</td>
      <td>15</td>
      <td>81</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Female</td>
      <td>20</td>
      <td>16</td>
      <td>6</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Female</td>
      <td>23</td>
      <td>16</td>
      <td>77</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Female</td>
      <td>31</td>
      <td>17</td>
      <td>40</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>195</th>
      <td>196</td>
      <td>Female</td>
      <td>35</td>
      <td>120</td>
      <td>79</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>196</th>
      <td>197</td>
      <td>Female</td>
      <td>45</td>
      <td>126</td>
      <td>28</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>197</th>
      <td>198</td>
      <td>Male</td>
      <td>32</td>
      <td>126</td>
      <td>74</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>198</th>
      <td>199</td>
      <td>Male</td>
      <td>32</td>
      <td>137</td>
      <td>18</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>199</th>
      <td>200</td>
      <td>Male</td>
      <td>30</td>
      <td>137</td>
      <td>83</td>
      <td>2</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
<p>200 rows × 7 columns</p>
</div>




```python
#clustering to CSV 
data.to_csv('Clustering.csv')
print('clustering csv file created')
```

    clustering csv file created
    

**By:** **DataSpieler12345**


```python

```
