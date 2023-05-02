```python
import pandas  as pd
```

## Data Cleaning


```python
df_historical_data = pd.read_csv('fifa_worldcup_matches.csv')
df_fixture = pd.read_csv('fifa_worldcup_fixture.csv')
df_missing_data = pd.read_csv('fifa_worldcup_missing_data.csv')
```

## Cleaning df_fixture


```python
df_fixture['home'] = df_fixture['home'].str.strip()
df_fixture['away'] = df_fixture['away'].str.strip()
```

## Cleaning df_missing_data and adding it to df_historical_data


```python
# df_missing_data[df_missing_data['home'].isnull()]
df_missing_data.dropna(inplace=True)
df_historical_data = pd.concat([df_historical_data, df_missing_data], ignore_index=True)
df_historical_data.drop_duplicates(inplace=True)
df_historical_data.sort_values('year', inplace=True)
df_historical_data
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
      <th>home</th>
      <th>score</th>
      <th>away</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>France</td>
      <td>4–1</td>
      <td>Mexico</td>
      <td>1930</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Uruguay</td>
      <td>4–2</td>
      <td>Argentina</td>
      <td>1930</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Uruguay</td>
      <td>6–1</td>
      <td>Yugoslavia</td>
      <td>1930</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Argentina</td>
      <td>6–1</td>
      <td>United States</td>
      <td>1930</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Paraguay</td>
      <td>1–0</td>
      <td>Belgium</td>
      <td>1930</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>419</th>
      <td>Brazil</td>
      <td>2–0</td>
      <td>Costa Rica</td>
      <td>2018</td>
    </tr>
    <tr>
      <th>420</th>
      <td>Serbia</td>
      <td>1–2</td>
      <td>Switzerland</td>
      <td>2018</td>
    </tr>
    <tr>
      <th>421</th>
      <td>Serbia</td>
      <td>0–2</td>
      <td>Brazil</td>
      <td>2018</td>
    </tr>
    <tr>
      <th>408</th>
      <td>France</td>
      <td>1–0</td>
      <td>Peru</td>
      <td>2018</td>
    </tr>
    <tr>
      <th>450</th>
      <td>Brazil</td>
      <td>1–2</td>
      <td>Belgium</td>
      <td>2018</td>
    </tr>
  </tbody>
</table>
<p>901 rows × 4 columns</p>
</div>



## Cleaning df_historical_data


```python
# deleting match with walk over
delete_index = df_historical_data[df_historical_data['home'].str.contains('Sweden') &
                                  df_historical_data['away'].str.contains('Austria')].index

df_historical_data.drop(index=delete_index, inplace=True)

# cleanning score and home/away columns
df_historical_data['score'] = df_historical_data['score'].str.replace('[^\d–]', '', regex=True)
df_historical_data['home'] = df_historical_data['home'].str.strip() # clean blank spaces: Yugoslavia twice
df_historical_data['away'] = df_historical_data['away'].str.strip()

# splitting score columns into home and away goals and dropping score column
df_historical_data[['HomeGoals', 'AwayGoals']] = df_historical_data['score'].str.split('–', expand=True)
df_historical_data.drop('score', axis=1, inplace=True)

# renaming columns and changing data types
df_historical_data.rename(columns={'home': 'HomeTeam', 'away': 'AwayTeam', 
                                   'year':'Year'}, inplace=True)
df_historical_data = df_historical_data.astype({'HomeGoals': int, 'AwayGoals':int, 'Year': int})

# creating new column "totalgoals"
df_historical_data['TotalGoals'] = df_historical_data['HomeGoals'] + df_historical_data['AwayGoals']
df_historical_data
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
      <th>HomeTeam</th>
      <th>AwayTeam</th>
      <th>Year</th>
      <th>HomeGoals</th>
      <th>AwayGoals</th>
      <th>TotalGoals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>France</td>
      <td>Mexico</td>
      <td>1930</td>
      <td>4</td>
      <td>1</td>
      <td>5</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Uruguay</td>
      <td>Argentina</td>
      <td>1930</td>
      <td>4</td>
      <td>2</td>
      <td>6</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Uruguay</td>
      <td>Yugoslavia</td>
      <td>1930</td>
      <td>6</td>
      <td>1</td>
      <td>7</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Argentina</td>
      <td>United States</td>
      <td>1930</td>
      <td>6</td>
      <td>1</td>
      <td>7</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Paraguay</td>
      <td>Belgium</td>
      <td>1930</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
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
      <th>419</th>
      <td>Brazil</td>
      <td>Costa Rica</td>
      <td>2018</td>
      <td>2</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>420</th>
      <td>Serbia</td>
      <td>Switzerland</td>
      <td>2018</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>421</th>
      <td>Serbia</td>
      <td>Brazil</td>
      <td>2018</td>
      <td>0</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>408</th>
      <td>France</td>
      <td>Peru</td>
      <td>2018</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>450</th>
      <td>Brazil</td>
      <td>Belgium</td>
      <td>2018</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
<p>900 rows × 6 columns</p>
</div>



## Exporting clean dataframes


```python
df_historical_data.to_csv('clean_fifa_worldcup_matches.csv',index=False)
df_fixture.to_csv('clean_fifa_worldcup_fixture.csv',index=False)
```

## Extra verifications


```python
# verify number of matches per competition
years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974,
         1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014,
         2018]

for year in years:
    print(year, len(df_historical_data[df_historical_data['Year']==year]))
```

    1930 18
    1934 17
    1938 18
    1950 22
    1954 26
    1958 35
    1962 32
    1966 32
    1970 32
    1974 38
    1978 38
    1982 52
    1986 52
    1990 52
    1994 52
    1998 64
    2002 64
    2006 64
    2010 64
    2014 64
    2018 64
    


```python
# verify data collected for a team
print(df_historical_data[df_historical_data['HomeTeam'].str.contains('Turkey')])
print(df_historical_data[df_historical_data['AwayTeam'].str.contains('Turkey')])
```

        HomeTeam     AwayTeam  Year  HomeGoals  AwayGoals  TotalGoals
    83    Turkey  South Korea  1954          7          0           7
    774   Turkey        China  2002          3          0           3
             HomeTeam AwayTeam  Year  HomeGoals  AwayGoals  TotalGoals
    80   West Germany   Turkey  1954          4          1           5
    84   West Germany   Turkey  1954          7          2           9
    769        Brazil   Turkey  2002          2          1           3
    287         Japan   Turkey  2002          0          1           1
    292       Senegal   Turkey  2002          0          1           1
    294        Brazil   Turkey  2002          1          0           1
    295   South Korea   Turkey  2002          2          3           5
    772    Costa Rica   Turkey  2002          1          1           2
    

**By:_** **DataSpieler12345**


```python

```
