```python
import pandas as pd
```


```python
url = 'https://raw.githubusercontent.com/dataquestio/project-walkthroughs/master/weather/local_weather.csv'
```


```python
weather = pd.read_csv(url, index_col="DATE")
print('File loaded')
```

    File loaded
    


```python
weather
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
      <th>STATION</th>
      <th>NAME</th>
      <th>ACMH</th>
      <th>ACSH</th>
      <th>AWND</th>
      <th>DAPR</th>
      <th>FMTM</th>
      <th>FRGT</th>
      <th>MDPR</th>
      <th>PGTM</th>
      <th>...</th>
      <th>WT01</th>
      <th>WT02</th>
      <th>WT03</th>
      <th>WT04</th>
      <th>WT05</th>
      <th>WT07</th>
      <th>WT08</th>
      <th>WT09</th>
      <th>WT16</th>
      <th>WT18</th>
    </tr>
    <tr>
      <th>DATE</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1960-01-01</th>
      <td>USW00023230</td>
      <td>OAKLAND INTERNATIONAL AIRPORT, CA US</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1960-01-02</th>
      <td>USW00023230</td>
      <td>OAKLAND INTERNATIONAL AIRPORT, CA US</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1960-01-03</th>
      <td>USW00023230</td>
      <td>OAKLAND INTERNATIONAL AIRPORT, CA US</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1960-01-04</th>
      <td>USW00023230</td>
      <td>OAKLAND INTERNATIONAL AIRPORT, CA US</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1960-01-05</th>
      <td>USW00023230</td>
      <td>OAKLAND INTERNATIONAL AIRPORT, CA US</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
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
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2022-01-24</th>
      <td>USW00023230</td>
      <td>OAKLAND INTERNATIONAL AIRPORT, CA US</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4.47</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2022-01-25</th>
      <td>USW00023230</td>
      <td>OAKLAND INTERNATIONAL AIRPORT, CA US</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4.70</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2022-01-26</th>
      <td>USW00023230</td>
      <td>OAKLAND INTERNATIONAL AIRPORT, CA US</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.68</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2022-01-27</th>
      <td>USW00023230</td>
      <td>OAKLAND INTERNATIONAL AIRPORT, CA US</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.13</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1526.0</td>
      <td>...</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2022-01-28</th>
      <td>USW00023230</td>
      <td>OAKLAND INTERNATIONAL AIRPORT, CA US</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>16859 rows × 35 columns</p>
</div>




```python
# if we want some range of data
weather.loc["1960-01-01"]
```




    STATION                             USW00023230
    NAME       OAKLAND INTERNATIONAL AIRPORT, CA US
    ACMH                                        NaN
    ACSH                                        NaN
    AWND                                        NaN
    DAPR                                        NaN
    FMTM                                        NaN
    FRGT                                        NaN
    MDPR                                        NaN
    PGTM                                        NaN
    PRCP                                        0.0
    SNOW                                        0.0
    SNWD                                        0.0
    TAVG                                        NaN
    TMAX                                       49.0
    TMIN                                       30.0
    TSUN                                        NaN
    WDF1                                        NaN
    WDF2                                        NaN
    WDF5                                        NaN
    WDFG                                        NaN
    WSF1                                        NaN
    WSF2                                        NaN
    WSF5                                        NaN
    WSFG                                        NaN
    WT01                                        NaN
    WT02                                        NaN
    WT03                                        NaN
    WT04                                        NaN
    WT05                                        NaN
    WT07                                        NaN
    WT08                                        NaN
    WT09                                        NaN
    WT16                                        NaN
    WT18                                        NaN
    Name: 1960-01-01, dtype: object



## fixing missing values 


```python
#fixing missing values 
weather.apply(pd.isnull).sum() # will go through all the columns
```




    STATION        0
    NAME           0
    ACMH       11015
    ACSH       11015
    AWND        8808
    DAPR       16851
    FMTM       14669
    FRGT       16857
    MDPR       16851
    PGTM        8347
    PRCP         281
    SNOW        5479
    SNWD        5355
    TAVG       14822
    TMAX           9
    TMIN          10
    TSUN       15708
    WDF1       11015
    WDF2        8807
    WDF5        8894
    WDFG       12592
    WSF1       11015
    WSF2        8806
    WSF5        8894
    WSFG       12592
    WT01       13149
    WT02       16526
    WT03       16740
    WT04       16855
    WT05       16831
    WT07       16857
    WT08       13662
    WT09       16857
    WT16       14904
    WT18       16856
    dtype: int64




```python
# percent of null values per columns
weather.apply(pd.isnull).sum()/weather.shape[0]
```




    STATION    0.000000
    NAME       0.000000
    ACMH       0.653360
    ACSH       0.653360
    AWND       0.522451
    DAPR       0.999525
    FMTM       0.870099
    FRGT       0.999881
    MDPR       0.999525
    PGTM       0.495106
    PRCP       0.016668
    SNOW       0.324990
    SNWD       0.317634
    TAVG       0.879174
    TMAX       0.000534
    TMIN       0.000593
    TSUN       0.931728
    WDF1       0.653360
    WDF2       0.522392
    WDF5       0.527552
    WDFG       0.746901
    WSF1       0.653360
    WSF2       0.522332
    WSF5       0.527552
    WSFG       0.746901
    WT01       0.779939
    WT02       0.980248
    WT03       0.992941
    WT04       0.999763
    WT05       0.998339
    WT07       0.999881
    WT08       0.810368
    WT09       0.999881
    WT16       0.884038
    WT18       0.999822
    dtype: float64




```python
#select few columns from the data set to another one
core_weather = weather[["PRCP","SNOW","SNWD","TMAX","TMIN"]].copy()
```


```python
#rename the columns 
core_weather.columns = ["precip", "snow", "snow_deph", "temp_max", "temp_min"]
```


```python
core_weather
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
      <th>precip</th>
      <th>snow</th>
      <th>snow_deph</th>
      <th>temp_max</th>
      <th>temp_min</th>
    </tr>
    <tr>
      <th>DATE</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1960-01-01</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>49.0</td>
      <td>30.0</td>
    </tr>
    <tr>
      <th>1960-01-02</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>49.0</td>
      <td>29.0</td>
    </tr>
    <tr>
      <th>1960-01-03</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>54.0</td>
      <td>35.0</td>
    </tr>
    <tr>
      <th>1960-01-04</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>54.0</td>
      <td>36.0</td>
    </tr>
    <tr>
      <th>1960-01-05</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>55.0</td>
      <td>33.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2022-01-24</th>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>60.0</td>
      <td>39.0</td>
    </tr>
    <tr>
      <th>2022-01-25</th>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>57.0</td>
      <td>43.0</td>
    </tr>
    <tr>
      <th>2022-01-26</th>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>57.0</td>
      <td>41.0</td>
    </tr>
    <tr>
      <th>2022-01-27</th>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>67.0</td>
      <td>39.0</td>
    </tr>
    <tr>
      <th>2022-01-28</th>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>64.0</td>
      <td>39.0</td>
    </tr>
  </tbody>
</table>
<p>16859 rows × 5 columns</p>
</div>



### Filling in Missing Values 


```python
#filling in Missing Values
core_weather.apply(pd.isnull).sum()/core_weather.shape[0]
```




    precip       0.016668
    snow         0.324990
    snow_deph    0.317634
    temp_max     0.000534
    temp_min     0.000593
    dtype: float64




```python
#column to ML model
core_weather["snow"].value_counts()
```




    0.0    11379
    1.0        1
    Name: snow, dtype: int64




```python
#delete the column snow 
del core_weather["snow"]
```


```python
core_weather
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
      <th>precip</th>
      <th>snow_deph</th>
      <th>temp_max</th>
      <th>temp_min</th>
    </tr>
    <tr>
      <th>DATE</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1960-01-01</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>49.0</td>
      <td>30.0</td>
    </tr>
    <tr>
      <th>1960-01-02</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>49.0</td>
      <td>29.0</td>
    </tr>
    <tr>
      <th>1960-01-03</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>54.0</td>
      <td>35.0</td>
    </tr>
    <tr>
      <th>1960-01-04</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>54.0</td>
      <td>36.0</td>
    </tr>
    <tr>
      <th>1960-01-05</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>55.0</td>
      <td>33.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2022-01-24</th>
      <td>0.0</td>
      <td>NaN</td>
      <td>60.0</td>
      <td>39.0</td>
    </tr>
    <tr>
      <th>2022-01-25</th>
      <td>0.0</td>
      <td>NaN</td>
      <td>57.0</td>
      <td>43.0</td>
    </tr>
    <tr>
      <th>2022-01-26</th>
      <td>0.0</td>
      <td>NaN</td>
      <td>57.0</td>
      <td>41.0</td>
    </tr>
    <tr>
      <th>2022-01-27</th>
      <td>0.0</td>
      <td>NaN</td>
      <td>67.0</td>
      <td>39.0</td>
    </tr>
    <tr>
      <th>2022-01-28</th>
      <td>0.0</td>
      <td>NaN</td>
      <td>64.0</td>
      <td>39.0</td>
    </tr>
  </tbody>
</table>
<p>16859 rows × 4 columns</p>
</div>




```python
#delete the column snow_deph
del core_weather["snow_deph"]
```


```python
core_weather
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
      <th>precip</th>
      <th>temp_max</th>
      <th>temp_min</th>
    </tr>
    <tr>
      <th>DATE</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1960-01-01</th>
      <td>0.0</td>
      <td>49.0</td>
      <td>30.0</td>
    </tr>
    <tr>
      <th>1960-01-02</th>
      <td>0.0</td>
      <td>49.0</td>
      <td>29.0</td>
    </tr>
    <tr>
      <th>1960-01-03</th>
      <td>0.0</td>
      <td>54.0</td>
      <td>35.0</td>
    </tr>
    <tr>
      <th>1960-01-04</th>
      <td>0.0</td>
      <td>54.0</td>
      <td>36.0</td>
    </tr>
    <tr>
      <th>1960-01-05</th>
      <td>0.0</td>
      <td>55.0</td>
      <td>33.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2022-01-24</th>
      <td>0.0</td>
      <td>60.0</td>
      <td>39.0</td>
    </tr>
    <tr>
      <th>2022-01-25</th>
      <td>0.0</td>
      <td>57.0</td>
      <td>43.0</td>
    </tr>
    <tr>
      <th>2022-01-26</th>
      <td>0.0</td>
      <td>57.0</td>
      <td>41.0</td>
    </tr>
    <tr>
      <th>2022-01-27</th>
      <td>0.0</td>
      <td>67.0</td>
      <td>39.0</td>
    </tr>
    <tr>
      <th>2022-01-28</th>
      <td>0.0</td>
      <td>64.0</td>
      <td>39.0</td>
    </tr>
  </tbody>
</table>
<p>16859 rows × 3 columns</p>
</div>




```python
#null values in column precip
core_weather[pd.isnull(core_weather["precip"])]
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
      <th>precip</th>
      <th>temp_max</th>
      <th>temp_min</th>
    </tr>
    <tr>
      <th>DATE</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1983-10-29</th>
      <td>NaN</td>
      <td>67.0</td>
      <td>57.0</td>
    </tr>
    <tr>
      <th>1983-10-30</th>
      <td>NaN</td>
      <td>70.0</td>
      <td>63.0</td>
    </tr>
    <tr>
      <th>1983-10-31</th>
      <td>NaN</td>
      <td>69.0</td>
      <td>61.0</td>
    </tr>
    <tr>
      <th>1983-11-12</th>
      <td>NaN</td>
      <td>63.0</td>
      <td>55.0</td>
    </tr>
    <tr>
      <th>1983-11-13</th>
      <td>NaN</td>
      <td>60.0</td>
      <td>50.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2013-12-15</th>
      <td>NaN</td>
      <td>58.0</td>
      <td>33.0</td>
    </tr>
    <tr>
      <th>2016-05-01</th>
      <td>NaN</td>
      <td>80.0</td>
      <td>55.0</td>
    </tr>
    <tr>
      <th>2016-05-02</th>
      <td>NaN</td>
      <td>68.0</td>
      <td>53.0</td>
    </tr>
    <tr>
      <th>2016-05-08</th>
      <td>NaN</td>
      <td>67.0</td>
      <td>56.0</td>
    </tr>
    <tr>
      <th>2017-10-28</th>
      <td>NaN</td>
      <td>68.0</td>
      <td>50.0</td>
    </tr>
  </tbody>
</table>
<p>281 rows × 3 columns</p>
</div>




```python
#lets see what happened
core_weather.loc["1983-10-20":"1983-11-05",:]
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
      <th>precip</th>
      <th>temp_max</th>
      <th>temp_min</th>
    </tr>
    <tr>
      <th>DATE</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1983-10-20</th>
      <td>0.00</td>
      <td>73.0</td>
      <td>52.0</td>
    </tr>
    <tr>
      <th>1983-10-21</th>
      <td>0.00</td>
      <td>70.0</td>
      <td>50.0</td>
    </tr>
    <tr>
      <th>1983-10-22</th>
      <td>0.00</td>
      <td>70.0</td>
      <td>50.0</td>
    </tr>
    <tr>
      <th>1983-10-23</th>
      <td>0.00</td>
      <td>69.0</td>
      <td>60.0</td>
    </tr>
    <tr>
      <th>1983-10-24</th>
      <td>0.00</td>
      <td>73.0</td>
      <td>58.0</td>
    </tr>
    <tr>
      <th>1983-10-25</th>
      <td>0.00</td>
      <td>75.0</td>
      <td>53.0</td>
    </tr>
    <tr>
      <th>1983-10-26</th>
      <td>0.00</td>
      <td>79.0</td>
      <td>53.0</td>
    </tr>
    <tr>
      <th>1983-10-27</th>
      <td>0.00</td>
      <td>82.0</td>
      <td>56.0</td>
    </tr>
    <tr>
      <th>1983-10-28</th>
      <td>0.00</td>
      <td>74.0</td>
      <td>56.0</td>
    </tr>
    <tr>
      <th>1983-10-29</th>
      <td>NaN</td>
      <td>67.0</td>
      <td>57.0</td>
    </tr>
    <tr>
      <th>1983-10-30</th>
      <td>NaN</td>
      <td>70.0</td>
      <td>63.0</td>
    </tr>
    <tr>
      <th>1983-10-31</th>
      <td>NaN</td>
      <td>69.0</td>
      <td>61.0</td>
    </tr>
    <tr>
      <th>1983-11-01</th>
      <td>0.26</td>
      <td>69.0</td>
      <td>60.0</td>
    </tr>
    <tr>
      <th>1983-11-02</th>
      <td>0.06</td>
      <td>68.0</td>
      <td>56.0</td>
    </tr>
    <tr>
      <th>1983-11-03</th>
      <td>0.00</td>
      <td>68.0</td>
      <td>56.0</td>
    </tr>
    <tr>
      <th>1983-11-04</th>
      <td>0.00</td>
      <td>67.0</td>
      <td>55.0</td>
    </tr>
    <tr>
      <th>1983-11-05</th>
      <td>0.00</td>
      <td>66.0</td>
      <td>51.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
core_weather["precip"].value_counts() #0.00    13664 (max)
```




    0.00    13664
    0.01      438
    0.02      199
    0.03      122
    0.04      102
            ...  
    1.29        1
    1.73        1
    1.05        1
    1.38        1
    1.02        1
    Name: precip, Length: 176, dtype: int64




```python
#fill out Nan values : precip column
core_weather["precip"] = core_weather["precip"].fillna(0)
```


```python
core_weather
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
      <th>precip</th>
      <th>temp_max</th>
      <th>temp_min</th>
    </tr>
    <tr>
      <th>DATE</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1960-01-01</th>
      <td>0.0</td>
      <td>49.0</td>
      <td>30.0</td>
    </tr>
    <tr>
      <th>1960-01-02</th>
      <td>0.0</td>
      <td>49.0</td>
      <td>29.0</td>
    </tr>
    <tr>
      <th>1960-01-03</th>
      <td>0.0</td>
      <td>54.0</td>
      <td>35.0</td>
    </tr>
    <tr>
      <th>1960-01-04</th>
      <td>0.0</td>
      <td>54.0</td>
      <td>36.0</td>
    </tr>
    <tr>
      <th>1960-01-05</th>
      <td>0.0</td>
      <td>55.0</td>
      <td>33.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2022-01-24</th>
      <td>0.0</td>
      <td>60.0</td>
      <td>39.0</td>
    </tr>
    <tr>
      <th>2022-01-25</th>
      <td>0.0</td>
      <td>57.0</td>
      <td>43.0</td>
    </tr>
    <tr>
      <th>2022-01-26</th>
      <td>0.0</td>
      <td>57.0</td>
      <td>41.0</td>
    </tr>
    <tr>
      <th>2022-01-27</th>
      <td>0.0</td>
      <td>67.0</td>
      <td>39.0</td>
    </tr>
    <tr>
      <th>2022-01-28</th>
      <td>0.0</td>
      <td>64.0</td>
      <td>39.0</td>
    </tr>
  </tbody>
</table>
<p>16859 rows × 3 columns</p>
</div>




```python
#null values in column temp_max
core_weather[pd.isnull(core_weather["temp_max"])]
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
      <th>precip</th>
      <th>temp_max</th>
      <th>temp_min</th>
    </tr>
    <tr>
      <th>DATE</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2004-11-20</th>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2013-06-16</th>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2019-04-18</th>
      <td>0.0</td>
      <td>NaN</td>
      <td>50.0</td>
    </tr>
    <tr>
      <th>2019-04-21</th>
      <td>0.0</td>
      <td>NaN</td>
      <td>52.0</td>
    </tr>
    <tr>
      <th>2019-04-22</th>
      <td>0.0</td>
      <td>NaN</td>
      <td>50.0</td>
    </tr>
    <tr>
      <th>2020-08-29</th>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2020-09-08</th>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2020-09-09</th>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2021-10-31</th>
      <td>0.0</td>
      <td>NaN</td>
      <td>56.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
#null values in column temp_min
core_weather[pd.isnull(core_weather["temp_min"])]
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
      <th>precip</th>
      <th>temp_max</th>
      <th>temp_min</th>
    </tr>
    <tr>
      <th>DATE</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2004-11-20</th>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2011-12-21</th>
      <td>0.0</td>
      <td>61.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2011-12-22</th>
      <td>0.0</td>
      <td>62.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2011-12-23</th>
      <td>0.0</td>
      <td>56.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2011-12-24</th>
      <td>0.0</td>
      <td>55.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2011-12-25</th>
      <td>0.0</td>
      <td>54.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2013-06-16</th>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2020-08-29</th>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2020-09-08</th>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2020-09-09</th>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
#fill out with the previus value
core_weather = core_weather.fillna(method="ffill")
```


```python
core_weather.apply(pd.isnull).sum()/core_weather.shape[0]
```




    precip      0.0
    temp_max    0.0
    temp_min    0.0
    dtype: float64



## Verifying we have the correct data types


```python
core_weather.dtypes
```




    precip      float64
    temp_max    float64
    temp_min    float64
    dtype: object




```python
core_weather.index #date is a object
```




    Index(['1960-01-01', '1960-01-02', '1960-01-03', '1960-01-04', '1960-01-05',
           '1960-01-06', '1960-01-07', '1960-01-08', '1960-01-09', '1960-01-10',
           ...
           '2022-01-19', '2022-01-20', '2022-01-21', '2022-01-22', '2022-01-23',
           '2022-01-24', '2022-01-25', '2022-01-26', '2022-01-27', '2022-01-28'],
          dtype='object', name='DATE', length=16859)




```python
#date index with datetime format
core_weather.index = pd.to_datetime(core_weather.index)
```


```python
core_weather.index #index dtype = datetime64
```




    DatetimeIndex(['1960-01-01', '1960-01-02', '1960-01-03', '1960-01-04',
                   '1960-01-05', '1960-01-06', '1960-01-07', '1960-01-08',
                   '1960-01-09', '1960-01-10',
                   ...
                   '2022-01-19', '2022-01-20', '2022-01-21', '2022-01-22',
                   '2022-01-23', '2022-01-24', '2022-01-25', '2022-01-26',
                   '2022-01-27', '2022-01-28'],
                  dtype='datetime64[ns]', name='DATE', length=16859, freq=None)




```python
#subset index
core_weather.index.year
```




    Int64Index([1960, 1960, 1960, 1960, 1960, 1960, 1960, 1960, 1960, 1960,
                ...
                2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022],
               dtype='int64', name='DATE', length=16859)




```python
core_weather.index.month
```




    Int64Index([1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                ...
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               dtype='int64', name='DATE', length=16859)




```python
core_weather.apply(lambda x: (x==9999).sum())
```




    precip      0
    temp_max    0
    temp_min    0
    dtype: int64



## Analyzing our weather data


```python
core_weather[["temp_max", "temp_min"]].plot()
```




    <AxesSubplot:xlabel='DATE'>




    
![png](output_36_1.png)
    



```python
core_weather.index.year.value_counts().sort_index()
```




    1960    366
    1961    365
    1962    365
    1963    365
    1964    366
    1965    365
    1966    365
    1967    365
    1968    366
    1969    365
    1970    365
    1971    365
    1972    366
    1973    365
    1974    365
    1975    365
    1976    366
    1977    365
    1978    365
    1979    365
    1980    366
    1983    184
    1984    366
    1985    365
    1986    212
    2000    365
    2001    365
    2002    365
    2003    365
    2004    366
    2005    365
    2006    365
    2007    365
    2008    366
    2009    365
    2010    365
    2011    365
    2012    365
    2013    365
    2014    365
    2015    365
    2016    366
    2017    365
    2018    365
    2019    365
    2020    366
    2021    364
    2022     28
    Name: DATE, dtype: int64




```python
#plot precip column
core_weather["precip"].plot()
```




    <AxesSubplot:xlabel='DATE'>




    
![png](output_38_1.png)
    



```python
#groupping by year
core_weather.groupby(core_weather.index.year).sum()["precip"]
```




    DATE
    1960    14.01
    1961    13.87
    1962    22.47
    1963    19.11
    1964    16.83
    1965    16.32
    1966    13.11
    1967    23.98
    1968    17.19
    1969    25.70
    1970    25.31
    1971    10.61
    1972    16.27
    1973    29.37
    1974    16.87
    1975    17.54
    1976     8.64
    1977    11.70
    1978    22.57
    1979    23.79
    1980    13.58
    1983     7.13
    1984    16.03
    1985     8.50
    1986     0.00
    2000    21.09
    2001    22.84
    2002    19.12
    2003    11.37
    2004    12.97
    2005    27.37
    2006    22.79
    2007    12.79
    2008    13.86
    2009    14.57
    2010    22.67
    2011    16.06
    2012    22.93
    2013     4.89
    2014    19.62
    2015     8.58
    2016    19.77
    2017    23.34
    2018    16.82
    2019    20.00
    2020     6.42
    2021    20.82
    2022     0.25
    Name: precip, dtype: float64



## Training our first Machine Learning Model


```python
#we want to predict tomorrow temp
core_weather["target"] = core_weather.shift(-1)["temp_max"]
```


```python
core_weather #target column 
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
      <th>precip</th>
      <th>temp_max</th>
      <th>temp_min</th>
      <th>target</th>
    </tr>
    <tr>
      <th>DATE</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1960-01-01</th>
      <td>0.0</td>
      <td>49.0</td>
      <td>30.0</td>
      <td>49.0</td>
    </tr>
    <tr>
      <th>1960-01-02</th>
      <td>0.0</td>
      <td>49.0</td>
      <td>29.0</td>
      <td>54.0</td>
    </tr>
    <tr>
      <th>1960-01-03</th>
      <td>0.0</td>
      <td>54.0</td>
      <td>35.0</td>
      <td>54.0</td>
    </tr>
    <tr>
      <th>1960-01-04</th>
      <td>0.0</td>
      <td>54.0</td>
      <td>36.0</td>
      <td>55.0</td>
    </tr>
    <tr>
      <th>1960-01-05</th>
      <td>0.0</td>
      <td>55.0</td>
      <td>33.0</td>
      <td>53.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2022-01-24</th>
      <td>0.0</td>
      <td>60.0</td>
      <td>39.0</td>
      <td>57.0</td>
    </tr>
    <tr>
      <th>2022-01-25</th>
      <td>0.0</td>
      <td>57.0</td>
      <td>43.0</td>
      <td>57.0</td>
    </tr>
    <tr>
      <th>2022-01-26</th>
      <td>0.0</td>
      <td>57.0</td>
      <td>41.0</td>
      <td>67.0</td>
    </tr>
    <tr>
      <th>2022-01-27</th>
      <td>0.0</td>
      <td>67.0</td>
      <td>39.0</td>
      <td>64.0</td>
    </tr>
    <tr>
      <th>2022-01-28</th>
      <td>0.0</td>
      <td>64.0</td>
      <td>39.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>16859 rows × 4 columns</p>
</div>




```python
#delete the last row with missing values
core_weather = core_weather.iloc[:-1].copy() # not included the last row
```


```python
core_weather
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
      <th>precip</th>
      <th>temp_max</th>
      <th>temp_min</th>
      <th>target</th>
    </tr>
    <tr>
      <th>DATE</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1960-01-01</th>
      <td>0.0</td>
      <td>49.0</td>
      <td>30.0</td>
      <td>49.0</td>
    </tr>
    <tr>
      <th>1960-01-02</th>
      <td>0.0</td>
      <td>49.0</td>
      <td>29.0</td>
      <td>54.0</td>
    </tr>
    <tr>
      <th>1960-01-03</th>
      <td>0.0</td>
      <td>54.0</td>
      <td>35.0</td>
      <td>54.0</td>
    </tr>
    <tr>
      <th>1960-01-04</th>
      <td>0.0</td>
      <td>54.0</td>
      <td>36.0</td>
      <td>55.0</td>
    </tr>
    <tr>
      <th>1960-01-05</th>
      <td>0.0</td>
      <td>55.0</td>
      <td>33.0</td>
      <td>53.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2022-01-23</th>
      <td>0.0</td>
      <td>60.0</td>
      <td>41.0</td>
      <td>60.0</td>
    </tr>
    <tr>
      <th>2022-01-24</th>
      <td>0.0</td>
      <td>60.0</td>
      <td>39.0</td>
      <td>57.0</td>
    </tr>
    <tr>
      <th>2022-01-25</th>
      <td>0.0</td>
      <td>57.0</td>
      <td>43.0</td>
      <td>57.0</td>
    </tr>
    <tr>
      <th>2022-01-26</th>
      <td>0.0</td>
      <td>57.0</td>
      <td>41.0</td>
      <td>67.0</td>
    </tr>
    <tr>
      <th>2022-01-27</th>
      <td>0.0</td>
      <td>67.0</td>
      <td>39.0</td>
      <td>64.0</td>
    </tr>
  </tbody>
</table>
<p>16858 rows × 4 columns</p>
</div>




```python
#import sklearn 
from sklearn.linear_model import Ridge

reg = Ridge(alpha=.1)
```


```python
predictors = ["precip", "temp_max", "temp_min"]
```


```python
#train the model date 2020 -12 -31 to 2021 -01-01
train = core_weather.loc[:"2020-12-31"]
```


```python
test = core_weather.loc["2021-01-01":]
```


```python
#fit the model
reg.fit(train[predictors], train["target"])
```




    Ridge(alpha=0.1)




```python
predictions = reg.predict(test[predictors])
```


```python
from sklearn.metrics import mean_absolute_error
```


```python
mean_absolute_error(test["target"], predictions)
```




    3.4111699434528306



## Evaluating our model


```python
combined = pd.concat([test["target"], pd.Series(predictions, index=test.index)], axis=1)
combined.columns = ["actual", "predictions"]
```


```python
combined
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
      <th>actual</th>
      <th>predictions</th>
    </tr>
    <tr>
      <th>DATE</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2021-01-01</th>
      <td>57.0</td>
      <td>59.806024</td>
    </tr>
    <tr>
      <th>2021-01-02</th>
      <td>56.0</td>
      <td>59.310181</td>
    </tr>
    <tr>
      <th>2021-01-03</th>
      <td>62.0</td>
      <td>58.538685</td>
    </tr>
    <tr>
      <th>2021-01-04</th>
      <td>59.0</td>
      <td>61.531814</td>
    </tr>
    <tr>
      <th>2021-01-05</th>
      <td>59.0</td>
      <td>59.444266</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2022-01-23</th>
      <td>60.0</td>
      <td>59.985714</td>
    </tr>
    <tr>
      <th>2022-01-24</th>
      <td>57.0</td>
      <td>59.626333</td>
    </tr>
    <tr>
      <th>2022-01-25</th>
      <td>57.0</td>
      <td>58.181680</td>
    </tr>
    <tr>
      <th>2022-01-26</th>
      <td>67.0</td>
      <td>57.822299</td>
    </tr>
    <tr>
      <th>2022-01-27</th>
      <td>64.0</td>
      <td>64.674302</td>
    </tr>
  </tbody>
</table>
<p>391 rows × 2 columns</p>
</div>




```python
combined.plot()
```




    <AxesSubplot:xlabel='DATE'>




    
![png](output_56_1.png)
    



```python
reg.coef_
```




    array([-2.20730384,  0.72113834,  0.17969047])



## Creating a function to make predictions


```python
def create_predictions(predictors, core_weather, reg):
    train = core_weather.loc[:"2020-12-31"]
    test = core_weather.loc["2021-01-01":]
    reg.fit(train[predictors], train["target"])
    predictions = reg.predict(test[predictors])
    error = mean_absolute_error(test["target"], predictions)
    combined = pd.concat([test["target"], pd.Series(predictions, index=test.index)], axis=1)
    combined.columns = ["actual", "predictions"]
    return error, combined    
```

## Adding in rolling means


```python
core_weather["month_max"] = core_weather["temp_max"].rolling(30).mean()
```


```python
core_weather
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
      <th>precip</th>
      <th>temp_max</th>
      <th>temp_min</th>
      <th>target</th>
      <th>month_max</th>
    </tr>
    <tr>
      <th>DATE</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1960-01-01</th>
      <td>0.0</td>
      <td>49.0</td>
      <td>30.0</td>
      <td>49.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1960-01-02</th>
      <td>0.0</td>
      <td>49.0</td>
      <td>29.0</td>
      <td>54.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1960-01-03</th>
      <td>0.0</td>
      <td>54.0</td>
      <td>35.0</td>
      <td>54.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1960-01-04</th>
      <td>0.0</td>
      <td>54.0</td>
      <td>36.0</td>
      <td>55.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1960-01-05</th>
      <td>0.0</td>
      <td>55.0</td>
      <td>33.0</td>
      <td>53.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2022-01-23</th>
      <td>0.0</td>
      <td>60.0</td>
      <td>41.0</td>
      <td>60.0</td>
      <td>56.900000</td>
    </tr>
    <tr>
      <th>2022-01-24</th>
      <td>0.0</td>
      <td>60.0</td>
      <td>39.0</td>
      <td>57.0</td>
      <td>57.066667</td>
    </tr>
    <tr>
      <th>2022-01-25</th>
      <td>0.0</td>
      <td>57.0</td>
      <td>43.0</td>
      <td>57.0</td>
      <td>57.200000</td>
    </tr>
    <tr>
      <th>2022-01-26</th>
      <td>0.0</td>
      <td>57.0</td>
      <td>41.0</td>
      <td>67.0</td>
      <td>57.400000</td>
    </tr>
    <tr>
      <th>2022-01-27</th>
      <td>0.0</td>
      <td>67.0</td>
      <td>39.0</td>
      <td>64.0</td>
      <td>57.933333</td>
    </tr>
  </tbody>
</table>
<p>16858 rows × 5 columns</p>
</div>




```python
# finding interesting ratios
core_weather["month_day_max"] = core_weather["month_max"] / core_weather["temp_max"]
```


```python
core_weather["max_min"] = core_weather["temp_max"] / core_weather["temp_min"]
```


```python
predictors = ["precip", "temp_max", "temp_min", "month_max", "month_day_max", "max_min"]
```


```python
core_weather = core_weather.iloc[30:,:].copy()
```


```python
error, combined = create_predictions(predictors, core_weather, reg)
```


```python
error #3.4111699434528306 before
```




    3.360129746207606




```python
combined.plot()
```




    <AxesSubplot:xlabel='DATE'>




    
![png](output_69_1.png)
    


## Adding in Monthly and Daily Averages


```python
core_weather["monthly_avg"] = core_weather["temp_max"].groupby(core_weather.index.month).apply(lambda x: x.expanding(1).mean())
```


```python
core_weather
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
      <th>precip</th>
      <th>temp_max</th>
      <th>temp_min</th>
      <th>target</th>
      <th>month_max</th>
      <th>month_day_max</th>
      <th>max_min</th>
      <th>monthly_avg</th>
    </tr>
    <tr>
      <th>DATE</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1960-01-31</th>
      <td>0.00</td>
      <td>59.0</td>
      <td>46.0</td>
      <td>62.0</td>
      <td>55.566667</td>
      <td>0.941808</td>
      <td>1.282609</td>
      <td>59.000000</td>
    </tr>
    <tr>
      <th>1960-02-01</th>
      <td>0.81</td>
      <td>62.0</td>
      <td>51.0</td>
      <td>59.0</td>
      <td>56.000000</td>
      <td>0.903226</td>
      <td>1.215686</td>
      <td>62.000000</td>
    </tr>
    <tr>
      <th>1960-02-02</th>
      <td>0.00</td>
      <td>59.0</td>
      <td>43.0</td>
      <td>59.0</td>
      <td>56.166667</td>
      <td>0.951977</td>
      <td>1.372093</td>
      <td>60.500000</td>
    </tr>
    <tr>
      <th>1960-02-03</th>
      <td>0.20</td>
      <td>59.0</td>
      <td>47.0</td>
      <td>60.0</td>
      <td>56.333333</td>
      <td>0.954802</td>
      <td>1.255319</td>
      <td>60.000000</td>
    </tr>
    <tr>
      <th>1960-02-04</th>
      <td>0.16</td>
      <td>60.0</td>
      <td>42.0</td>
      <td>60.0</td>
      <td>56.500000</td>
      <td>0.941667</td>
      <td>1.428571</td>
      <td>60.000000</td>
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
      <td>...</td>
    </tr>
    <tr>
      <th>2022-01-23</th>
      <td>0.00</td>
      <td>60.0</td>
      <td>41.0</td>
      <td>60.0</td>
      <td>56.900000</td>
      <td>0.948333</td>
      <td>1.463415</td>
      <td>56.781536</td>
    </tr>
    <tr>
      <th>2022-01-24</th>
      <td>0.00</td>
      <td>60.0</td>
      <td>39.0</td>
      <td>57.0</td>
      <td>57.066667</td>
      <td>0.951111</td>
      <td>1.538462</td>
      <td>56.783803</td>
    </tr>
    <tr>
      <th>2022-01-25</th>
      <td>0.00</td>
      <td>57.0</td>
      <td>43.0</td>
      <td>57.0</td>
      <td>57.200000</td>
      <td>1.003509</td>
      <td>1.325581</td>
      <td>56.783955</td>
    </tr>
    <tr>
      <th>2022-01-26</th>
      <td>0.00</td>
      <td>57.0</td>
      <td>41.0</td>
      <td>67.0</td>
      <td>57.400000</td>
      <td>1.007018</td>
      <td>1.390244</td>
      <td>56.784107</td>
    </tr>
    <tr>
      <th>2022-01-27</th>
      <td>0.00</td>
      <td>67.0</td>
      <td>39.0</td>
      <td>64.0</td>
      <td>57.933333</td>
      <td>0.864677</td>
      <td>1.717949</td>
      <td>56.791286</td>
    </tr>
  </tbody>
</table>
<p>16828 rows × 8 columns</p>
</div>




```python
core_weather["day_of_year_avg"] = core_weather["temp_max"].groupby(core_weather.index.day_of_year).apply(lambda x: x.expanding(1).mean())
```


```python
predictors = ["precip", "temp_max", "temp_min", "month_max", "month_day_max", "max_min", "day_of_year_avg", "monthly_avg"]
```


```python
error, combined = create_predictions(predictors, core_weather, reg)
```


```python
error
```




    3.360129746207606



## Running Model Diagnostics


```python
reg.coef_
```




    array([ -1.42071761,   0.38801898,   0.08885225,   0.49028138,
           -18.34609624,   0.10128198])




```python
core_weather.corr()["target"]
```




    precip            -0.205413
    temp_max           0.821650
    temp_min           0.596016
    target             1.000000
    month_max          0.686842
    month_day_max     -0.421537
    max_min            0.045228
    monthly_avg        0.689805
    day_of_year_avg    0.712334
    Name: target, dtype: float64




```python
combined["diff"] = (combined["actual"] - combined["predictions"]).abs()
```


```python
combined.sort_values("diff", ascending=False).head()
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
      <th>actual</th>
      <th>predictions</th>
      <th>diff</th>
    </tr>
    <tr>
      <th>DATE</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2021-05-07</th>
      <td>81.0</td>
      <td>67.256689</td>
      <td>13.743311</td>
    </tr>
    <tr>
      <th>2021-04-01</th>
      <td>62.0</td>
      <td>75.416541</td>
      <td>13.416541</td>
    </tr>
    <tr>
      <th>2021-01-17</th>
      <td>83.0</td>
      <td>69.799628</td>
      <td>13.200372</td>
    </tr>
    <tr>
      <th>2021-10-16</th>
      <td>66.0</td>
      <td>78.835061</td>
      <td>12.835061</td>
    </tr>
    <tr>
      <th>2021-02-21</th>
      <td>77.0</td>
      <td>64.657273</td>
      <td>12.342727</td>
    </tr>
  </tbody>
</table>
</div>



**By:_** **DataSpieler12345**



```python

```
