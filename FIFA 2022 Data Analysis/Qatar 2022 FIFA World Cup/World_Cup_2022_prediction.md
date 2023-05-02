```python
import pandas as pd
import pickle
from scipy.stats import poisson
```


```python
dict_table = pickle.load(open('dict_tables','rb'))
df_historical_data = pd.read_csv('clean_fifa_worldcup_matches.csv')
df_fixture = pd.read_csv('clean_fifa_worldcup_fixture.csv')
```

## Calculate Team Strength


```python
df_home = df_historical_data[['HomeTeam', 'HomeGoals', 'AwayGoals']]
df_away = df_historical_data[['AwayTeam', 'HomeGoals', 'AwayGoals']]

df_home = df_home.rename(columns={'HomeTeam':'Team', 'HomeGoals': 'GoalsScored', 'AwayGoals': 'GoalsConceded'})
df_away = df_away.rename(columns={'AwayTeam':'Team', 'HomeGoals': 'GoalsConceded', 'AwayGoals': 'GoalsScored'})

df_team_strength = pd.concat([df_home, df_away], ignore_index=True).groupby(['Team']).mean()
df_team_strength
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
      <th>GoalsScored</th>
      <th>GoalsConceded</th>
    </tr>
    <tr>
      <th>Team</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Algeria</th>
      <td>1.000000</td>
      <td>1.461538</td>
    </tr>
    <tr>
      <th>Angola</th>
      <td>0.333333</td>
      <td>0.666667</td>
    </tr>
    <tr>
      <th>Argentina</th>
      <td>1.691358</td>
      <td>1.148148</td>
    </tr>
    <tr>
      <th>Australia</th>
      <td>0.812500</td>
      <td>1.937500</td>
    </tr>
    <tr>
      <th>Austria</th>
      <td>1.482759</td>
      <td>1.620690</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Uruguay</th>
      <td>1.553571</td>
      <td>1.321429</td>
    </tr>
    <tr>
      <th>Wales</th>
      <td>0.800000</td>
      <td>0.800000</td>
    </tr>
    <tr>
      <th>West Germany</th>
      <td>2.112903</td>
      <td>1.241935</td>
    </tr>
    <tr>
      <th>Yugoslavia</th>
      <td>1.666667</td>
      <td>1.272727</td>
    </tr>
    <tr>
      <th>Zaire</th>
      <td>0.000000</td>
      <td>4.666667</td>
    </tr>
  </tbody>
</table>
<p>85 rows × 2 columns</p>
</div>



## Function predict_points


```python
def predict_points(home, away):
    if home in df_team_strength.index and away in df_team_strength.index:
        # goals_scored * goals_conceded
        lamb_home = df_team_strength.at[home,'GoalsScored'] * df_team_strength.at[away,'GoalsConceded']
        lamb_away = df_team_strength.at[away,'GoalsScored'] * df_team_strength.at[home,'GoalsConceded']
        prob_home, prob_away, prob_draw = 0, 0, 0
        for x in range(0,11): #number of goals home team
            for y in range(0, 11): #number of goals away team
                p = poisson.pmf(x, lamb_home) * poisson.pmf(y, lamb_away)
                if x == y:
                    prob_draw += p
                elif x > y:
                    prob_home += p
                else:
                    prob_away += p
        
        points_home = 3 * prob_home + prob_draw
        points_away = 3 * prob_away + prob_draw
        return (points_home, points_away)
    else:
        return (0, 0)
```

## Testing function


```python
print(predict_points('England', 'United States'))
print(predict_points('Argentina', 'Mexico'))
print(predict_points('Qatar (H)', 'Ecuador')) # Qatar vs Team X -> 0 points to both
```

    (2.2356147635326007, 0.5922397535606193)
    (2.3129151525530505, 0.5378377125059863)
    (0, 0)
    

## Predicting World Cup

### Group stage


```python
df_fixture_group_48 = df_fixture[:48].copy()
df_fixture_knockout = df_fixture[48:56].copy()
df_fixture_quarter = df_fixture[56:60].copy()
df_fixture_semi = df_fixture[60:62].copy()
df_fixture_final = df_fixture[62:].copy()
```


```python
for group in dict_table:
    teams_in_group = dict_table[group]['Team'].values
    df_fixture_group_6 = df_fixture_group_48[df_fixture_group_48['home'].isin(teams_in_group)]
    for index, row in df_fixture_group_6.iterrows():
        home, away = row['home'], row['away']
        points_home, points_away = predict_points(home, away)
        dict_table[group].loc[dict_table[group]['Team'] == home, 'Pts'] += points_home
        dict_table[group].loc[dict_table[group]['Team'] == away, 'Pts'] += points_away

    dict_table[group] = dict_table[group].sort_values('Pts', ascending=False).reset_index()
    dict_table[group] = dict_table[group][['Team', 'Pts']]
    dict_table[group] = dict_table[group].round(0)
```


```python
dict_table['Group A']
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
      <th>Team</th>
      <th>Pts</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Netherlands</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Senegal</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Ecuador</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Qatar (H)</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



## Knock out


```python
df_fixture_knockout
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
      <th>48</th>
      <td>Winners Group A</td>
      <td>Match 49</td>
      <td>Runners-up Group B</td>
      <td>2022</td>
    </tr>
    <tr>
      <th>49</th>
      <td>Winners Group C</td>
      <td>Match 50</td>
      <td>Runners-up Group D</td>
      <td>2022</td>
    </tr>
    <tr>
      <th>50</th>
      <td>Winners Group D</td>
      <td>Match 52</td>
      <td>Runners-up Group C</td>
      <td>2022</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Winners Group B</td>
      <td>Match 51</td>
      <td>Runners-up Group A</td>
      <td>2022</td>
    </tr>
    <tr>
      <th>52</th>
      <td>Winners Group E</td>
      <td>Match 53</td>
      <td>Runners-up Group F</td>
      <td>2022</td>
    </tr>
    <tr>
      <th>53</th>
      <td>Winners Group G</td>
      <td>Match 54</td>
      <td>Runners-up Group H</td>
      <td>2022</td>
    </tr>
    <tr>
      <th>54</th>
      <td>Winners Group F</td>
      <td>Match 55</td>
      <td>Runners-up Group E</td>
      <td>2022</td>
    </tr>
    <tr>
      <th>55</th>
      <td>Winners Group H</td>
      <td>Match 56</td>
      <td>Runners-up Group G</td>
      <td>2022</td>
    </tr>
  </tbody>
</table>
</div>




```python
for group in dict_table:
    group_winner = dict_table[group].loc[0, 'Team']
    runners_up = dict_table[group].loc[1, 'Team']
    df_fixture_knockout.replace({f'Winners {group}':group_winner,
                                 f'Runners-up {group}':runners_up}, inplace=True)

df_fixture_knockout['winner'] = '?'
df_fixture_knockout
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
      <th>winner</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>48</th>
      <td>Netherlands</td>
      <td>Match 49</td>
      <td>Wales</td>
      <td>2022</td>
      <td>?</td>
    </tr>
    <tr>
      <th>49</th>
      <td>Argentina</td>
      <td>Match 50</td>
      <td>Denmark</td>
      <td>2022</td>
      <td>?</td>
    </tr>
    <tr>
      <th>50</th>
      <td>France</td>
      <td>Match 52</td>
      <td>Poland</td>
      <td>2022</td>
      <td>?</td>
    </tr>
    <tr>
      <th>51</th>
      <td>England</td>
      <td>Match 51</td>
      <td>Senegal</td>
      <td>2022</td>
      <td>?</td>
    </tr>
    <tr>
      <th>52</th>
      <td>Germany</td>
      <td>Match 53</td>
      <td>Belgium</td>
      <td>2022</td>
      <td>?</td>
    </tr>
    <tr>
      <th>53</th>
      <td>Brazil</td>
      <td>Match 54</td>
      <td>Uruguay</td>
      <td>2022</td>
      <td>?</td>
    </tr>
    <tr>
      <th>54</th>
      <td>Croatia</td>
      <td>Match 55</td>
      <td>Spain</td>
      <td>2022</td>
      <td>?</td>
    </tr>
    <tr>
      <th>55</th>
      <td>Portugal</td>
      <td>Match 56</td>
      <td>Switzerland</td>
      <td>2022</td>
      <td>?</td>
    </tr>
  </tbody>
</table>
</div>




```python
def get_winner(df_fixture_updated):
    for index, row in df_fixture_updated.iterrows():
        home, away = row['home'], row['away']
        points_home, points_away = predict_points(home, away)
        if points_home > points_away:
            winner = home
        else:
            winner = away
        df_fixture_updated.loc[index, 'winner'] = winner
    return df_fixture_updated
```


```python
get_winner(df_fixture_knockout)
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
      <th>winner</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>48</th>
      <td>Netherlands</td>
      <td>Match 49</td>
      <td>Wales</td>
      <td>2022</td>
      <td>Netherlands</td>
    </tr>
    <tr>
      <th>49</th>
      <td>Argentina</td>
      <td>Match 50</td>
      <td>Denmark</td>
      <td>2022</td>
      <td>Argentina</td>
    </tr>
    <tr>
      <th>50</th>
      <td>France</td>
      <td>Match 52</td>
      <td>Poland</td>
      <td>2022</td>
      <td>France</td>
    </tr>
    <tr>
      <th>51</th>
      <td>England</td>
      <td>Match 51</td>
      <td>Senegal</td>
      <td>2022</td>
      <td>England</td>
    </tr>
    <tr>
      <th>52</th>
      <td>Germany</td>
      <td>Match 53</td>
      <td>Belgium</td>
      <td>2022</td>
      <td>Germany</td>
    </tr>
    <tr>
      <th>53</th>
      <td>Brazil</td>
      <td>Match 54</td>
      <td>Uruguay</td>
      <td>2022</td>
      <td>Brazil</td>
    </tr>
    <tr>
      <th>54</th>
      <td>Croatia</td>
      <td>Match 55</td>
      <td>Spain</td>
      <td>2022</td>
      <td>Spain</td>
    </tr>
    <tr>
      <th>55</th>
      <td>Portugal</td>
      <td>Match 56</td>
      <td>Switzerland</td>
      <td>2022</td>
      <td>Portugal</td>
    </tr>
  </tbody>
</table>
</div>



## Quarter Final


```python
def update_table(df_fixture_round_1, df_fixture_round_2):
    for index, row in df_fixture_round_1.iterrows():
        winner = df_fixture_round_1.loc[index, 'winner']
        match = df_fixture_round_1.loc[index, 'score']
        df_fixture_round_2.replace({f'Winners {match}':winner}, inplace=True)
    df_fixture_round_2['winner'] = '?'
    return df_fixture_round_2
```


```python
update_table(df_fixture_knockout, df_fixture_quarter)
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
      <th>winner</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>56</th>
      <td>Germany</td>
      <td>Match 58</td>
      <td>Brazil</td>
      <td>2022</td>
      <td>?</td>
    </tr>
    <tr>
      <th>57</th>
      <td>Netherlands</td>
      <td>Match 57</td>
      <td>Argentina</td>
      <td>2022</td>
      <td>?</td>
    </tr>
    <tr>
      <th>58</th>
      <td>Spain</td>
      <td>Match 60</td>
      <td>Portugal</td>
      <td>2022</td>
      <td>?</td>
    </tr>
    <tr>
      <th>59</th>
      <td>England</td>
      <td>Match 59</td>
      <td>France</td>
      <td>2022</td>
      <td>?</td>
    </tr>
  </tbody>
</table>
</div>




```python
get_winner(df_fixture_quarter)
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
      <th>winner</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>56</th>
      <td>Germany</td>
      <td>Match 58</td>
      <td>Brazil</td>
      <td>2022</td>
      <td>Brazil</td>
    </tr>
    <tr>
      <th>57</th>
      <td>Netherlands</td>
      <td>Match 57</td>
      <td>Argentina</td>
      <td>2022</td>
      <td>Netherlands</td>
    </tr>
    <tr>
      <th>58</th>
      <td>Spain</td>
      <td>Match 60</td>
      <td>Portugal</td>
      <td>2022</td>
      <td>Portugal</td>
    </tr>
    <tr>
      <th>59</th>
      <td>England</td>
      <td>Match 59</td>
      <td>France</td>
      <td>2022</td>
      <td>France</td>
    </tr>
  </tbody>
</table>
</div>



## Semifinal 


```python
update_table(df_fixture_quarter, df_fixture_semi)
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
      <th>winner</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>60</th>
      <td>Netherlands</td>
      <td>Match 61</td>
      <td>Brazil</td>
      <td>2022</td>
      <td>?</td>
    </tr>
    <tr>
      <th>61</th>
      <td>France</td>
      <td>Match 62</td>
      <td>Portugal</td>
      <td>2022</td>
      <td>?</td>
    </tr>
  </tbody>
</table>
</div>




```python
get_winner(df_fixture_semi)
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
      <th>winner</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>60</th>
      <td>Netherlands</td>
      <td>Match 61</td>
      <td>Brazil</td>
      <td>2022</td>
      <td>Brazil</td>
    </tr>
    <tr>
      <th>61</th>
      <td>France</td>
      <td>Match 62</td>
      <td>Portugal</td>
      <td>2022</td>
      <td>France</td>
    </tr>
  </tbody>
</table>
</div>



# Final


```python
update_table(df_fixture_semi, df_fixture_final)
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
      <th>winner</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>62</th>
      <td>Losers Match 61</td>
      <td>Match 63</td>
      <td>Losers Match 62</td>
      <td>2022</td>
      <td>?</td>
    </tr>
    <tr>
      <th>63</th>
      <td>Brazil</td>
      <td>Match 64</td>
      <td>France</td>
      <td>2022</td>
      <td>?</td>
    </tr>
  </tbody>
</table>
</div>




```python
get_winner(df_fixture_final)
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
      <th>winner</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>62</th>
      <td>Losers Match 61</td>
      <td>Match 63</td>
      <td>Losers Match 62</td>
      <td>2022</td>
      <td>Losers Match 62</td>
    </tr>
    <tr>
      <th>63</th>
      <td>Brazil</td>
      <td>Match 64</td>
      <td>France</td>
      <td>2022</td>
      <td>Brazil</td>
    </tr>
  </tbody>
</table>
</div>



**By:_** **DataSpieler12345**
