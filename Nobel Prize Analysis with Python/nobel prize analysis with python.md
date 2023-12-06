<center><h1><b><font size="6">Nobel Prize Analysis with Python</font></b></h1></center>

#### Packages


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
```

##### Load the data 


```python
url = "https://raw.githubusercontent.com/Adrian-Cancino/DataScience/main/Data/nobel.csv"
data = pd.read_csv(url)
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
      <th>year</th>
      <th>category</th>
      <th>prize</th>
      <th>motivation</th>
      <th>prize_share</th>
      <th>laureate_id</th>
      <th>laureate_type</th>
      <th>full_name</th>
      <th>birth_date</th>
      <th>birth_city</th>
      <th>birth_country</th>
      <th>sex</th>
      <th>organization_name</th>
      <th>organization_city</th>
      <th>organization_country</th>
      <th>death_date</th>
      <th>death_city</th>
      <th>death_country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1901</td>
      <td>Chemistry</td>
      <td>The Nobel Prize in Chemistry 1901</td>
      <td>"in recognition of the extraordinary services ...</td>
      <td>1/1</td>
      <td>160</td>
      <td>Individual</td>
      <td>Jacobus Henricus van 't Hoff</td>
      <td>1852-08-30</td>
      <td>Rotterdam</td>
      <td>Netherlands</td>
      <td>Male</td>
      <td>Berlin University</td>
      <td>Berlin</td>
      <td>Germany</td>
      <td>1911-03-01</td>
      <td>Berlin</td>
      <td>Germany</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1901</td>
      <td>Literature</td>
      <td>The Nobel Prize in Literature 1901</td>
      <td>"in special recognition of his poetic composit...</td>
      <td>1/1</td>
      <td>569</td>
      <td>Individual</td>
      <td>Sully Prudhomme</td>
      <td>1839-03-16</td>
      <td>Paris</td>
      <td>France</td>
      <td>Male</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1907-09-07</td>
      <td>Châtenay</td>
      <td>France</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1901</td>
      <td>Medicine</td>
      <td>The Nobel Prize in Physiology or Medicine 1901</td>
      <td>"for his work on serum therapy, especially its...</td>
      <td>1/1</td>
      <td>293</td>
      <td>Individual</td>
      <td>Emil Adolf von Behring</td>
      <td>1854-03-15</td>
      <td>Hansdorf (Lawice)</td>
      <td>Prussia (Poland)</td>
      <td>Male</td>
      <td>Marburg University</td>
      <td>Marburg</td>
      <td>Germany</td>
      <td>1917-03-31</td>
      <td>Marburg</td>
      <td>Germany</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1901</td>
      <td>Peace</td>
      <td>The Nobel Peace Prize 1901</td>
      <td>NaN</td>
      <td>1/2</td>
      <td>462</td>
      <td>Individual</td>
      <td>Jean Henry Dunant</td>
      <td>1828-05-08</td>
      <td>Geneva</td>
      <td>Switzerland</td>
      <td>Male</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1910-10-30</td>
      <td>Heiden</td>
      <td>Switzerland</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1901</td>
      <td>Peace</td>
      <td>The Nobel Peace Prize 1901</td>
      <td>NaN</td>
      <td>1/2</td>
      <td>463</td>
      <td>Individual</td>
      <td>Frédéric Passy</td>
      <td>1822-05-20</td>
      <td>Paris</td>
      <td>France</td>
      <td>Male</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1912-06-12</td>
      <td>Paris</td>
      <td>France</td>
    </tr>
  </tbody>
</table>
</div>



#### overview of the data set 


```python
data.info()
#NaN values
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 911 entries, 0 to 910
    Data columns (total 18 columns):
     #   Column                Non-Null Count  Dtype 
    ---  ------                --------------  ----- 
     0   year                  911 non-null    int64 
     1   category              911 non-null    object
     2   prize                 911 non-null    object
     3   motivation            823 non-null    object
     4   prize_share           911 non-null    object
     5   laureate_id           911 non-null    int64 
     6   laureate_type         911 non-null    object
     7   full_name             911 non-null    object
     8   birth_date            883 non-null    object
     9   birth_city            883 non-null    object
     10  birth_country         885 non-null    object
     11  sex                   885 non-null    object
     12  organization_name     665 non-null    object
     13  organization_city     667 non-null    object
     14  organization_country  667 non-null    object
     15  death_date            593 non-null    object
     16  death_city            576 non-null    object
     17  death_country         582 non-null    object
    dtypes: int64(2), object(16)
    memory usage: 128.2+ KB
    

#### NaN values


```python
data.isnull().sum()
```




    year                      0
    category                  0
    prize                     0
    motivation               88
    prize_share               0
    laureate_id               0
    laureate_type             0
    full_name                 0
    birth_date               28
    birth_city               28
    birth_country            26
    sex                       0
    organization_name       246
    organization_city       244
    organization_country    244
    death_date              318
    death_city              335
    death_country           329
    usa_born_winner           0
    decade                    0
    female_winner             0
    dtype: int64




```python
data.dropna(axis=0, inplace=True)
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
      <th>year</th>
      <th>category</th>
      <th>prize</th>
      <th>motivation</th>
      <th>prize_share</th>
      <th>laureate_id</th>
      <th>laureate_type</th>
      <th>full_name</th>
      <th>birth_date</th>
      <th>birth_city</th>
      <th>...</th>
      <th>sex</th>
      <th>organization_name</th>
      <th>organization_city</th>
      <th>organization_country</th>
      <th>death_date</th>
      <th>death_city</th>
      <th>death_country</th>
      <th>usa_born_winner</th>
      <th>decade</th>
      <th>female_winner</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1901</td>
      <td>Chemistry</td>
      <td>The Nobel Prize in Chemistry 1901</td>
      <td>"in recognition of the extraordinary services ...</td>
      <td>1/1</td>
      <td>160</td>
      <td>Individual</td>
      <td>Jacobus Henricus van 't Hoff</td>
      <td>1852-08-30</td>
      <td>Rotterdam</td>
      <td>...</td>
      <td>Female</td>
      <td>Berlin University</td>
      <td>Berlin</td>
      <td>Germany</td>
      <td>1911-03-01</td>
      <td>Berlin</td>
      <td>Germany</td>
      <td>False</td>
      <td>1900</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1901</td>
      <td>Medicine</td>
      <td>The Nobel Prize in Physiology or Medicine 1901</td>
      <td>"for his work on serum therapy, especially its...</td>
      <td>1/1</td>
      <td>293</td>
      <td>Individual</td>
      <td>Emil Adolf von Behring</td>
      <td>1854-03-15</td>
      <td>Hansdorf (Lawice)</td>
      <td>...</td>
      <td>Female</td>
      <td>Marburg University</td>
      <td>Marburg</td>
      <td>Germany</td>
      <td>1917-03-31</td>
      <td>Marburg</td>
      <td>Germany</td>
      <td>False</td>
      <td>1900</td>
      <td>True</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1901</td>
      <td>Physics</td>
      <td>The Nobel Prize in Physics 1901</td>
      <td>"in recognition of the extraordinary services ...</td>
      <td>1/1</td>
      <td>1</td>
      <td>Individual</td>
      <td>Wilhelm Conrad Röntgen</td>
      <td>1845-03-27</td>
      <td>Lennep (Remscheid)</td>
      <td>...</td>
      <td>Female</td>
      <td>Munich University</td>
      <td>Munich</td>
      <td>Germany</td>
      <td>1923-02-10</td>
      <td>Munich</td>
      <td>Germany</td>
      <td>False</td>
      <td>1900</td>
      <td>True</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1902</td>
      <td>Chemistry</td>
      <td>The Nobel Prize in Chemistry 1902</td>
      <td>"in recognition of the extraordinary services ...</td>
      <td>1/1</td>
      <td>161</td>
      <td>Individual</td>
      <td>Hermann Emil Fischer</td>
      <td>1852-10-09</td>
      <td>Euskirchen</td>
      <td>...</td>
      <td>Female</td>
      <td>Berlin University</td>
      <td>Berlin</td>
      <td>Germany</td>
      <td>1919-07-15</td>
      <td>Berlin</td>
      <td>Germany</td>
      <td>False</td>
      <td>1900</td>
      <td>True</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1902</td>
      <td>Medicine</td>
      <td>The Nobel Prize in Physiology or Medicine 1902</td>
      <td>"for his work on malaria, by which he has show...</td>
      <td>1/1</td>
      <td>294</td>
      <td>Individual</td>
      <td>Ronald Ross</td>
      <td>1857-05-13</td>
      <td>Almora</td>
      <td>...</td>
      <td>Female</td>
      <td>University College</td>
      <td>Liverpool</td>
      <td>United Kingdom</td>
      <td>1932-09-16</td>
      <td>Putney Heath</td>
      <td>United Kingdom</td>
      <td>False</td>
      <td>1900</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 21 columns</p>
</div>



### General knowledge of the set

#### Total registered awards?


```python
display(len(data))
```


    404


#### How many awards have been won by men and how many by women?


```python
display(data['sex'].value_counts())
```


    sex
    Female    404
    Name: count, dtype: int64


 #### Which countries have won the most awards?


```python
display(data['birth_country'].value_counts().head(10))
```


    birth_country
    United States of America    121
    United Kingdom               53
    Germany                      36
    France                       22
    Sweden                       12
    Netherlands                  11
    Italy                         9
    Austria                       9
    Russia                        8
    Canada                        8
    Name: count, dtype: int64


#### Wich category has the most awards?


```python
display(data['category'].value_counts().head(10))
```


    category
    Medicine     142
    Physics      115
    Chemistry    109
    Economics     38
    Name: count, dtype: int64


#### percentage of U.S. winners per decade?


```python
# add new column = usa_born_winner
data['usa_born_winner'] = data['birth_country'] == "United States of America"
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
      <th>year</th>
      <th>category</th>
      <th>prize</th>
      <th>motivation</th>
      <th>prize_share</th>
      <th>laureate_id</th>
      <th>laureate_type</th>
      <th>full_name</th>
      <th>birth_date</th>
      <th>birth_city</th>
      <th>...</th>
      <th>sex</th>
      <th>organization_name</th>
      <th>organization_city</th>
      <th>organization_country</th>
      <th>death_date</th>
      <th>death_city</th>
      <th>death_country</th>
      <th>usa_born_winner</th>
      <th>decade</th>
      <th>female_winner</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1901</td>
      <td>Chemistry</td>
      <td>The Nobel Prize in Chemistry 1901</td>
      <td>"in recognition of the extraordinary services ...</td>
      <td>1/1</td>
      <td>160</td>
      <td>Individual</td>
      <td>Jacobus Henricus van 't Hoff</td>
      <td>1852-08-30</td>
      <td>Rotterdam</td>
      <td>...</td>
      <td>Female</td>
      <td>Berlin University</td>
      <td>Berlin</td>
      <td>Germany</td>
      <td>1911-03-01</td>
      <td>Berlin</td>
      <td>Germany</td>
      <td>False</td>
      <td>1900</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1901</td>
      <td>Medicine</td>
      <td>The Nobel Prize in Physiology or Medicine 1901</td>
      <td>"for his work on serum therapy, especially its...</td>
      <td>1/1</td>
      <td>293</td>
      <td>Individual</td>
      <td>Emil Adolf von Behring</td>
      <td>1854-03-15</td>
      <td>Hansdorf (Lawice)</td>
      <td>...</td>
      <td>Female</td>
      <td>Marburg University</td>
      <td>Marburg</td>
      <td>Germany</td>
      <td>1917-03-31</td>
      <td>Marburg</td>
      <td>Germany</td>
      <td>False</td>
      <td>1900</td>
      <td>True</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1901</td>
      <td>Physics</td>
      <td>The Nobel Prize in Physics 1901</td>
      <td>"in recognition of the extraordinary services ...</td>
      <td>1/1</td>
      <td>1</td>
      <td>Individual</td>
      <td>Wilhelm Conrad Röntgen</td>
      <td>1845-03-27</td>
      <td>Lennep (Remscheid)</td>
      <td>...</td>
      <td>Female</td>
      <td>Munich University</td>
      <td>Munich</td>
      <td>Germany</td>
      <td>1923-02-10</td>
      <td>Munich</td>
      <td>Germany</td>
      <td>False</td>
      <td>1900</td>
      <td>True</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1902</td>
      <td>Chemistry</td>
      <td>The Nobel Prize in Chemistry 1902</td>
      <td>"in recognition of the extraordinary services ...</td>
      <td>1/1</td>
      <td>161</td>
      <td>Individual</td>
      <td>Hermann Emil Fischer</td>
      <td>1852-10-09</td>
      <td>Euskirchen</td>
      <td>...</td>
      <td>Female</td>
      <td>Berlin University</td>
      <td>Berlin</td>
      <td>Germany</td>
      <td>1919-07-15</td>
      <td>Berlin</td>
      <td>Germany</td>
      <td>False</td>
      <td>1900</td>
      <td>True</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1902</td>
      <td>Medicine</td>
      <td>The Nobel Prize in Physiology or Medicine 1902</td>
      <td>"for his work on malaria, by which he has show...</td>
      <td>1/1</td>
      <td>294</td>
      <td>Individual</td>
      <td>Ronald Ross</td>
      <td>1857-05-13</td>
      <td>Almora</td>
      <td>...</td>
      <td>Female</td>
      <td>University College</td>
      <td>Liverpool</td>
      <td>United Kingdom</td>
      <td>1932-09-16</td>
      <td>Putney Heath</td>
      <td>United Kingdom</td>
      <td>False</td>
      <td>1900</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 21 columns</p>
</div>




```python
# add another column called = decade
# np.floor = rounded to the nearest whole number
data['decade'] = (np.floor(data['year'] / 10) *10).astype(int)
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
      <th>year</th>
      <th>category</th>
      <th>prize</th>
      <th>motivation</th>
      <th>prize_share</th>
      <th>laureate_id</th>
      <th>laureate_type</th>
      <th>full_name</th>
      <th>birth_date</th>
      <th>birth_city</th>
      <th>...</th>
      <th>sex</th>
      <th>organization_name</th>
      <th>organization_city</th>
      <th>organization_country</th>
      <th>death_date</th>
      <th>death_city</th>
      <th>death_country</th>
      <th>usa_born_winner</th>
      <th>decade</th>
      <th>female_winner</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1901</td>
      <td>Chemistry</td>
      <td>The Nobel Prize in Chemistry 1901</td>
      <td>"in recognition of the extraordinary services ...</td>
      <td>1/1</td>
      <td>160</td>
      <td>Individual</td>
      <td>Jacobus Henricus van 't Hoff</td>
      <td>1852-08-30</td>
      <td>Rotterdam</td>
      <td>...</td>
      <td>Female</td>
      <td>Berlin University</td>
      <td>Berlin</td>
      <td>Germany</td>
      <td>1911-03-01</td>
      <td>Berlin</td>
      <td>Germany</td>
      <td>False</td>
      <td>1900</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1901</td>
      <td>Medicine</td>
      <td>The Nobel Prize in Physiology or Medicine 1901</td>
      <td>"for his work on serum therapy, especially its...</td>
      <td>1/1</td>
      <td>293</td>
      <td>Individual</td>
      <td>Emil Adolf von Behring</td>
      <td>1854-03-15</td>
      <td>Hansdorf (Lawice)</td>
      <td>...</td>
      <td>Female</td>
      <td>Marburg University</td>
      <td>Marburg</td>
      <td>Germany</td>
      <td>1917-03-31</td>
      <td>Marburg</td>
      <td>Germany</td>
      <td>False</td>
      <td>1900</td>
      <td>True</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1901</td>
      <td>Physics</td>
      <td>The Nobel Prize in Physics 1901</td>
      <td>"in recognition of the extraordinary services ...</td>
      <td>1/1</td>
      <td>1</td>
      <td>Individual</td>
      <td>Wilhelm Conrad Röntgen</td>
      <td>1845-03-27</td>
      <td>Lennep (Remscheid)</td>
      <td>...</td>
      <td>Female</td>
      <td>Munich University</td>
      <td>Munich</td>
      <td>Germany</td>
      <td>1923-02-10</td>
      <td>Munich</td>
      <td>Germany</td>
      <td>False</td>
      <td>1900</td>
      <td>True</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1902</td>
      <td>Chemistry</td>
      <td>The Nobel Prize in Chemistry 1902</td>
      <td>"in recognition of the extraordinary services ...</td>
      <td>1/1</td>
      <td>161</td>
      <td>Individual</td>
      <td>Hermann Emil Fischer</td>
      <td>1852-10-09</td>
      <td>Euskirchen</td>
      <td>...</td>
      <td>Female</td>
      <td>Berlin University</td>
      <td>Berlin</td>
      <td>Germany</td>
      <td>1919-07-15</td>
      <td>Berlin</td>
      <td>Germany</td>
      <td>False</td>
      <td>1900</td>
      <td>True</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1902</td>
      <td>Medicine</td>
      <td>The Nobel Prize in Physiology or Medicine 1902</td>
      <td>"for his work on malaria, by which he has show...</td>
      <td>1/1</td>
      <td>294</td>
      <td>Individual</td>
      <td>Ronald Ross</td>
      <td>1857-05-13</td>
      <td>Almora</td>
      <td>...</td>
      <td>Female</td>
      <td>University College</td>
      <td>Liverpool</td>
      <td>United Kingdom</td>
      <td>1932-09-16</td>
      <td>Putney Heath</td>
      <td>United Kingdom</td>
      <td>False</td>
      <td>1900</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 21 columns</p>
</div>



#### Group the data


```python
prop_usa_winners = data.groupby('decade', as_index=False)['usa_born_winner'].mean()
```


```python
prop_usa_winners
# usa accumulates more awards over time
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
      <th>decade</th>
      <th>usa_born_winner</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1900</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1910</td>
      <td>0.041667</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1920</td>
      <td>0.062500</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1930</td>
      <td>0.236842</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1940</td>
      <td>0.241379</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1950</td>
      <td>0.360000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1960</td>
      <td>0.290909</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1970</td>
      <td>0.350877</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1980</td>
      <td>0.441860</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1990</td>
      <td>0.633333</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2000</td>
      <td>0.533333</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2010</td>
      <td>0.666667</td>
    </tr>
  </tbody>
</table>
</div>



#### Graphic the result


```python
from matplotlib.ticker import PercentFormatter

plt.rcParams['figure.figsize'] = [11, 7]
ax = sns.lineplot(x='decade', y='usa_born_winner', data=prop_usa_winners)
ax.yaxis.set_major_formatter(PercentFormatter())
```


    
![png](output_27_0.png)
    


#### winning percentage between men and women in the different categories


```python
data['female_winner'] = data['sex'] == "Female"
print(data.head())
```

       year   category                                           prize  \
    0  1901  Chemistry               The Nobel Prize in Chemistry 1901   
    2  1901   Medicine  The Nobel Prize in Physiology or Medicine 1901   
    5  1901    Physics                 The Nobel Prize in Physics 1901   
    6  1902  Chemistry               The Nobel Prize in Chemistry 1902   
    8  1902   Medicine  The Nobel Prize in Physiology or Medicine 1902   
    
                                              motivation prize_share  laureate_id  \
    0  "in recognition of the extraordinary services ...         1/1          160   
    2  "for his work on serum therapy, especially its...         1/1          293   
    5  "in recognition of the extraordinary services ...         1/1            1   
    6  "in recognition of the extraordinary services ...         1/1          161   
    8  "for his work on malaria, by which he has show...         1/1          294   
    
      laureate_type                     full_name  birth_date          birth_city  \
    0    Individual  Jacobus Henricus van 't Hoff  1852-08-30           Rotterdam   
    2    Individual        Emil Adolf von Behring  1854-03-15   Hansdorf (Lawice)   
    5    Individual        Wilhelm Conrad Röntgen  1845-03-27  Lennep (Remscheid)   
    6    Individual          Hermann Emil Fischer  1852-10-09          Euskirchen   
    8    Individual                   Ronald Ross  1857-05-13              Almora   
    
       ...     sex   organization_name organization_city organization_country  \
    0  ...  Female   Berlin University            Berlin              Germany   
    2  ...  Female  Marburg University           Marburg              Germany   
    5  ...  Female   Munich University            Munich              Germany   
    6  ...  Female   Berlin University            Berlin              Germany   
    8  ...  Female  University College         Liverpool       United Kingdom   
    
       death_date    death_city   death_country usa_born_winner  decade  \
    0  1911-03-01        Berlin         Germany           False    1900   
    2  1917-03-31       Marburg         Germany           False    1900   
    5  1923-02-10        Munich         Germany           False    1900   
    6  1919-07-15        Berlin         Germany           False    1900   
    8  1932-09-16  Putney Heath  United Kingdom           False    1900   
    
       female_winner  
    0           True  
    2           True  
    5           True  
    6           True  
    8           True  
    
    [5 rows x 21 columns]
    

#### Group the data

#### the percentage / decade


```python
prop_female_winners = data.groupby(['decade', 'category'], as_index=False)['female_winner'].mean()
```


```python
prop_female_winners
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
      <th>decade</th>
      <th>category</th>
      <th>female_winner</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1900</td>
      <td>Chemistry</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1900</td>
      <td>Medicine</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1900</td>
      <td>Physics</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1910</td>
      <td>Chemistry</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1910</td>
      <td>Medicine</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1910</td>
      <td>Physics</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1920</td>
      <td>Chemistry</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1920</td>
      <td>Medicine</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1920</td>
      <td>Physics</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1930</td>
      <td>Chemistry</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1930</td>
      <td>Medicine</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>1930</td>
      <td>Physics</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>1940</td>
      <td>Chemistry</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>1940</td>
      <td>Medicine</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>1940</td>
      <td>Physics</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>1950</td>
      <td>Chemistry</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>1950</td>
      <td>Medicine</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>1950</td>
      <td>Physics</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>1960</td>
      <td>Chemistry</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>1960</td>
      <td>Economics</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>1960</td>
      <td>Medicine</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>21</th>
      <td>1960</td>
      <td>Physics</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>1970</td>
      <td>Chemistry</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>1970</td>
      <td>Economics</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>24</th>
      <td>1970</td>
      <td>Medicine</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>1970</td>
      <td>Physics</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>26</th>
      <td>1980</td>
      <td>Chemistry</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>27</th>
      <td>1980</td>
      <td>Economics</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>28</th>
      <td>1980</td>
      <td>Medicine</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>1980</td>
      <td>Physics</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>30</th>
      <td>1990</td>
      <td>Chemistry</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>31</th>
      <td>1990</td>
      <td>Economics</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>32</th>
      <td>1990</td>
      <td>Medicine</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>33</th>
      <td>1990</td>
      <td>Physics</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>34</th>
      <td>2000</td>
      <td>Chemistry</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>35</th>
      <td>2000</td>
      <td>Economics</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>36</th>
      <td>2000</td>
      <td>Medicine</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>37</th>
      <td>2000</td>
      <td>Physics</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>38</th>
      <td>2010</td>
      <td>Economics</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>39</th>
      <td>2010</td>
      <td>Medicine</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
print(data['female_winner'].unique())
```

    [ True]
    


```python
import matplotlib.pyplot as plt

plt.hist(data['female_winner'])
plt.xlabel('Female Winner')
plt.ylabel('Count')
plt.title('Distribution of Female Winner')
plt.show()

import warnings

# Ignore all warnings
warnings.filterwarnings("ignore")
```


    
![png](output_35_0.png)
    



```python
ax = sns.lineplot(x='decade',
                  y='female_winner', 
                  data=data, 
                  hue='category')

ax.yaxis.set_major_formatter(PercentFormatter())
```


    
![png](output_36_0.png)
    


#### winners by age


```python
data['birth_date'] = pd.to_datetime(data['birth_date'])

data['age'] = data['year'] - data['birth_date'].dt.year

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
      <th>year</th>
      <th>category</th>
      <th>prize</th>
      <th>motivation</th>
      <th>prize_share</th>
      <th>laureate_id</th>
      <th>laureate_type</th>
      <th>full_name</th>
      <th>birth_date</th>
      <th>birth_city</th>
      <th>...</th>
      <th>organization_name</th>
      <th>organization_city</th>
      <th>organization_country</th>
      <th>death_date</th>
      <th>death_city</th>
      <th>death_country</th>
      <th>usa_born_winner</th>
      <th>decade</th>
      <th>female_winner</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1901</td>
      <td>Chemistry</td>
      <td>The Nobel Prize in Chemistry 1901</td>
      <td>"in recognition of the extraordinary services ...</td>
      <td>1/1</td>
      <td>160</td>
      <td>Individual</td>
      <td>Jacobus Henricus van 't Hoff</td>
      <td>1852-08-30</td>
      <td>Rotterdam</td>
      <td>...</td>
      <td>Berlin University</td>
      <td>Berlin</td>
      <td>Germany</td>
      <td>1911-03-01</td>
      <td>Berlin</td>
      <td>Germany</td>
      <td>False</td>
      <td>1900</td>
      <td>True</td>
      <td>49</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1901</td>
      <td>Medicine</td>
      <td>The Nobel Prize in Physiology or Medicine 1901</td>
      <td>"for his work on serum therapy, especially its...</td>
      <td>1/1</td>
      <td>293</td>
      <td>Individual</td>
      <td>Emil Adolf von Behring</td>
      <td>1854-03-15</td>
      <td>Hansdorf (Lawice)</td>
      <td>...</td>
      <td>Marburg University</td>
      <td>Marburg</td>
      <td>Germany</td>
      <td>1917-03-31</td>
      <td>Marburg</td>
      <td>Germany</td>
      <td>False</td>
      <td>1900</td>
      <td>True</td>
      <td>47</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1901</td>
      <td>Physics</td>
      <td>The Nobel Prize in Physics 1901</td>
      <td>"in recognition of the extraordinary services ...</td>
      <td>1/1</td>
      <td>1</td>
      <td>Individual</td>
      <td>Wilhelm Conrad Röntgen</td>
      <td>1845-03-27</td>
      <td>Lennep (Remscheid)</td>
      <td>...</td>
      <td>Munich University</td>
      <td>Munich</td>
      <td>Germany</td>
      <td>1923-02-10</td>
      <td>Munich</td>
      <td>Germany</td>
      <td>False</td>
      <td>1900</td>
      <td>True</td>
      <td>56</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1902</td>
      <td>Chemistry</td>
      <td>The Nobel Prize in Chemistry 1902</td>
      <td>"in recognition of the extraordinary services ...</td>
      <td>1/1</td>
      <td>161</td>
      <td>Individual</td>
      <td>Hermann Emil Fischer</td>
      <td>1852-10-09</td>
      <td>Euskirchen</td>
      <td>...</td>
      <td>Berlin University</td>
      <td>Berlin</td>
      <td>Germany</td>
      <td>1919-07-15</td>
      <td>Berlin</td>
      <td>Germany</td>
      <td>False</td>
      <td>1900</td>
      <td>True</td>
      <td>50</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1902</td>
      <td>Medicine</td>
      <td>The Nobel Prize in Physiology or Medicine 1902</td>
      <td>"for his work on malaria, by which he has show...</td>
      <td>1/1</td>
      <td>294</td>
      <td>Individual</td>
      <td>Ronald Ross</td>
      <td>1857-05-13</td>
      <td>Almora</td>
      <td>...</td>
      <td>University College</td>
      <td>Liverpool</td>
      <td>United Kingdom</td>
      <td>1932-09-16</td>
      <td>Putney Heath</td>
      <td>United Kingdom</td>
      <td>False</td>
      <td>1900</td>
      <td>True</td>
      <td>45</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 22 columns</p>
</div>



#### Graphic Result


```python
ax = sns.lmplot(x='year',
                  y='age', 
                  data=data, 
                  lowess=True,
                 aspect=2,
                 line_kws={'color': 'black'})
```


    
![png](output_40_0.png)
    


#### Age range of the winners in the different categories 


```python
ax = sns.lmplot(x='year',
                  y='age', 
                  data=data, 
                  lowess=True,
                 aspect=2,
                 line_kws={'color': 'black'},
               	 row='category')
```


    
![png](output_42_0.png)
    


#### who is the oldest person to win the nobel prize and the youngest person to win the nobel prize


```python
display(data.nlargest(1, 'age'))

data.nsmallest(1, 'age')
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
      <th>year</th>
      <th>category</th>
      <th>prize</th>
      <th>motivation</th>
      <th>prize_share</th>
      <th>laureate_id</th>
      <th>laureate_type</th>
      <th>full_name</th>
      <th>birth_date</th>
      <th>birth_city</th>
      <th>...</th>
      <th>organization_name</th>
      <th>organization_city</th>
      <th>organization_country</th>
      <th>death_date</th>
      <th>death_city</th>
      <th>death_country</th>
      <th>usa_born_winner</th>
      <th>decade</th>
      <th>female_winner</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>793</th>
      <td>2007</td>
      <td>Economics</td>
      <td>The Sveriges Riksbank Prize in Economic Scienc...</td>
      <td>"for having laid the foundations of mechanism ...</td>
      <td>1/3</td>
      <td>820</td>
      <td>Individual</td>
      <td>Leonid Hurwicz</td>
      <td>1917-08-21</td>
      <td>Moscow</td>
      <td>...</td>
      <td>University of Minnesota</td>
      <td>Minneapolis, MN</td>
      <td>United States of America</td>
      <td>2008-06-24</td>
      <td>Minneapolis, MN</td>
      <td>United States of America</td>
      <td>False</td>
      <td>2000</td>
      <td>True</td>
      <td>90</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 22 columns</p>
</div>





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
      <th>year</th>
      <th>category</th>
      <th>prize</th>
      <th>motivation</th>
      <th>prize_share</th>
      <th>laureate_id</th>
      <th>laureate_type</th>
      <th>full_name</th>
      <th>birth_date</th>
      <th>birth_city</th>
      <th>...</th>
      <th>organization_name</th>
      <th>organization_city</th>
      <th>organization_country</th>
      <th>death_date</th>
      <th>death_city</th>
      <th>death_country</th>
      <th>usa_born_winner</th>
      <th>decade</th>
      <th>female_winner</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>85</th>
      <td>1915</td>
      <td>Physics</td>
      <td>The Nobel Prize in Physics 1915</td>
      <td>"for their services in the analysis of crystal...</td>
      <td>1/2</td>
      <td>21</td>
      <td>Individual</td>
      <td>William Lawrence Bragg</td>
      <td>1890-03-31</td>
      <td>Adelaide</td>
      <td>...</td>
      <td>Victoria University</td>
      <td>Manchester</td>
      <td>United Kingdom</td>
      <td>1971-07-01</td>
      <td>Ipswich</td>
      <td>United Kingdom</td>
      <td>False</td>
      <td>1910</td>
      <td>True</td>
      <td>25</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 22 columns</p>
</div>


