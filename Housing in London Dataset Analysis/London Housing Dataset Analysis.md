### LONDON HOUSING DATASET

This dataset is primarily centerd around the housing market of London. It contains a lot of additional relevant data:

* Monthly average house prices

* Yearly number of houses sold

* Monthly number of crimes commited


The data used here is from year 1995 to 2019 of each different area.

This data is available as a CSV file, downloaded from Kaggle.

We will analyze this data using the Pandas DataFrame.

Here, random sets of questions are given for which we have to fin correct results.

This project is for beginners and for those who want to know how we analyze big data with Python.


```python
#import pandas lib
import pandas as pd
```


```python
#import the dataset
data = pd.read_csv(r"E:\DATA SETS\London Housing Data.csv")
print("Dataset imported")
```

    Dataset imported
    


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
      <th>date</th>
      <th>area</th>
      <th>average_price</th>
      <th>code</th>
      <th>houses_sold</th>
      <th>no_of_crimes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/1995</td>
      <td>city of london</td>
      <td>91449</td>
      <td>E09000001</td>
      <td>17.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2/1/1995</td>
      <td>city of london</td>
      <td>82203</td>
      <td>E09000001</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3/1/1995</td>
      <td>city of london</td>
      <td>79121</td>
      <td>E09000001</td>
      <td>14.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4/1/1995</td>
      <td>city of london</td>
      <td>77101</td>
      <td>E09000001</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5/1/1995</td>
      <td>city of london</td>
      <td>84409</td>
      <td>E09000001</td>
      <td>10.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>13544</th>
      <td>9/1/2019</td>
      <td>england</td>
      <td>249942</td>
      <td>E92000001</td>
      <td>64605.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13545</th>
      <td>10/1/2019</td>
      <td>england</td>
      <td>249376</td>
      <td>E92000001</td>
      <td>68677.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13546</th>
      <td>11/1/2019</td>
      <td>england</td>
      <td>248515</td>
      <td>E92000001</td>
      <td>67814.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13547</th>
      <td>12/1/2019</td>
      <td>england</td>
      <td>250410</td>
      <td>E92000001</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13548</th>
      <td>1/1/2020</td>
      <td>england</td>
      <td>247355</td>
      <td>E92000001</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>13549 rows × 6 columns</p>
</div>




```python
# df.count()
data.count()
```




    date             13549
    area             13549
    average_price    13549
    code             13549
    houses_sold      13455
    no_of_crimes      7439
    dtype: int64




```python
# df.isnull().sum()
data.isnull().sum()
```




    date                0
    area                0
    average_price       0
    code                0
    houses_sold        94
    no_of_crimes     6110
    dtype: int64




```python
# Import seaborn as sns
# Import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
```


```python
# sns.heatmap(df.isnull())
sns.heatmap(data.isnull())
```




    <AxesSubplot:>




    
![png](output_8_1.png)
    


### Convert the Datatype of 'Date' column to Date-Time format


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
      <th>date</th>
      <th>area</th>
      <th>average_price</th>
      <th>code</th>
      <th>houses_sold</th>
      <th>no_of_crimes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/1995</td>
      <td>city of london</td>
      <td>91449</td>
      <td>E09000001</td>
      <td>17.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2/1/1995</td>
      <td>city of london</td>
      <td>82203</td>
      <td>E09000001</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3/1/1995</td>
      <td>city of london</td>
      <td>79121</td>
      <td>E09000001</td>
      <td>14.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4/1/1995</td>
      <td>city of london</td>
      <td>77101</td>
      <td>E09000001</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5/1/1995</td>
      <td>city of london</td>
      <td>84409</td>
      <td>E09000001</td>
      <td>10.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
#data.dtypes
data.dtypes # date column is an object datatype
```




    date              object
    area              object
    average_price      int64
    code              object
    houses_sold      float64
    no_of_crimes     float64
    dtype: object




```python
#data.date = pd.to_datetime(data.date)
data.date = pd.to_datetime(data.date)
print('Date field type updated')
```

    Date field type updated
    


```python
#check data.dtypes
data.dtypes
```




    date             datetime64[ns]
    area                     object
    average_price             int64
    code                     object
    houses_sold             float64
    no_of_crimes            float64
    dtype: object



### Add a new column "year" in the dataframe, which contains years only


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
      <th>date</th>
      <th>area</th>
      <th>average_price</th>
      <th>code</th>
      <th>houses_sold</th>
      <th>no_of_crimes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1995-01-01</td>
      <td>city of london</td>
      <td>91449</td>
      <td>E09000001</td>
      <td>17.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1995-02-01</td>
      <td>city of london</td>
      <td>82203</td>
      <td>E09000001</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1995-03-01</td>
      <td>city of london</td>
      <td>79121</td>
      <td>E09000001</td>
      <td>14.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1995-04-01</td>
      <td>city of london</td>
      <td>77101</td>
      <td>E09000001</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1995-05-01</td>
      <td>city of london</td>
      <td>84409</td>
      <td>E09000001</td>
      <td>10.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
#data['year'] = data.Date_Column.dt.year
data['year'] = data.date.dt.year
print('year column created')
```

    year column created
    


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
      <th>date</th>
      <th>area</th>
      <th>average_price</th>
      <th>code</th>
      <th>houses_sold</th>
      <th>no_of_crimes</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1995-01-01</td>
      <td>city of london</td>
      <td>91449</td>
      <td>E09000001</td>
      <td>17.0</td>
      <td>NaN</td>
      <td>1995</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1995-02-01</td>
      <td>city of london</td>
      <td>82203</td>
      <td>E09000001</td>
      <td>7.0</td>
      <td>NaN</td>
      <td>1995</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1995-03-01</td>
      <td>city of london</td>
      <td>79121</td>
      <td>E09000001</td>
      <td>14.0</td>
      <td>NaN</td>
      <td>1995</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1995-04-01</td>
      <td>city of london</td>
      <td>77101</td>
      <td>E09000001</td>
      <td>7.0</td>
      <td>NaN</td>
      <td>1995</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1995-05-01</td>
      <td>city of london</td>
      <td>84409</td>
      <td>E09000001</td>
      <td>10.0</td>
      <td>NaN</td>
      <td>1995</td>
    </tr>
  </tbody>
</table>
</div>



### Add a new column 'month' as 2nd column in the dataframe, which contain month only


```python
#data.insert(1 , 'month' , data.date.drt.month)
data.insert(1 , 'month' , data.date.dt.month)
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
      <th>date</th>
      <th>month</th>
      <th>area</th>
      <th>average_price</th>
      <th>code</th>
      <th>houses_sold</th>
      <th>no_of_crimes</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1995-01-01</td>
      <td>1</td>
      <td>city of london</td>
      <td>91449</td>
      <td>E09000001</td>
      <td>17.0</td>
      <td>NaN</td>
      <td>1995</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1995-02-01</td>
      <td>2</td>
      <td>city of london</td>
      <td>82203</td>
      <td>E09000001</td>
      <td>7.0</td>
      <td>NaN</td>
      <td>1995</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1995-03-01</td>
      <td>3</td>
      <td>city of london</td>
      <td>79121</td>
      <td>E09000001</td>
      <td>14.0</td>
      <td>NaN</td>
      <td>1995</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1995-04-01</td>
      <td>4</td>
      <td>city of london</td>
      <td>77101</td>
      <td>E09000001</td>
      <td>7.0</td>
      <td>NaN</td>
      <td>1995</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1995-05-01</td>
      <td>5</td>
      <td>city of london</td>
      <td>84409</td>
      <td>E09000001</td>
      <td>10.0</td>
      <td>NaN</td>
      <td>1995</td>
    </tr>
  </tbody>
</table>
</div>



### Remove the columns 'year' and 'month' from the dataframe


```python
#data.drop(['month', 'year'] , axis=1, inplace=True)
data.drop(['month', 'year'] , axis=1, inplace=True)
print('columns month and year are deleted')
```

    columns month and year are deleted
    


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
      <th>date</th>
      <th>area</th>
      <th>average_price</th>
      <th>code</th>
      <th>houses_sold</th>
      <th>no_of_crimes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1995-01-01</td>
      <td>city of london</td>
      <td>91449</td>
      <td>E09000001</td>
      <td>17.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1995-02-01</td>
      <td>city of london</td>
      <td>82203</td>
      <td>E09000001</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1995-03-01</td>
      <td>city of london</td>
      <td>79121</td>
      <td>E09000001</td>
      <td>14.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1995-04-01</td>
      <td>city of london</td>
      <td>77101</td>
      <td>E09000001</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1995-05-01</td>
      <td>city of london</td>
      <td>84409</td>
      <td>E09000001</td>
      <td>10.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



### Show all the records where 'no_if_crimes' is 0. And, how many such records are there?


```python
data.no_of_crimes == 0
```




    0        False
    1        False
    2        False
    3        False
    4        False
             ...  
    13544    False
    13545    False
    13546    False
    13547    False
    13548    False
    Name: no_of_crimes, Length: 13549, dtype: bool




```python
data[data.no_of_crimes == 0]
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
      <th>date</th>
      <th>area</th>
      <th>average_price</th>
      <th>code</th>
      <th>houses_sold</th>
      <th>no_of_crimes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>72</th>
      <td>2001-01-01</td>
      <td>city of london</td>
      <td>284262</td>
      <td>E09000001</td>
      <td>24.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>73</th>
      <td>2001-02-01</td>
      <td>city of london</td>
      <td>198137</td>
      <td>E09000001</td>
      <td>37.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>74</th>
      <td>2001-03-01</td>
      <td>city of london</td>
      <td>189033</td>
      <td>E09000001</td>
      <td>44.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>75</th>
      <td>2001-04-01</td>
      <td>city of london</td>
      <td>205494</td>
      <td>E09000001</td>
      <td>38.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>76</th>
      <td>2001-05-01</td>
      <td>city of london</td>
      <td>223459</td>
      <td>E09000001</td>
      <td>30.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>178</th>
      <td>2009-11-01</td>
      <td>city of london</td>
      <td>397909</td>
      <td>E09000001</td>
      <td>11.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>179</th>
      <td>2009-12-01</td>
      <td>city of london</td>
      <td>411955</td>
      <td>E09000001</td>
      <td>16.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>180</th>
      <td>2010-01-01</td>
      <td>city of london</td>
      <td>464436</td>
      <td>E09000001</td>
      <td>20.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>181</th>
      <td>2010-02-01</td>
      <td>city of london</td>
      <td>490525</td>
      <td>E09000001</td>
      <td>9.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>182</th>
      <td>2010-03-01</td>
      <td>city of london</td>
      <td>498241</td>
      <td>E09000001</td>
      <td>15.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>104 rows × 6 columns</p>
</div>




```python
#len(data[data.no_of_crimes == 0])
len(data[data.no_of_crimes == 0])
```




    104



### What is the maximum & minimum 'average_price' per year in England?


```python
#create the year column first
data['year'] = data.date.dt.year
print('year column created')
```

    year column created
    


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
      <th>date</th>
      <th>area</th>
      <th>average_price</th>
      <th>code</th>
      <th>houses_sold</th>
      <th>no_of_crimes</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1995-01-01</td>
      <td>city of london</td>
      <td>91449</td>
      <td>E09000001</td>
      <td>17.0</td>
      <td>NaN</td>
      <td>1995</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1995-02-01</td>
      <td>city of london</td>
      <td>82203</td>
      <td>E09000001</td>
      <td>7.0</td>
      <td>NaN</td>
      <td>1995</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1995-03-01</td>
      <td>city of london</td>
      <td>79121</td>
      <td>E09000001</td>
      <td>14.0</td>
      <td>NaN</td>
      <td>1995</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1995-04-01</td>
      <td>city of london</td>
      <td>77101</td>
      <td>E09000001</td>
      <td>7.0</td>
      <td>NaN</td>
      <td>1995</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1995-05-01</td>
      <td>city of london</td>
      <td>84409</td>
      <td>E09000001</td>
      <td>10.0</td>
      <td>NaN</td>
      <td>1995</td>
    </tr>
  </tbody>
</table>
</div>




```python
#df1 = data[data.area == 'england']
df1 = data[data.area == 'england']
df1
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
      <th>date</th>
      <th>area</th>
      <th>average_price</th>
      <th>code</th>
      <th>houses_sold</th>
      <th>no_of_crimes</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>13248</th>
      <td>1995-01-01</td>
      <td>england</td>
      <td>53203</td>
      <td>E92000001</td>
      <td>47639.0</td>
      <td>NaN</td>
      <td>1995</td>
    </tr>
    <tr>
      <th>13249</th>
      <td>1995-02-01</td>
      <td>england</td>
      <td>53096</td>
      <td>E92000001</td>
      <td>47880.0</td>
      <td>NaN</td>
      <td>1995</td>
    </tr>
    <tr>
      <th>13250</th>
      <td>1995-03-01</td>
      <td>england</td>
      <td>53201</td>
      <td>E92000001</td>
      <td>67025.0</td>
      <td>NaN</td>
      <td>1995</td>
    </tr>
    <tr>
      <th>13251</th>
      <td>1995-04-01</td>
      <td>england</td>
      <td>53591</td>
      <td>E92000001</td>
      <td>56925.0</td>
      <td>NaN</td>
      <td>1995</td>
    </tr>
    <tr>
      <th>13252</th>
      <td>1995-05-01</td>
      <td>england</td>
      <td>53678</td>
      <td>E92000001</td>
      <td>64192.0</td>
      <td>NaN</td>
      <td>1995</td>
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
      <th>13544</th>
      <td>2019-09-01</td>
      <td>england</td>
      <td>249942</td>
      <td>E92000001</td>
      <td>64605.0</td>
      <td>NaN</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>13545</th>
      <td>2019-10-01</td>
      <td>england</td>
      <td>249376</td>
      <td>E92000001</td>
      <td>68677.0</td>
      <td>NaN</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>13546</th>
      <td>2019-11-01</td>
      <td>england</td>
      <td>248515</td>
      <td>E92000001</td>
      <td>67814.0</td>
      <td>NaN</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>13547</th>
      <td>2019-12-01</td>
      <td>england</td>
      <td>250410</td>
      <td>E92000001</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>13548</th>
      <td>2020-01-01</td>
      <td>england</td>
      <td>247355</td>
      <td>E92000001</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2020</td>
    </tr>
  </tbody>
</table>
<p>301 rows × 7 columns</p>
</div>




```python
#df1.groupby('year').average_price.max()/min()/mean()
df1.groupby('year')
```




    <pandas.core.groupby.generic.DataFrameGroupBy object at 0x00000161AF11E6A0>




```python
#max prices
df1.groupby('year').average_price.max()
```




    year
    1995     53901
    1996     55755
    1997     61564
    1998     65743
    1999     75071
    2000     84191
    2001     95992
    2002    119982
    2003    138985
    2004    160330
    2005    167244
    2006    182031
    2007    194764
    2008    191750
    2009    174136
    2010    180807
    2011    177335
    2012    180129
    2013    188544
    2014    203639
    2015    219582
    2016    231922
    2017    242628
    2018    248620
    2019    250410
    2020    247355
    Name: average_price, dtype: int64




```python
#min prices
df1.groupby('year').average_price.min()
```




    year
    1995     52788
    1996     52333
    1997     55789
    1998     61659
    1999     65522
    2000     75219
    2001     84245
    2002     96215
    2003    121610
    2004    139719
    2005    158572
    2006    166544
    2007    181824
    2008    165795
    2009    159340
    2010    174458
    2011    173046
    2012    174161
    2013    176816
    2014    188265
    2015    202856
    2016    220361
    2017    231593
    2018    240428
    2019    243281
    2020    247355
    Name: average_price, dtype: int64




```python
#mean values
df1.groupby('year').average_price.mean()
```




    year
    1995     53322.416667
    1996     54151.500000
    1997     59160.666667
    1998     64301.666667
    1999     70070.750000
    2000     80814.333333
    2001     90306.750000
    2002    107981.500000
    2003    130218.583333
    2004    152314.416667
    2005    163570.000000
    2006    174351.500000
    2007    190025.583333
    2008    182379.916667
    2009    166558.666667
    2010    177472.666667
    2011    175230.000000
    2012    177488.000000
    2013    182581.416667
    2014    197771.083333
    2015    211174.750000
    2016    227337.166667
    2017    238161.166667
    2018    245018.333333
    2019    247101.083333
    2020    247355.000000
    Name: average_price, dtype: float64



### What is the Max & Min no_of_crimes recorded per area?


```python
#data.groupby('area').no_of_crimes.max()
```


```python
data.groupby('area')
```




    <pandas.core.groupby.generic.DataFrameGroupBy object at 0x00000161AF0DE220>




```python
#max
data.groupby('area').no_of_crimes.max().sort_values(ascending =True)
```




    area
    city of london              10.0
    kingston upon thames      1379.0
    sutton                    1425.0
    richmond upon thames      1551.0
    merton                    1623.0
    harrow                    1763.0
    bexley                    1914.0
    havering                  1956.0
    barking and dagenham      2049.0
    redbridge                 2560.0
    bromley                   2637.0
    hammersmith and fulham    2645.0
    kensington and chelsea    2778.0
    enfield                   2798.0
    lewisham                  2813.0
    hounslow                  2817.0
    hillingdon                2819.0
    greenwich                 2853.0
    barnet                    2893.0
    brent                     2937.0
    waltham forest            2941.0
    wandsworth                3051.0
    haringey                  3199.0
    croydon                   3263.0
    tower hamlets             3316.0
    islington                 3384.0
    ealing                    3401.0
    hackney                   3466.0
    newham                    3668.0
    southwark                 3821.0
    camden                    4558.0
    lambeth                   4701.0
    westminster               7461.0
    east midlands                NaN
    east of england              NaN
    england                      NaN
    inner london                 NaN
    london                       NaN
    north east                   NaN
    north west                   NaN
    outer london                 NaN
    south east                   NaN
    south west                   NaN
    west midlands                NaN
    yorks and the humber         NaN
    Name: no_of_crimes, dtype: float64




```python
#min
data.groupby('area').no_of_crimes.min().sort_values(ascending =True)
```




    area
    city of london               0.0
    kingston upon thames       692.0
    richmond upon thames       700.0
    sutton                     787.0
    merton                     819.0
    bexley                     860.0
    harrow                     937.0
    havering                  1130.0
    barking and dagenham      1217.0
    hammersmith and fulham    1323.0
    kensington and chelsea    1347.0
    bromley                   1441.0
    hillingdon                1445.0
    redbridge                 1487.0
    greenwich                 1513.0
    hounslow                  1529.0
    haringey                  1536.0
    waltham forest            1575.0
    wandsworth                1582.0
    enfield                   1635.0
    tower hamlets             1646.0
    lewisham                  1675.0
    barnet                    1703.0
    brent                     1850.0
    hackney                   1870.0
    ealing                    1871.0
    islington                 1871.0
    croydon                   2031.0
    camden                    2079.0
    newham                    2130.0
    southwark                 2267.0
    lambeth                   2381.0
    westminster               3504.0
    east midlands                NaN
    east of england              NaN
    england                      NaN
    inner london                 NaN
    london                       NaN
    north east                   NaN
    north west                   NaN
    outer london                 NaN
    south east                   NaN
    south west                   NaN
    west midlands                NaN
    yorks and the humber         NaN
    Name: no_of_crimes, dtype: float64




```python
#mean
data.groupby('area').no_of_crimes.mean().sort_values(ascending =True)
```




    area
    city of london               0.423423
    kingston upon thames       991.790393
    richmond upon thames      1041.620087
    sutton                    1078.213974
    merton                    1208.615721
    harrow                    1256.598253
    bexley                    1299.458515
    havering                  1530.358079
    barking and dagenham      1599.275109
    kensington and chelsea    1833.222707
    hammersmith and fulham    1914.676856
    redbridge                 1940.480349
    bromley                   2020.131004
    hounslow                  2040.231441
    enfield                   2077.921397
    waltham forest            2113.598253
    hillingdon                2141.768559
    greenwich                 2154.899563
    wandsworth                2209.716157
    barnet                    2278.441048
    lewisham                  2296.458515
    haringey                  2406.427948
    brent                     2415.602620
    islington                 2515.991266
    tower hamlets             2542.253275
    hackney                   2575.751092
    ealing                    2607.061135
    croydon                   2652.943231
    newham                    2851.432314
    southwark                 3028.563319
    camden                    3056.572052
    lambeth                   3141.720524
    westminster               5291.454148
    east midlands                     NaN
    east of england                   NaN
    england                           NaN
    inner london                      NaN
    london                            NaN
    north east                        NaN
    north west                        NaN
    outer london                      NaN
    south east                        NaN
    south west                        NaN
    west midlands                     NaN
    yorks and the humber              NaN
    Name: no_of_crimes, dtype: float64



### Show the total count of records of each area, where average price is less than 100000


```python
#data[data.average_price < 100000].area.value_counts()

```


```python
data.average_price < 100000
```




    0         True
    1         True
    2         True
    3         True
    4         True
             ...  
    13544    False
    13545    False
    13546    False
    13547    False
    13548    False
    Name: average_price, Length: 13549, dtype: bool




```python
data[data.average_price < 100000]
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
      <th>date</th>
      <th>area</th>
      <th>average_price</th>
      <th>code</th>
      <th>houses_sold</th>
      <th>no_of_crimes</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1995-01-01</td>
      <td>city of london</td>
      <td>91449</td>
      <td>E09000001</td>
      <td>17.0</td>
      <td>NaN</td>
      <td>1995</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1995-02-01</td>
      <td>city of london</td>
      <td>82203</td>
      <td>E09000001</td>
      <td>7.0</td>
      <td>NaN</td>
      <td>1995</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1995-03-01</td>
      <td>city of london</td>
      <td>79121</td>
      <td>E09000001</td>
      <td>14.0</td>
      <td>NaN</td>
      <td>1995</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1995-04-01</td>
      <td>city of london</td>
      <td>77101</td>
      <td>E09000001</td>
      <td>7.0</td>
      <td>NaN</td>
      <td>1995</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1995-05-01</td>
      <td>city of london</td>
      <td>84409</td>
      <td>E09000001</td>
      <td>10.0</td>
      <td>NaN</td>
      <td>1995</td>
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
      <th>13330</th>
      <td>2001-11-01</td>
      <td>england</td>
      <td>95083</td>
      <td>E92000001</td>
      <td>109149.0</td>
      <td>NaN</td>
      <td>2001</td>
    </tr>
    <tr>
      <th>13331</th>
      <td>2001-12-01</td>
      <td>england</td>
      <td>95992</td>
      <td>E92000001</td>
      <td>93329.0</td>
      <td>NaN</td>
      <td>2001</td>
    </tr>
    <tr>
      <th>13332</th>
      <td>2002-01-01</td>
      <td>england</td>
      <td>96215</td>
      <td>E92000001</td>
      <td>71678.0</td>
      <td>NaN</td>
      <td>2002</td>
    </tr>
    <tr>
      <th>13333</th>
      <td>2002-02-01</td>
      <td>england</td>
      <td>96676</td>
      <td>E92000001</td>
      <td>77131.0</td>
      <td>NaN</td>
      <td>2002</td>
    </tr>
    <tr>
      <th>13334</th>
      <td>2002-03-01</td>
      <td>england</td>
      <td>98962</td>
      <td>E92000001</td>
      <td>102828.0</td>
      <td>NaN</td>
      <td>2002</td>
    </tr>
  </tbody>
</table>
<p>2209 rows × 7 columns</p>
</div>




```python
data[data.average_price < 100000].area.value_counts()
```




    north east              112
    north west              111
    yorks and the humber    110
    east midlands            96
    west midlands            94
    england                  87
    barking and dagenham     85
    south west               78
    east of england          76
    newham                   72
    bexley                   64
    waltham forest           64
    lewisham                 62
    havering                 60
    south east               59
    greenwich                59
    croydon                  57
    enfield                  54
    sutton                   54
    hackney                  53
    redbridge                52
    southwark                48
    tower hamlets            47
    outer london             46
    hillingdon               44
    lambeth                  41
    hounslow                 41
    brent                    40
    london                   39
    merton                   35
    haringey                 33
    bromley                  33
    inner london             31
    ealing                   31
    kingston upon thames     30
    harrow                   30
    wandsworth               26
    barnet                   25
    islington                19
    city of london           11
    Name: area, dtype: int64



**By DataSpieler12345**

