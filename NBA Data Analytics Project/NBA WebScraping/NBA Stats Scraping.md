```python
import pandas as pd
import requests
pd.set_option('display.max.columns', None) # so we can see all columns in a wide DataFrame 
import time 
import numpy as np
```


```python
test_url = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=Totals&Scope=S&Season=2012-13&SeasonType=Regular%20Season&StatCategory=PTS'
```


```python
r = requests.get(url=test_url).json()
```


```python
table_headers = r['resultSet']['headers']
```


```python
table_headers
```




    ['PLAYER_ID',
     'RANK',
     'PLAYER',
     'TEAM_ID',
     'TEAM',
     'GP',
     'MIN',
     'FGM',
     'FGA',
     'FG_PCT',
     'FG3M',
     'FG3A',
     'FG3_PCT',
     'FTM',
     'FTA',
     'FT_PCT',
     'OREB',
     'DREB',
     'REB',
     'AST',
     'STL',
     'BLK',
     'TOV',
     'PF',
     'PTS',
     'EFF',
     'AST_TOV',
     'STL_TOV']




```python
pd.DataFrame(r['resultSet']['rowSet'], columns=table_headers)
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
      <th>PLAYER_ID</th>
      <th>RANK</th>
      <th>PLAYER</th>
      <th>TEAM_ID</th>
      <th>TEAM</th>
      <th>GP</th>
      <th>MIN</th>
      <th>FGM</th>
      <th>FGA</th>
      <th>FG_PCT</th>
      <th>FG3M</th>
      <th>FG3A</th>
      <th>FG3_PCT</th>
      <th>FTM</th>
      <th>FTA</th>
      <th>FT_PCT</th>
      <th>OREB</th>
      <th>DREB</th>
      <th>REB</th>
      <th>AST</th>
      <th>STL</th>
      <th>BLK</th>
      <th>TOV</th>
      <th>PF</th>
      <th>PTS</th>
      <th>EFF</th>
      <th>AST_TOV</th>
      <th>STL_TOV</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>201142</td>
      <td>1</td>
      <td>Kevin Durant</td>
      <td>1610612760</td>
      <td>OKC</td>
      <td>81</td>
      <td>3119</td>
      <td>731</td>
      <td>1433</td>
      <td>0.510</td>
      <td>139</td>
      <td>334</td>
      <td>0.416</td>
      <td>679</td>
      <td>750</td>
      <td>0.905</td>
      <td>46</td>
      <td>594</td>
      <td>640</td>
      <td>374</td>
      <td>116</td>
      <td>105</td>
      <td>280</td>
      <td>143</td>
      <td>2280</td>
      <td>2462</td>
      <td>1.34</td>
      <td>0.41</td>
    </tr>
    <tr>
      <th>1</th>
      <td>977</td>
      <td>2</td>
      <td>Kobe Bryant</td>
      <td>1610612747</td>
      <td>LAL</td>
      <td>78</td>
      <td>3013</td>
      <td>738</td>
      <td>1595</td>
      <td>0.463</td>
      <td>132</td>
      <td>407</td>
      <td>0.324</td>
      <td>525</td>
      <td>626</td>
      <td>0.839</td>
      <td>66</td>
      <td>367</td>
      <td>433</td>
      <td>469</td>
      <td>106</td>
      <td>25</td>
      <td>287</td>
      <td>173</td>
      <td>2133</td>
      <td>1921</td>
      <td>1.63</td>
      <td>0.37</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2544</td>
      <td>3</td>
      <td>LeBron James</td>
      <td>1610612748</td>
      <td>MIA</td>
      <td>76</td>
      <td>2877</td>
      <td>765</td>
      <td>1354</td>
      <td>0.565</td>
      <td>103</td>
      <td>254</td>
      <td>0.406</td>
      <td>403</td>
      <td>535</td>
      <td>0.753</td>
      <td>97</td>
      <td>513</td>
      <td>610</td>
      <td>551</td>
      <td>129</td>
      <td>67</td>
      <td>226</td>
      <td>110</td>
      <td>2036</td>
      <td>2446</td>
      <td>2.44</td>
      <td>0.57</td>
    </tr>
    <tr>
      <th>3</th>
      <td>201935</td>
      <td>4</td>
      <td>James Harden</td>
      <td>1610612745</td>
      <td>HOU</td>
      <td>78</td>
      <td>2985</td>
      <td>585</td>
      <td>1337</td>
      <td>0.438</td>
      <td>179</td>
      <td>486</td>
      <td>0.368</td>
      <td>674</td>
      <td>792</td>
      <td>0.851</td>
      <td>62</td>
      <td>317</td>
      <td>379</td>
      <td>455</td>
      <td>142</td>
      <td>38</td>
      <td>295</td>
      <td>178</td>
      <td>2023</td>
      <td>1872</td>
      <td>1.54</td>
      <td>0.48</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2546</td>
      <td>5</td>
      <td>Carmelo Anthony</td>
      <td>1610612752</td>
      <td>NYK</td>
      <td>67</td>
      <td>2482</td>
      <td>669</td>
      <td>1489</td>
      <td>0.449</td>
      <td>157</td>
      <td>414</td>
      <td>0.379</td>
      <td>425</td>
      <td>512</td>
      <td>0.830</td>
      <td>134</td>
      <td>326</td>
      <td>460</td>
      <td>171</td>
      <td>52</td>
      <td>32</td>
      <td>175</td>
      <td>205</td>
      <td>1920</td>
      <td>1553</td>
      <td>0.98</td>
      <td>0.30</td>
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
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>463</th>
      <td>203130</td>
      <td>463</td>
      <td>Darius Johnson-Odom</td>
      <td>1610612747</td>
      <td>LAL</td>
      <td>4</td>
      <td>6</td>
      <td>0</td>
      <td>4</td>
      <td>0.000</td>
      <td>0</td>
      <td>1</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>1</td>
      <td>3</td>
      <td>4</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>464</th>
      <td>2545</td>
      <td>463</td>
      <td>Darko Milicic</td>
      <td>1610612738</td>
      <td>BOS</td>
      <td>1</td>
      <td>5</td>
      <td>0</td>
      <td>1</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>0</td>
      <td>-2</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>465</th>
      <td>202458</td>
      <td>463</td>
      <td>Justin Dentmon</td>
      <td>1610612742</td>
      <td>DAL</td>
      <td>2</td>
      <td>4</td>
      <td>0</td>
      <td>2</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>-2</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>466</th>
      <td>2679</td>
      <td>463</td>
      <td>Matt Carroll</td>
      <td>1610612766</td>
      <td>CHA</td>
      <td>1</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>467</th>
      <td>200780</td>
      <td>463</td>
      <td>Solomon Jones</td>
      <td>1610612752</td>
      <td>NYK</td>
      <td>2</td>
      <td>26</td>
      <td>0</td>
      <td>1</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>
<p>468 rows × 28 columns</p>
</div>




```python
temp_df1 = pd.DataFrame(r['resultSet']['rowSet'], columns=table_headers)
temp_df2 = pd.DataFrame({'Year':['2012-13' for i in range(len(temp_df1))],
                         'Season_type':['Regular%20Season' for i in range(len(temp_df1))]})

temp_df3 = pd.concat([temp_df2, temp_df1], axis=1)
temp_df3
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
      <th>Year</th>
      <th>Season_type</th>
      <th>PLAYER_ID</th>
      <th>RANK</th>
      <th>PLAYER</th>
      <th>TEAM_ID</th>
      <th>TEAM</th>
      <th>GP</th>
      <th>MIN</th>
      <th>FGM</th>
      <th>FGA</th>
      <th>FG_PCT</th>
      <th>FG3M</th>
      <th>FG3A</th>
      <th>FG3_PCT</th>
      <th>FTM</th>
      <th>FTA</th>
      <th>FT_PCT</th>
      <th>OREB</th>
      <th>DREB</th>
      <th>REB</th>
      <th>AST</th>
      <th>STL</th>
      <th>BLK</th>
      <th>TOV</th>
      <th>PF</th>
      <th>PTS</th>
      <th>EFF</th>
      <th>AST_TOV</th>
      <th>STL_TOV</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2012-13</td>
      <td>Regular%20Season</td>
      <td>201142</td>
      <td>1</td>
      <td>Kevin Durant</td>
      <td>1610612760</td>
      <td>OKC</td>
      <td>81</td>
      <td>3119</td>
      <td>731</td>
      <td>1433</td>
      <td>0.510</td>
      <td>139</td>
      <td>334</td>
      <td>0.416</td>
      <td>679</td>
      <td>750</td>
      <td>0.905</td>
      <td>46</td>
      <td>594</td>
      <td>640</td>
      <td>374</td>
      <td>116</td>
      <td>105</td>
      <td>280</td>
      <td>143</td>
      <td>2280</td>
      <td>2462</td>
      <td>1.34</td>
      <td>0.41</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2012-13</td>
      <td>Regular%20Season</td>
      <td>977</td>
      <td>2</td>
      <td>Kobe Bryant</td>
      <td>1610612747</td>
      <td>LAL</td>
      <td>78</td>
      <td>3013</td>
      <td>738</td>
      <td>1595</td>
      <td>0.463</td>
      <td>132</td>
      <td>407</td>
      <td>0.324</td>
      <td>525</td>
      <td>626</td>
      <td>0.839</td>
      <td>66</td>
      <td>367</td>
      <td>433</td>
      <td>469</td>
      <td>106</td>
      <td>25</td>
      <td>287</td>
      <td>173</td>
      <td>2133</td>
      <td>1921</td>
      <td>1.63</td>
      <td>0.37</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2012-13</td>
      <td>Regular%20Season</td>
      <td>2544</td>
      <td>3</td>
      <td>LeBron James</td>
      <td>1610612748</td>
      <td>MIA</td>
      <td>76</td>
      <td>2877</td>
      <td>765</td>
      <td>1354</td>
      <td>0.565</td>
      <td>103</td>
      <td>254</td>
      <td>0.406</td>
      <td>403</td>
      <td>535</td>
      <td>0.753</td>
      <td>97</td>
      <td>513</td>
      <td>610</td>
      <td>551</td>
      <td>129</td>
      <td>67</td>
      <td>226</td>
      <td>110</td>
      <td>2036</td>
      <td>2446</td>
      <td>2.44</td>
      <td>0.57</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2012-13</td>
      <td>Regular%20Season</td>
      <td>201935</td>
      <td>4</td>
      <td>James Harden</td>
      <td>1610612745</td>
      <td>HOU</td>
      <td>78</td>
      <td>2985</td>
      <td>585</td>
      <td>1337</td>
      <td>0.438</td>
      <td>179</td>
      <td>486</td>
      <td>0.368</td>
      <td>674</td>
      <td>792</td>
      <td>0.851</td>
      <td>62</td>
      <td>317</td>
      <td>379</td>
      <td>455</td>
      <td>142</td>
      <td>38</td>
      <td>295</td>
      <td>178</td>
      <td>2023</td>
      <td>1872</td>
      <td>1.54</td>
      <td>0.48</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2012-13</td>
      <td>Regular%20Season</td>
      <td>2546</td>
      <td>5</td>
      <td>Carmelo Anthony</td>
      <td>1610612752</td>
      <td>NYK</td>
      <td>67</td>
      <td>2482</td>
      <td>669</td>
      <td>1489</td>
      <td>0.449</td>
      <td>157</td>
      <td>414</td>
      <td>0.379</td>
      <td>425</td>
      <td>512</td>
      <td>0.830</td>
      <td>134</td>
      <td>326</td>
      <td>460</td>
      <td>171</td>
      <td>52</td>
      <td>32</td>
      <td>175</td>
      <td>205</td>
      <td>1920</td>
      <td>1553</td>
      <td>0.98</td>
      <td>0.30</td>
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
      <th>463</th>
      <td>2012-13</td>
      <td>Regular%20Season</td>
      <td>203130</td>
      <td>463</td>
      <td>Darius Johnson-Odom</td>
      <td>1610612747</td>
      <td>LAL</td>
      <td>4</td>
      <td>6</td>
      <td>0</td>
      <td>4</td>
      <td>0.000</td>
      <td>0</td>
      <td>1</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>1</td>
      <td>3</td>
      <td>4</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>464</th>
      <td>2012-13</td>
      <td>Regular%20Season</td>
      <td>2545</td>
      <td>463</td>
      <td>Darko Milicic</td>
      <td>1610612738</td>
      <td>BOS</td>
      <td>1</td>
      <td>5</td>
      <td>0</td>
      <td>1</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>0</td>
      <td>-2</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>465</th>
      <td>2012-13</td>
      <td>Regular%20Season</td>
      <td>202458</td>
      <td>463</td>
      <td>Justin Dentmon</td>
      <td>1610612742</td>
      <td>DAL</td>
      <td>2</td>
      <td>4</td>
      <td>0</td>
      <td>2</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>-2</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>466</th>
      <td>2012-13</td>
      <td>Regular%20Season</td>
      <td>2679</td>
      <td>463</td>
      <td>Matt Carroll</td>
      <td>1610612766</td>
      <td>CHA</td>
      <td>1</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>467</th>
      <td>2012-13</td>
      <td>Regular%20Season</td>
      <td>200780</td>
      <td>463</td>
      <td>Solomon Jones</td>
      <td>1610612752</td>
      <td>NYK</td>
      <td>2</td>
      <td>26</td>
      <td>0</td>
      <td>1</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>
<p>468 rows × 30 columns</p>
</div>




```python
del temp_df1, temp_df2, temp_df3
```


```python
df_cols = ['Year','Season_Type'] + table_headers
```


```python
df_cols
```




    ['Year',
     'Season_Type',
     'PLAYER_ID',
     'RANK',
     'PLAYER',
     'TEAM_ID',
     'TEAM',
     'GP',
     'MIN',
     'FGM',
     'FGA',
     'FG_PCT',
     'FG3M',
     'FG3A',
     'FG3_PCT',
     'FTM',
     'FTA',
     'FT_PCT',
     'OREB',
     'DREB',
     'REB',
     'AST',
     'STL',
     'BLK',
     'TOV',
     'PF',
     'PTS',
     'EFF',
     'AST_TOV',
     'STL_TOV']




```python
pd.DataFrame(columns=df_cols)
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
      <th>Year</th>
      <th>Season_Type</th>
      <th>PLAYER_ID</th>
      <th>RANK</th>
      <th>PLAYER</th>
      <th>TEAM_ID</th>
      <th>TEAM</th>
      <th>GP</th>
      <th>MIN</th>
      <th>FGM</th>
      <th>FGA</th>
      <th>FG_PCT</th>
      <th>FG3M</th>
      <th>FG3A</th>
      <th>FG3_PCT</th>
      <th>FTM</th>
      <th>FTA</th>
      <th>FT_PCT</th>
      <th>OREB</th>
      <th>DREB</th>
      <th>REB</th>
      <th>AST</th>
      <th>STL</th>
      <th>BLK</th>
      <th>TOV</th>
      <th>PF</th>
      <th>PTS</th>
      <th>EFF</th>
      <th>AST_TOV</th>
      <th>STL_TOV</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>




```python
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
```


```python
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
```

    Finished scraping data for the 2012-13 Regular%20Season.
    ...waiting 16.3 seconds
    Finished scraping data for the 2012-13 Playoffs.
    ...waiting 30.7 seconds
    Finished scraping data for the 2013-14 Regular%20Season.
    ...waiting 31.9 seconds
    Finished scraping data for the 2013-14 Playoffs.
    ...waiting 26.1 seconds
    Finished scraping data for the 2014-15 Regular%20Season.
    ...waiting 24.7 seconds
    Finished scraping data for the 2014-15 Playoffs.
    ...waiting 9.1 seconds
    Finished scraping data for the 2015-16 Regular%20Season.
    ...waiting 6.6 seconds
    Finished scraping data for the 2015-16 Playoffs.
    ...waiting 8.2 seconds
    Finished scraping data for the 2016-17 Regular%20Season.
    ...waiting 19.0 seconds
    Finished scraping data for the 2016-17 Playoffs.
    ...waiting 12.9 seconds
    Finished scraping data for the 2017-18 Regular%20Season.
    ...waiting 27.3 seconds
    Finished scraping data for the 2017-18 Playoffs.
    ...waiting 37.6 seconds
    Finished scraping data for the 2018-19 Regular%20Season.
    ...waiting 33.1 seconds
    Finished scraping data for the 2018-19 Playoffs.
    ...waiting 19.2 seconds
    Finished scraping data for the 2019-20 Regular%20Season.
    ...waiting 34.5 seconds
    Finished scraping data for the 2019-20 Playoffs.
    ...waiting 34.8 seconds
    Finished scraping data for the 2020-21 Regular%20Season.
    ...waiting 34.6 seconds
    Finished scraping data for the 2020-21 Playoffs.
    ...waiting 10.8 seconds
    Finished scraping data for the 2021-22 Regular%20Season.
    ...waiting 33.8 seconds
    Finished scraping data for the 2021-22 Playoffs.
    ...waiting 21.0 seconds
    Process completed! Total run time: 8.01
    


```python
df
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
      <th>Year</th>
      <th>Season_Type</th>
      <th>PLAYER_ID</th>
      <th>RANK</th>
      <th>PLAYER</th>
      <th>TEAM_ID</th>
      <th>TEAM</th>
      <th>GP</th>
      <th>MIN</th>
      <th>FGM</th>
      <th>FGA</th>
      <th>FG_PCT</th>
      <th>FG3M</th>
      <th>FG3A</th>
      <th>FG3_PCT</th>
      <th>FTM</th>
      <th>FTA</th>
      <th>FT_PCT</th>
      <th>OREB</th>
      <th>DREB</th>
      <th>REB</th>
      <th>AST</th>
      <th>STL</th>
      <th>BLK</th>
      <th>TOV</th>
      <th>PF</th>
      <th>PTS</th>
      <th>EFF</th>
      <th>AST_TOV</th>
      <th>STL_TOV</th>
      <th>Season_type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2012-13</td>
      <td>NaN</td>
      <td>201142</td>
      <td>1</td>
      <td>Kevin Durant</td>
      <td>1610612760</td>
      <td>OKC</td>
      <td>81</td>
      <td>3119</td>
      <td>731</td>
      <td>1433</td>
      <td>0.510</td>
      <td>139</td>
      <td>334</td>
      <td>0.416</td>
      <td>679</td>
      <td>750</td>
      <td>0.905</td>
      <td>46</td>
      <td>594</td>
      <td>640</td>
      <td>374</td>
      <td>116</td>
      <td>105</td>
      <td>280</td>
      <td>143</td>
      <td>2280</td>
      <td>2462</td>
      <td>1.34</td>
      <td>0.41</td>
      <td>Regular%20Season</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2012-13</td>
      <td>NaN</td>
      <td>977</td>
      <td>2</td>
      <td>Kobe Bryant</td>
      <td>1610612747</td>
      <td>LAL</td>
      <td>78</td>
      <td>3013</td>
      <td>738</td>
      <td>1595</td>
      <td>0.463</td>
      <td>132</td>
      <td>407</td>
      <td>0.324</td>
      <td>525</td>
      <td>626</td>
      <td>0.839</td>
      <td>66</td>
      <td>367</td>
      <td>433</td>
      <td>469</td>
      <td>106</td>
      <td>25</td>
      <td>287</td>
      <td>173</td>
      <td>2133</td>
      <td>1921</td>
      <td>1.63</td>
      <td>0.37</td>
      <td>Regular%20Season</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2012-13</td>
      <td>NaN</td>
      <td>2544</td>
      <td>3</td>
      <td>LeBron James</td>
      <td>1610612748</td>
      <td>MIA</td>
      <td>76</td>
      <td>2877</td>
      <td>765</td>
      <td>1354</td>
      <td>0.565</td>
      <td>103</td>
      <td>254</td>
      <td>0.406</td>
      <td>403</td>
      <td>535</td>
      <td>0.753</td>
      <td>97</td>
      <td>513</td>
      <td>610</td>
      <td>551</td>
      <td>129</td>
      <td>67</td>
      <td>226</td>
      <td>110</td>
      <td>2036</td>
      <td>2446</td>
      <td>2.44</td>
      <td>0.57</td>
      <td>Regular%20Season</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2012-13</td>
      <td>NaN</td>
      <td>201935</td>
      <td>4</td>
      <td>James Harden</td>
      <td>1610612745</td>
      <td>HOU</td>
      <td>78</td>
      <td>2985</td>
      <td>585</td>
      <td>1337</td>
      <td>0.438</td>
      <td>179</td>
      <td>486</td>
      <td>0.368</td>
      <td>674</td>
      <td>792</td>
      <td>0.851</td>
      <td>62</td>
      <td>317</td>
      <td>379</td>
      <td>455</td>
      <td>142</td>
      <td>38</td>
      <td>295</td>
      <td>178</td>
      <td>2023</td>
      <td>1872</td>
      <td>1.54</td>
      <td>0.48</td>
      <td>Regular%20Season</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2012-13</td>
      <td>NaN</td>
      <td>2546</td>
      <td>5</td>
      <td>Carmelo Anthony</td>
      <td>1610612752</td>
      <td>NYK</td>
      <td>67</td>
      <td>2482</td>
      <td>669</td>
      <td>1489</td>
      <td>0.449</td>
      <td>157</td>
      <td>414</td>
      <td>0.379</td>
      <td>425</td>
      <td>512</td>
      <td>0.830</td>
      <td>134</td>
      <td>326</td>
      <td>460</td>
      <td>171</td>
      <td>52</td>
      <td>32</td>
      <td>175</td>
      <td>205</td>
      <td>1920</td>
      <td>1553</td>
      <td>0.98</td>
      <td>0.30</td>
      <td>Regular%20Season</td>
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
      <th>212</th>
      <td>2021-22</td>
      <td>NaN</td>
      <td>1629006</td>
      <td>206</td>
      <td>Josh Okogie</td>
      <td>1610612750</td>
      <td>MIN</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>Playoffs</td>
    </tr>
    <tr>
      <th>213</th>
      <td>2021-22</td>
      <td>NaN</td>
      <td>1630556</td>
      <td>206</td>
      <td>Kessler Edwards</td>
      <td>1610612751</td>
      <td>BKN</td>
      <td>2</td>
      <td>7</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>1.00</td>
      <td>1.00</td>
      <td>Playoffs</td>
    </tr>
    <tr>
      <th>214</th>
      <td>2021-22</td>
      <td>NaN</td>
      <td>1630201</td>
      <td>206</td>
      <td>Malachi Flynn</td>
      <td>1610612761</td>
      <td>TOR</td>
      <td>6</td>
      <td>36</td>
      <td>0</td>
      <td>7</td>
      <td>0.000</td>
      <td>0</td>
      <td>3</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>2</td>
      <td>1</td>
      <td>3</td>
      <td>3</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>6</td>
      <td>0</td>
      <td>-1</td>
      <td>3.00</td>
      <td>1.00</td>
      <td>Playoffs</td>
    </tr>
    <tr>
      <th>215</th>
      <td>2021-22</td>
      <td>NaN</td>
      <td>202693</td>
      <td>206</td>
      <td>Markieff Morris</td>
      <td>1610612748</td>
      <td>MIA</td>
      <td>2</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>-1</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>Playoffs</td>
    </tr>
    <tr>
      <th>216</th>
      <td>2021-22</td>
      <td>NaN</td>
      <td>200794</td>
      <td>206</td>
      <td>Paul Millsap</td>
      <td>1610612755</td>
      <td>PHI</td>
      <td>1</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>Playoffs</td>
    </tr>
  </tbody>
</table>
<p>7293 rows × 31 columns</p>
</div>


