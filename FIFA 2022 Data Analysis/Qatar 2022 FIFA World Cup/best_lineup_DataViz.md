```python
# Import the libraries 
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
sns.set_style('darkgrid')
```


```python
# nation_position, club_position, player_positions

df = pd.read_csv('players_22.csv', low_memory=False)

# selecting column
df = df[['short_name', 'age', 'nationality_name', 'overall', 'potential',
         'club_name', 'value_eur', 'wage_eur', 'player_positions']]

# selecting only one position
df['player_positions'] = df['player_positions'].str.split(',', expand=True)[0]

# dropping nan
df.dropna(inplace=True)
df = pd.read_csv('players_22.csv', low_memory=False)

# selecting column
df = df[['short_name', 'age', 'nationality_name', 'overall', 'potential',
         'club_name', 'value_eur', 'wage_eur', 'player_positions']]

# selecting only one position
df['player_positions'] = df['player_positions'].str.split(',', expand=True)[0]

# dropping nan
df.dropna(inplace=True)
```


```python
players_missing_worldcup = ['K. Benzema', 'S. Mané', 'S. Agüero', 'Sergio Ramos', 'P. Pogba',
                            'M. Reus', 'Diogo Jota', 'A. Harit', 'N. Kanté', 'G. Lo Celso', 'Piqué']

# dropping injured players
drop_index = df[df['short_name'].isin(players_missing_worldcup)].index
df.drop(drop_index, axis=0, inplace=True)
```


```python
teams_worldcup = [
    'Qatar', 'Brazil', 'Belgium', 'France', 'Argentina', 'England', 'Spain', 'Portugal',
    'Mexico', 'Netherlands', 'Denmark', 'Germany', 'Uruguay', 'Switzerland', 'United States', 'Croatia',
    'Senegal', 'Iran', 'Japan', 'Morocco', 'Serbia', 'Poland', 'South Korea', 'Tunisia',
    'Cameroon', 'Canada', 'Ecuador', 'Saudi Arabia', 'Ghana', 'Wales', 'Costa Rica', 'Australia'
]

# filtering only national teams in the world cup
df = df[df['nationality_name'].isin(teams_worldcup)]
```


```python
# best players
df.sort_values(by=['overall', 'potential', 'value_eur'], ascending=False, inplace=True)
```

## Distribution of players overall


```python
import numpy as np
fig, ax = plt.subplots(figsize=(12, 5), tight_layout=True)

sns.histplot(df, x='overall', binwidth=1)

bins = np.arange(df['overall'].min(), df['overall'].max(), 1)
plt.xticks(bins)
plt.show()
```


    
![png](output_6_0.png)
    


## Dream Team World Cup Players


```python
df.drop_duplicates('player_positions')
# viz -> https://trinket.io/python/0813ea96f6
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
      <th>short_name</th>
      <th>age</th>
      <th>nationality_name</th>
      <th>overall</th>
      <th>potential</th>
      <th>club_name</th>
      <th>value_eur</th>
      <th>wage_eur</th>
      <th>player_positions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <td>W. Szczęsny</td>
      <td>31.0</td>
      <td>Poland</td>
      <td>87.0</td>
      <td>87.0</td>
      <td>Juventus</td>
      <td>42000000.0</td>
      <td>105000.0</td>
      <td>GK</td>
    </tr>
    <tr>
      <th>67</th>
      <td>Rodri</td>
      <td>25.0</td>
      <td>Spain</td>
      <td>86.0</td>
      <td>89.0</td>
      <td>Manchester City</td>
      <td>81000000.0</td>
      <td>175000.0</td>
      <td>CDM</td>
    </tr>
    <tr>
      <th>57</th>
      <td>R. Varane</td>
      <td>28.0</td>
      <td>France</td>
      <td>86.0</td>
      <td>88.0</td>
      <td>Manchester United</td>
      <td>68500000.0</td>
      <td>180000.0</td>
      <td>CB</td>
    </tr>
    <tr>
      <th>87</th>
      <td>Carvajal</td>
      <td>29.0</td>
      <td>Spain</td>
      <td>85.0</td>
      <td>85.0</td>
      <td>Real Madrid CF</td>
      <td>47500000.0</td>
      <td>210000.0</td>
      <td>RB</td>
    </tr>
    <tr>
      <th>137</th>
      <td>T. Hernández</td>
      <td>23.0</td>
      <td>France</td>
      <td>84.0</td>
      <td>90.0</td>
      <td>AC Milan</td>
      <td>62500000.0</td>
      <td>51000.0</td>
      <td>LB</td>
    </tr>
    <tr>
      <th>135</th>
      <td>André Silva</td>
      <td>25.0</td>
      <td>Portugal</td>
      <td>84.0</td>
      <td>85.0</td>
      <td>RB Leipzig</td>
      <td>51000000.0</td>
      <td>110000.0</td>
      <td>ST</td>
    </tr>
    <tr>
      <th>196</th>
      <td>F. Valverde</td>
      <td>22.0</td>
      <td>Uruguay</td>
      <td>83.0</td>
      <td>89.0</td>
      <td>Real Madrid CF</td>
      <td>58000000.0</td>
      <td>160000.0</td>
      <td>CM</td>
    </tr>
    <tr>
      <th>817</th>
      <td>Prazeracinho</td>
      <td>21.0</td>
      <td>Brazil</td>
      <td>78.0</td>
      <td>78.0</td>
      <td>Flamengo</td>
      <td>16500000.0</td>
      <td>33000.0</td>
      <td>LW</td>
    </tr>
    <tr>
      <th>1048</th>
      <td>Muo Cadete</td>
      <td>21.0</td>
      <td>Brazil</td>
      <td>77.0</td>
      <td>77.0</td>
      <td>Palmeiras</td>
      <td>12500000.0</td>
      <td>28000.0</td>
      <td>LM</td>
    </tr>
    <tr>
      <th>1454</th>
      <td>Tete</td>
      <td>21.0</td>
      <td>Brazil</td>
      <td>76.0</td>
      <td>86.0</td>
      <td>Shakhtar Donetsk</td>
      <td>17000000.0</td>
      <td>800.0</td>
      <td>RM</td>
    </tr>
    <tr>
      <th>1421</th>
      <td>E. Smith Rowe</td>
      <td>20.0</td>
      <td>England</td>
      <td>76.0</td>
      <td>86.0</td>
      <td>Arsenal</td>
      <td>16500000.0</td>
      <td>49000.0</td>
      <td>CAM</td>
    </tr>
    <tr>
      <th>2888</th>
      <td>Claudiosa Paes</td>
      <td>33.0</td>
      <td>Brazil</td>
      <td>73.0</td>
      <td>73.0</td>
      <td>São Paulo</td>
      <td>1900000.0</td>
      <td>31000.0</td>
      <td>RW</td>
    </tr>
    <tr>
      <th>5437</th>
      <td>E. Meza</td>
      <td>22.0</td>
      <td>Argentina</td>
      <td>70.0</td>
      <td>76.0</td>
      <td>Club Atlético Colón</td>
      <td>2400000.0</td>
      <td>6000.0</td>
      <td>RWB</td>
    </tr>
    <tr>
      <th>7373</th>
      <td>Nilton Varela</td>
      <td>20.0</td>
      <td>Portugal</td>
      <td>68.0</td>
      <td>77.0</td>
      <td>Belenenses SAD</td>
      <td>2500000.0</td>
      <td>2000.0</td>
      <td>LWB</td>
    </tr>
    <tr>
      <th>7758</th>
      <td>D. Accam</td>
      <td>30.0</td>
      <td>Ghana</td>
      <td>67.0</td>
      <td>67.0</td>
      <td>Hammarby IF</td>
      <td>1000000.0</td>
      <td>3000.0</td>
      <td>CF</td>
    </tr>
  </tbody>
</table>
</div>



## The Most Skillful Players on each National Team


```python
df_best_players = df.copy()
df_best_players = df_best_players.drop_duplicates('nationality_name').reset_index(drop=True)
country_short =  df_best_players['nationality_name'].str.extract('(^\w{3})', expand=False).str.upper()
df_best_players['name_nationality'] = df_best_players['short_name'] +' (' + country_short + ')'

fig, ax = plt.subplots(figsize=(10, 6), tight_layout=True)

sns.barplot(x='overall', y='name_nationality', data=df_best_players,
            palette=sns.color_palette('pastel'))
plt.show()
```


    
![png](output_10_0.png)
    


## Best Squad per Team


```python
def best_squad(nationality):
    df_best_squad = df.copy()
    df_best_squad = df_best_squad.groupby(['nationality_name', 'player_positions']).head(2)
    df_best_squad = df_best_squad[df_best_squad['nationality_name']==nationality].sort_values(['player_positions', 'overall', 'potential'], ascending=False)
    return df_best_squad
```


```python
best_squad('Brazil')
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
      <th>short_name</th>
      <th>age</th>
      <th>nationality_name</th>
      <th>overall</th>
      <th>potential</th>
      <th>club_name</th>
      <th>value_eur</th>
      <th>wage_eur</th>
      <th>player_positions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>815</th>
      <td>Fredditinho</td>
      <td>33.0</td>
      <td>Brazil</td>
      <td>78.0</td>
      <td>78.0</td>
      <td>Palmeiras</td>
      <td>9000000.0</td>
      <td>43000.0</td>
      <td>ST</td>
    </tr>
    <tr>
      <th>1117</th>
      <td>Vinícius</td>
      <td>26.0</td>
      <td>Brazil</td>
      <td>77.0</td>
      <td>80.0</td>
      <td>PSV</td>
      <td>14000000.0</td>
      <td>16000.0</td>
      <td>ST</td>
    </tr>
    <tr>
      <th>2888</th>
      <td>Claudiosa Paes</td>
      <td>33.0</td>
      <td>Brazil</td>
      <td>73.0</td>
      <td>73.0</td>
      <td>São Paulo</td>
      <td>1900000.0</td>
      <td>31000.0</td>
      <td>RW</td>
    </tr>
    <tr>
      <th>3592</th>
      <td>Dersan Dinis</td>
      <td>29.0</td>
      <td>Brazil</td>
      <td>72.0</td>
      <td>72.0</td>
      <td>Palmeiras</td>
      <td>2300000.0</td>
      <td>28000.0</td>
      <td>RW</td>
    </tr>
    <tr>
      <th>1454</th>
      <td>Tete</td>
      <td>21.0</td>
      <td>Brazil</td>
      <td>76.0</td>
      <td>86.0</td>
      <td>Shakhtar Donetsk</td>
      <td>17000000.0</td>
      <td>800.0</td>
      <td>RM</td>
    </tr>
    <tr>
      <th>2881</th>
      <td>Brenito Duarte</td>
      <td>29.0</td>
      <td>Brazil</td>
      <td>73.0</td>
      <td>73.0</td>
      <td>Cuiabá</td>
      <td>3000000.0</td>
      <td>15000.0</td>
      <td>RM</td>
    </tr>
    <tr>
      <th>626</th>
      <td>Adnan Vidual</td>
      <td>29.0</td>
      <td>Brazil</td>
      <td>79.0</td>
      <td>79.0</td>
      <td>Internacional</td>
      <td>15500000.0</td>
      <td>32000.0</td>
      <td>RB</td>
    </tr>
    <tr>
      <th>1833</th>
      <td>Jesus Andradaldo</td>
      <td>29.0</td>
      <td>Brazil</td>
      <td>75.0</td>
      <td>75.0</td>
      <td>Grêmio</td>
      <td>4900000.0</td>
      <td>26000.0</td>
      <td>RB</td>
    </tr>
    <tr>
      <th>817</th>
      <td>Prazeracinho</td>
      <td>21.0</td>
      <td>Brazil</td>
      <td>78.0</td>
      <td>78.0</td>
      <td>Flamengo</td>
      <td>16500000.0</td>
      <td>33000.0</td>
      <td>LW</td>
    </tr>
    <tr>
      <th>3597</th>
      <td>Vicemte Tófoli</td>
      <td>25.0</td>
      <td>Brazil</td>
      <td>72.0</td>
      <td>72.0</td>
      <td>RB Bragantino</td>
      <td>2600000.0</td>
      <td>13000.0</td>
      <td>LW</td>
    </tr>
    <tr>
      <th>1048</th>
      <td>Muo Cadete</td>
      <td>21.0</td>
      <td>Brazil</td>
      <td>77.0</td>
      <td>77.0</td>
      <td>Palmeiras</td>
      <td>12500000.0</td>
      <td>28000.0</td>
      <td>LM</td>
    </tr>
    <tr>
      <th>2267</th>
      <td>Ailtio Coelho</td>
      <td>29.0</td>
      <td>Brazil</td>
      <td>74.0</td>
      <td>74.0</td>
      <td>São Paulo</td>
      <td>4100000.0</td>
      <td>32000.0</td>
      <td>LM</td>
    </tr>
    <tr>
      <th>386</th>
      <td>Renan Lodi</td>
      <td>23.0</td>
      <td>Brazil</td>
      <td>81.0</td>
      <td>86.0</td>
      <td>Atlético de Madrid</td>
      <td>36500000.0</td>
      <td>49000.0</td>
      <td>LB</td>
    </tr>
    <tr>
      <th>424</th>
      <td>Ismaily</td>
      <td>31.0</td>
      <td>Brazil</td>
      <td>80.0</td>
      <td>80.0</td>
      <td>Shakhtar Donetsk</td>
      <td>15500000.0</td>
      <td>1000.0</td>
      <td>LB</td>
    </tr>
    <tr>
      <th>222</th>
      <td>Neto</td>
      <td>31.0</td>
      <td>Brazil</td>
      <td>82.0</td>
      <td>82.0</td>
      <td>FC Barcelona</td>
      <td>16000000.0</td>
      <td>115000.0</td>
      <td>GK</td>
    </tr>
    <tr>
      <th>265</th>
      <td>Raphaelinho Anjos</td>
      <td>33.0</td>
      <td>Brazil</td>
      <td>82.0</td>
      <td>82.0</td>
      <td>RB Bragantino</td>
      <td>10000000.0</td>
      <td>20000.0</td>
      <td>GK</td>
    </tr>
    <tr>
      <th>483</th>
      <td>Gerson</td>
      <td>24.0</td>
      <td>Brazil</td>
      <td>80.0</td>
      <td>84.0</td>
      <td>Olympique de Marseille</td>
      <td>30000000.0</td>
      <td>41000.0</td>
      <td>CM</td>
    </tr>
    <tr>
      <th>1461</th>
      <td>Matheus Nunes</td>
      <td>22.0</td>
      <td>Brazil</td>
      <td>76.0</td>
      <td>85.0</td>
      <td>Sporting CP</td>
      <td>17000000.0</td>
      <td>12000.0</td>
      <td>CM</td>
    </tr>
    <tr>
      <th>294</th>
      <td>Lucas Leiva</td>
      <td>34.0</td>
      <td>Brazil</td>
      <td>81.0</td>
      <td>81.0</td>
      <td>Lazio</td>
      <td>9000000.0</td>
      <td>64000.0</td>
      <td>CDM</td>
    </tr>
    <tr>
      <th>628</th>
      <td>Melvin Parrela</td>
      <td>21.0</td>
      <td>Brazil</td>
      <td>79.0</td>
      <td>79.0</td>
      <td>RB Bragantino</td>
      <td>18500000.0</td>
      <td>15000.0</td>
      <td>CDM</td>
    </tr>
    <tr>
      <th>120</th>
      <td>Felipe</td>
      <td>32.0</td>
      <td>Brazil</td>
      <td>84.0</td>
      <td>84.0</td>
      <td>Atlético de Madrid</td>
      <td>27500000.0</td>
      <td>74000.0</td>
      <td>CB</td>
    </tr>
    <tr>
      <th>279</th>
      <td>Éder Militão</td>
      <td>23.0</td>
      <td>Brazil</td>
      <td>82.0</td>
      <td>89.0</td>
      <td>Real Madrid CF</td>
      <td>56500000.0</td>
      <td>130000.0</td>
      <td>CB</td>
    </tr>
    <tr>
      <th>2890</th>
      <td>Marlon Nideiro</td>
      <td>25.0</td>
      <td>Brazil</td>
      <td>73.0</td>
      <td>73.0</td>
      <td>Grêmio</td>
      <td>3400000.0</td>
      <td>22000.0</td>
      <td>CAM</td>
    </tr>
    <tr>
      <th>3653</th>
      <td>Caio Milaçar</td>
      <td>25.0</td>
      <td>Brazil</td>
      <td>72.0</td>
      <td>72.0</td>
      <td>Ceará Sporting Club</td>
      <td>2600000.0</td>
      <td>10000.0</td>
      <td>CAM</td>
    </tr>
  </tbody>
</table>
</div>




```python
average_overall = [best_squad(team)['overall'].mean() for team in teams_worldcup]

df_average_overall = pd.DataFrame({'Teams': teams_worldcup, 'AVG_Overall': average_overall})
df_average_overall = df_average_overall.dropna()
df_average_overall = df_average_overall.sort_values('AVG_Overall', ascending=False)
df_average_overall
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
      <th>Teams</th>
      <th>AVG_Overall</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Brazil</td>
      <td>77.333333</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Spain</td>
      <td>74.086957</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Portugal</td>
      <td>72.285714</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Uruguay</td>
      <td>71.842105</td>
    </tr>
    <tr>
      <th>3</th>
      <td>France</td>
      <td>71.444444</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Serbia</td>
      <td>71.125000</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Switzerland</td>
      <td>71.000000</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Poland</td>
      <td>70.714286</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Croatia</td>
      <td>70.714286</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Argentina</td>
      <td>70.666667</td>
    </tr>
    <tr>
      <th>5</th>
      <td>England</td>
      <td>70.555556</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Netherlands</td>
      <td>70.173913</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Senegal</td>
      <td>69.692308</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Germany</td>
      <td>69.464286</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Iran</td>
      <td>68.571429</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Denmark</td>
      <td>68.480000</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Costa Rica</td>
      <td>68.428571</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Mexico</td>
      <td>68.238095</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Cameroon</td>
      <td>67.384615</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Belgium</td>
      <td>67.181818</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Japan</td>
      <td>66.904762</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Morocco</td>
      <td>66.785714</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Tunisia</td>
      <td>66.625000</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Ghana</td>
      <td>66.047619</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Wales</td>
      <td>65.866667</td>
    </tr>
    <tr>
      <th>14</th>
      <td>United States</td>
      <td>65.833333</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Ecuador</td>
      <td>65.136364</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Canada</td>
      <td>63.200000</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Australia</td>
      <td>62.222222</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Saudi Arabia</td>
      <td>61.238095</td>
    </tr>
  </tbody>
</table>
</div>




```python
fig, ax = plt.subplots(figsize=(12, 5), tight_layout=True)

sns.barplot(data=df_average_overall[:10], x='Teams', y='AVG_Overall',
            palette=sns.color_palette('pastel'))

plt.show()
```


    
![png](output_15_0.png)
    


## Best Formation for each team


```python
def best_lineup(nationality, lineup):
    lineup_count = [lineup.count(i) for i in lineup]

    df_lineup = pd.DataFrame({'position': lineup, 'count': lineup_count})
    positions_non_repeated = df_lineup[df_lineup['count'] <= 1]['position'].values
    positions_repeated = df_lineup[df_lineup['count'] > 1]['position'].values

    df_squad = best_squad(nationality)

    df_lineup = pd.concat([
        df_squad[df_squad['player_positions'].isin(positions_non_repeated)].drop_duplicates('player_positions', keep='first'),
        df_squad[df_squad['player_positions'].isin(positions_repeated)]]
    )
    return df_lineup[['short_name', 'overall', 'club_name', 'player_positions']]
```


```python
dict_formation = {
    '4-3-3': ['GK', 'RB', 'CB', 'CB', 'LB', 'CDM', 'CM', 'CAM', 'RW', 'ST', 'LW'],
    '4-4-2': ['GK', 'RB', 'CB', 'CB', 'LB', 'RM', 'CM', 'CM', 'LM', 'ST', 'ST'],
    '4-2-3-1': ['GK', 'RB', 'CB', 'CB', 'LB', 'CDM', 'CDM', 'CAM', 'CAM', 'CAM', 'ST'],
}
```


```python
for index, row in df_average_overall[:9].iterrows():
    max_average = None
    for key, values in dict_formation.items():
        average = best_lineup(row['Teams'], values)['overall'].mean()
        if max_average is None or average>max_average:
            max_average = average
            formation = key
    print(row['Teams'], formation, max_average)
```

    Brazil 4-4-2 79.27272727272727
    Spain 4-4-2 78.81818181818181
    Portugal 4-4-2 75.63636363636364
    Uruguay 4-4-2 75.9090909090909
    France 4-4-2 78.0909090909091
    Serbia 4-4-2 73.77777777777777
    Switzerland 4-3-3 74.55555555555556
    Poland 4-4-2 74.0
    Croatia 4-4-2 74.875
    


```python
# best_lineup('Spain', dict_formation['4-2-3-1'])
# best_lineup('Argentina', dict_formation['4-3-3'])
best_lineup('Brazil', dict_formation['4-3-3'])
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
      <th>short_name</th>
      <th>overall</th>
      <th>club_name</th>
      <th>player_positions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>815</th>
      <td>Fredditinho</td>
      <td>78.0</td>
      <td>Palmeiras</td>
      <td>ST</td>
    </tr>
    <tr>
      <th>2888</th>
      <td>Claudiosa Paes</td>
      <td>73.0</td>
      <td>São Paulo</td>
      <td>RW</td>
    </tr>
    <tr>
      <th>626</th>
      <td>Adnan Vidual</td>
      <td>79.0</td>
      <td>Internacional</td>
      <td>RB</td>
    </tr>
    <tr>
      <th>817</th>
      <td>Prazeracinho</td>
      <td>78.0</td>
      <td>Flamengo</td>
      <td>LW</td>
    </tr>
    <tr>
      <th>386</th>
      <td>Renan Lodi</td>
      <td>81.0</td>
      <td>Atlético de Madrid</td>
      <td>LB</td>
    </tr>
    <tr>
      <th>222</th>
      <td>Neto</td>
      <td>82.0</td>
      <td>FC Barcelona</td>
      <td>GK</td>
    </tr>
    <tr>
      <th>483</th>
      <td>Gerson</td>
      <td>80.0</td>
      <td>Olympique de Marseille</td>
      <td>CM</td>
    </tr>
    <tr>
      <th>294</th>
      <td>Lucas Leiva</td>
      <td>81.0</td>
      <td>Lazio</td>
      <td>CDM</td>
    </tr>
    <tr>
      <th>2890</th>
      <td>Marlon Nideiro</td>
      <td>73.0</td>
      <td>Grêmio</td>
      <td>CAM</td>
    </tr>
    <tr>
      <th>120</th>
      <td>Felipe</td>
      <td>84.0</td>
      <td>Atlético de Madrid</td>
      <td>CB</td>
    </tr>
    <tr>
      <th>279</th>
      <td>Éder Militão</td>
      <td>82.0</td>
      <td>Real Madrid CF</td>
      <td>CB</td>
    </tr>
  </tbody>
</table>
</div>



**By:_** **DataSpieler12345**


```python

```
