```python
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
pd.set_option('display.max_columns', None)

data = pd.read_excel('nba_player_data_cleaned.xlsx')
```


```python
data.sample(20)
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
    <tr>
      <th>2760</th>
      <td>2016-17</td>
      <td>Regular%20Season</td>
      <td>201939</td>
      <td>8</td>
      <td>Stephen Curry</td>
      <td>1610612744</td>
      <td>GSW</td>
      <td>79</td>
      <td>2639</td>
      <td>675</td>
      <td>1443</td>
      <td>0.468</td>
      <td>324</td>
      <td>789</td>
      <td>0.411</td>
      <td>325</td>
      <td>362</td>
      <td>0.898</td>
      <td>61</td>
      <td>292</td>
      <td>353</td>
      <td>524</td>
      <td>142</td>
      <td>17</td>
      <td>239</td>
      <td>183</td>
      <td>1999</td>
      <td>1991</td>
      <td>2.19</td>
      <td>0.59</td>
    </tr>
    <tr>
      <th>2380</th>
      <td>2015-16</td>
      <td>Regular%20Season</td>
      <td>203200</td>
      <td>319</td>
      <td>Justin Holiday</td>
      <td>1610612741</td>
      <td>CHI</td>
      <td>53</td>
      <td>773</td>
      <td>88</td>
      <td>228</td>
      <td>0.386</td>
      <td>36</td>
      <td>105</td>
      <td>0.343</td>
      <td>27</td>
      <td>37</td>
      <td>0.730</td>
      <td>12</td>
      <td>78</td>
      <td>90</td>
      <td>56</td>
      <td>32</td>
      <td>19</td>
      <td>39</td>
      <td>61</td>
      <td>239</td>
      <td>247</td>
      <td>1.44</td>
      <td>0.82</td>
    </tr>
    <tr>
      <th>7060</th>
      <td>2021-22</td>
      <td>Regular%20Season</td>
      <td>1630624</td>
      <td>582</td>
      <td>Feron Hunt</td>
      <td>1610612752</td>
      <td>NYK</td>
      <td>2</td>
      <td>8</td>
      <td>0</td>
      <td>2</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1.00</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>5630</th>
      <td>2019-20</td>
      <td>Playoffs</td>
      <td>1626169</td>
      <td>153</td>
      <td>Stanley Johnson</td>
      <td>1610612761</td>
      <td>TOR</td>
      <td>3</td>
      <td>20</td>
      <td>5</td>
      <td>11</td>
      <td>0.455</td>
      <td>2</td>
      <td>5</td>
      <td>0.400</td>
      <td>1</td>
      <td>1</td>
      <td>1.000</td>
      <td>1</td>
      <td>3</td>
      <td>4</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>13</td>
      <td>16</td>
      <td>6.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>1487</th>
      <td>2014-15</td>
      <td>Regular%20Season</td>
      <td>2561</td>
      <td>126</td>
      <td>David West</td>
      <td>1610612754</td>
      <td>IND</td>
      <td>66</td>
      <td>1895</td>
      <td>323</td>
      <td>686</td>
      <td>0.471</td>
      <td>4</td>
      <td>20</td>
      <td>0.200</td>
      <td>119</td>
      <td>161</td>
      <td>0.739</td>
      <td>108</td>
      <td>341</td>
      <td>449</td>
      <td>223</td>
      <td>48</td>
      <td>48</td>
      <td>120</td>
      <td>160</td>
      <td>769</td>
      <td>1012</td>
      <td>1.86</td>
      <td>0.40</td>
    </tr>
    <tr>
      <th>2388</th>
      <td>2015-16</td>
      <td>Regular%20Season</td>
      <td>2419</td>
      <td>327</td>
      <td>Tayshaun Prince</td>
      <td>1610612750</td>
      <td>MIN</td>
      <td>77</td>
      <td>1462</td>
      <td>102</td>
      <td>229</td>
      <td>0.445</td>
      <td>4</td>
      <td>23</td>
      <td>0.174</td>
      <td>13</td>
      <td>19</td>
      <td>0.684</td>
      <td>32</td>
      <td>115</td>
      <td>147</td>
      <td>74</td>
      <td>36</td>
      <td>13</td>
      <td>27</td>
      <td>62</td>
      <td>221</td>
      <td>331</td>
      <td>2.74</td>
      <td>1.33</td>
    </tr>
    <tr>
      <th>1114</th>
      <td>2013-14</td>
      <td>Regular%20Season</td>
      <td>203139</td>
      <td>437</td>
      <td>Viacheslav Kravtsov</td>
      <td>1610612756</td>
      <td>PHX</td>
      <td>20</td>
      <td>59</td>
      <td>8</td>
      <td>15</td>
      <td>0.533</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>4</td>
      <td>8</td>
      <td>0.500</td>
      <td>9</td>
      <td>8</td>
      <td>17</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>6</td>
      <td>7</td>
      <td>20</td>
      <td>22</td>
      <td>0.17</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2414</th>
      <td>2015-16</td>
      <td>Regular%20Season</td>
      <td>1626199</td>
      <td>353</td>
      <td>Darrun Hilliard</td>
      <td>1610612765</td>
      <td>DET</td>
      <td>38</td>
      <td>383</td>
      <td>52</td>
      <td>131</td>
      <td>0.397</td>
      <td>19</td>
      <td>50</td>
      <td>0.380</td>
      <td>29</td>
      <td>40</td>
      <td>0.725</td>
      <td>5</td>
      <td>40</td>
      <td>45</td>
      <td>27</td>
      <td>9</td>
      <td>1</td>
      <td>19</td>
      <td>28</td>
      <td>152</td>
      <td>125</td>
      <td>1.42</td>
      <td>0.47</td>
    </tr>
    <tr>
      <th>382</th>
      <td>2012-13</td>
      <td>Regular%20Season</td>
      <td>1894</td>
      <td>383</td>
      <td>Corey Maggette</td>
      <td>1610612765</td>
      <td>DET</td>
      <td>18</td>
      <td>257</td>
      <td>27</td>
      <td>76</td>
      <td>0.355</td>
      <td>5</td>
      <td>21</td>
      <td>0.238</td>
      <td>36</td>
      <td>48</td>
      <td>0.750</td>
      <td>5</td>
      <td>20</td>
      <td>25</td>
      <td>19</td>
      <td>6</td>
      <td>2</td>
      <td>17</td>
      <td>42</td>
      <td>95</td>
      <td>69</td>
      <td>1.12</td>
      <td>0.35</td>
    </tr>
    <tr>
      <th>3415</th>
      <td>2016-17</td>
      <td>Playoffs</td>
      <td>1627738</td>
      <td>176</td>
      <td>Deyonta Davis</td>
      <td>1610612763</td>
      <td>MEM</td>
      <td>3</td>
      <td>11</td>
      <td>3</td>
      <td>5</td>
      <td>0.600</td>
      <td>0</td>
      <td>0</td>
      <td>0.000</td>
      <td>1</td>
      <td>2</td>
      <td>0.500</td>
      <td>2</td>
      <td>3</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>7</td>
      <td>9</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2226</th>
      <td>2015-16</td>
      <td>Regular%20Season</td>
      <td>203487</td>
      <td>165</td>
      <td>Michael Carter-Williams</td>
      <td>1610612749</td>
      <td>MIL</td>
      <td>54</td>
      <td>1649</td>
      <td>251</td>
      <td>555</td>
      <td>0.452</td>
      <td>15</td>
      <td>55</td>
      <td>0.273</td>
      <td>106</td>
      <td>162</td>
      <td>0.654</td>
      <td>48</td>
      <td>228</td>
      <td>276</td>
      <td>281</td>
      <td>80</td>
      <td>41</td>
      <td>153</td>
      <td>162</td>
      <td>623</td>
      <td>788</td>
      <td>1.84</td>
      <td>0.52</td>
    </tr>
    <tr>
      <th>4076</th>
      <td>2017-18</td>
      <td>Playoffs</td>
      <td>2546</td>
      <td>83</td>
      <td>Carmelo Anthony</td>
      <td>1610612760</td>
      <td>OKC</td>
      <td>6</td>
      <td>194</td>
      <td>27</td>
      <td>72</td>
      <td>0.375</td>
      <td>6</td>
      <td>28</td>
      <td>0.214</td>
      <td>11</td>
      <td>15</td>
      <td>0.733</td>
      <td>3</td>
      <td>31</td>
      <td>34</td>
      <td>2</td>
      <td>10</td>
      <td>4</td>
      <td>6</td>
      <td>14</td>
      <td>71</td>
      <td>66</td>
      <td>0.33</td>
      <td>1.67</td>
    </tr>
    <tr>
      <th>891</th>
      <td>2013-14</td>
      <td>Regular%20Season</td>
      <td>2199</td>
      <td>215</td>
      <td>Tyson Chandler</td>
      <td>1610612752</td>
      <td>NYK</td>
      <td>55</td>
      <td>1662</td>
      <td>191</td>
      <td>322</td>
      <td>0.593</td>
      <td>0</td>
      <td>1</td>
      <td>0.000</td>
      <td>98</td>
      <td>155</td>
      <td>0.632</td>
      <td>159</td>
      <td>370</td>
      <td>529</td>
      <td>59</td>
      <td>36</td>
      <td>63</td>
      <td>71</td>
      <td>145</td>
      <td>480</td>
      <td>908</td>
      <td>0.83</td>
      <td>0.51</td>
    </tr>
    <tr>
      <th>2778</th>
      <td>2016-17</td>
      <td>Regular%20Season</td>
      <td>201572</td>
      <td>26</td>
      <td>Brook Lopez</td>
      <td>1610612751</td>
      <td>BKN</td>
      <td>75</td>
      <td>2222</td>
      <td>555</td>
      <td>1172</td>
      <td>0.474</td>
      <td>134</td>
      <td>387</td>
      <td>0.346</td>
      <td>295</td>
      <td>364</td>
      <td>0.810</td>
      <td>121</td>
      <td>282</td>
      <td>403</td>
      <td>176</td>
      <td>38</td>
      <td>124</td>
      <td>184</td>
      <td>192</td>
      <td>1539</td>
      <td>1410</td>
      <td>0.96</td>
      <td>0.21</td>
    </tr>
    <tr>
      <th>6692</th>
      <td>2021-22</td>
      <td>Regular%20Season</td>
      <td>1629020</td>
      <td>222</td>
      <td>Jarred Vanderbilt</td>
      <td>1610612750</td>
      <td>MIN</td>
      <td>74</td>
      <td>1881</td>
      <td>212</td>
      <td>361</td>
      <td>0.587</td>
      <td>2</td>
      <td>14</td>
      <td>0.143</td>
      <td>86</td>
      <td>131</td>
      <td>0.656</td>
      <td>215</td>
      <td>409</td>
      <td>624</td>
      <td>94</td>
      <td>99</td>
      <td>46</td>
      <td>73</td>
      <td>181</td>
      <td>512</td>
      <td>1108</td>
      <td>1.29</td>
      <td>1.36</td>
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
      <th>746</th>
      <td>2013-14</td>
      <td>Regular%20Season</td>
      <td>200751</td>
      <td>69</td>
      <td>Randy Foye</td>
      <td>1610612743</td>
      <td>DEN</td>
      <td>81</td>
      <td>2485</td>
      <td>361</td>
      <td>875</td>
      <td>0.413</td>
      <td>189</td>
      <td>498</td>
      <td>0.380</td>
      <td>157</td>
      <td>185</td>
      <td>0.849</td>
      <td>36</td>
      <td>196</td>
      <td>232</td>
      <td>287</td>
      <td>67</td>
      <td>39</td>
      <td>145</td>
      <td>205</td>
      <td>1068</td>
      <td>1006</td>
      <td>1.98</td>
      <td>0.46</td>
    </tr>
    <tr>
      <th>2082</th>
      <td>2015-16</td>
      <td>Regular%20Season</td>
      <td>201572</td>
      <td>21</td>
      <td>Brook Lopez</td>
      <td>1610612751</td>
      <td>BKN</td>
      <td>73</td>
      <td>2457</td>
      <td>591</td>
      <td>1157</td>
      <td>0.511</td>
      <td>2</td>
      <td>14</td>
      <td>0.143</td>
      <td>317</td>
      <td>403</td>
      <td>0.787</td>
      <td>204</td>
      <td>369</td>
      <td>573</td>
      <td>146</td>
      <td>58</td>
      <td>124</td>
      <td>175</td>
      <td>215</td>
      <td>1501</td>
      <td>1575</td>
      <td>0.83</td>
      <td>0.33</td>
    </tr>
    <tr>
      <th>6009</th>
      <td>2020-21</td>
      <td>Regular%20Season</td>
      <td>203476</td>
      <td>318</td>
      <td>Gorgui Dieng</td>
      <td>1610612759</td>
      <td>SAS</td>
      <td>38</td>
      <td>553</td>
      <td>85</td>
      <td>163</td>
      <td>0.521</td>
      <td>30</td>
      <td>70</td>
      <td>0.429</td>
      <td>58</td>
      <td>67</td>
      <td>0.866</td>
      <td>40</td>
      <td>100</td>
      <td>140</td>
      <td>48</td>
      <td>26</td>
      <td>16</td>
      <td>32</td>
      <td>56</td>
      <td>258</td>
      <td>369</td>
      <td>1.50</td>
      <td>0.81</td>
    </tr>
    <tr>
      <th>2552</th>
      <td>2015-16</td>
      <td>Playoffs</td>
      <td>203468</td>
      <td>15</td>
      <td>CJ McCollum</td>
      <td>1610612757</td>
      <td>POR</td>
      <td>11</td>
      <td>442</td>
      <td>84</td>
      <td>197</td>
      <td>0.426</td>
      <td>20</td>
      <td>58</td>
      <td>0.345</td>
      <td>37</td>
      <td>46</td>
      <td>0.804</td>
      <td>7</td>
      <td>33</td>
      <td>40</td>
      <td>36</td>
      <td>10</td>
      <td>5</td>
      <td>20</td>
      <td>30</td>
      <td>225</td>
      <td>174</td>
      <td>1.80</td>
      <td>0.50</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.shape
```




    (7293, 30)



# Data cleaning & analysis preparation


```python
data.isna().sum() # there is no null values in the dataset 
```




    Year           0
    Season_Type    0
    PLAYER_ID      0
    RANK           0
    PLAYER         0
    TEAM_ID        0
    TEAM           0
    GP             0
    MIN            0
    FGM            0
    FGA            0
    FG_PCT         0
    FG3M           0
    FG3A           0
    FG3_PCT        0
    FTM            0
    FTA            0
    FT_PCT         0
    OREB           0
    DREB           0
    REB            0
    AST            0
    STL            0
    BLK            0
    TOV            0
    PF             0
    PTS            0
    EFF            0
    AST_TOV        0
    STL_TOV        0
    dtype: int64




```python
# Drop the unusel columns = RANK, EFF
```


```python
data.drop(columns=['RANK','EFF'], inplace=True)
```


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
      <th>Year</th>
      <th>Season_Type</th>
      <th>PLAYER_ID</th>
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
      <td>1.34</td>
      <td>0.41</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2012-13</td>
      <td>Regular%20Season</td>
      <td>977</td>
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
      <td>1.63</td>
      <td>0.37</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2012-13</td>
      <td>Regular%20Season</td>
      <td>2544</td>
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
      <td>2.44</td>
      <td>0.57</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2012-13</td>
      <td>Regular%20Season</td>
      <td>201935</td>
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
      <td>1.54</td>
      <td>0.48</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2012-13</td>
      <td>Regular%20Season</td>
      <td>2546</td>
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
      <th>7288</th>
      <td>2021-22</td>
      <td>Playoffs</td>
      <td>1629006</td>
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
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>7289</th>
      <td>2021-22</td>
      <td>Playoffs</td>
      <td>1630556</td>
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
      <td>1.00</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>7290</th>
      <td>2021-22</td>
      <td>Playoffs</td>
      <td>1630201</td>
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
      <td>3.00</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>7291</th>
      <td>2021-22</td>
      <td>Playoffs</td>
      <td>202693</td>
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
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>7292</th>
      <td>2021-22</td>
      <td>Playoffs</td>
      <td>200794</td>
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
      <td>0.00</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>
<p>7293 rows × 28 columns</p>
</div>




```python
# Year Column 4 digits astype int, to identify the year
data['season_start_year'] = data['Year'].str[:4].astype(int)
```


```python
# teams , figure out: NOH | NOP
data.TEAM.unique()
```




    array(['OKC', 'LAL', 'MIA', 'HOU', 'NYK', 'GSW', 'MIL', 'POR', 'TOR',
           'BKN', 'CHA', 'LAC', 'BOS', 'UTA', 'PHI', 'IND', 'SAS', 'ATL',
           'CLE', 'NOH', 'DET', 'CHI', 'SAC', 'DAL', 'DEN', 'MEM', 'PHX',
           'ORL', 'MIN', 'WAS', 'NOP'], dtype=object)




```python
# teams = 30 and not 31
data.TEAM.nunique()
```




    31




```python
data['TEAM'].replace(to_replace=['NOP','NOH'], value='NO', inplace=True)
```


```python
# check again | NO
data.TEAM.unique()
```




    array(['OKC', 'LAL', 'MIA', 'HOU', 'NYK', 'GSW', 'MIL', 'POR', 'TOR',
           'BKN', 'CHA', 'LAC', 'BOS', 'UTA', 'PHI', 'IND', 'SAS', 'ATL',
           'CLE', 'NO', 'DET', 'CHI', 'SAC', 'DAL', 'DEN', 'MEM', 'PHX',
           'ORL', 'MIN', 'WAS'], dtype=object)




```python
# clean the Season_type column

data['Season_Type'].replace('Regular%20Season','RS', inplace=True)
```


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
      <th>Year</th>
      <th>Season_Type</th>
      <th>PLAYER_ID</th>
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
      <th>AST_TOV</th>
      <th>STL_TOV</th>
      <th>season_start_year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2012-13</td>
      <td>RS</td>
      <td>201142</td>
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
      <td>1.34</td>
      <td>0.41</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2012-13</td>
      <td>RS</td>
      <td>977</td>
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
      <td>1.63</td>
      <td>0.37</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2012-13</td>
      <td>RS</td>
      <td>2544</td>
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
      <td>2.44</td>
      <td>0.57</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2012-13</td>
      <td>RS</td>
      <td>201935</td>
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
      <td>1.54</td>
      <td>0.48</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2012-13</td>
      <td>RS</td>
      <td>2546</td>
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
      <td>0.98</td>
      <td>0.30</td>
      <td>2012</td>
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
    </tr>
    <tr>
      <th>7288</th>
      <td>2021-22</td>
      <td>Playoffs</td>
      <td>1629006</td>
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
      <td>0.00</td>
      <td>0.00</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>7289</th>
      <td>2021-22</td>
      <td>Playoffs</td>
      <td>1630556</td>
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
      <td>1.00</td>
      <td>1.00</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>7290</th>
      <td>2021-22</td>
      <td>Playoffs</td>
      <td>1630201</td>
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
      <td>3.00</td>
      <td>1.00</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>7291</th>
      <td>2021-22</td>
      <td>Playoffs</td>
      <td>202693</td>
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
      <td>0.00</td>
      <td>0.00</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>7292</th>
      <td>2021-22</td>
      <td>Playoffs</td>
      <td>200794</td>
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
      <td>0.00</td>
      <td>0.00</td>
      <td>2021</td>
    </tr>
  </tbody>
</table>
<p>7293 rows × 29 columns</p>
</div>




```python
# filter dataset with RS first
rs_df = data[data['Season_Type']=='RS']
rs_df
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
      <th>AST_TOV</th>
      <th>STL_TOV</th>
      <th>season_start_year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2012-13</td>
      <td>RS</td>
      <td>201142</td>
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
      <td>1.34</td>
      <td>0.41</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2012-13</td>
      <td>RS</td>
      <td>977</td>
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
      <td>1.63</td>
      <td>0.37</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2012-13</td>
      <td>RS</td>
      <td>2544</td>
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
      <td>2.44</td>
      <td>0.57</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2012-13</td>
      <td>RS</td>
      <td>201935</td>
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
      <td>1.54</td>
      <td>0.48</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2012-13</td>
      <td>RS</td>
      <td>2546</td>
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
      <td>0.98</td>
      <td>0.30</td>
      <td>2012</td>
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
    </tr>
    <tr>
      <th>7071</th>
      <td>2021-22</td>
      <td>RS</td>
      <td>1630207</td>
      <td>Nate Hinton</td>
      <td>1610612754</td>
      <td>IND</td>
      <td>2</td>
      <td>2</td>
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
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>7072</th>
      <td>2021-22</td>
      <td>RS</td>
      <td>1626155</td>
      <td>Sam Dekker</td>
      <td>1610612761</td>
      <td>TOR</td>
      <td>1</td>
      <td>1</td>
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
      <td>0.00</td>
      <td>0.00</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>7073</th>
      <td>2021-22</td>
      <td>RS</td>
      <td>1629309</td>
      <td>Trayvon Palmer</td>
      <td>1610612765</td>
      <td>DET</td>
      <td>1</td>
      <td>17</td>
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
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>7074</th>
      <td>2021-22</td>
      <td>RS</td>
      <td>1629788</td>
      <td>Tyler Hall</td>
      <td>1610612752</td>
      <td>NYK</td>
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
      <td>0.00</td>
      <td>0.00</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>7075</th>
      <td>2021-22</td>
      <td>RS</td>
      <td>1629597</td>
      <td>Zylan Cheatham</td>
      <td>1610612762</td>
      <td>UTA</td>
      <td>1</td>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>0.000</td>
      <td>0</td>
      <td>2</td>
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
      <td>0.00</td>
      <td>0.00</td>
      <td>2021</td>
    </tr>
  </tbody>
</table>
<p>5148 rows × 29 columns</p>
</div>




```python
# same with playoffs
playoffs_df = data[data['Season_Type']=='Playoffs']
playoffs_df
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
      <th>AST_TOV</th>
      <th>STL_TOV</th>
      <th>season_start_year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>468</th>
      <td>2012-13</td>
      <td>Playoffs</td>
      <td>2544</td>
      <td>LeBron James</td>
      <td>1610612748</td>
      <td>MIA</td>
      <td>23</td>
      <td>960</td>
      <td>212</td>
      <td>432</td>
      <td>0.491</td>
      <td>36</td>
      <td>96</td>
      <td>0.375</td>
      <td>136</td>
      <td>175</td>
      <td>0.777</td>
      <td>37</td>
      <td>156</td>
      <td>193</td>
      <td>152</td>
      <td>41</td>
      <td>18</td>
      <td>70</td>
      <td>43</td>
      <td>596</td>
      <td>2.17</td>
      <td>0.59</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>469</th>
      <td>2012-13</td>
      <td>Playoffs</td>
      <td>2225</td>
      <td>Tony Parker</td>
      <td>1610612759</td>
      <td>SAS</td>
      <td>21</td>
      <td>765</td>
      <td>167</td>
      <td>365</td>
      <td>0.458</td>
      <td>11</td>
      <td>31</td>
      <td>0.355</td>
      <td>87</td>
      <td>112</td>
      <td>0.777</td>
      <td>14</td>
      <td>54</td>
      <td>68</td>
      <td>146</td>
      <td>24</td>
      <td>3</td>
      <td>53</td>
      <td>26</td>
      <td>432</td>
      <td>2.75</td>
      <td>0.45</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>470</th>
      <td>2012-13</td>
      <td>Playoffs</td>
      <td>1495</td>
      <td>Tim Duncan</td>
      <td>1610612759</td>
      <td>SAS</td>
      <td>21</td>
      <td>735</td>
      <td>151</td>
      <td>321</td>
      <td>0.470</td>
      <td>0</td>
      <td>1</td>
      <td>0.000</td>
      <td>79</td>
      <td>98</td>
      <td>0.806</td>
      <td>54</td>
      <td>160</td>
      <td>214</td>
      <td>40</td>
      <td>18</td>
      <td>34</td>
      <td>42</td>
      <td>53</td>
      <td>381</td>
      <td>0.95</td>
      <td>0.43</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>471</th>
      <td>2012-13</td>
      <td>Playoffs</td>
      <td>202331</td>
      <td>Paul George</td>
      <td>1610612754</td>
      <td>IND</td>
      <td>19</td>
      <td>780</td>
      <td>119</td>
      <td>277</td>
      <td>0.430</td>
      <td>34</td>
      <td>104</td>
      <td>0.327</td>
      <td>93</td>
      <td>128</td>
      <td>0.727</td>
      <td>16</td>
      <td>125</td>
      <td>141</td>
      <td>96</td>
      <td>25</td>
      <td>9</td>
      <td>75</td>
      <td>72</td>
      <td>365</td>
      <td>1.28</td>
      <td>0.33</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>472</th>
      <td>2012-13</td>
      <td>Playoffs</td>
      <td>2548</td>
      <td>Dwyane Wade</td>
      <td>1610612748</td>
      <td>MIA</td>
      <td>22</td>
      <td>782</td>
      <td>144</td>
      <td>315</td>
      <td>0.457</td>
      <td>1</td>
      <td>4</td>
      <td>0.250</td>
      <td>60</td>
      <td>80</td>
      <td>0.750</td>
      <td>38</td>
      <td>64</td>
      <td>102</td>
      <td>105</td>
      <td>38</td>
      <td>23</td>
      <td>58</td>
      <td>45</td>
      <td>349</td>
      <td>1.81</td>
      <td>0.66</td>
      <td>2012</td>
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
    </tr>
    <tr>
      <th>7288</th>
      <td>2021-22</td>
      <td>Playoffs</td>
      <td>1629006</td>
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
      <td>0.00</td>
      <td>0.00</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>7289</th>
      <td>2021-22</td>
      <td>Playoffs</td>
      <td>1630556</td>
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
      <td>1.00</td>
      <td>1.00</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>7290</th>
      <td>2021-22</td>
      <td>Playoffs</td>
      <td>1630201</td>
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
      <td>3.00</td>
      <td>1.00</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>7291</th>
      <td>2021-22</td>
      <td>Playoffs</td>
      <td>202693</td>
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
      <td>0.00</td>
      <td>0.00</td>
      <td>2021</td>
    </tr>
    <tr>
      <th>7292</th>
      <td>2021-22</td>
      <td>Playoffs</td>
      <td>200794</td>
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
      <td>0.00</td>
      <td>0.00</td>
      <td>2021</td>
    </tr>
  </tbody>
</table>
<p>2145 rows × 29 columns</p>
</div>




```python
#check the columns of the data DF
data.columns
```




    Index(['Year', 'Season_Type', 'PLAYER_ID', 'PLAYER', 'TEAM_ID', 'TEAM', 'GP',
           'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA',
           'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF',
           'PTS', 'AST_TOV', 'STL_TOV', 'season_start_year'],
          dtype='object')




```python
#Select the columns 
total_cols = ['MIN','FGM','FGA','FG3M','FG3A','FTM','FTA',
              'OREB','DREB','REB','AST','STL','BLK','TOV','PF','PTS']
```

### Wich player stats are correlated with each other?


```python
# Select only the numeric columns
data_numeric = data.select_dtypes(include='number')

# Calculating the correlation matrix
correlation_matrix = data_numeric.corr()
correlation_matrix
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
      <th>TEAM_ID</th>
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
      <th>AST_TOV</th>
      <th>STL_TOV</th>
      <th>season_start_year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>PLAYER_ID</th>
      <td>1.000000</td>
      <td>0.016102</td>
      <td>-0.123665</td>
      <td>-0.160812</td>
      <td>-0.137554</td>
      <td>-0.139728</td>
      <td>-0.044359</td>
      <td>-0.063209</td>
      <td>-0.057878</td>
      <td>0.011896</td>
      <td>-0.144029</td>
      <td>-0.146257</td>
      <td>-0.103690</td>
      <td>-0.118451</td>
      <td>-0.140710</td>
      <td>-0.138966</td>
      <td>-0.124454</td>
      <td>-0.140518</td>
      <td>-0.100507</td>
      <td>-0.150331</td>
      <td>-0.144051</td>
      <td>-0.136810</td>
      <td>-0.018408</td>
      <td>0.011474</td>
      <td>0.574698</td>
    </tr>
    <tr>
      <th>TEAM_ID</th>
      <td>0.016102</td>
      <td>1.000000</td>
      <td>0.029724</td>
      <td>0.020884</td>
      <td>0.013657</td>
      <td>0.017528</td>
      <td>-0.022576</td>
      <td>-0.012016</td>
      <td>-0.009738</td>
      <td>-0.009956</td>
      <td>0.016047</td>
      <td>0.017336</td>
      <td>-0.002840</td>
      <td>0.020158</td>
      <td>0.013304</td>
      <td>0.015691</td>
      <td>0.001249</td>
      <td>0.015868</td>
      <td>0.016956</td>
      <td>0.008195</td>
      <td>0.021100</td>
      <td>0.011811</td>
      <td>-0.004494</td>
      <td>0.020821</td>
      <td>0.004533</td>
    </tr>
    <tr>
      <th>GP</th>
      <td>-0.123665</td>
      <td>0.029724</td>
      <td>1.000000</td>
      <td>0.905608</td>
      <td>0.789848</td>
      <td>0.796535</td>
      <td>0.217880</td>
      <td>0.617089</td>
      <td>0.639598</td>
      <td>0.203980</td>
      <td>0.639904</td>
      <td>0.660181</td>
      <td>0.345681</td>
      <td>0.631183</td>
      <td>0.776140</td>
      <td>0.760203</td>
      <td>0.636788</td>
      <td>0.787656</td>
      <td>0.579758</td>
      <td>0.753761</td>
      <td>0.900406</td>
      <td>0.777601</td>
      <td>0.144630</td>
      <td>0.079466</td>
      <td>-0.102255</td>
    </tr>
    <tr>
      <th>MIN</th>
      <td>-0.160812</td>
      <td>0.020884</td>
      <td>0.905608</td>
      <td>1.000000</td>
      <td>0.935088</td>
      <td>0.940743</td>
      <td>0.200545</td>
      <td>0.728095</td>
      <td>0.748195</td>
      <td>0.229306</td>
      <td>0.802258</td>
      <td>0.814633</td>
      <td>0.338089</td>
      <td>0.651454</td>
      <td>0.861414</td>
      <td>0.829745</td>
      <td>0.777331</td>
      <td>0.890922</td>
      <td>0.610058</td>
      <td>0.887284</td>
      <td>0.917585</td>
      <td>0.929248</td>
      <td>0.161256</td>
      <td>0.038046</td>
      <td>-0.086147</td>
    </tr>
    <tr>
      <th>FGM</th>
      <td>-0.137554</td>
      <td>0.013657</td>
      <td>0.789848</td>
      <td>0.935088</td>
      <td>1.000000</td>
      <td>0.989459</td>
      <td>0.212113</td>
      <td>0.713755</td>
      <td>0.730225</td>
      <td>0.214321</td>
      <td>0.895489</td>
      <td>0.898680</td>
      <td>0.313388</td>
      <td>0.628332</td>
      <td>0.849227</td>
      <td>0.814045</td>
      <td>0.788669</td>
      <td>0.830690</td>
      <td>0.589914</td>
      <td>0.918063</td>
      <td>0.832574</td>
      <td>0.993742</td>
      <td>0.120812</td>
      <td>-0.032905</td>
      <td>-0.041261</td>
    </tr>
    <tr>
      <th>FGA</th>
      <td>-0.139728</td>
      <td>0.017528</td>
      <td>0.796535</td>
      <td>0.940743</td>
      <td>0.989459</td>
      <td>1.000000</td>
      <td>0.163044</td>
      <td>0.769594</td>
      <td>0.791253</td>
      <td>0.242616</td>
      <td>0.888476</td>
      <td>0.882753</td>
      <td>0.330974</td>
      <td>0.559782</td>
      <td>0.812269</td>
      <td>0.766880</td>
      <td>0.810013</td>
      <td>0.844514</td>
      <td>0.530731</td>
      <td>0.923041</td>
      <td>0.823042</td>
      <td>0.991104</td>
      <td>0.142703</td>
      <td>-0.025393</td>
      <td>-0.050273</td>
    </tr>
    <tr>
      <th>FG_PCT</th>
      <td>-0.044359</td>
      <td>-0.022576</td>
      <td>0.217880</td>
      <td>0.200545</td>
      <td>0.212113</td>
      <td>0.163044</td>
      <td>1.000000</td>
      <td>0.026541</td>
      <td>0.015603</td>
      <td>0.150446</td>
      <td>0.170257</td>
      <td>0.195832</td>
      <td>0.188619</td>
      <td>0.312947</td>
      <td>0.262171</td>
      <td>0.285202</td>
      <td>0.100443</td>
      <td>0.152606</td>
      <td>0.280728</td>
      <td>0.167697</td>
      <td>0.246865</td>
      <td>0.192359</td>
      <td>0.019698</td>
      <td>0.070350</td>
      <td>0.023296</td>
    </tr>
    <tr>
      <th>FG3M</th>
      <td>-0.063209</td>
      <td>-0.012016</td>
      <td>0.617089</td>
      <td>0.728095</td>
      <td>0.713755</td>
      <td>0.769594</td>
      <td>0.026541</td>
      <td>1.000000</td>
      <td>0.992040</td>
      <td>0.387790</td>
      <td>0.594705</td>
      <td>0.548579</td>
      <td>0.328327</td>
      <td>0.133505</td>
      <td>0.477402</td>
      <td>0.395030</td>
      <td>0.639617</td>
      <td>0.659748</td>
      <td>0.186129</td>
      <td>0.646404</td>
      <td>0.571964</td>
      <td>0.757302</td>
      <td>0.195808</td>
      <td>0.047404</td>
      <td>0.078814</td>
    </tr>
    <tr>
      <th>FG3A</th>
      <td>-0.057878</td>
      <td>-0.009738</td>
      <td>0.639598</td>
      <td>0.748195</td>
      <td>0.730225</td>
      <td>0.791253</td>
      <td>0.015603</td>
      <td>0.992040</td>
      <td>1.000000</td>
      <td>0.375069</td>
      <td>0.618485</td>
      <td>0.574868</td>
      <td>0.334657</td>
      <td>0.147951</td>
      <td>0.496640</td>
      <td>0.413532</td>
      <td>0.665279</td>
      <td>0.685530</td>
      <td>0.200059</td>
      <td>0.675136</td>
      <td>0.593905</td>
      <td>0.773190</td>
      <td>0.201529</td>
      <td>0.048826</td>
      <td>0.081333</td>
    </tr>
    <tr>
      <th>FG3_PCT</th>
      <td>0.011896</td>
      <td>-0.009956</td>
      <td>0.203980</td>
      <td>0.229306</td>
      <td>0.214321</td>
      <td>0.242616</td>
      <td>0.150446</td>
      <td>0.387790</td>
      <td>0.375069</td>
      <td>1.000000</td>
      <td>0.155608</td>
      <td>0.125497</td>
      <td>0.292931</td>
      <td>-0.083778</td>
      <td>0.094308</td>
      <td>0.046656</td>
      <td>0.225072</td>
      <td>0.218278</td>
      <td>-0.032831</td>
      <td>0.184881</td>
      <td>0.149306</td>
      <td>0.232953</td>
      <td>0.258865</td>
      <td>0.123466</td>
      <td>0.108059</td>
    </tr>
    <tr>
      <th>FTM</th>
      <td>-0.144029</td>
      <td>0.016047</td>
      <td>0.639904</td>
      <td>0.802258</td>
      <td>0.895489</td>
      <td>0.888476</td>
      <td>0.170257</td>
      <td>0.594705</td>
      <td>0.618485</td>
      <td>0.155608</td>
      <td>1.000000</td>
      <td>0.987628</td>
      <td>0.286228</td>
      <td>0.537560</td>
      <td>0.750768</td>
      <td>0.714559</td>
      <td>0.757236</td>
      <td>0.739736</td>
      <td>0.513849</td>
      <td>0.880927</td>
      <td>0.703658</td>
      <td>0.924384</td>
      <td>0.089693</td>
      <td>-0.069042</td>
      <td>-0.060002</td>
    </tr>
    <tr>
      <th>FTA</th>
      <td>-0.146257</td>
      <td>0.017336</td>
      <td>0.660181</td>
      <td>0.814633</td>
      <td>0.898680</td>
      <td>0.882753</td>
      <td>0.195832</td>
      <td>0.548579</td>
      <td>0.574868</td>
      <td>0.125497</td>
      <td>0.987628</td>
      <td>1.000000</td>
      <td>0.256116</td>
      <td>0.612609</td>
      <td>0.796518</td>
      <td>0.770150</td>
      <td>0.741826</td>
      <td>0.749419</td>
      <td>0.575220</td>
      <td>0.888274</td>
      <td>0.736829</td>
      <td>0.918892</td>
      <td>0.070869</td>
      <td>-0.067916</td>
      <td>-0.070697</td>
    </tr>
    <tr>
      <th>FT_PCT</th>
      <td>-0.103690</td>
      <td>-0.002840</td>
      <td>0.345681</td>
      <td>0.338089</td>
      <td>0.313388</td>
      <td>0.330974</td>
      <td>0.188619</td>
      <td>0.328327</td>
      <td>0.334657</td>
      <td>0.292931</td>
      <td>0.286228</td>
      <td>0.256116</td>
      <td>1.000000</td>
      <td>0.124504</td>
      <td>0.239286</td>
      <td>0.214405</td>
      <td>0.275164</td>
      <td>0.287876</td>
      <td>0.127261</td>
      <td>0.289026</td>
      <td>0.300684</td>
      <td>0.324687</td>
      <td>0.282028</td>
      <td>0.160636</td>
      <td>0.003087</td>
    </tr>
    <tr>
      <th>OREB</th>
      <td>-0.118451</td>
      <td>0.020158</td>
      <td>0.631183</td>
      <td>0.651454</td>
      <td>0.628332</td>
      <td>0.559782</td>
      <td>0.312947</td>
      <td>0.133505</td>
      <td>0.147951</td>
      <td>-0.083778</td>
      <td>0.537560</td>
      <td>0.612609</td>
      <td>0.124504</td>
      <td>1.000000</td>
      <td>0.844124</td>
      <td>0.916110</td>
      <td>0.326077</td>
      <td>0.522441</td>
      <td>0.796824</td>
      <td>0.562423</td>
      <td>0.746577</td>
      <td>0.582833</td>
      <td>-0.076210</td>
      <td>-0.014588</td>
      <td>-0.083319</td>
    </tr>
    <tr>
      <th>DREB</th>
      <td>-0.140710</td>
      <td>0.013304</td>
      <td>0.776140</td>
      <td>0.861414</td>
      <td>0.849227</td>
      <td>0.812269</td>
      <td>0.262171</td>
      <td>0.477402</td>
      <td>0.496640</td>
      <td>0.094308</td>
      <td>0.750768</td>
      <td>0.796518</td>
      <td>0.239286</td>
      <td>0.844124</td>
      <td>1.000000</td>
      <td>0.988267</td>
      <td>0.607862</td>
      <td>0.737908</td>
      <td>0.771924</td>
      <td>0.798257</td>
      <td>0.863288</td>
      <td>0.827034</td>
      <td>0.041247</td>
      <td>-0.013224</td>
      <td>-0.044384</td>
    </tr>
    <tr>
      <th>REB</th>
      <td>-0.138966</td>
      <td>0.015691</td>
      <td>0.760203</td>
      <td>0.829745</td>
      <td>0.814045</td>
      <td>0.766880</td>
      <td>0.285202</td>
      <td>0.395030</td>
      <td>0.413532</td>
      <td>0.046656</td>
      <td>0.714559</td>
      <td>0.770150</td>
      <td>0.214405</td>
      <td>0.916110</td>
      <td>0.988267</td>
      <td>1.000000</td>
      <td>0.547447</td>
      <td>0.700635</td>
      <td>0.804239</td>
      <td>0.757154</td>
      <td>0.858245</td>
      <td>0.784487</td>
      <td>0.009133</td>
      <td>-0.014045</td>
      <td>-0.056926</td>
    </tr>
    <tr>
      <th>AST</th>
      <td>-0.124454</td>
      <td>0.001249</td>
      <td>0.636788</td>
      <td>0.777331</td>
      <td>0.788669</td>
      <td>0.810013</td>
      <td>0.100443</td>
      <td>0.639617</td>
      <td>0.665279</td>
      <td>0.225072</td>
      <td>0.757236</td>
      <td>0.741826</td>
      <td>0.275164</td>
      <td>0.326077</td>
      <td>0.607862</td>
      <td>0.547447</td>
      <td>1.000000</td>
      <td>0.806639</td>
      <td>0.304027</td>
      <td>0.896472</td>
      <td>0.643843</td>
      <td>0.802840</td>
      <td>0.319355</td>
      <td>-0.037456</td>
      <td>-0.026299</td>
    </tr>
    <tr>
      <th>STL</th>
      <td>-0.140518</td>
      <td>0.015868</td>
      <td>0.787656</td>
      <td>0.890922</td>
      <td>0.830690</td>
      <td>0.844514</td>
      <td>0.152606</td>
      <td>0.659748</td>
      <td>0.685530</td>
      <td>0.218278</td>
      <td>0.739736</td>
      <td>0.749419</td>
      <td>0.287876</td>
      <td>0.522441</td>
      <td>0.737908</td>
      <td>0.700635</td>
      <td>0.806639</td>
      <td>1.000000</td>
      <td>0.493957</td>
      <td>0.847021</td>
      <td>0.812453</td>
      <td>0.832418</td>
      <td>0.203368</td>
      <td>0.151876</td>
      <td>-0.080368</td>
    </tr>
    <tr>
      <th>BLK</th>
      <td>-0.100507</td>
      <td>0.016956</td>
      <td>0.579758</td>
      <td>0.610058</td>
      <td>0.589914</td>
      <td>0.530731</td>
      <td>0.280728</td>
      <td>0.186129</td>
      <td>0.200059</td>
      <td>-0.032831</td>
      <td>0.513849</td>
      <td>0.575220</td>
      <td>0.127261</td>
      <td>0.796824</td>
      <td>0.771924</td>
      <td>0.804239</td>
      <td>0.304027</td>
      <td>0.493957</td>
      <td>1.000000</td>
      <td>0.523227</td>
      <td>0.700297</td>
      <td>0.556081</td>
      <td>-0.067553</td>
      <td>-0.000803</td>
      <td>-0.060701</td>
    </tr>
    <tr>
      <th>TOV</th>
      <td>-0.150331</td>
      <td>0.008195</td>
      <td>0.753761</td>
      <td>0.887284</td>
      <td>0.918063</td>
      <td>0.923041</td>
      <td>0.167697</td>
      <td>0.646404</td>
      <td>0.675136</td>
      <td>0.184881</td>
      <td>0.880927</td>
      <td>0.888274</td>
      <td>0.289026</td>
      <td>0.562423</td>
      <td>0.798257</td>
      <td>0.757154</td>
      <td>0.896472</td>
      <td>0.847021</td>
      <td>0.523227</td>
      <td>1.000000</td>
      <td>0.812178</td>
      <td>0.923062</td>
      <td>0.130607</td>
      <td>-0.088625</td>
      <td>-0.084464</td>
    </tr>
    <tr>
      <th>PF</th>
      <td>-0.144051</td>
      <td>0.021100</td>
      <td>0.900406</td>
      <td>0.917585</td>
      <td>0.832574</td>
      <td>0.823042</td>
      <td>0.246865</td>
      <td>0.571964</td>
      <td>0.593905</td>
      <td>0.149306</td>
      <td>0.703658</td>
      <td>0.736829</td>
      <td>0.300684</td>
      <td>0.746577</td>
      <td>0.863288</td>
      <td>0.858245</td>
      <td>0.643843</td>
      <td>0.812453</td>
      <td>0.700297</td>
      <td>0.812178</td>
      <td>1.000000</td>
      <td>0.816389</td>
      <td>0.077363</td>
      <td>0.033166</td>
      <td>-0.095391</td>
    </tr>
    <tr>
      <th>PTS</th>
      <td>-0.136810</td>
      <td>0.011811</td>
      <td>0.777601</td>
      <td>0.929248</td>
      <td>0.993742</td>
      <td>0.991104</td>
      <td>0.192359</td>
      <td>0.757302</td>
      <td>0.773190</td>
      <td>0.232953</td>
      <td>0.924384</td>
      <td>0.918892</td>
      <td>0.324687</td>
      <td>0.582833</td>
      <td>0.827034</td>
      <td>0.784487</td>
      <td>0.802840</td>
      <td>0.832418</td>
      <td>0.556081</td>
      <td>0.923062</td>
      <td>0.816389</td>
      <td>1.000000</td>
      <td>0.129067</td>
      <td>-0.032397</td>
      <td>-0.033057</td>
    </tr>
    <tr>
      <th>AST_TOV</th>
      <td>-0.018408</td>
      <td>-0.004494</td>
      <td>0.144630</td>
      <td>0.161256</td>
      <td>0.120812</td>
      <td>0.142703</td>
      <td>0.019698</td>
      <td>0.195808</td>
      <td>0.201529</td>
      <td>0.258865</td>
      <td>0.089693</td>
      <td>0.070869</td>
      <td>0.282028</td>
      <td>-0.076210</td>
      <td>0.041247</td>
      <td>0.009133</td>
      <td>0.319355</td>
      <td>0.203368</td>
      <td>-0.067553</td>
      <td>0.130607</td>
      <td>0.077363</td>
      <td>0.129067</td>
      <td>1.000000</td>
      <td>0.463105</td>
      <td>0.102759</td>
    </tr>
    <tr>
      <th>STL_TOV</th>
      <td>0.011474</td>
      <td>0.020821</td>
      <td>0.079466</td>
      <td>0.038046</td>
      <td>-0.032905</td>
      <td>-0.025393</td>
      <td>0.070350</td>
      <td>0.047404</td>
      <td>0.048826</td>
      <td>0.123466</td>
      <td>-0.069042</td>
      <td>-0.067916</td>
      <td>0.160636</td>
      <td>-0.014588</td>
      <td>-0.013224</td>
      <td>-0.014045</td>
      <td>-0.037456</td>
      <td>0.151876</td>
      <td>-0.000803</td>
      <td>-0.088625</td>
      <td>0.033166</td>
      <td>-0.032397</td>
      <td>0.463105</td>
      <td>1.000000</td>
      <td>0.044033</td>
    </tr>
    <tr>
      <th>season_start_year</th>
      <td>0.574698</td>
      <td>0.004533</td>
      <td>-0.102255</td>
      <td>-0.086147</td>
      <td>-0.041261</td>
      <td>-0.050273</td>
      <td>0.023296</td>
      <td>0.078814</td>
      <td>0.081333</td>
      <td>0.108059</td>
      <td>-0.060002</td>
      <td>-0.070697</td>
      <td>0.003087</td>
      <td>-0.083319</td>
      <td>-0.044384</td>
      <td>-0.056926</td>
      <td>-0.026299</td>
      <td>-0.080368</td>
      <td>-0.060701</td>
      <td>-0.084464</td>
      <td>-0.095391</td>
      <td>-0.033057</td>
      <td>0.102759</td>
      <td>0.044033</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
data_per_min = data.groupby(['PLAYER_ID','PLAYER','Year'])[total_cols].sum().reset_index()
for col in data_per_min.columns[4:]:
    data_per_min[col] =  data_per_min[col]/data_per_min['MIN']

data_per_min['FG%'] =  data_per_min['FGM']/data_per_min['FGA']
data_per_min['3PT%'] =  data_per_min['FG3M']/data_per_min['FG3A']
data_per_min['FT%'] =  data_per_min['FTM']/data_per_min['FTA']
data_per_min['FG3A%'] =  data_per_min['FG3A']/data_per_min['FGA']
data_per_min['PTS/FGA'] =  data_per_min['PTS']/data_per_min['FGA']
data_per_min['FG3M/FGM'] =  data_per_min['FG3M']/data_per_min['FGM']
data_per_min['FTA/FGA'] =  data_per_min['FTA']/data_per_min['FGA']
data_per_min['TRU%'] = 0.5*data_per_min['PTS']/(data_per_min['FGA']+0.475*data_per_min['FTA'])
data_per_min['AST_TOV'] =  data_per_min['AST']/data_per_min['TOV']

data_per_min = data_per_min[data_per_min['MIN']>=50]
data_per_min.drop(columns='PLAYER_ID', inplace=True)

data_per_min
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
      <th>PLAYER</th>
      <th>Year</th>
      <th>MIN</th>
      <th>FGM</th>
      <th>FGA</th>
      <th>FG3M</th>
      <th>FG3A</th>
      <th>FTM</th>
      <th>FTA</th>
      <th>OREB</th>
      <th>DREB</th>
      <th>REB</th>
      <th>AST</th>
      <th>STL</th>
      <th>BLK</th>
      <th>TOV</th>
      <th>PF</th>
      <th>PTS</th>
      <th>FG%</th>
      <th>3PT%</th>
      <th>FT%</th>
      <th>FG3A%</th>
      <th>PTS/FGA</th>
      <th>FG3M/FGM</th>
      <th>FTA/FGA</th>
      <th>TRU%</th>
      <th>AST_TOV</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Grant Hill</td>
      <td>2012-13</td>
      <td>457</td>
      <td>0.087527</td>
      <td>0.223195</td>
      <td>0.006565</td>
      <td>0.024070</td>
      <td>0.030635</td>
      <td>0.052516</td>
      <td>0.017505</td>
      <td>0.098468</td>
      <td>0.115974</td>
      <td>0.061269</td>
      <td>0.024070</td>
      <td>0.015317</td>
      <td>0.056893</td>
      <td>0.096280</td>
      <td>0.212254</td>
      <td>0.392157</td>
      <td>0.272727</td>
      <td>0.583333</td>
      <td>0.107843</td>
      <td>0.950980</td>
      <td>0.075000</td>
      <td>0.235294</td>
      <td>0.427690</td>
      <td>1.076923</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Juwan Howard</td>
      <td>2012-13</td>
      <td>51</td>
      <td>0.196078</td>
      <td>0.372549</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.019608</td>
      <td>0.019608</td>
      <td>0.000000</td>
      <td>0.156863</td>
      <td>0.156863</td>
      <td>0.117647</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.078431</td>
      <td>0.176471</td>
      <td>0.411765</td>
      <td>0.526316</td>
      <td>NaN</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>1.105263</td>
      <td>0.000000</td>
      <td>0.052632</td>
      <td>0.539153</td>
      <td>1.500000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Jason Kidd</td>
      <td>2012-13</td>
      <td>2290</td>
      <td>0.067686</td>
      <td>0.189520</td>
      <td>0.051092</td>
      <td>0.149345</td>
      <td>0.018341</td>
      <td>0.021834</td>
      <td>0.024891</td>
      <td>0.134498</td>
      <td>0.159389</td>
      <td>0.119214</td>
      <td>0.059825</td>
      <td>0.012664</td>
      <td>0.038865</td>
      <td>0.059825</td>
      <td>0.204803</td>
      <td>0.357143</td>
      <td>0.342105</td>
      <td>0.840000</td>
      <td>0.788018</td>
      <td>1.080645</td>
      <td>0.754839</td>
      <td>0.115207</td>
      <td>0.512288</td>
      <td>3.067416</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Kurt Thomas</td>
      <td>2012-13</td>
      <td>392</td>
      <td>0.114796</td>
      <td>0.211735</td>
      <td>0.002551</td>
      <td>0.002551</td>
      <td>0.015306</td>
      <td>0.033163</td>
      <td>0.061224</td>
      <td>0.165816</td>
      <td>0.227041</td>
      <td>0.053571</td>
      <td>0.025510</td>
      <td>0.040816</td>
      <td>0.020408</td>
      <td>0.132653</td>
      <td>0.247449</td>
      <td>0.542169</td>
      <td>1.000000</td>
      <td>0.461538</td>
      <td>0.012048</td>
      <td>1.168675</td>
      <td>0.022222</td>
      <td>0.156627</td>
      <td>0.543874</td>
      <td>2.625000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Kevin Garnett</td>
      <td>2012-13</td>
      <td>2234</td>
      <td>0.202328</td>
      <td>0.407341</td>
      <td>0.000895</td>
      <td>0.008057</td>
      <td>0.077887</td>
      <td>0.097583</td>
      <td>0.037601</td>
      <td>0.236347</td>
      <td>0.273948</td>
      <td>0.080573</td>
      <td>0.037153</td>
      <td>0.030439</td>
      <td>0.057744</td>
      <td>0.079230</td>
      <td>0.483438</td>
      <td>0.496703</td>
      <td>0.111111</td>
      <td>0.798165</td>
      <td>0.019780</td>
      <td>1.186813</td>
      <td>0.004425</td>
      <td>0.239560</td>
      <td>0.532781</td>
      <td>1.395349</td>
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
    </tr>
    <tr>
      <th>5145</th>
      <td>Jamorko Pickett</td>
      <td>2021-22</td>
      <td>176</td>
      <td>0.102273</td>
      <td>0.284091</td>
      <td>0.073864</td>
      <td>0.221591</td>
      <td>0.005682</td>
      <td>0.011364</td>
      <td>0.034091</td>
      <td>0.147727</td>
      <td>0.181818</td>
      <td>0.039773</td>
      <td>0.000000</td>
      <td>0.039773</td>
      <td>0.028409</td>
      <td>0.068182</td>
      <td>0.284091</td>
      <td>0.360000</td>
      <td>0.333333</td>
      <td>0.500000</td>
      <td>0.780000</td>
      <td>1.000000</td>
      <td>0.722222</td>
      <td>0.040000</td>
      <td>0.490677</td>
      <td>1.400000</td>
    </tr>
    <tr>
      <th>5149</th>
      <td>Kevin Pangos</td>
      <td>2021-22</td>
      <td>166</td>
      <td>0.090361</td>
      <td>0.277108</td>
      <td>0.036145</td>
      <td>0.156627</td>
      <td>0.018072</td>
      <td>0.024096</td>
      <td>0.012048</td>
      <td>0.054217</td>
      <td>0.066265</td>
      <td>0.180723</td>
      <td>0.018072</td>
      <td>0.000000</td>
      <td>0.042169</td>
      <td>0.066265</td>
      <td>0.234940</td>
      <td>0.326087</td>
      <td>0.230769</td>
      <td>0.750000</td>
      <td>0.565217</td>
      <td>0.847826</td>
      <td>0.400000</td>
      <td>0.086957</td>
      <td>0.407098</td>
      <td>4.285714</td>
    </tr>
    <tr>
      <th>5150</th>
      <td>Aleem Ford</td>
      <td>2021-22</td>
      <td>74</td>
      <td>0.081081</td>
      <td>0.270270</td>
      <td>0.027027</td>
      <td>0.202703</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.027027</td>
      <td>0.175676</td>
      <td>0.202703</td>
      <td>0.027027</td>
      <td>0.013514</td>
      <td>0.000000</td>
      <td>0.054054</td>
      <td>0.094595</td>
      <td>0.189189</td>
      <td>0.300000</td>
      <td>0.133333</td>
      <td>NaN</td>
      <td>0.750000</td>
      <td>0.700000</td>
      <td>0.333333</td>
      <td>0.000000</td>
      <td>0.350000</td>
      <td>0.500000</td>
    </tr>
    <tr>
      <th>5152</th>
      <td>Malcolm Hill</td>
      <td>2021-22</td>
      <td>212</td>
      <td>0.113208</td>
      <td>0.245283</td>
      <td>0.061321</td>
      <td>0.169811</td>
      <td>0.051887</td>
      <td>0.066038</td>
      <td>0.051887</td>
      <td>0.113208</td>
      <td>0.165094</td>
      <td>0.037736</td>
      <td>0.033019</td>
      <td>0.014151</td>
      <td>0.014151</td>
      <td>0.113208</td>
      <td>0.339623</td>
      <td>0.461538</td>
      <td>0.361111</td>
      <td>0.785714</td>
      <td>0.692308</td>
      <td>1.384615</td>
      <td>0.541667</td>
      <td>0.269231</td>
      <td>0.613811</td>
      <td>2.666667</td>
    </tr>
    <tr>
      <th>5153</th>
      <td>Olivier Sarr</td>
      <td>2021-22</td>
      <td>421</td>
      <td>0.137767</td>
      <td>0.239905</td>
      <td>0.030879</td>
      <td>0.068884</td>
      <td>0.057007</td>
      <td>0.068884</td>
      <td>0.080760</td>
      <td>0.140143</td>
      <td>0.220903</td>
      <td>0.045131</td>
      <td>0.014252</td>
      <td>0.035629</td>
      <td>0.052257</td>
      <td>0.123515</td>
      <td>0.363420</td>
      <td>0.574257</td>
      <td>0.448276</td>
      <td>0.827586</td>
      <td>0.287129</td>
      <td>1.514851</td>
      <td>0.224138</td>
      <td>0.287129</td>
      <td>0.666521</td>
      <td>0.863636</td>
    </tr>
  </tbody>
</table>
<p>4749 rows × 27 columns</p>
</div>




```python
fig = px.imshow(data_numeric.corr())
fig.show()
```


<div>                            <div id="5b50d484-70af-42a6-8c4c-c964c89624f5" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("5b50d484-70af-42a6-8c4c-c964c89624f5")) {                    Plotly.newPlot(                        "5b50d484-70af-42a6-8c4c-c964c89624f5",                        [{"coloraxis":"coloraxis","name":"0","x":["PLAYER_ID","TEAM_ID","GP","MIN","FGM","FGA","FG_PCT","FG3M","FG3A","FG3_PCT","FTM","FTA","FT_PCT","OREB","DREB","REB","AST","STL","BLK","TOV","PF","PTS","AST_TOV","STL_TOV","season_start_year"],"y":["PLAYER_ID","TEAM_ID","GP","MIN","FGM","FGA","FG_PCT","FG3M","FG3A","FG3_PCT","FTM","FTA","FT_PCT","OREB","DREB","REB","AST","STL","BLK","TOV","PF","PTS","AST_TOV","STL_TOV","season_start_year"],"z":[[1.0,0.016101564385848387,-0.12366526559188147,-0.16081183014871375,-0.13755375079291568,-0.1397275886149642,-0.04435937275448197,-0.06320902327798854,-0.05787809707997265,0.011895904160289227,-0.14402894186190437,-0.14625700451827311,-0.10369041823920347,-0.11845135041044358,-0.14070957647914561,-0.13896600888465377,-0.12445359100886229,-0.14051796121236304,-0.10050708439061831,-0.1503307252206407,-0.14405124346493312,-0.1368098563323149,-0.01840784367296909,0.011473637308239996,0.5746979231775432],[0.016101564385848387,1.0,0.02972389458313805,0.020883909649039592,0.01365713480777669,0.01752846050574357,-0.022575738873946736,-0.012015804538819319,-0.00973753606520075,-0.009956158646150797,0.01604729167186594,0.01733621576019403,-0.0028404323957505868,0.02015840766870058,0.01330353486572216,0.01569102488121786,0.001248869866151483,0.015868434564281803,0.016955541468535545,0.00819491224749515,0.02110034434120139,0.011810914275504696,-0.004493573273044055,0.020821418948473336,0.004532613961366425],[-0.12366526559188147,0.02972389458313805,1.0,0.9056076451046384,0.7898480388062976,0.7965345885474213,0.21787955305579776,0.6170885042288708,0.6395984070367542,0.2039802668693205,0.6399042369945082,0.6601809271634863,0.3456813244079315,0.6311834512861995,0.7761397457255951,0.7602031151866588,0.6367882601228562,0.7876561007647666,0.5797582465559432,0.753760797963878,0.9004061944783689,0.7776007811502121,0.14462970195325364,0.07946561390168015,-0.10225532211529424],[-0.16081183014871375,0.020883909649039592,0.9056076451046384,1.0,0.9350883535353085,0.940743401565885,0.2005452178633324,0.7280947469447686,0.7481946217994216,0.22930559914729615,0.8022575186440674,0.8146330961678471,0.33808938553371476,0.6514538134939373,0.8614144830032071,0.8297454893601746,0.7773308141263721,0.8909220323056914,0.61005831101639,0.8872840634193554,0.9175847979066689,0.9292482585265791,0.1612564466330906,0.03804638338204309,-0.0861474745242581],[-0.13755375079291568,0.01365713480777669,0.7898480388062976,0.9350883535353085,1.0,0.9894592979482678,0.21211299759151786,0.7137547340230268,0.7302254043919133,0.21432106640134674,0.8954885447535942,0.8986804552440348,0.3133875721959094,0.6283324583144663,0.8492265267858202,0.814044596284448,0.7886690880729919,0.8306898322832806,0.5899137122538661,0.9180630924884345,0.8325736437047391,0.9937420194143424,0.12081159615097704,-0.032905185856826745,-0.041260715116721636],[-0.1397275886149642,0.01752846050574357,0.7965345885474213,0.940743401565885,0.9894592979482678,1.0,0.16304371841275508,0.7695936743870617,0.7912528906540084,0.2426164972762935,0.8884760800773628,0.8827532815043968,0.3309744687554303,0.5597822070767655,0.8122693418700572,0.7668796389957152,0.810012955583998,0.8445140607064322,0.5307313135323641,0.9230407527468868,0.8230423619096596,0.9911042031182221,0.14270324668913895,-0.025393105534547173,-0.050272634042559515],[-0.04435937275448197,-0.022575738873946736,0.21787955305579776,0.2005452178633324,0.21211299759151786,0.16304371841275508,1.0,0.02654078582685547,0.015602626819888674,0.15044596977769759,0.17025707969957637,0.19583195996114652,0.18861866613187148,0.3129473561885382,0.2621713760879465,0.2852023966109048,0.10044345177074865,0.1526059106616036,0.280728492176655,0.16769658960188602,0.24686452025214733,0.19235892825303325,0.01969765625700305,0.07034971520536534,0.023296066125147712],[-0.06320902327798854,-0.012015804538819319,0.6170885042288708,0.7280947469447686,0.7137547340230268,0.7695936743870617,0.02654078582685547,1.0,0.9920395263450307,0.3877899550200829,0.5947054963505916,0.5485789576070078,0.3283266930285281,0.13350497238770975,0.47740170748786726,0.395030028515789,0.6396174455917779,0.6597479424443786,0.1861287506292334,0.6464035378008048,0.5719636132613489,0.7573018915506724,0.19580756359660065,0.04740410442389703,0.07881426881868812],[-0.05787809707997265,-0.00973753606520075,0.6395984070367542,0.7481946217994216,0.7302254043919133,0.7912528906540084,0.015602626819888674,0.9920395263450307,1.0,0.37506947232652754,0.618484918075366,0.5748679574412178,0.33465744943897924,0.14795113273961216,0.4966404800776794,0.41353206122077985,0.6652794784130415,0.685529842674854,0.20005925121530022,0.6751360562959801,0.5939046626227883,0.773189740929927,0.2015287030309534,0.0488260976389277,0.08133270930182078],[0.011895904160289227,-0.009956158646150797,0.2039802668693205,0.22930559914729615,0.21432106640134674,0.2426164972762935,0.15044596977769759,0.3877899550200829,0.37506947232652754,1.0,0.15560802562231987,0.12549655360807402,0.29293067882055634,-0.08377755083303179,0.09430828148239359,0.046656273084028706,0.22507218466438175,0.21827826053173177,-0.03283055955234412,0.18488105406255914,0.14930566970555986,0.23295317332031318,0.25886514325605187,0.12346595893083297,0.10805934819853975],[-0.14402894186190437,0.01604729167186594,0.6399042369945082,0.8022575186440674,0.8954885447535942,0.8884760800773628,0.17025707969957637,0.5947054963505916,0.618484918075366,0.15560802562231987,1.0,0.987628457113302,0.286227692405602,0.5375603776513143,0.7507682431128876,0.7145590537370893,0.7572359797045886,0.7397357731778511,0.5138485718829982,0.8809272786843063,0.7036584105837277,0.9243841999884518,0.08969295862403473,-0.06904235019387298,-0.06000192926408283],[-0.14625700451827311,0.01733621576019403,0.6601809271634863,0.8146330961678471,0.8986804552440348,0.8827532815043968,0.19583195996114652,0.5485789576070078,0.5748679574412178,0.12549655360807402,0.987628457113302,1.0,0.25611583738204535,0.6126085221249217,0.796517780099497,0.7701499859634587,0.7418257156391584,0.7494192930539048,0.5752203569034993,0.8882735529109128,0.7368289723115962,0.9188915220824492,0.07086938716354318,-0.06791570076372924,-0.07069730147505776],[-0.10369041823920347,-0.0028404323957505868,0.3456813244079315,0.33808938553371476,0.3133875721959094,0.3309744687554303,0.18861866613187148,0.3283266930285281,0.33465744943897924,0.29293067882055634,0.286227692405602,0.25611583738204535,1.0,0.12450380315190887,0.23928590697064928,0.21440478468697877,0.27516433940669965,0.2878758268035017,0.12726075509668147,0.2890255171192515,0.3006837431339924,0.32468661232524554,0.28202797751040615,0.16063595618156504,0.003086615534182435],[-0.11845135041044358,0.02015840766870058,0.6311834512861995,0.6514538134939373,0.6283324583144663,0.5597822070767655,0.3129473561885382,0.13350497238770975,0.14795113273961216,-0.08377755083303179,0.5375603776513143,0.6126085221249217,0.12450380315190887,1.0,0.8441236482770487,0.9161098543983298,0.32607721624492547,0.5224412170723621,0.796824006496164,0.5624233464008704,0.7465772096832335,0.582832799507287,-0.07621015457810935,-0.01458756540138372,-0.08331865438809538],[-0.14070957647914561,0.01330353486572216,0.7761397457255951,0.8614144830032071,0.8492265267858202,0.8122693418700572,0.2621713760879465,0.47740170748786726,0.4966404800776794,0.09430828148239359,0.7507682431128876,0.796517780099497,0.23928590697064928,0.8441236482770487,1.0,0.9882666058623458,0.6078621309257574,0.7379076702187752,0.7719243386436939,0.7982574543488322,0.8632879411682418,0.8270335696424134,0.041247212176456965,-0.013224144869379919,-0.04438357673328008],[-0.13896600888465377,0.01569102488121786,0.7602031151866588,0.8297454893601746,0.814044596284448,0.7668796389957152,0.2852023966109048,0.395030028515789,0.41353206122077985,0.046656273084028706,0.7145590537370893,0.7701499859634587,0.21440478468697877,0.9161098543983298,0.9882666058623458,1.0,0.5474474670442597,0.70063485953141,0.8042387728613937,0.7571540795054174,0.8582453261116795,0.7844868871312299,0.0091334648976886,-0.014044628702448221,-0.0569255926690611],[-0.12445359100886229,0.001248869866151483,0.6367882601228562,0.7773308141263721,0.7886690880729919,0.810012955583998,0.10044345177074865,0.6396174455917779,0.6652794784130415,0.22507218466438175,0.7572359797045886,0.7418257156391584,0.27516433940669965,0.32607721624492547,0.6078621309257574,0.5474474670442597,1.0,0.8066389048256702,0.30402744166918605,0.8964717737865381,0.6438425098144365,0.8028401671479567,0.3193553054213916,-0.03745646419505955,-0.026299353523843196],[-0.14051796121236304,0.015868434564281803,0.7876561007647666,0.8909220323056914,0.8306898322832806,0.8445140607064322,0.1526059106616036,0.6597479424443786,0.685529842674854,0.21827826053173177,0.7397357731778511,0.7494192930539048,0.2878758268035017,0.5224412170723621,0.7379076702187752,0.70063485953141,0.8066389048256702,1.0,0.4939570212596115,0.8470209280534508,0.812453094622199,0.8324176362131349,0.20336815999120822,0.1518757137801966,-0.08036759940552606],[-0.10050708439061831,0.016955541468535545,0.5797582465559432,0.61005831101639,0.5899137122538661,0.5307313135323641,0.280728492176655,0.1861287506292334,0.20005925121530022,-0.03283055955234412,0.5138485718829982,0.5752203569034993,0.12726075509668147,0.796824006496164,0.7719243386436939,0.8042387728613937,0.30402744166918605,0.4939570212596115,1.0,0.5232266827430315,0.7002972855612243,0.556081477469842,-0.067552954107452,-0.0008026119602064526,-0.060701130289226024],[-0.1503307252206407,0.00819491224749515,0.753760797963878,0.8872840634193554,0.9180630924884345,0.9230407527468868,0.16769658960188602,0.6464035378008048,0.6751360562959801,0.18488105406255914,0.8809272786843063,0.8882735529109128,0.2890255171192515,0.5624233464008704,0.7982574543488322,0.7571540795054174,0.8964717737865381,0.8470209280534508,0.5232266827430315,1.0,0.8121779928448007,0.9230624199957504,0.13060691943189065,-0.08862531923309717,-0.084463801279757],[-0.14405124346493312,0.02110034434120139,0.9004061944783689,0.9175847979066689,0.8325736437047391,0.8230423619096596,0.24686452025214733,0.5719636132613489,0.5939046626227883,0.14930566970555986,0.7036584105837277,0.7368289723115962,0.3006837431339924,0.7465772096832335,0.8632879411682418,0.8582453261116795,0.6438425098144365,0.812453094622199,0.7002972855612243,0.8121779928448007,1.0,0.8163892448564516,0.07736267276551904,0.03316569412922298,-0.09539127552634273],[-0.1368098563323149,0.011810914275504696,0.7776007811502121,0.9292482585265791,0.9937420194143424,0.9911042031182221,0.19235892825303325,0.7573018915506724,0.773189740929927,0.23295317332031318,0.9243841999884518,0.9188915220824492,0.32468661232524554,0.582832799507287,0.8270335696424134,0.7844868871312299,0.8028401671479567,0.8324176362131349,0.556081477469842,0.9230624199957504,0.8163892448564516,1.0,0.129066549980409,-0.03239735847465077,-0.033056943848679805],[-0.01840784367296909,-0.004493573273044055,0.14462970195325364,0.1612564466330906,0.12081159615097704,0.14270324668913895,0.01969765625700305,0.19580756359660065,0.2015287030309534,0.25886514325605187,0.08969295862403473,0.07086938716354318,0.28202797751040615,-0.07621015457810935,0.041247212176456965,0.0091334648976886,0.3193553054213916,0.20336815999120822,-0.067552954107452,0.13060691943189065,0.07736267276551904,0.129066549980409,1.0,0.4631053329955077,0.10275857581392381],[0.011473637308239996,0.020821418948473336,0.07946561390168015,0.03804638338204309,-0.032905185856826745,-0.025393105534547173,0.07034971520536534,0.04740410442389703,0.0488260976389277,0.12346595893083297,-0.06904235019387298,-0.06791570076372924,0.16063595618156504,-0.01458756540138372,-0.013224144869379919,-0.014044628702448221,-0.03745646419505955,0.1518757137801966,-0.0008026119602064526,-0.08862531923309717,0.03316569412922298,-0.03239735847465077,0.4631053329955077,1.0,0.04403323203585575],[0.5746979231775432,0.004532613961366425,-0.10225532211529424,-0.0861474745242581,-0.041260715116721636,-0.050272634042559515,0.023296066125147712,0.07881426881868812,0.08133270930182078,0.10805934819853975,-0.06000192926408283,-0.07069730147505776,0.003086615534182435,-0.08331865438809538,-0.04438357673328008,-0.0569255926690611,-0.026299353523843196,-0.08036759940552606,-0.060701130289226024,-0.084463801279757,-0.09539127552634273,-0.033056943848679805,0.10275857581392381,0.04403323203585575,1.0]],"type":"heatmap","xaxis":"x","yaxis":"y","hovertemplate":"x: %{x}<br>y: %{y}<br>color: %{z}<extra></extra>"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"xaxis":{"anchor":"y","domain":[0.0,1.0],"scaleanchor":"y","constrain":"domain"},"yaxis":{"anchor":"x","domain":[0.0,1.0],"autorange":"reversed","constrain":"domain"},"coloraxis":{"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]},"margin":{"t":60}},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('5b50d484-70af-42a6-8c4c-c964c89624f5');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>



```python
(data_per_min['MIN']>=500).mean()
```




    0.6929194956353055



### How are minutes played distributed?


```python
fig = px.histogram(x=rs_df['MIN'], histnorm='percent')
fig.show()
```


<div>                            <div id="2c007ecb-dfb2-42fe-b6c8-70ff5fc31be6" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("2c007ecb-dfb2-42fe-b6c8-70ff5fc31be6")) {                    Plotly.newPlot(                        "2c007ecb-dfb2-42fe-b6c8-70ff5fc31be6",                        [{"alignmentgroup":"True","bingroup":"x","histnorm":"percent","hovertemplate":"x=%{x}<br>percent=%{y}<extra></extra>","legendgroup":"","marker":{"color":"#636efa","pattern":{"shape":""}},"name":"","offsetgroup":"","orientation":"v","showlegend":false,"x":[3119,3013,2877,2985,2482,2861,2983,3076,3167,2790,3013,2842,2391,2907,2859,2678,2598,2253,2575,2897,2578,2926,2972,2687,2936,2174,2683,2048,2503,2687,2722,2756,2546,2289,2230,2913,2435,2903,2454,2078,2513,2335,2758,2642,2607,2757,2628,2309,2375,2581,2796,2629,2122,2379,2640,2892,2093,2685,2136,2620,2086,2307,2133,2486,2184,2807,2779,2252,2349,2403,2323,2104,1959,2559,2022,2365,2003,2016,2372,2012,2564,2313,2474,2269,1916,2530,2136,2248,1661,1726,1602,2233,1756,2285,2249,1652,2171,1876,2200,1846,2035,2170,2632,1555,2541,1560,2201,1997,1713,2464,2159,1977,2058,1709,2325,1879,2010,2259,2124,2034,2020,2151,1943,2426,1745,1659,2052,1554,2058,1775,1364,1783,1787,2010,1721,2293,1433,1264,1636,1689,2134,1393,2109,2025,1882,2239,1937,2010,1495,1363,1765,1810,2164,2278,1876,1655,2278,1837,2068,1840,1300,1817,1484,1553,1627,1219,1411,1974,1631,1663,1402,1661,2229,1941,2033,1691,1299,1524,1418,1682,1249,1421,1366,1428,1079,2066,1324,1482,1119,1521,1149,1457,1641,1288,2076,1471,1727,1423,1527,1459,1064,1078,1910,1789,967,1088,862,1243,1507,1786,1092,1239,1435,1764,2043,1669,1029,1035,1137,1188,1590,1003,1278,1709,1363,1080,1110,876,1455,682,1583,1322,1487,953,912,1111,1353,1095,1326,2186,827,1418,892,1206,997,1191,1243,902,993,1219,1967,970,1226,901,936,1075,827,1056,980,1954,618,1616,851,1175,1085,1312,1029,765,1408,1209,1134,996,894,656,963,1414,909,792,1158,900,878,920,1263,862,694,892,655,1017,1156,830,887,963,919,538,676,730,1037,803,638,924,1221,713,1061,1162,508,513,713,397,624,507,663,735,619,428,444,1209,683,489,458,625,1120,499,812,786,418,376,544,644,549,852,568,575,542,503,857,698,693,475,383,770,693,578,401,646,376,296,380,369,329,702,416,441,477,820,457,431,388,601,435,360,516,267,701,513,407,694,284,338,342,441,288,318,352,366,510,276,528,388,386,392,392,829,257,334,437,272,280,566,221,322,263,289,224,371,202,215,207,147,198,197,256,221,290,196,200,187,151,119,387,350,141,203,142,250,385,269,149,158,104,144,189,82,93,122,102,86,74,495,68,51,59,58,63,226,26,52,57,137,25,32,100,55,78,31,31,25,54,26,32,58,21,32,36,28,9,29,5,12,4,7,68,20,6,6,5,4,6,26,3122,2982,2902,2797,2863,2846,2777,3017,2898,2628,2937,2298,2499,2553,2980,3023,2668,2868,2496,2497,2531,2862,2718,2358,2805,2705,2780,2552,2482,2542,2177,2396,2330,2400,2614,2094,2531,2730,2288,2446,2530,2690,2800,2575,2728,2666,2783,2556,2171,2414,1810,1997,2457,2158,2472,2153,2072,2723,2487,2178,2619,2222,2193,2461,2752,2421,2956,2351,2655,2485,2470,2277,2141,2028,1884,1775,2214,1950,2213,2098,2820,1412,2609,2460,2057,2138,2041,2201,1973,2594,1663,1765,1939,2584,2468,2078,2282,2059,2266,2069,2016,2312,2604,2262,1850,1855,2054,1860,2159,2591,2409,1970,2870,2408,1927,1923,1550,2213,1527,1875,1618,2179,1859,1812,2341,2309,2214,1800,2409,2337,2434,2638,1856,1466,1770,1482,1416,1973,2252,2490,2157,1779,1560,2204,1833,2187,1974,2178,2240,1741,1936,1500,1667,1686,2116,1538,2360,1471,1964,1557,1662,1504,1426,2017,1974,1399,1445,1735,1820,1396,1651,1478,1346,1400,1674,1950,2040,1419,2007,1376,1707,1751,2045,1773,1257,1532,1114,1800,1490,958,987,1339,1614,2014,1077,1897,1275,1349,1797,1729,1635,982,984,1506,1214,1962,1278,1769,1553,1417,1283,1143,1054,1271,1662,1396,1312,1583,1742,866,1948,1502,831,795,1174,908,1564,1188,1428,1414,1309,912,1193,1325,736,1157,1020,1726,911,1161,1209,1049,1298,956,1584,1498,962,956,1254,533,1109,925,875,998,1089,883,1173,1231,936,984,1065,952,1016,1271,873,848,1353,870,951,818,1083,978,1141,1071,642,830,1416,1468,818,982,968,897,751,519,869,1248,741,971,1197,1007,1020,768,789,1283,664,789,578,1048,952,857,511,516,1003,1072,663,765,899,1132,1207,629,527,751,675,476,643,723,776,690,533,695,684,414,641,395,465,655,584,540,494,727,653,848,473,387,488,491,311,1007,570,591,317,265,368,606,398,393,575,804,290,482,372,388,638,633,242,378,753,489,562,392,396,429,392,488,313,442,434,313,252,392,279,339,355,390,236,270,317,180,330,270,362,248,225,238,177,327,418,319,233,215,399,250,260,377,292,180,309,198,172,322,212,148,354,251,224,251,244,224,116,126,226,184,99,165,146,75,158,162,100,185,156,187,79,100,109,155,146,186,192,80,72,142,97,172,132,79,95,59,38,33,120,34,63,92,107,38,30,85,161,55,77,17,110,47,15,160,50,62,74,42,27,34,10,10,15,19,45,30,13,1,9,12,11,7,2,10,15,3,11,24,5,9,2981,2613,2302,2493,2925,2455,2512,2455,2730,2857,2699,2356,2618,2681,2408,2529,2013,2687,2969,2837,2800,2282,1971,2690,2513,2573,2409,2640,2581,2414,2016,2100,2532,2390,2100,2280,2455,2369,2136,2228,2318,2791,2665,2304,2502,2268,2225,1726,2137,2471,1992,2119,2428,2434,2035,2227,2033,2378,2930,2587,2186,2502,2541,2301,1703,2421,2453,2670,1953,2288,2315,1428,2150,1980,2096,2107,2241,2024,1885,2312,2820,2086,1956,1841,2208,1556,2490,2087,2116,2418,1530,1874,2114,1446,2189,1914,1929,2037,2079,2045,1874,1692,1654,1675,1731,1907,2318,2018,2368,2092,1697,1681,1926,1207,1806,2046,1207,2260,1302,1902,2354,1964,1991,2286,1566,1895,1516,2271,1659,2245,2311,1587,1694,1426,2489,2381,1565,1743,2383,2193,1984,1476,1854,1661,1979,2194,1267,913,2158,1244,1319,1685,2380,1462,1916,1840,1785,1424,1675,2156,1223,1692,1398,1173,1647,1776,1462,2019,1730,1494,2069,1717,1587,1838,1416,1303,1399,1362,1505,2035,1831,1422,1388,1727,1564,1638,1142,1000,1982,1370,1411,1870,1744,1449,1192,1641,1648,1793,1771,1444,1457,1563,1123,1406,1808,1235,1717,866,1345,895,1192,1436,1573,1545,1991,1352,2049,1433,1330,1744,1487,1228,1865,982,1122,1468,1623,1286,1230,1432,957,1491,1087,1412,767,1397,1064,1518,938,1244,785,1030,1103,1274,973,1583,1348,1366,1377,678,1188,1287,984,1673,1817,1107,1324,904,1131,815,889,1091,988,1270,721,1195,1610,899,1037,1253,801,1529,790,1087,1652,892,976,831,1233,847,1047,952,1132,1380,1127,1070,1051,828,738,798,1133,951,1243,833,894,633,904,824,1194,824,976,864,1101,1197,1101,1058,1146,935,1012,995,937,830,636,657,687,669,924,1148,614,797,838,661,591,705,535,1286,568,692,982,593,713,845,781,740,505,647,736,878,504,485,672,742,502,586,492,603,613,719,683,854,631,531,795,509,600,764,397,628,416,617,683,529,527,674,555,504,410,455,423,383,383,441,493,297,327,324,344,544,430,549,411,417,321,701,281,256,352,209,332,368,259,272,486,248,540,268,236,266,244,406,299,259,159,363,358,262,261,296,338,197,164,137,215,192,126,108,240,180,174,91,123,177,255,216,219,200,194,158,270,247,101,73,122,208,119,105,198,119,286,89,90,143,271,65,128,120,75,68,93,87,128,126,76,72,74,67,123,104,72,89,86,103,56,71,51,69,66,43,23,64,36,33,23,43,23,29,18,14,7,22,36,13,43,2,14,3,7,3,6,2,19,8,3125,2700,2578,2709,2676,2750,2819,2804,2644,2666,2246,2885,2845,2780,2851,2893,2530,2784,2380,2627,2457,2424,2164,2420,2852,2258,2474,2647,2364,2823,2261,2666,2631,2255,2424,2097,2552,2566,2314,2379,2291,2037,2353,1863,2536,2379,2294,2541,2808,2856,2008,2734,2126,2513,2789,2407,1831,2097,2408,2259,2108,2448,1667,2125,2016,1721,2308,1839,2219,2047,1907,2859,1870,2363,1983,2256,1778,2703,2500,2598,2644,2280,2239,1686,1708,2362,2338,2253,2439,1591,2286,2106,2048,2394,2371,2524,2115,1621,2068,2083,2276,1682,1791,2537,1903,1761,1980,2271,1966,2219,2341,1799,1694,1915,2105,2220,1880,1667,1667,1733,2145,1646,2042,1557,1880,2323,1629,1861,2192,2152,2334,2154,2190,1464,1170,2066,2084,1965,1435,2401,1747,1863,1821,2041,1672,1662,1395,1481,1366,2046,1636,1816,2540,2004,1513,2269,1774,2098,2014,1059,1373,1936,2033,1431,1649,1367,1809,1557,1708,1464,1687,1669,1108,1615,1951,1227,1446,1800,1372,2062,1867,1255,1751,1096,1667,1932,1134,1404,1666,1181,2024,2020,1471,1505,1620,1443,1262,1482,1516,1684,1094,1536,1275,1070,1233,1095,832,1333,1114,2232,1457,1606,1108,1520,1382,1280,1386,1971,1313,1878,1758,1413,1198,1499,1326,1642,1342,1618,1178,1041,1146,1632,1412,1732,1808,1058,1263,1102,1044,1079,1599,903,1265,1199,1318,1258,1231,797,1027,1313,1326,992,960,1005,1033,807,823,1341,926,765,1451,1160,1411,710,982,861,569,1245,1266,616,835,1241,1107,1176,1035,748,1301,1553,868,880,813,1211,800,845,864,1632,1090,770,665,870,863,1316,764,1075,876,917,1055,634,762,1036,692,508,908,926,702,786,698,1174,725,930,1178,547,741,705,363,986,866,476,773,869,578,671,977,1274,547,703,1462,658,1001,647,437,654,708,470,857,600,579,857,565,526,426,721,463,480,590,370,508,615,329,573,384,380,383,470,595,471,823,461,656,379,496,631,474,496,486,460,304,397,635,432,460,699,556,429,410,262,599,362,400,291,498,403,321,343,229,196,315,399,263,542,235,205,320,395,212,305,244,279,283,305,206,277,311,251,167,225,294,144,192,225,176,147,373,145,218,249,260,159,156,204,156,112,192,156,173,143,103,169,154,107,68,199,84,72,102,73,44,82,66,95,72,50,50,43,63,57,61,93,96,55,42,42,42,35,41,36,18,21,39,45,48,19,19,15,6,24,27,6,29,24,6,43,15,6,23,6,2802,2947,2569,2708,3030,2693,2620,2639,2795,2465,3048,2475,2796,2845,2739,2809,2525,2836,2684,2689,2649,2731,2538,2516,2070,2222,2804,2459,2531,1993,2292,2485,2176,2244,2566,2076,2513,2657,2343,2335,2038,2323,2397,2164,2198,2541,2422,2234,2617,2082,2134,2154,1885,2744,2197,2083,2409,2565,1921,1792,2163,2605,2142,2223,2374,2529,2412,2129,1533,2570,2190,1786,1728,2298,2157,2199,2177,2335,2495,1811,2116,2085,2132,2066,2193,1823,2048,2773,1754,2389,2063,2029,1835,2054,1749,2556,1954,1888,2119,1955,1782,2295,1989,2254,2148,2271,2469,2459,2399,1544,1705,1551,2653,1776,2237,1765,1963,1627,1556,1778,2471,2223,1516,1424,1944,1982,1754,1955,2188,1743,1424,1593,1679,2349,2279,2003,1384,1843,1286,1754,1657,1820,2101,2045,2336,1732,1538,1753,1398,1761,1667,1391,1500,1914,1725,2058,1881,1534,1587,1368,1998,2336,1639,786,1538,1560,1421,1198,1406,1143,1140,1508,1134,1296,1324,1659,1800,1494,1271,1972,1801,1986,1477,1998,1937,2374,1013,1193,2133,1183,1643,2236,1614,1843,1700,931,1773,1227,1517,935,1137,1776,1064,883,2376,1608,1291,1333,1580,1341,1728,1419,1605,1807,1966,1229,1176,1787,1793,1392,1631,1186,739,1419,1237,1525,1197,1477,1133,1442,1614,1047,1599,1190,1596,1123,1177,1158,1001,1087,1531,1649,1237,1362,1334,1205,1501,1138,889,1268,1474,1486,1016,1068,1427,963,1228,788,1263,1055,1190,1222,1104,1298,1123,1248,1345,1330,1091,771,980,1031,1281,1028,1163,1284,1187,1642,708,1371,1283,797,981,738,1265,1065,894,960,1040,854,811,1365,842,804,808,1232,846,1333,577,977,612,703,609,653,1074,1013,696,968,841,714,442,639,538,689,1088,1020,560,843,1015,559,859,588,560,562,558,682,575,512,857,905,675,774,584,506,752,789,1030,625,293,447,642,810,557,461,973,592,525,871,555,545,386,626,558,384,462,719,777,446,479,521,234,457,574,432,416,459,539,467,299,447,381,322,381,355,408,362,397,394,264,485,214,294,381,231,405,531,371,342,346,331,471,316,285,287,385,199,308,482,165,314,277,583,198,187,249,236,220,135,157,135,237,123,205,146,174,219,238,160,189,163,195,159,125,115,170,76,81,141,118,80,107,84,71,128,80,130,114,151,79,122,110,75,62,108,53,108,93,99,85,92,40,52,31,48,134,44,35,47,31,89,47,17,24,12,40,28,25,39,13,33,22,28,9,18,13,32,23,52,7,11,25,17,10,1,43,9,3026,2551,2727,2914,2756,2670,2977,2712,2325,2589,2736,2918,2509,2552,2891,2924,2982,2638,2927,2668,1931,2504,2979,2634,1912,2443,2565,2463,1865,1631,2190,2322,2164,2078,2378,2732,2142,2683,2510,2501,2408,2154,1970,2401,1737,2116,2625,2305,2464,2465,2310,2432,2088,1887,2443,1553,1847,2024,2487,2049,2690,1651,1967,2020,2034,1909,2586,2152,1837,1959,1607,2531,2254,2306,1830,2726,1885,2311,2458,2197,2180,1727,1653,1947,1643,2029,1735,2093,2607,2231,1975,1921,2153,2579,1683,2044,2277,2423,1900,2057,2175,2310,2068,2350,2043,1616,2265,1835,1779,2041,1810,1494,1864,1508,2018,1828,1975,2026,2052,1968,2282,1789,1293,1836,1653,2107,2131,1603,1809,1410,1943,2095,2269,1785,1812,2287,2090,1760,1536,1850,1690,1816,1364,1730,2006,1234,1981,2346,1442,1391,1657,1757,1622,1337,1525,1732,2074,1647,1850,1574,1672,1406,1812,1969,2244,1433,1520,1201,1231,1743,2210,2034,2072,1536,1944,1768,1436,1686,1542,1725,1791,1894,1340,1679,1395,1441,1978,1393,1299,1421,1542,1524,1661,1365,1463,1527,1517,1646,1433,1143,1658,1244,1454,1387,1614,1615,1705,1326,2069,1680,1780,1041,1439,1643,1240,2053,1604,1421,2281,929,1461,999,1059,1119,862,1485,1707,1368,1391,1365,1333,1495,1548,1706,785,1564,1086,1371,1506,1167,1488,1108,1481,918,1134,1134,1158,1091,854,1071,1562,1467,1471,984,1359,1060,974,1486,675,656,1129,743,1206,1264,1062,1622,1209,972,1205,1145,943,863,1238,1134,1150,1170,758,1014,686,936,640,691,671,1270,1026,741,806,746,615,977,925,1072,883,742,1151,807,1353,1045,851,691,1156,1050,910,695,876,809,715,914,581,484,1013,494,835,673,918,519,338,627,778,775,961,1020,534,683,582,824,776,427,729,418,707,419,600,558,373,516,643,583,1150,428,1037,763,461,498,519,474,523,537,682,578,353,838,713,422,379,814,713,629,810,404,410,982,459,403,687,384,314,329,576,522,210,535,805,193,381,455,392,562,326,334,307,472,359,448,418,214,235,353,285,254,378,274,344,273,724,480,180,253,176,290,338,284,299,323,225,277,239,235,279,189,228,181,205,159,385,209,221,212,242,276,189,245,233,224,140,161,141,139,174,115,237,304,90,216,196,98,136,87,115,126,80,216,122,160,40,125,152,53,86,139,75,163,147,187,118,98,122,104,106,89,64,123,80,59,75,182,72,124,43,53,71,70,64,80,175,107,45,25,27,61,70,35,95,80,120,39,52,30,49,28,40,28,74,9,25,32,38,35,18,20,29,72,66,38,7,31,11,22,33,32,13,4,15,1,7,45,21,9,13,2,5,6,5,12,4,13,19,3,8,9,1,8,9,6,8,2,10,1,2,8,2867,2841,2863,3028,2838,2702,2358,2331,2545,2622,2598,2154,2687,2448,2242,2615,2652,2629,2510,2848,2688,2504,2040,2214,2232,2503,2318,1937,1993,2171,2342,2375,2573,1850,2402,2393,2546,2379,2605,2647,2447,2215,2158,2548,2059,2700,2543,2314,2577,2533,2289,2633,2455,2272,2553,2314,2150,2185,2539,2250,1828,2057,2183,1914,1974,2249,2010,2669,2158,2612,1885,2436,1935,2091,1838,2294,2489,2322,1832,2568,2444,1947,2119,1682,2293,2213,1913,2158,2166,1761,2269,2097,1842,2035,1724,2213,1973,1568,1392,1879,1639,1988,1857,1766,1671,2174,1674,1895,1607,2096,1899,2349,2022,2607,1544,2143,1970,2091,1960,1815,1863,2215,1663,1908,1893,1515,1812,1684,2004,1643,1360,1091,2292,2047,1496,2133,1686,1703,1552,1788,1639,1913,2049,1508,1802,1996,1879,1298,2164,2200,1791,1436,1402,1606,1760,2354,1245,1459,1609,1931,2417,1591,1473,1147,1745,1728,1104,1698,1258,1731,1463,1125,1795,1905,1529,2028,1437,1371,1985,1632,2802,1334,1696,2137,2041,1613,1399,1184,1722,1757,1757,1340,1330,1375,1063,1271,1120,1297,1961,1327,2063,1294,1003,983,1138,1234,1039,1715,1389,1126,1439,1931,1356,1206,1264,1059,1211,1550,1251,1481,1243,1169,1606,991,1189,1123,771,2065,1031,1502,1360,935,1470,1430,1446,1198,1352,1560,1481,1423,1203,1415,1082,1218,1396,1302,1110,1207,1231,1306,1250,1304,1247,1503,1071,1164,1179,1671,1369,1273,681,1154,1261,812,1067,829,752,1133,820,1358,755,973,1015,1578,1230,896,728,1056,908,598,795,1034,979,1064,878,1282,857,1233,1003,984,1079,972,784,1449,760,759,1120,1176,958,693,698,646,766,664,1220,789,821,721,800,812,882,679,1079,805,743,878,737,967,712,984,939,730,904,694,746,643,782,516,750,669,826,480,531,895,861,520,522,788,628,676,416,657,639,446,783,529,610,474,435,928,879,526,387,609,416,496,594,715,499,628,277,464,875,250,576,454,588,333,375,372,392,402,502,371,427,492,503,546,641,379,399,343,498,428,559,330,294,372,440,411,410,341,534,333,320,361,230,328,259,439,632,321,312,428,305,156,292,181,259,251,163,268,167,240,214,283,211,127,173,188,141,158,222,397,214,176,210,191,321,313,195,204,212,186,148,221,145,104,161,150,95,67,93,118,178,113,111,204,254,111,134,98,128,174,120,118,101,67,167,194,111,103,94,90,55,68,143,63,75,69,49,57,94,39,65,47,61,39,120,51,26,36,123,26,36,84,56,44,152,64,47,32,16,23,29,19,16,40,37,40,26,22,43,33,13,17,64,21,6,8,15,4,16,7,8,6,11,5,13,1,15,2,6,6,1,2,6,1,1,4,2483,2474,2512,1917,2120,2047,2053,2316,2364,2131,2557,2049,2265,1848,2085,2316,2103,2335,2469,2216,2110,2143,2428,2202,1994,1853,2083,2080,2208,1999,2076,1998,2074,1864,2112,1859,1749,1506,2117,1814,1834,1934,1959,2159,2417,2211,1742,2165,2098,2091,1904,1705,1634,2482,1933,1845,2008,1452,1936,1419,2333,1962,1889,1878,1754,2123,1754,1622,1780,2166,1663,1928,2017,1187,1766,1581,1646,1740,1298,1902,2017,1666,1363,1916,1996,2137,1674,1892,2016,1485,1996,1330,1654,1583,2011,1479,1817,1325,1704,2026,1576,1526,2018,1919,1852,1857,1485,1677,1693,1826,2025,1508,1787,1492,2066,1824,1786,1461,1687,1910,1782,1619,1372,1759,1579,2137,1632,1559,1300,1236,1875,1760,1681,1722,2120,1702,1363,1890,1394,2042,1913,1637,1591,1755,1444,1762,1878,1341,1730,1464,1617,1423,1209,1551,1520,1147,1826,1566,1420,1688,1594,1326,1240,1412,1780,1506,1449,1345,1291,1472,1169,1188,1271,1300,658,1196,1687,1279,1209,1332,668,1242,1547,918,1016,1634,1306,903,1255,1570,1265,1274,1375,2467,1162,1635,1452,925,1369,1232,1256,934,1641,1080,983,1020,1022,1234,1097,1326,1242,1759,1167,1266,960,2049,1246,1127,1130,922,971,1057,1307,785,1186,1492,1166,1122,986,819,1207,1342,980,1271,850,1042,1029,835,923,1330,1097,988,960,1025,777,805,1061,1269,1171,797,886,743,853,883,1045,1243,1187,1427,958,1175,867,1222,1129,1129,984,1015,878,1161,718,1250,833,1088,836,979,896,667,1072,1034,887,1287,953,876,776,422,834,744,945,663,808,776,512,668,528,709,620,495,591,767,930,774,871,915,488,820,467,754,929,520,713,903,1043,1011,684,619,590,572,687,508,450,600,609,1257,479,719,527,530,559,684,922,505,484,430,734,440,872,532,381,495,487,567,375,537,871,334,462,558,593,821,484,653,471,572,908,412,331,468,291,486,437,566,471,291,301,447,388,401,253,832,346,363,378,418,352,351,365,432,317,207,345,286,272,266,268,357,139,313,328,368,362,227,355,418,221,256,436,244,293,232,183,290,386,222,505,370,380,204,290,180,272,364,262,187,288,161,99,235,251,118,161,281,150,139,159,105,151,232,129,241,181,248,303,141,117,180,64,130,87,126,119,160,133,103,135,134,105,162,109,118,81,219,112,87,83,41,107,80,145,44,96,98,33,54,83,87,40,71,81,62,53,45,53,79,52,61,45,48,35,74,62,54,28,50,47,50,49,13,47,53,38,78,44,51,46,28,33,32,47,41,24,11,28,32,26,20,31,9,19,40,33,6,25,6,14,10,15,14,15,8,33,23,13,4,19,4,11,1,3,15,13,2152,2398,2488,2147,2262,2013,2270,2667,2290,2026,2348,2125,2034,2036,2115,1585,1886,2092,2369,1999,2383,1771,2314,2269,2364,2056,1772,2206,2511,2231,1821,1818,1689,2216,2014,1829,2053,2143,2006,1930,2433,1985,1912,1997,2200,1504,1745,1848,1600,1609,1755,2139,1907,2156,1899,1704,2187,2115,2142,2348,1898,1485,1997,1157,2262,1790,1956,2102,1580,1690,1619,1802,1968,1954,2112,1781,1327,1496,1326,1902,1697,1909,1887,1688,1932,1180,1877,1369,1560,1498,1954,1288,1652,2126,1453,1461,1659,1650,1635,1867,1757,1864,1469,1747,1196,2043,1602,1797,1853,1162,1347,1502,2183,1372,1714,1746,1835,1423,1685,1279,1244,1543,1214,1305,1259,1347,1358,1790,1544,1638,1736,1949,1354,1317,1815,1242,1433,1222,1337,1522,1778,1464,1983,1934,1902,1080,1609,2173,1748,1354,1484,1601,1581,1519,1255,1384,1511,988,1415,1112,1375,1273,1226,1648,1796,1845,2243,1455,1921,1304,1772,1499,1451,1437,1403,1324,1403,1064,1835,1455,1425,1074,1260,1426,1232,1446,1268,1007,1187,1079,1104,1162,1062,1154,2240,878,936,1196,1529,789,1334,1196,1176,1045,1263,1120,1575,955,1005,964,836,1307,1982,1223,1012,1129,1605,871,1350,836,1511,1246,880,979,1528,1068,985,1229,911,1287,1200,905,1036,861,782,1318,1425,738,1085,905,1080,1088,695,791,759,1212,900,1079,950,1216,920,1050,1039,1043,1090,725,713,846,765,1038,888,928,1341,788,674,1133,904,986,678,1139,904,1257,966,1056,645,678,766,1053,1349,723,1091,980,1547,1514,1197,932,755,715,722,907,622,737,1108,684,924,1138,972,546,750,845,869,841,906,1130,833,679,1339,800,803,607,781,1006,837,818,993,672,950,553,938,853,1298,683,1161,992,717,700,943,577,655,595,769,936,559,507,561,627,519,620,601,488,520,640,669,723,852,594,684,849,582,772,1356,438,575,433,546,499,507,670,602,274,334,551,499,464,513,523,355,258,323,271,437,420,383,474,347,271,395,310,327,450,397,316,566,415,389,493,399,279,269,276,364,258,308,369,654,320,358,210,392,297,348,346,347,205,519,215,434,445,236,238,539,172,280,189,269,447,249,194,322,233,232,177,302,235,336,281,212,305,153,218,245,432,211,157,197,179,332,165,241,247,160,192,148,138,117,182,196,283,137,161,156,226,123,299,136,121,115,85,141,87,101,98,133,93,217,152,94,98,158,93,224,84,147,74,68,92,64,125,76,84,107,79,40,84,116,50,48,75,54,88,83,45,64,27,71,99,36,32,57,56,40,38,48,82,63,61,29,36,27,75,56,35,88,56,29,26,47,56,62,39,29,63,81,12,45,33,19,3,15,16,11,11,18,49,34,6,4,12,11,3,2652,2743,2296,2731,2476,2204,2301,2345,2475,2266,2084,2047,2328,2211,2837,1889,2220,2578,2466,2422,2430,2544,2678,2366,2420,2458,2283,2417,2266,1942,2145,2083,2151,2141,2704,2462,2240,2650,2418,2524,2448,2392,2126,2141,2499,2587,2337,2543,2330,2131,1869,2207,1931,2094,2429,2694,2077,2136,2854,2138,1999,2617,2204,2375,2358,2088,1825,2059,2028,2138,2276,2331,1481,2120,2329,1665,1713,2199,1681,1780,2058,2134,2139,1976,1849,1907,2239,2318,1640,1852,1439,1404,2346,1793,2056,1981,1970,1810,1500,2162,1878,2188,1802,2644,1665,1663,1937,2317,1838,2043,2076,2296,1458,1612,2133,1578,1919,1564,1730,1728,2042,1791,1092,1657,1536,1852,1564,1675,1849,1672,1670,1824,1690,1077,2057,1924,2335,1805,1587,1541,1798,1462,1577,2005,1736,1310,1656,1056,1489,1466,1206,1984,1172,2110,1730,1444,1700,1768,1246,1600,1725,1286,1285,1398,1185,941,1712,1230,1774,1803,1691,1215,1269,1801,1886,1549,1448,1278,1367,1567,1564,1848,1050,1804,1749,1940,1875,1245,1511,1589,885,1816,1981,1334,1902,1437,1223,1437,1176,2406,1307,960,1216,1164,1372,1245,1866,1146,1235,1981,1279,1361,1162,1476,1999,975,1372,1600,1484,1596,1396,1881,1414,1248,1177,1346,1012,1732,1463,1402,1185,1793,944,968,924,1519,1074,1257,1233,1212,1017,948,1647,839,1179,1038,970,1418,1001,1142,1085,948,717,1065,1209,1148,1450,1126,936,1088,974,1480,1021,1406,992,977,814,1015,1005,1685,971,1353,1087,764,878,869,1072,908,958,799,729,1292,1329,593,896,760,1453,895,1191,801,1174,957,737,1253,864,1184,834,830,1122,845,1040,1094,1039,714,736,806,636,536,640,1098,1147,706,994,541,883,844,965,810,899,1026,987,1055,905,786,775,754,698,980,696,589,716,612,701,1002,727,991,685,620,609,902,652,946,607,685,640,771,502,864,441,506,536,668,604,622,639,652,696,439,465,391,609,906,574,360,766,537,823,690,389,698,333,463,566,316,502,450,344,473,709,549,445,298,360,460,628,423,498,371,346,407,421,422,549,367,469,304,341,359,355,267,516,545,360,445,338,298,411,434,177,603,383,461,303,376,459,359,336,341,240,316,378,173,128,406,340,462,181,349,222,187,555,265,372,153,213,562,320,231,281,199,220,195,197,304,261,244,195,186,212,168,222,240,372,262,200,158,176,205,134,206,137,188,112,155,120,200,145,171,176,241,121,148,239,121,104,120,174,163,74,167,166,208,43,129,145,183,81,65,120,83,104,156,178,54,103,73,85,56,201,51,65,91,58,43,79,63,82,60,119,63,71,74,44,108,108,56,39,35,91,75,76,36,63,74,46,39,107,38,16,44,128,52,71,69,31,59,31,50,27,21,24,8,139,18,42,39,19,16,19,7,11,30,31,19,44,15,19,39,23,22,21,37,15,18,23,27,11,5,11,17,1,9,6,12,16,2,20,10,3,19,7,1,8,5,2,13,2,1,18,8,11,3,3,20,7,8,2,6,8,2,2,1,17,2,5],"xaxis":"x","yaxis":"y","type":"histogram"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"xaxis":{"anchor":"y","domain":[0.0,1.0],"title":{"text":"x"}},"yaxis":{"anchor":"x","domain":[0.0,1.0],"title":{"text":"percent"}},"legend":{"tracegroupgap":0},"margin":{"t":60},"barmode":"relative"},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('2c007ecb-dfb2-42fe-b6c8-70ff5fc31be6');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>



```python
fig = px.histogram(x=playoffs_df['MIN'], histnorm='percent')
fig.show()
```


<div>                            <div id="02bd9691-4f38-4354-99ce-10b253f3aa95" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("02bd9691-4f38-4354-99ce-10b253f3aa95")) {                    Plotly.newPlot(                        "02bd9691-4f38-4354-99ce-10b253f3aa95",                        [{"alignmentgroup":"True","bingroup":"x","histnorm":"percent","hovertemplate":"x=%{x}<br>percent=%{y}<extra></extra>","legendgroup":"","marker":{"color":"#636efa","pattern":{"shape":""}},"name":"","offsetgroup":"","orientation":"v","showlegend":false,"x":[960,765,735,780,782,481,485,694,689,775,497,751,685,554,609,575,560,573,669,650,426,431,404,461,495,673,454,490,243,351,263,323,422,368,292,390,246,366,320,224,325,357,409,418,303,236,258,388,255,337,357,238,243,454,271,392,199,218,316,261,327,154,243,267,213,158,206,241,212,208,138,189,205,162,200,223,253,224,225,126,350,273,146,161,164,300,177,161,192,175,232,152,146,105,178,133,136,145,91,230,68,76,117,114,120,162,112,113,105,191,204,97,115,93,80,108,136,209,83,67,65,107,79,150,69,101,75,114,30,68,130,61,68,134,210,144,100,53,59,59,84,50,47,71,84,59,33,82,48,20,39,33,31,68,247,37,31,72,28,22,45,33,10,23,68,54,40,35,17,20,39,71,33,14,20,5,28,48,19,20,7,9,20,14,36,6,8,26,18,11,13,16,3,9,17,22,6,2,11,24,2,23,1,5,4,8,3,31,2,815,763,735,781,719,752,693,586,736,478,686,441,687,705,472,469,466,687,529,604,458,531,581,313,527,420,542,428,351,516,351,282,459,368,263,296,426,231,407,271,382,249,325,267,242,263,535,442,356,404,299,250,325,257,419,267,249,243,367,234,342,220,217,319,250,248,317,404,154,190,230,228,250,176,153,191,172,200,299,199,191,261,190,224,331,177,218,141,163,146,246,384,124,187,193,133,118,106,236,115,156,167,126,210,202,173,158,121,87,154,138,104,81,108,68,84,195,81,100,169,149,119,70,241,57,202,82,163,158,134,146,91,90,183,101,135,122,68,146,88,136,144,114,170,113,81,28,70,45,59,65,55,41,77,23,45,36,29,45,23,48,53,81,17,14,15,22,29,21,38,25,7,9,19,24,15,15,46,9,3,6,5,4,24,9,6,8,3,14,7,7,3,6,26,9,5,4,5,8,10,1,15,7,844,826,636,761,557,784,574,506,529,445,464,454,566,418,558,522,560,396,655,681,635,416,529,540,727,428,482,695,379,401,382,487,526,367,298,290,317,497,250,389,197,172,250,307,273,234,250,243,208,201,409,181,375,229,331,249,298,232,440,276,311,303,166,198,159,257,175,210,218,143,153,191,192,209,112,183,119,201,395,196,178,142,279,116,164,199,190,206,154,204,127,107,150,131,132,156,153,293,142,102,160,172,133,80,131,112,106,100,95,140,118,102,144,106,107,110,125,129,75,120,90,106,99,127,67,106,90,72,126,43,101,124,107,126,117,74,123,57,75,86,55,37,31,53,51,38,49,49,22,68,36,39,37,55,21,33,40,37,65,10,16,79,26,10,43,13,12,10,36,60,10,9,2,16,48,18,14,12,10,9,14,7,11,21,16,12,8,12,5,4,25,4,13,3,2,2,5,3,4,1,12,5,7,16,5,7,3,3,849,822,774,726,674,614,746,766,879,473,613,437,730,472,442,339,337,743,602,767,514,275,495,553,596,452,323,492,365,321,372,260,583,491,220,279,622,327,201,193,254,335,506,272,291,325,191,237,381,302,199,264,316,170,365,471,125,235,168,203,387,330,189,267,166,225,214,241,306,234,172,193,197,144,198,367,206,131,192,180,154,167,161,173,144,205,159,161,127,257,137,203,218,176,156,172,197,144,147,162,198,95,80,120,134,190,159,95,91,98,125,139,110,190,121,134,76,56,228,124,181,112,81,81,82,98,94,129,140,72,113,100,42,92,64,67,99,110,77,129,77,49,61,85,93,68,87,76,89,33,64,53,38,50,19,38,74,77,79,49,76,32,41,33,22,12,26,44,35,20,46,10,4,34,78,79,36,43,55,51,8,8,10,11,55,20,51,29,54,38,27,22,41,26,14,10,43,2,10,12,10,2,32,10,2,18,7,6,7,1,15,12,12,26,6,744,601,653,533,507,521,429,505,407,578,645,610,411,537,596,596,373,593,194,260,346,416,306,428,373,538,243,211,224,562,219,487,307,358,326,272,239,211,300,281,436,365,325,413,286,240,419,264,226,172,151,219,264,284,326,409,227,246,336,277,192,277,149,140,190,161,154,196,231,215,225,195,212,141,191,262,200,212,221,162,275,220,333,184,142,187,206,107,203,168,99,245,181,185,150,185,179,195,183,155,181,224,162,157,159,251,118,113,157,140,111,98,159,97,118,136,128,133,155,124,121,157,119,127,178,142,112,95,116,185,84,78,82,59,99,47,75,22,92,66,80,90,45,90,56,67,60,106,92,76,38,101,73,82,100,48,81,33,52,31,39,68,29,63,26,53,17,29,53,26,61,31,68,3,36,21,11,24,10,16,15,10,7,22,21,21,25,21,17,12,6,9,18,4,12,5,7,27,7,4,30,10,17,31,12,9,19,11,5,10,3,10,11,10,20,922,807,621,794,555,683,583,517,660,696,679,358,411,549,562,354,819,520,348,706,342,505,280,235,557,361,275,329,278,523,369,382,261,234,569,582,251,449,244,383,362,216,320,273,401,176,416,389,323,272,286,284,155,227,307,225,233,156,302,260,286,238,166,196,260,215,387,158,181,127,120,175,281,164,214,170,238,237,259,170,162,149,194,119,190,167,131,165,179,153,126,146,200,161,186,160,175,123,181,148,155,105,160,206,114,158,140,125,94,107,162,133,130,114,173,154,81,96,101,151,143,114,130,67,230,107,79,123,52,90,96,87,70,73,94,77,149,29,110,104,47,103,72,74,79,15,95,134,64,77,54,82,70,26,53,59,62,23,33,54,78,40,71,35,66,48,29,33,8,58,18,13,60,8,44,17,23,3,11,48,16,55,19,8,2,19,6,5,6,21,6,6,16,19,2,6,14,24,3,3,3,4,2,2,3,3,3,11,4,6,939,846,891,818,650,635,442,514,900,556,424,508,850,515,421,735,500,334,629,423,469,517,410,592,330,397,443,461,395,438,421,684,375,373,251,366,431,204,244,295,388,298,176,328,310,274,426,254,201,399,197,281,158,275,331,193,191,144,272,148,324,330,198,326,322,267,170,232,173,178,168,164,212,224,215,131,148,193,108,151,235,141,146,105,141,218,175,133,84,133,103,195,159,176,162,127,130,193,147,152,110,62,137,179,177,58,117,174,162,149,245,130,106,131,90,97,126,152,141,96,121,119,137,92,151,110,131,85,109,119,53,92,52,68,128,81,56,60,28,75,60,55,67,69,40,39,115,43,36,59,46,79,41,79,52,63,15,57,19,36,35,42,82,57,17,18,30,14,27,22,20,14,28,32,79,13,29,21,13,4,18,20,14,15,49,12,42,28,22,12,15,2,13,11,8,15,5,4,28,5,20,11,10,2,6,4,5,10,2,12,8,6,769,762,753,806,694,690,672,511,448,687,707,628,553,479,264,660,648,600,277,608,653,430,451,484,410,355,413,418,215,406,525,341,251,328,388,482,459,261,273,395,262,185,341,510,243,379,258,386,227,145,320,270,200,196,393,279,204,212,267,282,379,279,165,143,268,414,239,160,376,273,135,140,156,410,222,173,176,175,156,246,161,94,210,123,243,144,128,165,228,171,234,131,146,149,119,191,147,170,114,126,211,179,93,157,102,166,137,153,149,170,126,207,130,84,95,82,135,132,203,171,249,125,144,119,106,72,72,84,131,128,82,89,65,68,97,58,97,122,53,76,75,50,21,28,53,30,39,41,31,55,39,17,34,25,24,20,27,42,38,54,86,46,23,10,48,43,26,16,8,20,75,14,28,41,21,20,21,42,11,25,9,9,16,17,27,4,40,5,6,24,5,12,20,3,4,7,7,6,9,13,0,3,3,2,2,0,31,2,6,2,3,7,4,2,4,0,2,800,888,922,776,603,485,912,683,801,622,432,346,357,667,345,438,598,576,281,707,729,604,442,381,248,418,325,390,558,298,322,569,366,332,443,376,546,185,555,203,195,378,402,224,277,286,434,273,175,240,404,262,306,299,318,301,216,681,175,277,186,270,305,233,176,180,183,144,266,196,195,219,323,173,167,157,166,143,173,271,162,128,137,117,147,220,136,117,154,109,199,149,205,114,228,220,152,190,58,121,132,92,206,148,83,166,83,105,162,142,112,100,93,107,91,129,106,145,187,73,93,109,121,129,111,59,94,103,110,116,119,65,112,83,146,130,77,99,88,48,57,138,39,92,68,42,52,46,96,30,46,57,67,145,69,75,22,71,31,47,63,50,18,21,56,36,18,38,40,45,23,70,34,17,25,16,35,12,36,12,18,22,15,33,34,7,10,5,19,15,14,18,9,30,66,29,10,3,17,14,11,6,10,15,5,9,5,9,4,4,15,1,18,13,3,2,12,17,12,33,2,6,8,4,4,10,5,8,3,4,3,6,6,7,6,41,19,1,1,983,764,920,552,629,792,629,448,605,767,760,815,614,501,485,338,385,397,366,463,448,428,479,688,654,466,585,523,707,381,332,703,500,236,335,368,457,171,230,227,296,423,509,320,260,234,222,394,298,332,448,383,318,309,262,214,175,170,176,203,217,319,371,305,181,199,175,170,138,133,203,295,187,153,209,345,192,159,196,221,197,156,160,200,172,168,130,194,226,167,158,153,249,198,132,107,139,170,130,140,130,174,172,57,138,192,112,119,133,117,122,87,154,140,150,98,79,98,137,105,139,188,83,129,124,37,83,120,65,71,61,137,112,108,113,86,38,72,60,54,114,125,126,121,9,20,108,86,76,69,87,69,59,113,63,56,60,56,30,26,24,52,37,61,65,49,26,31,8,31,56,22,25,24,16,8,22,72,19,13,12,76,15,17,5,15,20,22,9,6,40,8,7,20,38,10,10,9,12,3,19,9,2,15,5,8,0,0,13,2,9,5,2,7,36,3,6],"xaxis":"x","yaxis":"y","type":"histogram"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"xaxis":{"anchor":"y","domain":[0.0,1.0],"title":{"text":"x"}},"yaxis":{"anchor":"x","domain":[0.0,1.0],"title":{"text":"percent"}},"legend":{"tracegroupgap":0},"margin":{"t":60},"barmode":"relative"},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('02bd9691-4f38-4354-99ce-10b253f3aa95');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>



```python
def hist_data(df=rs_df, min_MIN=0, min_GP=0):
    return df.loc[(df['MIN']>=min_MIN) & (df['GP']>=min_GP), 'MIN']/\
    df.loc[(df['MIN']>=min_MIN) & (df['GP']>=min_GP), 'GP']
```


```python
fig = go.Figure()
fig.add_trace(go.Histogram(x=hist_data(rs_df,50,5), histnorm='percent', name='RS', xbins={'start':0,'end':45,'size':1}))
fig.add_trace(go.Histogram(x=hist_data(playoffs_df,5,1), histnorm='percent', name='Playoffs', xbins={'start':0,'end':45,'size':1}))

fig.update_layout(barmode='overlay')
fig.update_traces(opacity=0.5)
fig.show()
```


<div>                            <div id="3d29d914-624e-457e-a64e-cdcedcea8d43" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("3d29d914-624e-457e-a64e-cdcedcea8d43")) {                    Plotly.newPlot(                        "3d29d914-624e-457e-a64e-cdcedcea8d43",                        [{"histnorm":"percent","name":"RS","x":[38.50617283950617,38.62820512820513,37.85526315789474,38.26923076923077,37.04477611940298,34.890243902439025,38.243589743589745,37.51219512195122,38.6219512195122,37.7027027027027,36.74390243902439,36.43589743589744,34.65217391304348,36.79746835443038,34.86585365853659,33.475,32.475,30.445945945945947,33.44155844155844,36.2125,33.05128205128205,37.51282051282051,37.620253164556964,35.82666666666667,35.80487804878049,32.93939393939394,35.30263157894737,34.71186440677966,30.901234567901234,33.17283950617284,35.81578947368421,37.24324324324324,32.22784810126582,30.52,29.342105263157894,35.52439024390244,33.35616438356164,38.70666666666666,33.16216216216216,30.115942028985508,34.42465753424658,33.357142857142854,36.28947368421053,36.69444444444444,34.30263157894737,34.4625,32.85,32.521126760563384,30.44871794871795,33.51948051948052,34.95,34.5921052631579,26.860759493670887,30.5,32.19512195121951,35.26829268292683,25.839506172839506,34.42307692307692,27.74025974025974,34.473684210526315,25.4390243902439,36.046875,31.36764705882353,31.075,26.634146341463413,38.45205479452055,34.7375,27.80246913580247,29.734177215189874,34.82608695652174,29.0375,29.22222222222222,31.596774193548388,33.23376623376623,29.735294117647058,31.533333333333335,24.426829268292682,31.015384615384615,29.28395061728395,27.561643835616437,31.26829268292683,34.01470588235294,30.170731707317074,28.72151898734177,24.564102564102566,33.733333333333334,26.048780487804876,28.1,31.339622641509433,23.97222222222222,32.69387755102041,27.23170731707317,28.78688524590164,27.865853658536587,27.426829268292682,27.081967213114755,28.56578947368421,23.160493827160494,28.94736842105263,28.84375,25.759493670886076,27.468354430379748,32.09756097560975,18.963414634146343,30.98780487804878,20.8,27.5125,24.65432098765432,23.14864864864865,30.048780487804876,29.575342465753426,35.30357142857143,25.725,24.414285714285715,28.703703703703702,24.08974358974359,30.0,30.527027027027028,26.88607594936709,31.78125,29.705882352941178,26.23170731707317,25.906666666666666,36.75757575757576,31.160714285714285,27.19672131147541,25.974683544303797,20.72,25.40740740740741,25.0,20.984615384615385,22.569620253164558,23.207792207792206,24.51219512195122,21.78481012658228,27.963414634146343,18.139240506329113,30.095238095238095,21.526315789473685,25.208955223880597,26.024390243902438,23.216666666666665,26.696202531645568,25.96153846153846,25.78082191780822,27.641975308641975,27.281690140845072,25.125,23.0,20.651515151515152,22.0625,31.20689655172414,32.78787878787879,29.205128205128204,30.75409836065574,33.775510204081634,29.973684210526315,22.402439024390244,26.857142857142858,23.896103896103895,16.455696202531644,22.432098765432098,21.823529411764707,20.43421052631579,32.54,18.753846153846155,23.915254237288135,25.973684210526315,20.135802469135804,21.32051282051282,23.76271186440678,21.294871794871796,27.51851851851852,24.884615384615383,26.4025974025974,29.666666666666668,23.618181818181817,19.792207792207794,30.82608695652174,22.426666666666666,16.653333333333332,24.5,16.864197530864196,26.943396226415093,25.093023255813954,27.18421052631579,16.974358974358974,23.903225806451612,28.692307692307693,19.0125,17.953125,22.075757575757574,20.25925925925926,18.140845070422536,30.08695652173913,26.267857142857142,23.65753424657534,37.44736842105263,21.208333333333332,22.446153846153845,31.294117647058822,15.4,24.17721518987342,24.84722222222222,14.014492753623188,21.76,15.392857142857142,20.716666666666665,19.571428571428573,24.805555555555557,15.826086956521738,16.972602739726028,28.7,29.4,26.88157894736842,21.126582278481013,18.70909090909091,15.0,17.765625,16.5,19.875,28.65714285714286,22.42105263157895,22.786666666666665,23.10169491525424,18.0,15.857142857142858,17.176470588235293,22.045454545454547,23.517241379310345,19.54320987654321,16.525,22.19402985074627,19.06,12.493150684931507,16.833333333333332,17.346153846153847,17.950819672131146,22.862068965517242,27.325,13.126984126984127,23.24590163934426,18.20408163265306,17.47826086956522,18.81132075471698,18.323076923076922,21.06779661016949,14.78688524590164,14.185714285714285,17.666666666666668,24.5875,16.440677966101696,16.13157894736842,36.04,28.363636363636363,19.545454545454547,13.126984126984127,15.085714285714285,16.610169491525422,25.05128205128205,34.333333333333336,19.70731707317073,13.950819672131148,26.11111111111111,18.389830508474578,17.263157894736842,17.74137931034483,16.27659574468085,19.027027027027028,15.907894736842104,21.807692307692307,22.133333333333333,12.246575342465754,11.310344827586206,15.046875,18.85333333333333,13.367647058823529,14.4,20.678571428571427,15.254237288135593,16.25925925925926,12.777777777777779,16.192307692307693,19.155555555555555,16.926829268292682,19.822222222222223,16.794871794871796,13.038461538461538,22.666666666666668,13.60655737704918,18.479166666666668,15.53225806451613,19.97826086956522,12.227272727272727,12.290909090909091,11.774193548387096,20.333333333333332,12.746031746031745,11.192982456140351,16.210526315789473,18.5,17.390243902439025,13.430379746835444,19.049180327868854,22.08695652173913,12.512195121951219,13.711538461538462,9.925,14.857142857142858,15.84375,11.05,13.363636363636363,12.137254901960784,11.263157894736842,11.68421052631579,16.33783783783784,14.229166666666666,17.464285714285715,15.793103448275861,12.5,14.35897435897436,9.415094339622641,16.571428571428573,24.5625,19.0,9.4,14.702702702702704,17.88888888888889,12.2,14.2,10.142857142857142,17.424242424242426,11.53191489361702,11.69767441860465,17.14,13.169811320754716,11.0,17.59259259259259,9.341463414634147,11.666666666666666,12.375,12.297872340425531,10.282051282051283,10.94915254237288,18.8,14.095238095238095,9.5,9.972972972972974,8.435897435897436,14.625,13.419354838709678,9.0,9.352941176470589,17.82608695652174,9.934782608695652,23.944444444444443,13.857142857142858,11.784313725490197,7.631578947368421,13.846153846153847,9.923076923076923,4.377049180327869,10.784615384615385,12.214285714285714,9.926829268292684,13.346153846153847,9.466666666666667,11.655172413793103,11.793103448275861,7.47457627118644,7.2,13.25,11.35483870967742,8.926829268292684,13.076923076923077,14.526315789473685,13.538461538461538,8.622222222222222,20.31578947368421,8.166666666666666,10.051282051282051,17.270833333333332,14.277777777777779,10.4375,15.068965517241379,7.771428571428571,7.368421052631579,9.129032258064516,5.815789473684211,10.733333333333333,11.434782608695652,18.0625,8.96,9.512820512820513,7.481481481481482,5.8108108108108105,18.818181818181817,6.391304347826087,12.375,10.368421052631579,18.285714285714285,5.815789473684211,7.435897435897436,10.88888888888889,7.142857142857143,6.678571428571429,9.4375,11.9,14.884615384615385,9.210526315789474,8.8125,6.34375,15.777777777777779,10.416666666666666,10.131578947368421,12.227272727272727,7.842105263157895,13.166666666666666,8.0,5.76,17.181818181818183,11.714285714285714,4.894736842105263,24.4,12.75,7.166666666666667,14.8,9.339622641509434,3.238095238095238,7.285714285714286,5.9,3.625,10.5,10.272727272727273,3.0588235294117645,4.75,6.85,7.142857142857143,3.9285714285714284,11.142857142857142,5.4,4.461538461538462,5.666666666666667,38.54320987654321,38.72727272727273,37.688311688311686,36.324675324675326,35.7875,36.48717948717949,38.04109589041096,38.18987341772152,36.225,32.85,35.81707317073171,32.36619718309859,36.21739130434783,34.97260273972603,36.34146341463415,36.86585365853659,35.10526315789474,35.407407407407405,35.15492957746479,34.68055555555556,34.67123287671233,36.22784810126582,34.40506329113924,35.19402985074627,34.207317073170735,34.24050632911393,33.90243902439025,34.95890410958904,33.54054054054054,32.177215189873415,32.01470588235294,33.74647887323944,28.414634146341463,33.333333333333336,35.80821917808219,30.347826086956523,32.037974683544306,35.45454545454545,33.15942028985507,33.50684931506849,34.657534246575345,32.80487804878049,36.36363636363637,32.59493670886076,34.1,32.91358024691358,37.608108108108105,33.1948051948052,35.016129032258064,34.48571428571429,28.28125,29.36764705882353,30.333333333333332,29.16216216216216,30.9,26.580246913580247,29.6,35.36363636363637,31.0875,27.225,32.333333333333336,35.83870967741935,28.115384615384617,31.961038961038962,35.282051282051285,32.71621621621622,36.048780487804876,28.670731707317074,32.77777777777778,30.679012345679013,30.875,28.4625,28.17105263157895,28.166666666666668,31.4,32.870370370370374,26.674698795180724,26.71232876712329,35.12698412698413,27.973333333333333,35.25,30.695652173913043,32.20987654320987,30.0,32.140625,26.725,27.58108108108108,30.15068493150685,24.358024691358025,31.634146341463413,30.796296296296298,24.51388888888889,27.309859154929576,31.51219512195122,30.469135802469136,27.342105263157894,28.17283950617284,32.171875,27.634146341463413,25.8625,25.2,28.195121951219512,31.75609756097561,32.31428571428572,30.327868852459016,30.916666666666668,28.929577464788732,22.962962962962962,26.65432098765432,38.67164179104478,29.74074074074074,33.389830508474574,35.0,33.91549295774648,31.080645161290324,29.136363636363637,22.794117647058822,26.98780487804878,18.85185185185185,23.14814814814815,22.164383561643834,32.044117647058826,26.942028985507246,31.789473684210527,32.06849315068493,28.8625,28.753246753246753,21.951219512195124,31.69736842105263,28.5,32.026315789473685,32.170731707317074,26.514285714285716,22.553846153846155,21.585365853658537,18.525,32.93023255813954,24.974683544303797,28.15,30.74074074074074,27.653846153846153,22.518987341772153,29.433962264150942,28.256410256410255,24.77027027027027,26.670731707317074,24.9873417721519,29.835616438356166,28.354430379746834,24.180555555555557,26.52054794520548,20.833333333333332,23.15277777777778,23.416666666666668,28.986301369863014,19.71794871794872,30.256410256410255,18.620253164556964,24.55,21.625,24.441176470588236,19.789473684210527,18.763157894736842,31.03076923076923,25.973684210526315,17.0609756097561,24.083333333333332,27.53968253968254,23.333333333333332,19.38888888888889,24.279411764705884,26.87272727272727,25.884615384615383,20.0,25.363636363636363,24.375,32.38095238095238,25.339285714285715,24.475609756097562,19.942028985507246,20.817073170731707,31.267857142857142,25.5625,22.73076923076923,29.928571428571427,23.56923076923077,21.423076923076923,27.692307692307693,20.410958904109588,33.03448275862069,28.2,19.405797101449274,20.175,24.5609756097561,18.56896551724138,24.636363636363637,18.214285714285715,16.8625,21.914634146341463,23.364864864864863,20.185185185185187,12.430379746835444,19.294117647058822,19.063291139240505,15.564102564102564,26.513513513513512,23.236363636363638,26.402985074626866,21.569444444444443,17.28048780487805,18.070422535211268,33.61764705882353,18.821428571428573,21.54237288135593,30.21818181818182,19.38888888888889,22.23728813559322,19.7875,22.623376623376622,19.681818181818183,25.63157894736842,24.225806451612904,15.10909090909091,36.13636363636363,15.447368421052632,21.11627906976744,28.962962962962962,17.217391304347824,17.62962962962963,19.36986301369863,22.56896551724138,22.24390243902439,18.936507936507937,25.0,18.871794871794872,17.26865671641791,17.0,22.128205128205128,13.597014925373134,17.073529411764707,18.318181818181817,14.985714285714286,20.28125,18.384615384615383,25.9672131147541,27.236363636363638,18.150943396226417,15.174603174603174,16.076923076923077,31.352941176470587,20.537037037037038,18.5,19.02173913043478,33.266666666666666,16.753846153846155,20.068181818181817,16.52112676056338,15.987012987012987,13.764705882352942,14.470588235294118,16.904761904761905,15.35483870967742,20.73469387755102,17.65277777777778,12.471428571428572,20.682926829268293,16.703703703703702,14.745762711864407,16.982142857142858,20.45,19.69090909090909,15.28125,18.704918032786885,16.476923076923075,13.10204081632653,26.774193548387096,24.413793103448278,20.10958904109589,13.633333333333333,16.93103448275862,20.166666666666668,19.933333333333334,18.317073170731707,10.591836734693878,15.8,16.207792207792206,11.578125,16.183333333333334,14.777777777777779,14.385714285714286,15.692307692307692,14.222222222222221,15.173076923076923,19.439393939393938,10.53968253968254,19.725,10.90566037735849,14.76056338028169,13.04109589041096,19.044444444444444,15.029411764705882,19.846153846153847,15.671875,13.922077922077921,12.75,12.338709677419354,16.64814814814815,15.093333333333334,19.467741935483872,24.192307692307693,12.255813953488373,20.86111111111111,13.235294117647058,12.526315789473685,15.682926829268293,16.066666666666666,14.37037037037037,11.311475409836065,10.25,13.11320754716981,11.793103448275861,9.2,13.081632653061224,17.954545454545453,9.6875,12.358490566037736,25.391304347826086,10.0,10.51063829787234,13.98076923076923,14.195652173913043,13.46031746031746,17.51851851851852,9.439024390243903,13.18918918918919,9.264150943396226,31.1,18.30909090909091,16.285714285714285,14.071428571428571,9.057142857142857,6.463414634146342,18.4,19.548387096774192,9.707317073170731,8.733333333333333,11.27450980392157,19.142857142857142,7.837837837837838,7.901639344262295,7.294117647058823,13.379310344827585,8.506666666666666,19.78125,8.344827586206897,7.56,12.344262295081966,10.1875,7.025,10.31578947368421,9.209302325581396,16.5,8.166666666666666,14.352941176470589,11.592592592592593,11.05,9.644444444444444,20.866666666666667,11.454545454545455,8.71111111111111,14.68421052631579,14.125,8.875,12.580645161290322,11.8,18.0,9.90625,9.0,7.173913043478261,11.73913043478261,8.619047619047619,11.272727272727273,11.25,7.0,29.5,10.548387096774194,11.0,8.621621621621621,12.944444444444445,10.75,9.975,10.0,10.4,12.161290322580646,9.419354838709678,20.0,16.263157894736842,6.387096774193548,7.478260869565218,10.733333333333333,9.217391304347826,6.7272727272727275,9.567567567567568,11.409090909090908,8.615384615384615,8.655172413793103,16.266666666666666,9.333333333333334,12.88888888888889,15.75,8.071428571428571,8.761904761904763,3.5357142857142856,12.692307692307692,10.428571428571429,15.0,12.153846153846153,7.714285714285714,9.090909090909092,9.736842105263158,7.090909090909091,15.583333333333334,15.8,6.666666666666667,9.909090909090908,5.961538461538462,4.866666666666666,5.636363636363637,8.347826086956522,6.153846153846154,9.0,5.916666666666667,6.466666666666667,7.818181818181818,9.428571428571429,3.761904761904762,6.785714285714286,2.95,5.714285714285714,7.875,4.380952380952381,11.88888888888889,7.7272727272727275,6.708333333333333,9.166666666666666,7.0,13.75,6.666666666666667,10.0,2.5833333333333335,5.285714285714286,36.80246913580247,32.6625,34.35820895522388,36.130434782608695,35.670731707317074,31.883116883116884,35.38028169014085,36.10294117647059,36.4,34.84146341463415,33.7375,35.16417910447761,34.44736842105263,34.37179487179487,35.411764705882355,34.17567567567568,34.11864406779661,33.17283950617284,36.207317073170735,35.91139240506329,34.5679012345679,29.636363636363637,31.79032258064516,34.050632911392405,38.66153846153846,35.736111111111114,30.884615384615383,33.84615384615385,31.475609756097562,34.48571428571429,25.2,29.166666666666668,33.76,32.73972602739726,35.0,30.81081081081081,31.474358974358974,34.838235294117645,28.48,30.52054794520548,30.5,34.8875,35.53333333333333,32.45070422535211,30.51219512195122,29.454545454545453,31.785714285714285,25.761194029850746,30.971014492753625,31.67948717948718,30.646153846153847,34.17741935483871,31.532467532467532,32.026315789473685,32.301587301587304,28.92207792207792,31.765625,30.10126582278481,35.73170731707317,31.548780487804876,33.121212121212125,32.07692307692308,31.37037037037037,27.72289156626506,26.609375,33.625,29.914634146341463,32.5609756097561,28.720588235294116,30.105263157894736,28.9375,35.7,32.57575757575758,29.11764705882353,26.2,33.44444444444444,28.0125,33.733333333333334,22.98780487804878,28.54320987654321,34.390243902439025,27.813333333333333,27.942857142857143,26.3,27.6,35.36363636363637,31.518987341772153,26.0875,33.0625,32.24,30.0,26.3943661971831,31.08823529411765,19.54054054054054,31.271428571428572,26.21917808219178,23.524390243902438,28.690140845070424,29.7,25.246913580246915,26.771428571428572,23.830985915492956,20.170731707317074,27.459016393442624,21.109756097560975,25.77027027027027,28.26829268292683,33.08196721311475,29.6,25.51219512195122,23.901408450704224,24.014285714285716,25.342105263157894,15.881578947368421,24.405405405405407,25.25925925925926,34.48571428571429,27.5609756097561,33.38461538461539,24.7012987012987,30.571428571428573,23.951219512195124,24.28048780487805,30.48,27.0,28.71212121212121,19.68831168831169,29.88157894736842,20.48148148148148,29.539473684210527,30.813333333333333,22.67142857142857,25.28358208955224,24.16949152542373,30.353658536585368,29.036585365853657,34.77777777777778,21.25609756097561,30.55128205128205,30.041095890410958,24.493827160493826,25.016949152542374,23.76923076923077,28.637931034482758,26.386666666666667,26.75609756097561,29.46511627906977,33.81481481481482,26.317073170731707,21.084745762711865,22.74137931034483,22.17105263157895,33.521126760563384,24.366666666666667,28.597014925373134,23.29113924050633,21.76829268292683,22.25,25.76923076923077,26.617283950617285,29.829268292682926,27.29032258064516,18.89189189189189,28.609756097560975,20.085365853658537,25.014084507042252,19.756756756756758,29.691176470588236,23.698630136986303,18.911392405063292,26.87012987012987,22.2987012987013,28.854545454545455,29.174603174603174,21.134328358208954,32.575,19.164383561643834,17.68831168831169,20.066666666666666,26.08974358974359,24.413333333333334,24.94736842105263,22.387096774193548,30.839285714285715,19.79746835443038,27.76271186440678,23.791666666666668,23.80952380952381,26.07894736842105,19.571428571428573,19.328767123287673,24.933333333333334,23.56756756756757,19.32,22.074074074074073,21.31168831168831,26.158730158730158,23.906666666666666,25.3,18.27848101265823,32.37777777777778,20.56578947368421,16.514705882352942,22.317460317460316,26.98507462686567,15.632911392405063,23.84722222222222,22.789473684210527,21.015625,29.833333333333332,17.02857142857143,21.11764705882353,25.78688524590164,24.919354838709676,24.580246913580247,21.806451612903224,30.582089552238806,18.855263157894736,18.47222222222222,21.8,23.983870967741936,18.328358208955223,24.539473684210527,14.878787878787879,16.02857142857143,18.82051282051282,20.807692307692307,19.19402985074627,16.4,19.35135135135135,14.073529411764707,24.048387096774192,21.74,19.61111111111111,18.261904761904763,24.086206896551722,21.28,22.0,19.95744680851064,16.81081081081081,27.06896551724138,19.807692307692307,17.79032258064516,17.45205479452055,15.693548387096774,23.62686567164179,16.641975308641975,18.45945945945946,21.184615384615384,10.59375,18.5625,18.926470588235293,16.96551724137931,21.17721518987342,22.158536585365855,20.88679245283019,17.653333333333332,18.448979591836736,15.283783783783784,26.29032258064516,26.939393939393938,16.53030303030303,17.03448275862069,30.238095238095237,15.020833333333334,18.96825396825397,24.393939393939394,33.2962962962963,16.46031746031746,15.469135802469136,15.705882352941176,18.876543209876544,14.107142857142858,17.253968253968253,25.03030303030303,22.3,16.0,15.10909090909091,23.71153846153846,15.4,15.397058823529411,20.25531914893617,18.866666666666667,20.597014925373134,15.438356164383562,16.984126984126984,16.951612903225808,16.56,29.52,14.777777777777779,16.91044776119403,18.28846153846154,19.421875,15.145454545454545,15.68421052631579,13.46808510638298,12.216216216216216,16.15686274509804,16.356164383561644,13.079365079365079,18.76923076923077,16.941176470588236,19.31578947368421,17.865671641791046,16.681818181818183,14.297297297297296,18.78688524590164,12.98611111111111,19.84313725490196,16.048387096774192,17.67924528301887,13.174603174603174,24.46153846153846,11.135593220338983,15.266666666666667,11.736842105263158,19.659574468085108,16.88235294117647,15.35,16.95744680851064,14.448275862068966,12.24074074074074,14.071428571428571,11.370967741935484,13.048780487804878,19.19402985074627,29.894736842105264,31.454545454545453,22.837209302325583,12.354166666666666,17.390243902439025,14.322033898305085,16.617021276595743,23.125,21.041666666666668,16.58974358974359,14.153846153846153,14.39344262295082,10.956521739130435,15.15625,13.176470588235293,16.488888888888887,12.55,21.703703703703702,12.3,18.84375,20.433333333333334,13.072727272727272,14.53191489361702,12.376811594202898,14.674418604651162,10.62,18.488372093023255,10.18,12.0,16.25531914893617,8.446808510638299,26.166666666666668,21.894736842105264,12.854166666666666,13.392156862745098,14.694444444444445,18.17241379310345,14.977777777777778,16.818181818181817,9.0,9.534883720930232,13.382352941176471,15.666666666666666,8.704545454545455,7.509803921568627,9.58695652173913,9.666666666666666,12.375,20.4375,12.461538461538462,10.117647058823529,17.0,14.827586206896552,18.93103448275862,12.454545454545455,14.892857142857142,8.916666666666666,13.48076923076923,9.689655172413794,11.130434782608695,11.0,9.952380952380953,10.709677419354838,10.823529411764707,7.0,12.952380952380953,13.5,8.266666666666667,13.170731707317072,11.166666666666666,8.137931034482758,7.0,14.352941176470589,8.285714285714286,7.868421052631579,10.36,10.6,8.642857142857142,10.848484848484848,9.357142857142858,7.457142857142857,17.41176470588235,9.38888888888889,5.628571428571429,6.833333333333333,9.133333333333333,12.647058823529411,6.4,6.631578947368421,5.4,21.818181818181817,6.206896551724138,8.7,15.166666666666666,20.5,14.75,8.793103448275861,8.307692307692308,18.25,14.285714285714286,11.411764705882353,9.875,12.857142857142858,11.761904761904763,4.809523809523809,8.11111111111111,8.714285714285714,13.0,9.153846153846153,5.25,8.608695652173912,5.409090909090909,8.9375,4.684210526315789,7.5,8.9375,8.212121212121213,5.416666666666667,3.878787878787879,12.0,4.6875,11.333333333333334,9.3,5.4375,5.565217391304348,6.0,7.6,9.571428571428571,3.727272727272727,9.454545454545455,4.5,17.8,9.555555555555555,8.583333333333334,11.2,7.888888888888889,6.375,8.625,3.8823529411764706,3.5555555555555554,38.109756097560975,34.177215189873415,35.80555555555556,35.64473684210526,35.68,34.375,34.80246913580247,35.94871794871795,32.24390243902439,33.325,34.55384615384615,35.617283950617285,35.123456790123456,34.75,37.02597402597402,36.1625,35.138888888888886,36.15584415584416,33.05555555555556,32.03658536585366,33.657534246575345,30.68354430379747,35.47540983606557,32.7027027027027,36.10126582278481,30.513513513513512,36.92537313432836,32.67901234567901,31.52,35.2875,30.554054054054053,32.91358024691358,32.08536585365854,28.544303797468356,31.48051948051948,27.96,32.30379746835443,32.48101265822785,29.29113924050633,33.98571428571429,31.819444444444443,31.338461538461537,28.695121951219512,28.227272727272727,33.36842105263158,33.041666666666664,27.975609756097562,32.164556962025316,34.666666666666664,35.7,30.424242424242426,33.75308641975309,26.911392405063292,33.06578947368421,36.69736842105263,32.97260273972603,28.16923076923077,31.772727272727273,31.68421052631579,28.2375,27.736842105263158,34.97142857142857,31.452830188679247,29.10958904109589,29.647058823529413,20.98780487804878,31.616438356164384,34.698113207547166,29.986486486486488,28.430555555555557,28.46268656716418,35.2962962962963,35.96153846153846,32.81944444444444,31.983870967741936,30.08,33.54716981132076,33.370370370370374,32.05128205128205,33.74025974025974,33.8974358974359,32.11267605633803,29.07792207792208,21.341772151898734,31.054545454545455,30.675324675324674,28.864197530864196,28.1625,32.0921052631579,30.0188679245283,28.22222222222222,32.4,26.256410256410255,32.351351351351354,33.394366197183096,34.108108108108105,26.772151898734176,20.2625,30.41176470588235,27.773333333333333,30.346666666666668,20.51219512195122,34.44230769230769,35.236111111111114,28.402985074626866,31.446428571428573,27.5,28.037037037037038,25.532467532467532,27.0609756097561,28.548780487804876,29.491803278688526,25.28358208955224,23.641975308641975,25.987654320987655,27.073170731707318,27.246376811594203,20.329268292682926,22.527027027027028,21.6625,29.383561643835616,24.939393939393938,30.939393939393938,25.95,25.405405405405407,30.56578947368421,25.453125,22.97530864197531,27.4,27.58974358974359,29.544303797468356,27.974025974025974,28.81578947368421,22.875,33.42857142857143,26.83116883116883,25.414634146341463,29.328358208955223,17.9375,30.0125,23.931506849315067,23.884615384615383,23.346153846153847,28.746478873239436,24.58823529411765,20.51851851851852,20.217391304347824,32.91111111111111,21.34375,25.575,21.526315789473685,25.577464788732396,30.975609756097562,26.36842105263158,20.726027397260275,27.670731707317074,24.301369863013697,25.901234567901234,25.175,34.16129032258065,22.508196721311474,26.52054794520548,24.79268292682927,19.875,30.537037037037038,22.783333333333335,24.78082191780822,22.565217391304348,21.08641975308642,21.850746268656717,23.10958904109589,20.353658536585368,18.16393442622951,21.25,24.3875,18.59090909090909,18.53846153846154,22.78481012658228,19.884057971014492,26.10126582278481,24.56578947368421,18.73134328358209,22.44871794871795,23.319148936170212,27.327868852459016,31.672131147540984,19.551724137931036,18.0,20.825,15.539473684210526,28.11111111111111,25.569620253164558,19.103896103896105,28.942307692307693,25.3125,21.220588235294116,20.688524590163933,19.0,21.65714285714286,20.790123456790123,19.19298245614035,25.18032786885246,21.982758620689655,22.76595744680851,15.222222222222221,19.90909090909091,11.555555555555555,21.852459016393443,19.54385964912281,28.615384615384617,18.67948717948718,19.82716049382716,16.057971014492754,19.487179487179485,17.275,20.0,18.236842105263158,24.6375,22.25423728813559,23.185185185185187,23.44,17.88607594936709,26.622222222222224,18.506172839506174,17.44736842105263,20.271604938271604,20.333333333333332,24.515151515151516,19.0,17.64406779661017,15.28,20.658227848101266,21.393939393939394,26.646153846153847,22.048780487804876,20.346153846153847,21.406779661016948,17.774193548387096,20.88,15.867647058823529,20.240506329113924,16.418181818181818,16.644736842105264,17.12857142857143,21.60655737704918,17.47222222222222,18.102941176470587,25.70967741935484,32.09375,19.893939393939394,17.91891891891892,14.376811594202898,16.842105263157894,16.75,19.12962962962963,20.175,14.696428571428571,18.625,13.617647058823529,30.6,20.728571428571428,15.89041095890411,21.37878787878788,11.833333333333334,15.838709677419354,14.59322033898305,15.805555555555555,15.961538461538462,20.095238095238095,19.870967741935484,15.754716981132075,15.320987654320987,21.28846153846154,15.076923076923077,18.157894736842106,18.24390243902439,20.328125,22.185714285714287,18.083333333333332,16.0,14.781818181818181,19.532258064516128,13.333333333333334,17.97872340425532,16.941176470588236,22.356164383561644,26.585365853658537,16.73913043478261,10.725806451612904,14.262295081967213,23.97222222222222,24.37037037037037,11.753846153846155,17.916666666666668,14.847457627118644,12.915492957746478,14.652777777777779,13.782608695652174,14.653846153846153,26.564102564102566,15.727272727272727,9.407407407407407,14.885245901639344,16.24561403508772,13.764705882352942,30.23076923076923,12.24561403508772,15.051282051282051,14.795918367346939,14.090909090909092,17.323529411764707,17.09375,14.529411764705882,12.155172413793103,18.15,17.0,14.677966101694915,11.069767441860465,14.584905660377359,16.39622641509434,8.757575757575758,10.65079365079365,14.367647058823529,16.986666666666668,14.783783783783784,22.677419354838708,18.98701298701299,12.901960784313726,14.3,11.763636363636364,12.485714285714286,14.217391304347826,16.09090909090909,9.215686274509803,12.242857142857142,10.909090909090908,16.083333333333332,12.984848484848484,9.416666666666666,10.958333333333334,10.923076923076923,14.137254901960784,9.645833333333334,11.162790697674419,16.857142857142858,10.882352941176471,11.28888888888889,21.20689655172414,14.954545454545455,15.486486486486486,9.365853658536585,14.074074074074074,10.078947368421053,13.055555555555555,14.166666666666666,10.02127659574468,13.94915254237288,11.820512820512821,19.87878787878788,9.717948717948717,9.358490566037736,13.717391304347826,11.560975609756097,12.717948717948717,9.346153846153847,20.0,27.636363636363637,11.676470588235293,21.896551724137932,9.391304347826088,12.432432432432432,11.847457627118644,14.631578947368421,11.594594594594595,9.318181818181818,6.390243902439025,20.655172413793103,15.083333333333334,13.333333333333334,24.25,11.581395348837209,14.925925925925926,10.35483870967742,7.795454545454546,8.481481481481481,8.909090909090908,8.75,9.975,18.785714285714285,14.64864864864865,6.351351351351352,29.285714285714285,12.8,11.285714285714286,17.666666666666668,10.166666666666666,17.428571428571427,19.928571428571427,12.304347826086957,14.523809523809524,6.866666666666666,8.393939393939394,7.9743589743589745,8.366666666666667,7.260869565217392,13.235294117647058,11.307692307692308,18.0,14.76923076923077,7.758620689655173,10.352941176470589,5.653846153846154,7.9361702127659575,8.529411764705882,7.517241379310345,8.892857142857142,7.027027027027027,13.25,13.0,7.0344827586206895,6.5,7.0,10.666666666666666,7.8,8.65,4.205882352941177,5.722222222222222,24.142857142857142,9.058823529411764,6.294117647058823,6.8,6.862068965517241,4.421052631578948,3.6,14.571428571428571,6.636363636363637,6.833333333333333,4.4,3.8,9.0,6.25,6.25,5.25,3.5625,7.625,4.428571428571429,5.052631578947368,11.0,34.592592592592595,36.382716049382715,33.80263157894737,36.10666666666667,36.951219512195124,35.906666666666666,35.4054054054054,33.40506329113924,37.770270270270274,34.236111111111114,37.170731707317074,33.445945945945944,34.95,35.5625,34.67088607594937,36.96052631578947,35.06944444444444,36.35897435897436,34.857142857142854,35.85333333333333,33.96153846153846,35.01282051282051,34.2972972972973,34.465753424657535,33.38709677419355,29.626666666666665,35.49367088607595,33.68493150684932,34.2027027027027,24.604938271604937,33.21739130434783,31.455696202531644,32.96969696969697,37.4,31.29268292682927,34.032786885245905,32.63636363636363,32.40243902439025,33.95652173913044,32.43055555555556,27.91780821917808,30.973333333333333,29.23170731707317,32.78787878787879,28.17948717948718,31.37037037037037,30.658227848101266,32.85294117647059,33.98701298701299,32.53125,33.87301587301587,27.265822784810126,31.416666666666668,33.876543209876544,30.943661971830984,25.71604938271605,29.74074074074074,32.46835443037975,31.491803278688526,29.866666666666667,28.84,32.5625,26.121951219512194,33.17910447761194,31.236842105263158,33.276315789473685,29.414634146341463,26.28395061728395,21.291666666666668,31.728395061728396,32.6865671641791,24.465753424657535,33.88235294117647,28.725,26.304878048780488,29.716216216216218,29.82191780821918,32.43055555555556,34.178082191780824,28.746031746031747,29.38888888888889,27.43421052631579,28.81081081081081,25.825,32.25,22.506172839506174,31.03030303030303,34.6625,25.057142857142857,29.8625,30.33823529411765,28.985714285714284,33.36363636363637,27.756756756756758,37.212765957446805,31.170731707317074,26.053333333333335,23.024390243902438,31.62686567164179,25.064102564102566,31.263157894736842,30.19736842105263,25.5,28.531645569620252,26.51851851851852,28.037037037037038,32.92,31.935064935064936,30.367088607594937,31.510204081632654,28.416666666666668,23.861538461538462,32.353658536585364,23.36842105263158,30.22972972972973,21.524390243902438,26.89041095890411,25.421875,25.933333333333334,24.027027027027028,32.51315789473684,28.87012987012987,19.435897435897434,26.37037037037037,25.92,26.426666666666666,21.925,24.135802469135804,27.35,21.25609756097561,27.384615384615383,27.0,23.985714285714284,29.0,28.848101265822784,25.0375,30.08695652173913,23.628205128205128,15.682926829268293,24.704225352112676,25.890625,24.931506849315067,27.285714285714285,27.266666666666666,29.2,25.10144927536232,20.506666666666668,26.16417910447761,18.89189189189189,22.576923076923077,23.15277777777778,21.4,24.193548387096776,26.95774647887324,27.822580645161292,30.71641791044776,26.125,22.231884057971016,25.19047619047619,18.0,27.0,29.94871794871795,19.98780487804878,25.35483870967742,19.71794871794872,20.25974025974026,18.946666666666665,17.880597014925375,25.563636363636363,18.43548387096774,21.11111111111111,22.848484848484848,22.68,21.24590163934426,18.38888888888889,25.523076923076925,24.65753424657534,20.18918918918919,23.537037037037038,24.048780487804876,22.234567901234566,26.13157894736842,18.696202531645568,26.289473684210527,25.486842105263158,29.675,33.766666666666666,20.92982456140351,26.333333333333332,17.65671641791045,22.506849315068493,27.604938271604937,30.452830188679247,26.71014492753623,21.25,14.106060606060606,29.065573770491802,16.36,22.308823529411764,16.696428571428573,14.766233766233766,24.0,18.344827586206897,24.52777777777778,30.075949367088608,20.1,18.71014492753623,17.31168831168831,25.901639344262296,17.192307692307693,26.584615384615386,18.428571428571427,20.31645569620253,26.573529411764707,25.205128205128204,15.556962025316455,19.278688524590162,22.3375,22.135802469135804,17.846153846153847,20.135802469135804,23.72,9.597402597402597,19.985915492957748,21.70175438596491,23.46153846153846,26.02173913043478,22.723076923076924,16.185714285714287,22.88888888888889,20.430379746835442,20.529411764705884,24.6,17.246376811594203,25.741935483870968,18.40983606557377,18.390625,16.309859154929576,15.640625,16.723076923076924,19.1375,24.984848484848484,17.67142857142857,21.28125,22.610169491525422,21.90909090909091,23.453125,21.884615384615383,30.655172413793103,18.114285714285714,20.47222222222222,26.535714285714285,14.941176470588236,14.432432432432432,20.681159420289855,14.373134328358208,18.606060606060606,19.7,17.06756756756757,15.514705882352942,18.307692307692307,16.513513513513512,20.444444444444443,27.617021276595743,19.362068965517242,17.095890410958905,17.69736842105263,17.5,16.28358208955224,22.02857142857143,14.0,14.52112676056338,15.621951219512194,16.317460317460316,15.506666666666666,18.608695652173914,28.951219512195124,20.271604938271604,15.063829787234043,17.805194805194805,17.575342465753426,14.75925925925926,16.627118644067796,20.5,17.094594594594593,15.661764705882353,13.753846153846155,14.76923076923077,15.757575757575758,12.558823529411764,16.22,18.445945945945947,13.580645161290322,16.08,12.059701492537313,15.794871794871796,18.8,17.08974358974359,11.096153846153847,17.140350877192983,18.545454545454547,12.333333333333334,16.026315789473685,15.547619047619047,15.126760563380282,16.338709677419356,17.846153846153847,21.043478260869566,15.867924528301886,14.571428571428571,23.263157894736842,15.585365853658537,11.446808510638299,12.303571428571429,19.087719298245613,14.166666666666666,11.666666666666666,19.15909090909091,22.065217391304348,11.408163265306122,15.618181818181819,11.09433962264151,14.35897435897436,9.859649122807017,14.68421052631579,14.208333333333334,17.424242424242426,9.660377358490566,16.48076923076923,12.397260273972602,19.852941176470587,12.9,14.974358974358974,10.326530612244898,18.8,17.152173913043477,21.914893617021278,34.72222222222222,8.371428571428572,15.964285714285714,17.833333333333332,11.911764705882353,18.566666666666666,12.805555555555555,15.203125,15.179487179487179,10.294117647058824,14.278688524590164,17.903225806451612,17.03125,9.19047619047619,11.592592592592593,13.285714285714286,10.378378378378379,14.903225806451612,12.614035087719298,12.53225806451613,16.51851851851852,14.088235294117647,9.648148148148149,13.0,8.788461538461538,13.348837209302326,8.470588235294118,10.146341463414634,11.195121951219512,13.146341463414634,15.064516129032258,11.5,8.433962264150944,7.9375,8.473684210526315,9.76923076923077,16.136363636363637,9.714285714285714,20.11111111111111,19.85,16.416666666666668,11.478260869565217,10.777777777777779,14.266666666666667,7.945945945945946,17.318181818181817,13.588235294117647,12.272727272727273,8.564516129032258,9.763157894736842,9.0,8.65,10.34375,13.457142857142857,8.102564102564102,7.916666666666667,9.566666666666666,12.03125,11.705882352941176,10.266666666666667,15.548387096774194,7.5,6.977777777777778,11.08,21.59259259259259,9.0,13.357142857142858,7.114285714285714,16.857142857142858,7.586206896551724,4.090909090909091,26.166666666666668,7.5,10.304347826086957,4.92,10.25,7.684210526315789,9.666666666666666,7.551724137931035,6.611111111111111,6.4,7.0,7.409090909090909,10.833333333333334,14.454545454545455,9.615384615384615,12.777777777777779,8.095238095238095,9.5,7.363636363636363,5.64,10.727272727272727,5.0,8.23076923076923,9.333333333333334,6.4,5.0,8.125,9.5,7.55,13.166666666666666,6.421052631578948,6.875,3.9473684210526314,12.4,5.684210526315789,4.416666666666667,4.909090909090909,4.043478260869565,16.5,8.5,6.571428571428571,10.4,9.571428571428571,6.846153846153846,36.90243902439025,35.43055555555556,36.36,36.425,36.74666666666667,36.57534246575342,36.30487804878049,33.9,34.19117647058823,32.77215189873418,34.2,35.58536585365854,33.45333333333333,34.026666666666664,36.59493670886076,36.098765432098766,36.36585365853659,33.392405063291136,36.135802469135804,33.35,32.18333333333333,34.3013698630137,36.329268292682926,34.20779220779221,30.349206349206348,32.57333333333333,31.666666666666668,30.40740740740741,34.53703703703704,31.980392156862745,26.70731707317073,31.37837837837838,36.67796610169491,31.01492537313433,31.706666666666667,33.72839506172839,32.95384615384615,33.123456790123456,32.17948717948718,32.06410256410256,32.986301369863014,31.217391304347824,33.96551724137931,31.181818181818183,36.1875,30.228571428571428,33.65384615384615,34.40298507462686,30.048780487804876,30.8125,29.615384615384617,31.584415584415584,26.430379746835442,23.296296296296298,30.5375,32.354166666666664,31.844827586206897,25.3,32.723684210526315,29.695652173913043,33.20987654320987,27.983050847457626,24.5875,29.705882352941178,27.486486486486488,32.91379310344828,31.536585365853657,30.742857142857144,32.228070175438596,25.441558441558442,30.903846153846153,31.6375,29.272727272727273,28.825,25.774647887323944,33.24390243902439,33.07017543859649,33.01428571428571,33.21621621621622,29.293333333333333,29.863013698630137,22.428571428571427,22.33783783783784,24.3375,22.506849315068493,29.405797101449274,23.445945945945947,27.539473684210527,32.18518518518518,27.54320987654321,33.47457627118644,28.25,27.961038961038962,31.451219512195124,29.526315789473685,28.0,31.625,31.467532467532468,24.675324675324674,33.721311475409834,27.884615384615383,30.394736842105264,25.85,28.658536585365855,24.914634146341463,26.933333333333334,31.458333333333332,23.227848101265824,23.407894736842106,26.506493506493506,24.45945945945946,27.163636363636364,26.253521126760564,25.559322033898304,29.246376811594203,23.435897435897434,25.32051282051282,27.753424657534246,28.5,26.958904109589042,27.829268292682926,27.523076923076925,17.013157894736842,28.246153846153845,20.6625,25.695121951219512,33.82539682539682,23.231884057971016,28.714285714285715,34.390243902439025,26.616438356164384,27.207792207792206,33.865671641791046,24.12162162162162,23.532467532467532,32.67142857142857,26.125,23.466666666666665,22.925373134328357,22.5609756097561,26.40625,32.42857142857143,25.25925925925926,25.07246376811594,25.71794871794872,25.708333333333332,30.953125,31.7027027027027,26.703703703703702,19.054794520547944,22.093333333333334,22.240506329113924,20.531645569620252,19.1,29.326923076923077,27.93548387096774,25.29268292682927,20.333333333333332,25.0,21.561643835616437,21.164556962025316,18.5,27.044776119402986,25.907894736842106,28.05,31.152173913043477,20.0,26.68888888888889,21.596491228070175,21.51851851851852,26.951219512195124,25.746835443037973,30.028985507246375,20.756756756756758,23.70731707317073,21.82716049382716,29.916666666666668,22.783783783783782,24.870967741935484,26.136363636363637,25.585714285714285,27.44927536231884,18.87323943661972,20.728395061728396,20.217391304347824,20.01388888888889,26.72972972972973,17.4125,19.984615384615385,21.53030303030303,28.036363636363635,18.585365853658537,22.753424657534246,16.646341463414632,20.041095890410958,21.208333333333332,18.9625,23.514285714285716,20.768115942028984,30.07894736842105,23.35211267605634,19.4375,19.64864864864865,18.01298701298701,29.88888888888889,24.846153846153847,26.23076923076923,23.678571428571427,25.23170731707317,24.705882352941178,34.23076923076923,20.41176470588235,19.445945945945947,22.506849315068493,20.666666666666668,27.373333333333335,22.27777777777778,21.53030303030303,27.817073170731707,22.658536585365855,23.19047619047619,13.684931506849315,16.546875,14.532467532467532,26.9375,18.333333333333332,22.460526315789473,19.82608695652174,19.591549295774648,19.782608695652176,16.873417721518987,18.23170731707317,24.967741935483872,21.871794871794872,21.805555555555557,25.639344262295083,14.103896103896103,20.46268656716418,22.147058823529413,17.417910447761194,18.146341463414632,16.78787878787879,20.013513513513512,30.6,15.324324324324325,25.2,17.029411764705884,19.482142857142858,13.555555555555555,19.472727272727273,21.397260273972602,17.890243902439025,18.858974358974358,18.923076923076923,19.414285714285715,20.0,17.392857142857142,20.08108108108108,12.98076923076923,27.333333333333332,15.901408450704226,23.967741935483872,16.75,21.423728813559322,15.17142857142857,25.34375,16.791666666666668,14.08695652173913,21.90909090909091,14.87012987012987,15.209677419354838,14.879310344827585,16.72972972972973,15.12,16.666666666666668,15.81081081081081,14.576923076923077,18.77777777777778,19.055555555555557,14.857142857142858,12.307692307692308,19.742857142857144,31.952380952380953,15.487804878048781,17.689655172413794,22.454545454545453,21.210526315789473,15.541666666666666,9.461538461538462,17.763636363636362,23.71794871794872,20.22641509433962,12.095890410958905,14.0,25.02173913043478,15.51923076923077,18.534246575342465,15.833333333333334,28.366666666666667,19.194444444444443,15.835616438356164,16.666666666666668,13.787878787878787,13.11320754716981,16.22222222222222,14.192982456140351,14.3,16.035087719298247,11.173076923076923,13.444444444444445,20.26,10.291666666666666,16.057692307692307,11.032786885245901,16.69090909090909,13.657894736842104,8.666666666666666,19.0,16.208333333333332,14.351851851851851,16.859649122807017,16.451612903225808,9.709090909090909,12.648148148148149,23.28,15.25925925925926,14.37037037037037,14.724137931034482,11.950819672131148,9.720930232558139,18.605263157894736,16.76,25.0,10.528301886792454,31.083333333333332,14.333333333333334,20.09375,9.403225806451612,15.753424657534246,10.19047619047619,26.58974358974359,12.508196721311476,14.40625,12.146341463414634,13.307692307692308,10.772727272727273,12.75609756097561,10.529411764705882,12.867924528301886,13.761904761904763,12.607142857142858,14.203389830508474,13.452830188679245,21.1,10.527777777777779,15.96078431372549,18.763157894736842,16.128205128205128,12.857142857142858,26.933333333333334,9.534883720930232,14.231884057971014,8.660377358490566,17.52173913043478,14.3125,16.695652173913043,16.526315789473685,8.657894736842104,9.0,10.875,23.333333333333332,19.814814814814813,12.014925373134329,27.571428571428573,13.607142857142858,17.5,14.0,15.18918918918919,16.3,30.363636363636363,14.619047619047619,15.733333333333333,11.580645161290322,21.333333333333332,8.53061224489796,6.6875,16.785714285714285,13.576923076923077,8.636363636363637,7.696969696969697,18.9,18.266666666666666,15.636363636363637,12.409090909090908,12.482758620689655,15.0,11.25,18.071428571428573,16.0,18.125,14.695652173913043,12.347826086956522,16.61111111111111,12.423076923076923,11.25,11.08,13.277777777777779,7.121212121212121,18.6,5.90625,13.411764705882353,11.3125,14.642857142857142,15.9,13.275862068965518,13.933333333333334,9.608695652173912,7.571428571428571,11.523809523809524,19.714285714285715,7.0,12.25,25.88888888888889,5.333333333333333,8.75,5.193548387096774,7.421052631578948,8.176470588235293,7.25,5.75,13.166666666666666,12.666666666666666,4.7368421052631575,12.0,8.521739130434783,5.444444444444445,17.0,12.428571428571429,8.846153846153847,8.4,11.428571428571429,9.0,7.176470588235294,4.571428571428571,12.5,8.0,10.6,17.2,9.928571428571429,5.0,8.15,9.1875,15.583333333333334,23.6,16.333333333333332,13.555555555555555,4.16,8.833333333333334,5.933333333333334,7.235294117647059,5.714285714285714,4.916666666666667,10.11111111111111,4.8,6.888888888888889,3.7857142857142856,3.227272727272727,14.0,9.142857142857142,13.333333333333334,7.608695652173913,5.944444444444445,10.166666666666666,7.0,6.785714285714286,5.333333333333333,12.0,6.5,5.142857142857143,4.714285714285714,36.756410256410255,36.896103896103895,34.91463414634146,36.926829268292686,35.475,34.64102564102564,32.75,33.78260869565217,33.05194805194805,34.96,33.74025974025974,33.65625,33.17283950617284,30.22222222222222,35.03125,31.890243902439025,34.0,36.013698630136986,31.375,34.73170731707317,34.90909090909091,31.3,34.0,33.04477611940298,30.575342465753426,30.901234567901234,32.19444444444444,35.21818181818182,26.573333333333334,34.46031746031746,33.457142857142856,33.92857142857143,31.765432098765434,33.035714285714285,35.850746268656714,31.07792207792208,31.432098765432098,31.30263157894737,31.76829268292683,33.50632911392405,32.626666666666665,27.34567901234568,26.317073170731707,31.85,30.279411764705884,34.177215189873415,34.83561643835616,33.05714285714286,31.814814814814813,32.896103896103895,27.914634146341463,33.756410256410255,31.075949367088608,29.128205128205128,31.51851851851852,29.29113924050633,26.54320987654321,33.61538461538461,34.78082191780822,28.481012658227847,29.9672131147541,31.646153846153847,30.746478873239436,28.147058823529413,27.416666666666668,33.56716417910448,27.16216216216216,33.3625,31.735294117647058,32.65,26.180555555555557,30.835443037974684,28.043478260869566,27.88,24.83783783783784,30.18421052631579,30.728395061728396,28.666666666666668,28.625,31.317073170731707,32.1578947368421,27.814285714285713,28.635135135135137,32.34615384615385,27.963414634146343,27.320987654320987,25.85135135135135,28.773333333333333,27.075,33.86538461538461,28.012345679012345,27.233766233766232,26.695652173913043,24.817073170731707,26.9375,34.04615384615385,29.014705882352942,25.29032258064516,27.294117647058822,23.19753086419753,24.46268656716418,25.164556962025316,32.01724137931034,23.236842105263158,22.28,26.51219512195122,23.25,27.071428571428573,27.23728813559322,26.2,27.926470588235293,34.04347826086956,24.962962962962962,31.79268292682927,20.051948051948052,28.19736842105263,24.024390243902438,30.304347826086957,29.696969696969695,22.974683544303797,25.875,27.6875,21.5974025974026,23.26829268292683,26.291666666666668,26.120689655172413,22.936708860759495,30.071428571428573,27.45205479452055,24.52238805970149,31.627906976744185,22.26530612244898,28.296296296296298,29.666666666666668,20.77777777777778,28.44,24.085714285714285,25.417910447761194,28.21818181818182,23.22077922077922,28.75438596491228,23.329268292682926,27.32,28.452830188679247,22.810126582278482,26.613333333333333,29.825396825396826,25.96,27.05,27.5,22.670886075949365,19.405405405405407,20.318840579710145,21.7027027027027,27.5,31.386666666666667,27.065217391304348,22.796875,25.140625,23.548780487804876,29.475609756097562,21.794520547945204,20.17808219178082,31.86111111111111,21.8125,25.791044776119403,34.5,22.64,17.232876712328768,21.109756097560975,27.60377358490566,19.396551724137932,26.791044776119403,30.238095238095237,26.82456140350877,26.68421052631579,22.80952380952381,21.092307692307692,24.506172839506174,21.473684210526315,34.170731707317074,19.057142857142857,21.2,27.397435897435898,27.213333333333335,19.91358024691358,18.905405405405407,16.914285714285715,25.323529411764707,23.743243243243242,25.463768115942027,17.4025974025974,17.5,21.484375,26.575,21.913793103448278,17.5,24.471698113207548,24.209876543209877,18.690140845070424,25.158536585365855,20.53968253968254,17.910714285714285,17.553571428571427,25.863636363636363,20.915254237288135,17.610169491525422,25.597014925373134,30.195652173913043,18.766666666666666,19.186666666666667,26.094594594594593,17.61038961038961,20.79310344827586,30.095238095238095,14.31081081081081,18.921875,23.484848484848484,22.339285714285715,18.5125,25.367346938775512,19.16393442622951,22.0,27.52777777777778,27.651162790697676,16.514705882352942,25.7,31.28787878787879,13.56578947368421,21.154929577464788,20.606060606060606,15.847457627118644,19.342105263157894,19.589041095890412,17.85185185185185,27.86046511627907,20.17910447761194,22.941176470588236,23.887096774193548,30.27659574468085,34.371428571428574,23.583333333333332,18.338983050847457,16.684931506849313,17.670886075949365,21.7,25.227272727272727,18.28787878787879,18.37313432835821,20.40625,29.761904761904763,17.62162162162162,21.87719298245614,20.04,15.75,21.163636363636364,18.421875,20.378048780487806,29.76086956521739,16.532467532467532,11.741379310344827,19.233333333333334,20.672131147540984,14.0,15.028169014084508,14.543859649122806,19.789473684210527,26.348837209302324,14.137931034482758,19.4,16.06382978723404,16.216666666666665,14.926470588235293,23.205882352941178,21.20689655172414,14.0,19.675675675675677,13.714285714285714,13.757575757575758,27.181818181818183,15.588235294117647,17.82758620689655,25.102564102564102,19.0,14.39344262295082,29.813953488372093,16.169811320754718,18.13235294117647,13.930555555555555,19.294117647058822,16.6,15.1875,17.043478260869566,19.58108108108108,14.901960784313726,17.651162790697676,18.983050847457626,23.058823529411764,18.07547169811321,16.5,14.541666666666666,12.92,16.29787234042553,15.80952380952381,20.677966101694917,16.78723404255319,16.098039215686274,14.714285714285714,23.529411764705884,16.916666666666668,18.375,14.145833333333334,23.456521739130434,17.5,15.16326530612245,12.911764705882353,18.897435897435898,15.109375,17.8,19.68,15.65,14.038461538461538,21.023255813953487,11.37704918032787,12.433333333333334,12.86,14.481481481481481,8.745762711864407,15.957446808510639,13.38,17.956521739130434,11.162790697674419,21.24,20.34090909090909,13.666666666666666,14.444444444444445,9.0,11.588235294117647,10.129032258064516,14.695652173913043,10.947368421052632,19.323529411764707,14.522727272727273,10.372093023255815,17.02173913043478,10.372549019607844,12.97872340425532,12.81081081081081,11.447368421052632,14.5,19.977272727272727,10.313725490196079,13.344827586206897,12.18,21.894736842105264,19.84,10.607142857142858,20.428571428571427,11.604651162790697,20.933333333333334,10.653846153846153,9.666666666666666,15.909090909090908,11.904761904761905,14.76923076923077,10.80952380952381,18.967741935483872,12.333333333333334,11.71875,15.5,17.818181818181817,9.804878048780488,11.952380952380953,8.244444444444444,22.473684210526315,15.870967741935484,16.766666666666666,13.0,12.568627450980392,11.484848484848484,11.083333333333334,9.527777777777779,14.647058823529411,12.588235294117647,14.333333333333334,18.333333333333332,29.4,13.285714285714286,10.476190476190476,15.222222222222221,17.083333333333332,9.472222222222221,14.052631578947368,12.807692307692308,6.2745098039215685,12.033333333333333,25.555555555555557,7.809523809523809,13.631578947368421,16.25925925925926,12.89795918367347,9.727272727272727,14.857142857142858,12.588235294117647,14.523809523809524,7.090909090909091,5.509433962264151,15.083333333333334,13.631578947368421,6.121951219512195,5.821428571428571,13.4,27.833333333333332,7.5,13.375,8.84375,11.722222222222221,9.61111111111111,13.428571428571429,7.05,8.31578947368421,20.181818181818183,13.689655172413794,15.285714285714286,8.0,9.130434782608695,9.55,12.84,4.890625,7.5,10.736842105263158,8.153846153846153,10.941176470588236,10.571428571428571,7.892857142857143,5.0,13.0,10.733333333333333,10.0,13.571428571428571,6.090909090909091,15.5,6.9411764705882355,8.476190476190476,4.913043478260869,7.4,6.8,14.11111111111111,18.5,12.181818181818182,12.25,8.533333333333333,11.6,12.0,13.11111111111111,6.733333333333333,6.7,13.916666666666666,10.210526315789474,7.928571428571429,4.681818181818182,5.875,11.25,4.583333333333333,5.666666666666667,23.833333333333332,7.5,4.0588235294117645,3.5625,3.76,10.833333333333334,5.454545454545454,8.5,12.3,6.0,11.2,10.133333333333333,4.571428571428571,8.0,36.51470588235294,37.484848484848484,35.885714285714286,30.428571428571427,35.333333333333336,33.557377049180324,36.01754385964912,34.56716417910448,34.26086956521739,34.37096774193548,36.52857142857143,35.94736842105263,34.31818181818182,32.421052631578945,34.75,34.05882352941177,33.91935483870968,31.986301369863014,34.291666666666664,30.77777777777778,35.166666666666664,32.96923076923077,34.68571428571428,32.865671641791046,31.15625,29.887096774193548,33.06349206349206,32.5,31.542857142857144,30.753846153846155,31.454545454545453,32.225806451612904,30.955223880597014,28.676923076923078,28.931506849315067,34.425925925925924,27.761904761904763,29.529411764705884,34.704918032786885,31.82456140350877,29.580645161290324,33.92982456140351,33.775862068965516,34.82258064516129,33.56944444444444,35.095238095238095,31.107142857142858,34.36507936507937,36.172413793103445,29.450704225352112,32.271186440677965,24.014084507042252,32.03921568627451,34.47222222222222,34.517857142857146,26.357142857142858,29.970149253731343,32.266666666666666,31.225806451612904,29.5625,34.30882352941177,29.28358208955224,27.3768115942029,32.94736842105263,33.094339622641506,30.768115942028984,26.575757575757574,28.45614035087719,31.785714285714285,29.671232876712327,28.1864406779661,35.7037037037037,35.3859649122807,33.91428571428571,28.950819672131146,26.35,26.983606557377048,33.46153846153846,25.96,32.793103448275865,32.53225806451613,30.85185185185185,33.24390243902439,33.03448275862069,27.72222222222222,30.52857142857143,25.753846153846155,26.64788732394366,31.015384615384615,27.0,30.70769230769231,29.555555555555557,27.566666666666666,29.314814814814813,27.930555555555557,28.442307692307693,26.720588235294116,21.370967741935484,30.428571428571427,30.238805970149254,24.625,25.016393442622952,32.03174603174603,31.983333333333334,26.457142857142856,29.015625,22.5,24.66176470588235,30.78181818181818,29.451612903225808,32.142857142857146,27.418181818181818,26.279411764705884,29.84,29.942028985507246,30.915254237288135,28.806451612903224,21.80597014925373,25.560606060606062,29.384615384615383,25.82608695652174,22.802816901408452,19.884057971014492,30.32758620689655,25.063492063492063,29.680555555555557,24.727272727272727,21.65277777777778,22.413793103448278,32.526315789473685,28.846153846153847,31.428571428571427,26.682539682539684,30.210526315789473,29.859154929577464,25.78787878787879,29.0,25.54054054054054,21.12121212121212,27.972602739726028,30.365079365079364,22.424657534246574,24.859375,27.0,30.083333333333332,25.536231884057973,28.892307692307693,23.120689655172413,27.903225806451612,24.8135593220339,24.5,29.040816326530614,21.98181818181818,26.74137931034483,23.03030303030303,24.934782608695652,25.013698630136986,24.092307692307692,24.912280701754387,24.823529411764707,23.441176470588236,18.416666666666668,24.313725490196077,23.147540983606557,31.785714285714285,23.904761904761905,20.7,24.017857142857142,28.065217391304348,26.285714285714285,21.254545454545454,20.482758620689655,21.54237288135593,19.402985074626866,32.9,20.271186440677965,24.808823529411764,32.794871794871796,16.791666666666668,21.83606557377049,27.833333333333332,28.227272727272727,24.951612903225808,24.157894736842106,28.22222222222222,28.17241379310345,18.92753623188406,16.418181818181818,22.017543859649123,21.506849315068493,22.589285714285715,22.350877192982455,23.305084745762713,34.263888888888886,23.24,24.402985074626866,27.39622641509434,23.125,19.281690140845072,18.953846153846154,29.209302325581394,22.238095238095237,27.8135593220339,16.875,16.948275862068964,18.214285714285715,17.92982456140351,22.035714285714285,17.41269841269841,18.676056338028168,24.352941176470587,24.430555555555557,19.45,18.347826086956523,20.0,28.859154929577464,27.68888888888889,18.475409836065573,16.61764705882353,32.92857142857143,17.654545454545456,17.327868852459016,20.746031746031747,21.216216216216218,24.20408163265306,28.150943396226417,17.93846153846154,18.7,15.65079365079365,13.209677419354838,17.75,26.313725490196077,28.823529411764707,20.174603174603174,15.74074074074074,17.366666666666667,19.41509433962264,18.555555555555557,13.984848484848484,19.850746268656717,20.314814814814813,16.19672131147541,16.551724137931036,16.532258064516128,19.923076923076923,20.125,26.525,24.88235294117647,17.742424242424242,13.508474576271187,18.081632653061224,23.967741935483872,18.148936170212767,15.491228070175438,16.076923076923077,18.55223880597015,20.82456140350877,23.016129032258064,14.515151515151516,18.359375,15.763636363636364,28.41860465116279,19.46551724137931,18.508196721311474,20.5,22.555555555555557,14.161290322580646,26.386363636363637,18.894736842105264,18.939393939393938,18.511111111111113,18.440677966101696,17.416666666666668,15.53968253968254,19.47826086956522,14.5,18.482758620689655,20.274509803921568,16.12727272727273,19.8,18.326923076923077,14.6,13.152542372881356,9.590909090909092,17.375,16.90909090909091,16.29310344827586,11.431034482758621,21.263157894736842,12.933333333333334,28.444444444444443,12.37037037037037,27.789473684210527,18.17948717948718,19.375,16.5,12.574468085106384,14.75,16.03448275862069,17.59090909090909,16.433962264150942,21.27906976744186,13.555555555555555,22.77777777777778,15.566666666666666,19.842105263157894,16.89090909090909,15.757575757575758,12.732142857142858,18.8125,15.115942028985508,14.652173913043478,23.586206896551722,29.476190476190474,19.666666666666668,12.170212765957446,17.615384615384617,11.545454545454545,15.517241379310345,15.0,14.162790697674419,22.446428571428573,10.191489361702128,13.072727272727272,18.821428571428573,10.6,15.527777777777779,14.553191489361701,19.208333333333332,21.956521739130434,11.255813953488373,12.647058823529411,20.97142857142857,10.731707317073171,15.854545454545455,11.319148936170214,17.318181818181817,15.96774193548387,12.175,17.181818181818183,12.096774193548388,15.794117647058824,15.553571428571429,25.692307692307693,18.48,15.5,14.825,14.403508771929825,11.0,17.64864864864865,8.722222222222221,11.916666666666666,24.54054054054054,14.206896551724139,23.642857142857142,9.75,8.818181818181818,13.885714285714286,16.185185185185187,13.476190476190476,13.852941176470589,12.125,17.705882352941178,14.419354838709678,13.379310344827585,14.321428571428571,31.625,21.333333333333332,7.863636363636363,9.81081081081081,10.5,14.413793103448276,32.0,9.486486486486486,11.06060606060606,14.89655172413793,17.61111111111111,20.7,14.375,17.875,12.363636363636363,11.565217391304348,13.4,9.153846153846153,27.8,10.793103448275861,10.580645161290322,11.151515151515152,8.829268292682928,12.61111111111111,13.148148148148149,19.904761904761905,10.045454545454545,8.827586206896552,10.634146341463415,8.133333333333333,18.3125,6.444444444444445,22.875,12.083333333333334,17.545454545454547,7.928571428571429,22.954545454545453,11.5625,21.11111111111111,29.142857142857142,26.363636363636363,10.588235294117647,20.923076923076923,8.088888888888889,13.1,12.466666666666667,10.666666666666666,16.1,11.0,7.833333333333333,13.210526315789474,13.11111111111111,8.05,11.24,6.0,9.928571428571429,8.833333333333334,5.833333333333333,10.066666666666666,9.666666666666666,6.45,18.53846153846154,9.526315789473685,9.538461538461538,10.821428571428571,10.846153846153847,11.7,12.0,5.333333333333333,5.909090909090909,12.428571428571429,6.631578947368421,10.818181818181818,11.428571428571429,14.777777777777779,7.923076923076923,7.105263157894737,6.380952380952381,5.833333333333333,5.785714285714286,10.9,6.9411764705882355,13.5,8.423076923076923,10.181818181818182,8.7,8.3,10.7,13.333333333333334,11.153846153846153,10.666666666666666,14.0,4.153846153846154,9.222222222222221,12.428571428571429,5.916666666666667,7.363636363636363,6.2,7.571428571428571,5.888888888888889,13.166666666666666,5.2,7.625,4.111111111111111,7.75,10.8,10.0,5.0,5.3,7.090909090909091,34.15873015873016,35.791044776119406,34.55555555555556,35.78333333333333,34.27272727272727,33.0,33.88059701492537,37.563380281690144,35.78125,33.21311475409836,33.542857142857144,33.73015873015873,35.06896551724138,35.10344827586207,35.25,31.07843137254902,34.925925925925924,34.295081967213115,36.44615384615385,34.46551724137931,34.53623188405797,33.41509433962264,32.138888888888886,33.36764705882353,33.29577464788732,33.704918032786885,34.07692307692308,31.971014492753625,34.875,35.983870967741936,33.72222222222222,26.735294117647058,33.78,30.77777777777778,32.483870967741936,33.870370370370374,32.58730158730159,33.484375,35.82142857142857,34.464285714285715,34.267605633802816,28.357142857142858,31.34426229508197,29.80597014925373,31.428571428571427,33.422222222222224,33.55769230769231,29.333333333333332,34.04255319148936,36.56818181818182,28.306451612903224,31.925373134328357,32.32203389830509,31.246376811594203,36.51923076923077,35.5,30.802816901408452,30.652173913043477,31.043478260869566,32.611111111111114,30.126984126984127,31.595744680851062,28.52857142857143,33.05714285714286,31.416666666666668,33.148148148148145,32.0655737704918,36.241379310344826,22.89855072463768,24.492753623188406,24.53030303030303,31.06896551724138,28.52173913043478,28.735294117647058,29.746478873239436,29.19672131147541,30.86046511627907,34.0,32.34146341463415,27.17142857142857,24.955882352941178,27.271428571428572,27.347826086956523,30.69090909090909,29.272727272727273,33.714285714285715,32.36206896551724,31.837209302325583,25.161290322580644,29.372549019607842,30.53125,32.2,24.294117647058822,30.81159420289855,24.216666666666665,23.19047619047619,30.163636363636364,29.464285714285715,30.27777777777778,27.865671641791046,24.40277777777778,29.58730158730159,28.80392156862745,31.763636363636362,28.476190476190474,29.185714285714287,34.82608695652174,31.526315789473685,25.73611111111111,32.27777777777778,19.242857142857144,26.350877192982455,30.319444444444443,20.78787878787879,31.163636363636364,30.103448275862068,26.985294117647058,21.560606060606062,24.779411764705884,25.58,19.4375,29.673076923076923,32.810810810810814,29.65909090909091,29.976190476190474,29.282608695652176,21.555555555555557,30.338983050847457,23.044776119402986,28.736842105263158,31.0,29.984615384615385,19.34285714285714,25.823529411764707,27.5,27.0,33.325581395348834,23.96078431372549,26.74,25.366666666666667,27.353846153846153,25.68421052631579,27.929577464788732,28.028985507246375,28.388059701492537,32.72727272727273,22.34722222222222,32.43283582089552,27.746031746031747,19.070422535211268,23.555555555555557,24.630769230769232,32.9375,22.33823529411765,25.612244897959183,27.68,25.610169491525422,19.372549019607842,23.983050847457626,25.86046511627907,25.462962962962962,27.085106382978722,23.576923076923077,27.466666666666665,26.028985507246375,26.73913043478261,32.042857142857144,30.95744680851064,32.016666666666666,20.06153846153846,26.058823529411764,26.767857142857142,22.323076923076922,23.95,23.0,20.060606060606062,21.921875,29.555555555555557,27.388059701492537,21.397058823529413,23.360655737704917,17.60655737704918,25.2,21.606060606060606,19.555555555555557,22.952380952380953,19.21212121212121,21.891304347826086,25.804347826086957,17.983333333333334,17.25,20.75,19.30909090909091,16.02777777777778,31.549295774647888,20.904761904761905,15.344262295081966,17.333333333333332,22.82089552238806,29.22222222222222,19.91044776119403,25.4468085106383,17.818181818181817,20.096153846153847,18.850746268656717,19.310344827586206,22.82608695652174,23.29268292682927,20.9375,16.066666666666666,21.435897435897434,22.53448275862069,31.46031746031746,17.47142857142857,22.0,19.80701754385965,27.67241379310345,17.42,28.72340425531915,32.15384615384615,23.984126984126984,21.859649122807017,23.783783783783782,15.296875,27.285714285714285,23.733333333333334,18.942307692307693,24.098039215686274,14.693548387096774,23.833333333333332,19.672131147540984,17.07547169811321,16.70967741935484,16.245283018867923,27.928571428571427,22.724137931034484,21.923076923076923,18.45,18.389830508474578,22.073170731707318,27.692307692307693,21.76,17.375,14.648148148148149,18.071428571428573,19.238095238095237,17.307692307692307,18.92982456140351,17.272727272727273,20.96551724137931,21.3953488372093,18.103448275862068,15.279411764705882,20.45098039215686,24.22222222222222,15.76086956521739,17.390243902439025,18.0,21.25,16.21875,17.41176470588235,19.74468085106383,26.82,23.87878787878788,25.923076923076923,25.177777777777777,19.23404255319149,24.048780487804876,29.47826086956522,17.796875,16.74074074074074,23.27777777777778,16.655172413793103,17.032258064516128,18.428571428571427,14.73913043478261,12.766666666666667,17.262295081967213,20.439393939393938,16.431818181818183,31.17142857142857,18.49056603773585,24.171875,21.323943661971832,20.28813559322034,25.88888888888889,13.981481481481481,15.212765957446809,16.044444444444444,19.717391304347824,24.88,12.081967213114755,20.90566037735849,16.285714285714285,21.0,18.063492063492063,19.058823529411764,15.166666666666666,28.846153846153847,23.47222222222222,15.517857142857142,28.033333333333335,17.09433962264151,19.482758620689655,22.513513513513512,22.633333333333333,21.253968253968253,25.806451612903224,16.06,21.678571428571427,16.270833333333332,16.491803278688526,20.414634146341463,15.433962264150944,19.096153846153847,22.4,16.964285714285715,14.552631578947368,18.392156862745097,27.516129032258064,19.96923076923077,11.016129032258064,19.0327868852459,21.106382978723403,11.95,21.875,17.145454545454545,16.970588235294116,13.1,16.08108108108108,17.08888888888889,20.8,12.152173913043478,13.0,12.466666666666667,13.933333333333334,24.714285714285715,13.191489361702128,12.02,13.555555555555555,26.0,13.333333333333334,14.543478260869565,14.46,16.705882352941178,18.5625,17.53846153846154,16.326923076923077,15.31578947368421,20.864864864864863,26.076923076923077,10.95,13.372093023255815,12.371428571428572,14.0,14.676470588235293,19.5,25.76923076923077,22.296296296296298,9.133333333333333,10.4375,9.666666666666666,12.475,11.047619047619047,16.548387096774192,15.382352941176471,14.791666666666666,23.454545454545453,9.228571428571428,8.212121212121213,13.65625,18.26086956521739,9.341463414634147,11.560975609756097,12.851851851851851,27.1,8.977272727272727,8.61111111111111,7.266666666666667,10.227272727272727,9.452380952380953,10.89655172413793,12.577777777777778,17.291666666666668,14.407407407407407,15.903225806451612,12.46875,8.454545454545455,8.151515151515152,8.903225806451612,12.133333333333333,6.615384615384615,9.333333333333334,16.043478260869566,16.76923076923077,16.842105263157894,15.565217391304348,13.125,19.6,11.0,9.157894736842104,13.84,11.193548387096774,5.54054054054054,9.61111111111111,26.875,18.869565217391305,11.41025641025641,18.153846153846153,9.153846153846153,13.146341463414634,13.23076923076923,7.17948717948718,10.5,7.27027027027027,12.08108108108108,19.153846153846153,12.125,9.757575757575758,7.766666666666667,10.545454545454545,6.8076923076923075,10.066666666666666,7.580645161290323,16.0,6.853658536585366,21.2,17.941176470588236,30.6,8.384615384615385,8.166666666666666,10.8,8.115384615384615,6.826086956521739,10.944444444444445,13.76923076923077,9.764705882352942,12.692307692307692,11.476190476190476,19.0,5.0,6.4,8.705882352941176,4.928571428571429,10.11111111111111,14.0,15.722222222222221,13.7,5.366666666666666,5.777777777777778,6.848484848484849,15.375,13.0,7.157894736842105,6.05,6.052631578947368,14.166666666666666,10.071428571428571,14.428571428571429,4.454545454545454,6.65,4.428571428571429,10.333333333333334,16.88888888888889,7.230769230769231,4.9,8.777777777777779,3.875,17.23076923076923,5.068965517241379,9.25,4.857142857142857,6.133333333333334,3.5555555555555554,5.9523809523809526,9.5,5.6,9.727272727272727,4.666666666666667,19.333333333333332,4.545454545454546,8.333333333333334,4.909090909090909,9.777777777777779,6.384615384615385,3.9444444444444446,9.0,3.8,4.0,13.666666666666666,3.5,7.625,4.411764705882353,3.7333333333333334,8.8,5.090909090909091,12.4,12.6,6.75,34.89473684210526,36.0921052631579,33.76470588235294,35.93421052631579,33.45945945945946,32.8955223880597,35.4,34.48529411764706,33.445945945945944,33.82089552238806,37.214285714285715,37.21818181818182,34.74626865671642,34.546875,35.4625,33.14035087719298,33.63636363636363,37.911764705882355,34.25,32.29333333333334,35.73529411764706,35.333333333333336,34.333333333333336,34.794117647058826,37.23076923076923,33.67123287671233,30.039473684210527,34.52857142857143,29.81578947368421,34.67857142857143,34.596774193548384,35.30508474576271,32.59090909090909,32.43939393939394,32.97560975609756,37.87692307692308,30.27027027027027,35.333333333333336,33.12328767123287,31.949367088607595,34.97142857142857,31.893333333333334,27.256410256410255,27.10126582278481,30.85185185185185,33.5974025974026,31.16,34.83561643835616,31.91780821917808,30.884057971014492,33.981818181818184,32.940298507462686,33.87719298245614,30.794117647058822,30.746835443037973,34.98701298701299,31.953846153846154,34.45161290322581,34.80487804878049,31.91044776119403,26.30263157894737,35.36486486486486,33.39393939393939,31.666666666666668,29.475,32.625,32.589285714285715,31.676923076923078,28.166666666666668,28.13157894736842,32.056338028169016,33.78260869565217,29.03921568627451,32.121212121212125,30.246753246753247,22.5,29.53448275862069,29.32,29.49122807017544,30.689655172413794,28.583333333333332,33.34375,32.90769230769231,25.0126582278481,29.349206349206348,31.262295081967213,29.85333333333333,28.617283950617285,23.098591549295776,29.870967741935484,35.975,35.1,28.962962962962962,25.985507246376812,26.358974358974358,29.567164179104477,28.970588235294116,32.32142857142857,31.914893617021278,28.44736842105263,30.78688524590164,29.56756756756757,23.102564102564102,33.05,32.64705882352941,30.796296296296298,27.281690140845072,28.604938271604937,28.71875,25.860759493670887,27.68,32.33802816901409,32.4,23.02857142857143,33.857142857142854,28.178571428571427,27.414285714285715,28.962962962962962,26.21212121212121,36.0,27.594594594594593,33.166666666666664,37.6551724137931,22.698630136986303,20.48,24.36842105263158,31.918367346938776,27.459016393442624,24.653333333333332,25.333333333333332,29.29824561403509,25.690140845070424,21.125,34.74193548387097,27.7972972972973,27.884057971014492,29.935897435897434,27.348484848484848,23.33823529411765,28.01818181818182,21.926829268292682,22.151515151515152,29.754716981132077,29.057971014492754,22.842105263157894,18.985507246376812,20.962025316455698,36.41379310344828,20.680555555555557,22.553846153846155,33.5,24.195121951219512,15.837837837837839,27.4025974025974,28.360655737704917,20.055555555555557,31.48148148148148,27.2,19.46875,24.615384615384617,23.63013698630137,17.14666666666667,20.078125,19.97142857142857,16.928571428571427,29.40625,26.338461538461537,17.083333333333332,24.63888888888889,25.757142857142856,26.015384615384615,15.779220779220779,21.879310344827587,23.38961038961039,28.149253731343283,21.21917808219178,22.984126984126984,22.03448275862069,22.783333333333335,22.71014492753623,23.34328358208955,25.666666666666668,22.340425531914892,29.57377049180328,24.985714285714284,27.323943661971832,24.350649350649352,29.642857142857142,25.183333333333334,23.36764705882353,27.65625,25.577464788732396,29.567164179104477,18.027027027027028,27.970588235294116,19.684931506849313,23.980392156862745,20.82608695652174,17.55223880597015,31.246753246753247,27.229166666666668,15.238095238095237,17.88235294117647,21.962264150943398,22.866666666666667,17.535211267605632,26.281690140845072,23.875,29.404761904761905,27.901408450704224,21.316666666666666,25.203703703703702,17.876923076923077,25.448275862068964,26.30263157894737,15.725806451612904,19.6,24.615384615384617,21.507246376811594,20.46153846153846,22.158730158730158,25.41891891891892,21.104477611940297,17.577464788732396,17.057971014492754,21.70967741935484,20.653061224489797,21.121951219512194,24.796610169491526,21.90625,19.112903225806452,24.561643835616437,22.476190476190474,20.166666666666668,18.11764705882353,23.369230769230768,23.866666666666667,19.952380952380953,20.21311475409836,34.628571428571426,18.160714285714285,21.066666666666666,24.954545454545453,16.78,21.436363636363637,18.87272727272727,28.529411764705884,23.24590163934426,14.098591549295774,16.08450704225352,16.19402985074627,25.62162162162162,14.9375,15.895522388059701,24.18,16.63768115942029,24.576271186440678,17.323076923076922,16.714285714285715,25.904761904761905,20.72340425531915,22.08955223880597,16.206349206349206,22.677419354838708,20.666666666666668,20.78723404255319,17.695652173913043,16.11111111111111,23.928571428571427,25.53030303030303,16.183333333333334,21.822580645161292,22.183673469387756,19.1,16.25925925925926,18.104166666666668,21.877551020408163,17.80392156862745,17.107142857142858,14.267857142857142,14.58,17.944444444444443,28.891304347826086,13.790697674418604,15.719298245614034,14.901960784313726,18.87012987012987,16.272727272727273,19.20967741935484,16.6875,20.24137931034483,16.220338983050848,12.706896551724139,23.203703703703702,13.935483870967742,18.215384615384615,15.444444444444445,16.274509803921568,24.933333333333334,16.25,22.608695652173914,22.791666666666668,15.507462686567164,21.636363636363637,13.381818181818181,14.392857142857142,24.46153846153846,17.866666666666667,26.666666666666668,18.610169491525422,27.975609756097562,12.607142857142858,13.616438356164384,15.027777777777779,16.054545454545455,15.62962962962963,19.3,18.837209302325583,17.627450980392158,18.321428571428573,20.5625,15.984848484848484,13.712121212121213,17.08695652173913,16.145833333333332,14.784313725490197,17.024390243902438,19.215686274509803,18.81081081081081,10.907407407407407,12.785714285714286,17.0,13.226415094339623,20.448979591836736,17.30952380952381,18.01818181818182,11.810344827586206,15.897435897435898,13.23913043478261,14.548387096774194,24.14814814814815,18.192307692307693,11.673076923076923,13.173076923076923,13.333333333333334,16.0625,17.928571428571427,18.382978723404257,10.5,14.055555555555555,12.761904761904763,13.916666666666666,16.324324324324323,12.958333333333334,17.27027027027027,16.71794871794872,10.875,16.25925925925926,18.6,12.21875,11.072727272727272,16.472727272727273,11.038461538461538,20.0,12.766666666666667,12.204545454545455,15.528301886792454,23.0,12.15625,17.897435897435898,15.136363636363637,10.522727272727273,17.6875,28.727272727272727,13.944444444444445,15.0,8.6,9.854166666666666,13.634615384615385,9.981818181818182,11.710526315789474,22.923076923076923,8.571428571428571,11.5,12.816326530612244,30.214285714285715,23.714285714285715,8.431818181818182,10.176470588235293,9.926829268292684,19.136363636363637,24.823529411764707,10.98,7.34,12.342105263157896,9.806451612903226,14.208333333333334,13.807692307692308,13.148148148148149,7.216216216216216,10.53061224489796,13.974358974358974,11.25,11.125,9.135135135135135,17.529411764705884,11.742857142857142,12.055555555555555,5.709677419354839,19.451612903225808,20.157894736842106,12.805555555555555,7.973684210526316,11.393939393939394,9.18,7.977777777777778,24.0,15.5,34.285714285714285,19.75,9.947368421052632,21.625,5.565217391304348,13.533333333333333,18.88888888888889,19.25,20.11111111111111,11.258064516129032,7.4,18.7,13.536585365853659,29.444444444444443,9.3,5.1,16.384615384615383,22.48,13.91304347826087,6.794117647058823,7.805555555555555,10.473684210526315,7.857142857142857,11.470588235294118,17.90909090909091,12.16,10.875,11.619047619047619,13.928571428571429,9.789473684210526,11.157894736842104,7.304347826086956,9.25,14.117647058823529,10.941176470588236,7.9393939393939394,10.0,6.076923076923077,11.733333333333333,7.068965517241379,7.052631578947368,12.117647058823529,13.7,14.461538461538462,9.333333333333334,17.22222222222222,5.454545454545454,11.764705882352942,29.0,21.375,13.538461538461538,6.885714285714286,6.722222222222222,7.7894736842105265,9.958333333333334,8.066666666666666,10.4,8.0,8.578947368421053,7.4,7.260869565217392,6.916666666666667,17.333333333333332,14.333333333333334,10.357142857142858,9.15,5.785714285714286,13.0,6.384615384615385,20.8,17.333333333333332,8.090909090909092,6.866666666666666,6.636363636363637,7.7272727272727275,8.0,6.483870967741935,9.1,9.666666666666666,3.0,5.0,13.222222222222221,4.2,14.2,6.166666666666667,12.0,8.0,15.166666666666666,12.5,7.6,4.5,14.8,15.285714285714286,10.666666666666666,4.7272727272727275,5.916666666666667,4.6,5.363636363636363,10.692307692307692],"xbins":{"end":45,"size":1,"start":0},"type":"histogram","opacity":0.5},{"histnorm":"percent","name":"Playoffs","x":[41.73913043478261,36.42857142857143,35.0,41.05263157894737,35.54545454545455,40.083333333333336,44.09090909090909,36.526315789473685,36.26315789473684,36.904761904761905,41.416666666666664,32.65217391304348,38.05555555555556,36.93333333333333,40.6,38.333333333333336,26.666666666666668,24.91304347826087,31.857142857142858,28.26086956521739,35.5,35.916666666666664,33.666666666666664,38.416666666666664,41.25,35.421052631578945,37.833333333333336,40.833333333333336,40.5,31.90909090909091,37.57142857142857,29.363636363636363,28.133333333333333,33.45454545454545,41.714285714285715,18.571428571428573,20.5,33.27272727272727,21.333333333333332,37.333333333333336,27.083333333333332,23.8,34.083333333333336,19.904761904761905,15.15,39.333333333333336,43.0,20.42105263157895,42.5,28.083333333333332,16.227272727272727,39.666666666666664,40.5,30.266666666666666,38.714285714285715,17.818181818181817,33.166666666666664,36.333333333333336,16.63157894736842,23.727272727272727,27.25,25.666666666666668,34.714285714285715,13.35,35.5,26.333333333333332,17.166666666666668,12.68421052631579,35.333333333333336,34.666666666666664,19.714285714285715,31.5,34.166666666666664,27.0,33.333333333333336,18.583333333333332,21.083333333333332,44.8,37.5,31.5,29.166666666666668,17.0625,24.333333333333332,26.833333333333332,27.333333333333332,27.272727272727273,29.5,23.0,9.6,11.666666666666666,13.647058823529411,38.0,36.5,11.666666666666666,16.181818181818183,33.25,22.666666666666668,29.0,22.75,20.90909090909091,34.0,6.333333333333333,29.25,9.5,24.0,40.5,18.666666666666668,28.25,26.25,31.833333333333332,34.0,16.166666666666668,19.166666666666668,10.333333333333334,26.666666666666668,18.0,34.0,29.857142857142858,11.857142857142858,11.166666666666666,10.833333333333334,17.833333333333332,19.75,8.333333333333334,17.25,16.833333333333332,37.5,8.142857142857142,6.0,17.0,8.666666666666666,30.5,11.333333333333334,11.166666666666666,19.09090909090909,24.0,16.666666666666668,13.25,11.8,11.8,28.0,5.555555555555555,4.2727272727272725,7.888888888888889,21.0,11.8,8.25,20.5,6.0,5.0,5.571428571428571,11.0,3.4444444444444446,34.0,20.583333333333332,7.4,10.333333333333334,9.0,2.3333333333333335,5.5,11.25,3.6666666666666665,10.0,5.75,8.5,13.5,5.714285714285714,17.5,2.8333333333333335,5.0,9.75,5.071428571428571,8.25,2.8,6.666666666666667,5.0,7.0,9.6,3.8,20.0,2.3333333333333335,2.25,20.0,2.8,6.0,2.0,1.6,6.5,9.0,2.2,6.5,1.7777777777777777,9.0,5.666666666666667,3.6666666666666665,3.0,2.75,6.0,11.5,5.0,8.0,5.166666666666667,42.89473684210526,38.15,38.68421052631579,41.10526315789474,31.26086956521739,32.69565217391305,34.65,25.47826086956522,32.0,36.76923076923077,34.3,40.09090909090909,36.1578947368421,37.10526315789474,36.30769230769231,39.083333333333336,42.36363636363637,36.1578947368421,23.0,26.26086956521739,41.63636363636363,27.94736842105263,34.1764705882353,24.076923076923077,26.35,38.18181818181818,28.526315789473685,35.666666666666664,27.0,22.434782608695652,15.26086956521739,40.285714285714285,41.72727272727273,30.666666666666668,43.833333333333336,42.285714285714285,38.72727272727273,38.5,37.0,38.714285714285715,34.72727272727273,35.57142857142857,32.5,38.142857142857146,34.57142857142857,37.57142857142857,26.75,34.0,15.478260869565217,31.076923076923077,42.714285714285715,41.666666666666664,27.083333333333332,36.714285714285715,23.27777777777778,38.142857142857146,19.153846153846153,13.5,33.36363636363637,39.0,18.0,18.333333333333332,31.0,17.72222222222222,35.714285714285715,35.42857142857143,17.61111111111111,20.2,30.8,27.142857142857142,32.857142857142854,32.57142857142857,20.833333333333332,25.142857142857142,38.25,27.285714285714285,14.333333333333334,28.571428571428573,15.736842105263158,28.428571428571427,27.285714285714285,21.75,27.142857142857142,32.0,18.38888888888889,29.5,43.6,28.2,32.6,20.857142857142858,35.142857142857146,20.210526315789473,12.4,23.375,27.571428571428573,19.0,16.857142857142858,35.333333333333336,15.733333333333333,16.428571428571427,22.285714285714285,33.4,8.4,42.0,33.666666666666664,24.714285714285715,12.153846153846153,24.2,5.117647058823529,38.5,23.0,26.0,11.571428571428571,9.818181818181818,9.714285714285714,12.0,17.727272727272727,13.5,9.090909090909092,10.5625,12.416666666666666,29.75,17.5,12.68421052631579,9.5,12.625,6.833333333333333,27.166666666666668,22.571428571428573,10.307692307692308,14.6,22.75,15.0,10.764705882352942,7.214285714285714,19.285714285714285,11.090909090909092,17.0,16.22222222222222,11.0,6.181818181818182,14.4,11.4,24.285714285714285,16.142857142857142,11.571428571428571,9.333333333333334,6.363636363636363,6.428571428571429,8.428571428571429,3.823529411764706,5.0,8.2,12.833333333333334,5.75,7.5,9.0,2.9,6.428571428571429,7.666666666666667,16.0,13.25,11.571428571428571,2.4285714285714284,7.0,3.75,11.0,9.666666666666666,5.25,7.6,3.5714285714285716,3.5,0.9,3.8,4.0,5.0,3.75,9.2,1.8,2.0,2.5,2.6666666666666665,4.5,6.0,4.0,3.5,2.3333333333333335,3.5,1.5,8.666666666666666,2.25,2.5,2.5,2.6666666666666665,5.0,3.75,3.5,42.2,39.333333333333336,37.411764705882355,36.23809523809524,39.785714285714285,37.333333333333336,33.76470588235294,42.166666666666664,33.0625,37.083333333333336,35.69230769230769,37.833333333333336,35.375,41.8,34.875,32.625,31.11111111111111,23.294117647058822,38.529411764705884,32.42857142857143,30.238095238095237,37.81818181818182,26.45,38.57142857142857,36.35,25.176470588235293,34.42857142857143,34.75,27.071428571428573,23.58823529411765,34.72727272727273,28.647058823529413,37.57142857142857,33.36363636363637,29.8,18.125,31.7,24.85,35.714285714285715,32.416666666666664,39.4,43.0,35.714285714285715,30.7,39.0,39.0,17.857142857142858,30.375,41.6,40.2,29.214285714285715,36.2,17.857142857142858,10.904761904761905,33.1,41.5,27.09090909090909,38.666666666666664,23.157894736842106,23.0,15.55,18.9375,33.2,28.285714285714285,39.75,25.7,17.5,30.0,21.8,35.75,25.5,31.833333333333332,32.0,41.8,16.0,9.15,29.75,33.5,32.916666666666664,17.818181818181817,17.8,23.666666666666668,27.9,16.571428571428573,14.909090909090908,13.266666666666667,31.666666666666668,34.333333333333336,30.8,29.142857142857142,7.470588235294118,26.75,30.0,18.714285714285715,11.0,26.0,25.5,17.235294117647058,23.666666666666668,25.5,32.0,15.636363636363637,33.25,20.0,32.75,28.0,26.5,25.0,23.75,12.727272727272727,29.5,10.2,10.285714285714286,26.5,8.23076923076923,18.333333333333332,31.25,21.5,15.0,20.0,22.5,21.2,9.9,11.545454545454545,6.7,26.5,22.5,12.0,12.6,8.6,25.25,31.0,26.75,12.6,23.4,18.5,17.571428571428573,7.125,18.75,21.5,18.333333333333332,18.5,10.333333333333334,13.25,12.75,5.428571428571429,8.166666666666666,5.444444444444445,5.5,17.0,12.0,19.5,37.0,5.0,5.25,4.125,10.0,12.333333333333334,7.222222222222222,3.3333333333333335,2.6666666666666665,19.75,6.5,2.5,8.6,6.5,12.0,5.0,5.142857142857143,20.0,3.3333333333333335,3.0,16.0,12.0,1.6363636363636365,4.666666666666667,6.0,2.0,2.25,4.666666666666667,2.3333333333333335,2.2,2.625,16.0,3.0,1.6,12.0,5.0,4.166666666666667,2.1666666666666665,5.0,4.0,5.0,3.5,5.333333333333333,2.5,3.5,35.375,39.142857142857146,36.857142857142854,40.333333333333336,37.44444444444444,34.111111111111114,37.3,38.3,38.21739130434783,33.785714285714285,30.65,39.72727272727273,34.76190476190476,33.714285714285715,40.18181818181818,33.9,33.7,30.958333333333332,33.44444444444444,31.958333333333332,21.416666666666668,39.285714285714285,35.357142857142854,30.72222222222222,29.8,22.6,17.944444444444443,35.142857142857146,36.5,26.75,33.81818181818182,37.142857142857146,29.15,27.27777777777778,36.666666666666664,27.9,29.61904761904762,32.7,8.375,38.6,11.043478260869565,16.75,25.3,24.727272727272727,29.1,32.5,19.1,13.941176470588236,18.142857142857142,27.454545454545453,33.166666666666664,26.4,31.6,34.0,16.59090909090909,26.166666666666668,31.25,33.57142857142857,24.0,8.826086956521738,27.642857142857142,25.384615384615383,27.0,26.7,27.666666666666668,32.142857142857146,35.666666666666664,12.05,27.818181818181817,21.272727272727273,34.4,32.166666666666664,28.142857142857142,36.0,33.0,17.476190476190474,11.444444444444445,32.75,19.2,36.0,9.625,16.7,16.1,34.6,24.0,18.636363636363637,26.5,40.25,31.75,36.714285714285715,19.571428571428573,20.3,21.8,17.6,39.0,24.571428571428573,32.833333333333336,28.8,36.75,27.0,28.285714285714285,23.75,16.0,30.0,22.333333333333332,27.142857142857142,17.666666666666668,19.0,22.75,19.6,17.857142857142858,34.75,9.166666666666666,11.875,24.2,13.4,5.428571428571429,14.0,32.57142857142857,24.8,36.2,22.4,20.25,13.5,9.11111111111111,9.8,23.5,25.8,12.727272727272727,18.0,28.25,25.0,6.0,13.142857142857142,16.0,7.444444444444445,19.8,7.857142857142857,12.833333333333334,12.9,15.4,9.8,12.2,9.444444444444445,5.470588235294118,5.230769230769231,9.666666666666666,19.0,22.25,33.0,6.4,10.6,12.666666666666666,3.3333333333333335,3.8,9.5,10.571428571428571,12.833333333333334,19.75,16.333333333333332,5.846153846153846,8.0,4.555555555555555,16.5,11.0,4.0,8.666666666666666,11.0,7.0,5.0,23.0,2.5,8.5,15.6,8.777777777777779,3.6,8.6,5.5,8.5,1.3333333333333333,1.3333333333333333,2.5,5.5,4.583333333333333,5.0,8.5,5.8,10.8,4.75,4.5,11.0,8.2,8.666666666666666,7.0,5.0,10.75,5.0,6.0,3.3333333333333335,8.0,2.0,4.5,3.5,3.0,3.5,3.0,4.0,2.0,5.2,3.0,41.333333333333336,35.35294117647059,36.27777777777778,35.53333333333333,39.0,34.733333333333334,35.75,38.84615384615385,37.0,32.111111111111114,35.833333333333336,33.888888888888886,37.36363636363637,33.5625,35.05882352941177,33.111111111111114,37.3,34.88235294117647,38.8,37.142857142857146,19.22222222222222,26.0,20.4,32.92307692307692,28.692307692307693,29.88888888888889,40.5,35.166666666666664,37.333333333333336,31.22222222222222,36.5,27.055555555555557,30.7,32.54545454545455,29.636363636363637,24.727272727272727,39.833333333333336,26.375,37.5,35.125,27.25,22.8125,29.545454545454547,37.54545454545455,26.0,40.0,26.1875,20.307692307692307,22.6,43.0,37.75,13.6875,37.714285714285715,17.75,18.11111111111111,31.46153846153846,25.22222222222222,27.333333333333332,30.545454545454547,25.181818181818183,14.76923076923077,16.294117647058822,9.3125,35.0,31.666666666666668,17.88888888888889,12.833333333333334,28.0,38.5,12.647058823529411,20.454545454545453,13.0,21.2,23.5,31.833333333333332,14.555555555555555,33.333333333333336,14.133333333333333,13.0,27.0,16.176470588235293,15.714285714285714,30.272727272727273,15.333333333333334,35.5,31.166666666666668,29.428571428571427,26.75,18.454545454545453,15.272727272727273,33.0,16.333333333333332,12.066666666666666,30.833333333333332,25.0,37.0,12.785714285714286,32.5,30.5,17.22222222222222,36.2,32.0,27.0,12.076923076923077,26.5,25.1,23.6,28.25,26.166666666666668,35.0,22.2,14.0,26.5,8.083333333333334,19.666666666666668,22.666666666666668,10.666666666666666,33.25,15.5,31.0,20.166666666666668,31.4,19.833333333333332,18.142857142857142,13.692307692307692,10.142857142857142,8.615384615384615,31.666666666666668,19.333333333333332,18.5,12.0,7.090909090909091,20.5,14.75,24.75,11.75,12.5,4.4,10.222222222222221,13.2,16.0,30.0,9.0,15.0,4.3076923076923075,33.5,6.666666666666667,17.666666666666668,23.0,19.0,4.75,14.428571428571429,12.166666666666666,13.666666666666666,25.0,12.0,13.5,3.3,10.4,10.333333333333334,3.9,11.333333333333334,4.142857142857143,12.6,8.666666666666666,10.6,2.4285714285714284,9.666666666666666,8.833333333333334,4.333333333333333,5.083333333333333,7.75,11.333333333333334,3.6,5.25,3.6666666666666665,8.0,5.0,8.0,5.0,3.3333333333333335,7.0,5.5,7.0,4.2,6.25,10.5,5.666666666666667,6.0,3.0,4.5,9.0,6.0,5.0,2.3333333333333335,9.0,3.5,3.75,3.3333333333333335,17.0,10.333333333333334,4.0,2.25,3.8,3.6666666666666665,1.25,3.3333333333333335,10.0,3.6666666666666665,5.0,6.666666666666667,41.90909090909091,38.42857142857143,36.529411764705884,37.80952380952381,37.0,35.94736842105263,32.388888888888886,34.46666666666667,31.428571428571427,36.63157894736842,35.73684210526316,39.77777777777778,37.36363636363637,32.294117647058826,29.57894736842105,35.4,39.0,30.58823529411765,38.666666666666664,32.09090909090909,34.2,22.954545454545453,40.0,39.166666666666664,29.31578947368421,36.1,39.285714285714285,32.9,34.75,23.772727272727273,36.9,34.72727272727273,37.285714285714285,39.0,33.470588235294116,34.23529411764706,41.833333333333336,29.933333333333334,24.4,34.81818181818182,17.238095238095237,36.0,35.55555555555556,27.3,26.733333333333334,35.2,21.894736842105264,20.473684210526315,29.363636363636363,16.0,26.0,31.555555555555557,38.75,22.7,15.35,32.142857142857146,23.3,31.2,33.55555555555556,15.294117647058824,15.052631578947368,34.0,23.714285714285715,28.0,26.0,21.5,18.428571428571427,12.153846153846153,30.166666666666668,25.4,13.333333333333334,10.294117647058824,28.1,32.8,30.571428571428573,34.0,23.8,33.857142857142854,23.545454545454547,34.0,40.5,21.285714285714285,32.333333333333336,23.8,21.11111111111111,23.857142857142858,32.75,33.0,17.9,30.6,21.0,29.2,33.333333333333336,32.2,26.571428571428573,32.0,9.722222222222221,24.6,30.166666666666668,24.666666666666668,15.5,9.545454545454545,26.666666666666668,10.3,11.4,31.6,15.555555555555555,25.0,23.5,21.4,18.0,22.166666666666668,26.0,19.0,10.176470588235293,14.0,16.2,19.2,20.2,25.166666666666668,20.428571428571427,12.666666666666666,21.666666666666668,13.4,13.529411764705882,9.727272727272727,13.166666666666666,24.6,8.666666666666666,18.0,19.2,29.0,17.5,14.6,11.75,15.4,16.555555555555557,7.25,18.333333333333332,8.0,9.4,20.6,9.0,37.0,7.9,7.5,8.636363636363637,19.142857142857142,9.142857142857142,15.4,13.5,16.4,14.0,3.7142857142857144,26.5,14.75,4.428571428571429,2.875,3.0,6.75,13.0,6.666666666666667,17.75,17.5,9.428571428571429,6.857142857142857,7.25,4.714285714285714,4.0,9.666666666666666,6.0,4.333333333333333,10.0,8.0,14.666666666666666,2.4285714285714284,7.666666666666667,2.75,4.0,2.6666666666666665,13.75,4.75,8.0,4.75,2.0,5.0,3.0,3.5,3.0,6.0,4.0,2.7142857142857144,2.0,4.666666666666667,4.8,3.6666666666666665,3.0,39.125,38.45454545454545,37.125,38.95238095238095,40.625,39.6875,36.833333333333336,34.266666666666666,37.5,39.714285714285715,38.54545454545455,36.285714285714285,38.63636363636363,34.333333333333336,35.083333333333336,30.625,20.833333333333332,30.363636363636363,29.952380952380953,28.2,33.5,36.92857142857143,37.27272727272727,24.666666666666668,36.666666666666664,36.09090909090909,36.916666666666664,28.8125,26.333333333333332,29.2,35.083333333333336,28.5,31.25,23.3125,35.857142857142854,15.91304347826087,20.523809523809526,40.8,34.857142857142854,32.77777777777778,24.25,21.285714285714285,29.333333333333332,23.428571428571427,34.44444444444444,30.444444444444443,38.72727272727273,28.22222222222222,33.5,24.9375,39.4,20.071428571428573,26.333333333333332,17.1875,30.09090909090909,38.6,27.285714285714285,28.8,18.133333333333333,29.6,21.6,23.571428571428573,28.285714285714285,20.375,14.636363636363637,29.666666666666668,15.454545454545455,21.09090909090909,28.833333333333332,25.428571428571427,33.6,32.8,30.285714285714285,16.0,21.5,26.2,37.0,11.352941176470589,27.0,30.2,10.681818181818182,23.5,29.2,9.545454545454545,28.2,15.571428571428571,35.0,16.625,21.0,33.25,20.6,32.5,31.8,35.2,18.0,31.75,26.0,19.3,29.4,30.4,22.0,15.5,27.4,9.421052631578947,25.285714285714285,29.0,29.25,29.0,14.727272727272727,29.8,15.3125,32.5,7.066666666666666,18.714285714285715,9.0,8.818181818181818,31.5,21.714285714285715,20.142857142857142,24.0,7.5625,23.8,27.4,18.4,30.2,27.5,32.75,21.25,13.625,29.75,7.571428571428571,18.4,7.428571428571429,17.0,25.6,20.25,9.333333333333334,12.0,9.333333333333334,8.333333333333334,12.0,11.0,4.785714285714286,17.25,3.6363636363636362,9.75,12.777777777777779,5.375,9.0,11.8,9.2,15.8,13.666666666666666,7.9,13.0,10.5,5.0,14.25,3.8,12.0,5.833333333333333,6.0,20.5,11.4,4.25,6.0,7.5,7.0,3.375,7.333333333333333,5.0,3.5,2.8,16.0,15.8,2.6,9.666666666666666,3.5,4.333333333333333,2.5714285714285716,3.3333333333333335,4.666666666666667,5.0,4.454545454545454,3.0,10.5,3.111111111111111,11.0,2.4,7.5,4.333333333333333,5.5,2.0,3.0,1.6666666666666667,3.5,5.0,6.666666666666667,3.6666666666666665,10.0,3.0,1.6666666666666667,3.3333333333333335,2.4,2.6666666666666665,3.0,36.61904761904762,36.285714285714285,39.63157894736842,38.38095238095238,36.526315789473685,40.588235294117645,39.529411764705884,39.30769230769231,37.333333333333336,36.1578947368421,33.666666666666664,36.94117647058823,32.529411764705884,36.84615384615385,37.714285714285715,31.428571428571427,38.11764705882353,28.571428571428573,30.77777777777778,28.952380952380953,34.36842105263158,39.09090909090909,23.736842105263158,23.047619047619047,34.166666666666664,35.5,37.54545454545455,38.0,35.833333333333336,21.36842105263158,25.0,26.23076923076923,22.818181818181817,32.8,29.846153846153847,28.352941176470587,24.157894736842106,37.285714285714285,24.818181818181817,24.6875,32.75,37.0,28.416666666666668,24.285714285714285,18.692307692307693,31.583333333333332,15.176470588235293,18.38095238095238,32.42857142857143,36.25,24.615384615384617,38.57142857142857,28.571428571428573,39.2,35.72727272727273,39.857142857142854,34.0,30.285714285714285,29.666666666666668,15.666666666666666,27.071428571428573,31.0,33.0,35.75,26.8,34.5,15.933333333333334,40.0,19.789473684210527,16.058823529411764,27.0,35.0,39.0,19.523809523809526,17.076923076923077,28.833333333333332,35.2,29.166666666666668,26.0,24.6,32.2,31.333333333333332,30.0,30.75,18.692307692307693,36.0,25.6,16.5,20.727272727272727,34.2,33.42857142857143,32.75,36.5,37.25,11.9,31.833333333333332,29.4,14.166666666666666,16.285714285714285,31.5,17.583333333333332,17.9,23.25,31.4,9.272727272727273,20.75,34.25,30.6,11.461538461538462,10.0,18.0,10.894736842105264,11.818181818181818,14.0,23.75,13.666666666666666,9.642857142857142,33.0,33.833333333333336,17.1,35.57142857142857,10.416666666666666,28.8,23.8,21.2,36.0,18.0,8.4,32.75,32.0,20.5,17.8,16.25,13.6,6.466666666666667,14.5,13.857142857142858,9.384615384615385,13.25,15.2,7.5,12.5,5.25,9.333333333333334,13.25,5.0,13.0,13.666666666666666,10.333333333333334,9.166666666666666,7.8,8.5,11.333333333333334,8.333333333333334,4.0,6.666666666666667,9.0,6.0,7.6,13.5,12.285714285714286,6.571428571428571,7.666666666666667,5.0,8.0,6.142857142857143,13.0,3.2,4.0,6.666666666666667,18.75,7.0,9.333333333333334,13.666666666666666,7.0,5.0,7.0,10.5,5.5,8.333333333333334,4.5,4.5,5.333333333333333,5.666666666666667,2.076923076923077,10.0,5.0,6.0,4.8,5.0,3.0,10.0,2.3333333333333335,3.5,3.0,4.5,6.5,3.4444444444444446,6.0,7.0,38.095238095238095,40.36363636363637,40.08695652173913,40.8421052631579,37.6875,40.416666666666664,39.65217391304348,34.15,36.40909090909091,32.73684210526316,39.27272727272727,34.6,32.45454545454545,29.0,34.5,36.5,33.22222222222222,32.0,40.142857142857146,32.13636363636363,33.13636363636363,31.789473684210527,24.555555555555557,31.75,41.333333333333336,19.0,36.111111111111114,35.45454545454545,31.0,27.09090909090909,35.77777777777778,31.61111111111111,18.3,33.2,21.095238095238095,34.18181818181818,23.73913043478261,37.0,29.210526315789473,40.6,39.0,19.894736842105264,33.5,37.333333333333336,15.38888888888889,28.6,36.166666666666664,13.65,35.0,40.0,36.72727272727273,37.42857142857143,27.818181818181817,29.9,26.5,17.705882352941178,36.0,29.608695652173914,35.0,23.083333333333332,37.2,27.0,30.5,33.285714285714285,29.333333333333332,36.0,36.6,28.8,12.090909090909092,32.666666666666664,16.25,14.6,19.0,28.833333333333332,33.4,13.083333333333334,33.2,23.833333333333332,34.6,38.714285714285715,32.4,25.6,27.4,29.25,10.5,18.333333333333332,34.0,23.4,38.5,12.11111111111111,24.875,12.416666666666666,17.083333333333332,16.285714285714285,38.0,16.923076923076923,30.4,19.0,8.285714285714286,10.083333333333334,26.4,23.0,17.166666666666668,24.666666666666668,27.666666666666668,9.222222222222221,20.75,21.0,32.4,28.4,12.444444444444445,25.0,23.25,17.833333333333332,30.333333333333332,21.5,26.5,13.181818181818182,26.714285714285715,14.6,23.25,27.25,20.166666666666668,11.727272727272727,22.2,14.75,13.428571428571429,11.444444444444445,18.333333333333332,23.2,7.4375,13.0,22.4,16.6,29.2,10.833333333333334,15.4,19.8,17.6,12.0,14.25,27.6,9.75,18.4,6.8,8.4,7.428571428571429,15.333333333333334,24.0,15.0,6.571428571428571,11.4,13.4,10.357142857142858,8.625,15.0,4.4,17.75,6.2,9.4,10.5,4.545454545454546,3.6,4.2,11.2,7.2,9.0,9.5,4.444444444444445,3.4615384615384617,4.6,23.333333333333332,8.5,2.4285714285714284,3.5714285714285716,1.6,5.0,4.0,9.0,2.0,9.0,3.142857142857143,3.0,6.6,6.8,2.3333333333333335,2.5,2.5,3.1666666666666665,1.875,4.666666666666667,3.0,3.0,3.75,7.333333333333333,5.8,5.0,5.666666666666667,2.3333333333333335,3.6666666666666665,2.0,2.5,1.6666666666666667,2.5,4.5,5.0,2.25,7.5,6.0,6.5,6.0,8.5,6.0,8.25,2.0,4.0,2.5,2.5,1.3333333333333333,3.0,3.0,2.3333333333333335,3.0,5.125,6.333333333333333,40.958333333333336,34.72727272727273,38.333333333333336,36.8,37.0,36.0,34.94444444444444,37.333333333333336,27.5,34.86363636363637,36.19047619047619,35.43478260869565,34.111111111111114,27.833333333333332,40.416666666666664,37.55555555555556,38.5,30.53846153846154,36.6,38.583333333333336,34.46153846153846,35.666666666666664,39.916666666666664,38.22222222222222,27.25,38.833333333333336,25.434782608695652,29.055555555555557,39.27777777777778,25.4,27.666666666666668,31.954545454545453,38.46153846153846,39.333333333333336,30.454545454545453,24.533333333333335,25.38888888888889,34.2,38.333333333333336,37.833333333333336,24.666666666666668,23.5,28.27777777777778,24.615384615384617,43.333333333333336,39.0,37.0,23.176470588235293,24.833333333333332,27.666666666666668,20.363636363636363,29.46153846153846,26.5,12.875,21.833333333333332,35.666666666666664,35.0,28.333333333333332,44.0,40.6,36.166666666666664,26.583333333333332,19.526315789473685,25.416666666666668,36.2,33.166666666666664,29.166666666666668,42.5,8.625,11.083333333333334,16.916666666666668,29.5,37.4,38.25,12.294117647058824,28.75,10.666666666666666,12.23076923076923,32.666666666666664,18.416666666666668,32.833333333333336,31.2,32.0,12.5,34.4,16.8,21.666666666666668,32.333333333333336,37.666666666666664,27.833333333333332,13.166666666666666,30.6,13.833333333333334,16.5,33.0,26.75,34.75,17.0,21.666666666666668,35.0,21.666666666666668,29.0,13.23076923076923,11.4,9.857142857142858,16.0,22.4,19.833333333333332,33.25,19.5,24.4,17.4,30.8,11.666666666666666,10.0,19.6,19.75,24.5,27.4,8.076923076923077,15.444444444444445,31.333333333333332,13.833333333333334,21.5,7.75,3.7,16.6,20.0,13.0,35.5,6.777777777777778,15.222222222222221,18.666666666666668,21.6,28.25,9.555555555555555,4.222222222222222,18.0,10.0,10.8,16.285714285714285,10.416666666666666,11.454545454545455,7.5625,4.5,3.3333333333333335,21.6,17.2,15.2,13.8,14.5,7.666666666666667,11.8,22.6,10.5,9.333333333333334,15.0,9.333333333333334,3.75,3.7142857142857144,1.8461538461538463,3.466666666666667,12.333333333333334,8.714285714285714,10.833333333333334,3.5,2.888888888888889,10.333333333333334,4.0,3.875,7.0,3.6666666666666665,12.5,6.0,1.7777777777777777,2.0,7.333333333333333,14.4,2.111111111111111,2.6,12.0,15.2,2.142857142857143,2.4285714285714284,5.0,2.142857142857143,2.5,5.5,4.5,2.0,20.0,4.0,3.5,2.5,7.6,2.5,5.0,4.5,4.0,2.375,4.5,1.6666666666666667,1.6666666666666667,2.0,3.25,4.5,5.0,3.5,6.0,6.0],"xbins":{"end":45,"size":1,"start":0},"type":"histogram","opacity":0.5}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"barmode":"overlay"},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('3d29d914-624e-457e-a64e-cdcedcea8d43');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>



```python
# 75 % same values 
((hist_data(rs_df,50,5)>=12)&(hist_data(rs_df,50,5)<=34)).mean()
```




    0.7495223943960942



### has the game changed over the past 10 years?


```python
change_df = data.groupby('season_start_year')[total_cols].sum().reset_index()
change_df['POSS_est'] = change_df['FGA']-change_df['OREB']+change_df['TOV']+0.44*change_df['FTA']
change_df = change_df[list(change_df.columns[0:2])+['POSS_est']+list(change_df.columns[2:-1])]


change_df['FG%'] = change_df['FGM']/change_df['FGA']
change_df['3PT%'] = change_df['FG3M']/change_df['FG3A']
change_df['FT%'] = change_df['FTM']/change_df['FTA']
change_df['FG3A%'] = change_df['FG3A']/change_df['FGA']
change_df['PTS/FGA'] = change_df['PTS']/change_df['FGA']
change_df['FG3M/FGM'] = change_df['FG3M']/change_df['FGM']
change_df['FTA/FGA'] = change_df['FTA']/change_df['FGA']
change_df['TRU%'] = 0.5*change_df['PTS']/(change_df['FGA']+0.475*change_df['FTA'])
change_df['AST_TOV'] =  change_df['AST']/change_df['TOV']

change_df

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
      <th>season_start_year</th>
      <th>MIN</th>
      <th>POSS_est</th>
      <th>FGM</th>
      <th>FGA</th>
      <th>FG3M</th>
      <th>FG3A</th>
      <th>FTM</th>
      <th>FTA</th>
      <th>OREB</th>
      <th>DREB</th>
      <th>REB</th>
      <th>AST</th>
      <th>STL</th>
      <th>BLK</th>
      <th>TOV</th>
      <th>PF</th>
      <th>PTS</th>
      <th>FG%</th>
      <th>3PT%</th>
      <th>FT%</th>
      <th>FG3A%</th>
      <th>PTS/FGA</th>
      <th>FG3M/FGM</th>
      <th>FTA/FGA</th>
      <th>TRU%</th>
      <th>AST_TOV</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2012</td>
      <td>635884</td>
      <td>248201.92</td>
      <td>97235</td>
      <td>215105</td>
      <td>18808</td>
      <td>52569</td>
      <td>44125</td>
      <td>58618</td>
      <td>29237</td>
      <td>81362</td>
      <td>110599</td>
      <td>57694</td>
      <td>20376</td>
      <td>13444</td>
      <td>36542</td>
      <td>52548</td>
      <td>257403</td>
      <td>0.452035</td>
      <td>0.357777</td>
      <td>0.752755</td>
      <td>0.244388</td>
      <td>1.196639</td>
      <td>0.193428</td>
      <td>0.272509</td>
      <td>0.529748</td>
      <td>1.578841</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2013</td>
      <td>638373</td>
      <td>254032.80</td>
      <td>99251</td>
      <td>218411</td>
      <td>20480</td>
      <td>56952</td>
      <td>47219</td>
      <td>62420</td>
      <td>28669</td>
      <td>83812</td>
      <td>112481</td>
      <td>57657</td>
      <td>20156</td>
      <td>12369</td>
      <td>36826</td>
      <td>54839</td>
      <td>266201</td>
      <td>0.454423</td>
      <td>0.359601</td>
      <td>0.756472</td>
      <td>0.260756</td>
      <td>1.218808</td>
      <td>0.206346</td>
      <td>0.285791</td>
      <td>0.536565</td>
      <td>1.565660</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2014</td>
      <td>634546</td>
      <td>253004.12</td>
      <td>98251</td>
      <td>219265</td>
      <td>20724</td>
      <td>59276</td>
      <td>45098</td>
      <td>60248</td>
      <td>28566</td>
      <td>85231</td>
      <td>113797</td>
      <td>57727</td>
      <td>20261</td>
      <td>12665</td>
      <td>35796</td>
      <td>53272</td>
      <td>262324</td>
      <td>0.448092</td>
      <td>0.349619</td>
      <td>0.748539</td>
      <td>0.270340</td>
      <td>1.196379</td>
      <td>0.210929</td>
      <td>0.274773</td>
      <td>0.529129</td>
      <td>1.612666</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2015</td>
      <td>636391</td>
      <td>258064.80</td>
      <td>100351</td>
      <td>222344</td>
      <td>22524</td>
      <td>63673</td>
      <td>46516</td>
      <td>61520</td>
      <td>27426</td>
      <td>87611</td>
      <td>115037</td>
      <td>58251</td>
      <td>20562</td>
      <td>13046</td>
      <td>36078</td>
      <td>53478</td>
      <td>269742</td>
      <td>0.451332</td>
      <td>0.353745</td>
      <td>0.756112</td>
      <td>0.286372</td>
      <td>1.213174</td>
      <td>0.224452</td>
      <td>0.276688</td>
      <td>0.536126</td>
      <td>1.614585</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016</td>
      <td>632482</td>
      <td>258443.80</td>
      <td>102147</td>
      <td>223333</td>
      <td>25408</td>
      <td>71018</td>
      <td>46806</td>
      <td>60620</td>
      <td>26470</td>
      <td>87173</td>
      <td>113643</td>
      <td>59162</td>
      <td>20143</td>
      <td>12409</td>
      <td>34908</td>
      <td>52232</td>
      <td>276508</td>
      <td>0.457375</td>
      <td>0.357768</td>
      <td>0.772121</td>
      <td>0.317992</td>
      <td>1.238097</td>
      <td>0.248740</td>
      <td>0.271433</td>
      <td>0.548350</td>
      <td>1.694798</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2017</td>
      <td>633425</td>
      <td>260904.52</td>
      <td>103729</td>
      <td>225523</td>
      <td>27530</td>
      <td>76245</td>
      <td>43721</td>
      <td>57008</td>
      <td>25397</td>
      <td>88678</td>
      <td>114075</td>
      <td>60739</td>
      <td>20181</td>
      <td>12636</td>
      <td>35695</td>
      <td>52238</td>
      <td>278709</td>
      <td>0.459949</td>
      <td>0.361073</td>
      <td>0.766927</td>
      <td>0.338081</td>
      <td>1.235834</td>
      <td>0.265403</td>
      <td>0.252781</td>
      <td>0.551677</td>
      <td>1.701611</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2018</td>
      <td>634231</td>
      <td>268739.84</td>
      <td>107374</td>
      <td>233717</td>
      <td>29817</td>
      <td>84143</td>
      <td>46671</td>
      <td>60811</td>
      <td>27128</td>
      <td>91360</td>
      <td>118488</td>
      <td>64257</td>
      <td>19940</td>
      <td>12984</td>
      <td>35394</td>
      <td>55063</td>
      <td>291236</td>
      <td>0.459419</td>
      <td>0.354361</td>
      <td>0.767476</td>
      <td>0.360021</td>
      <td>1.246105</td>
      <td>0.277693</td>
      <td>0.260191</td>
      <td>0.554519</td>
      <td>1.815477</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2019</td>
      <td>552262</td>
      <td>234384.64</td>
      <td>92997</td>
      <td>202223</td>
      <td>28032</td>
      <td>78279</td>
      <td>40949</td>
      <td>52906</td>
      <td>22802</td>
      <td>79318</td>
      <td>102120</td>
      <td>55445</td>
      <td>17368</td>
      <td>11085</td>
      <td>31685</td>
      <td>47615</td>
      <td>254975</td>
      <td>0.459874</td>
      <td>0.358104</td>
      <td>0.773995</td>
      <td>0.387092</td>
      <td>1.260861</td>
      <td>0.301429</td>
      <td>0.261622</td>
      <td>0.560746</td>
      <td>1.749882</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2020</td>
      <td>562518</td>
      <td>235759.48</td>
      <td>95849</td>
      <td>205754</td>
      <td>29549</td>
      <td>80653</td>
      <td>39624</td>
      <td>50917</td>
      <td>22918</td>
      <td>80151</td>
      <td>103069</td>
      <td>57311</td>
      <td>17491</td>
      <td>11272</td>
      <td>30520</td>
      <td>45152</td>
      <td>260871</td>
      <td>0.465843</td>
      <td>0.366372</td>
      <td>0.778208</td>
      <td>0.391988</td>
      <td>1.267878</td>
      <td>0.308287</td>
      <td>0.247465</td>
      <td>0.567260</td>
      <td>1.877818</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2021</td>
      <td>635572</td>
      <td>264004.96</td>
      <td>106569</td>
      <td>231293</td>
      <td>32733</td>
      <td>92552</td>
      <td>44740</td>
      <td>57709</td>
      <td>27052</td>
      <td>89602</td>
      <td>116654</td>
      <td>64618</td>
      <td>20006</td>
      <td>12387</td>
      <td>34372</td>
      <td>52038</td>
      <td>290611</td>
      <td>0.460753</td>
      <td>0.353671</td>
      <td>0.775269</td>
      <td>0.400150</td>
      <td>1.256463</td>
      <td>0.307153</td>
      <td>0.249506</td>
      <td>0.561665</td>
      <td>1.879960</td>
    </tr>
  </tbody>
</table>
</div>




```python
change_per48_df = change_df.copy()
for col in change_per48_df.columns[2:18]:
    change_per48_df[col] = (change_per48_df[col]/change_per48_df['MIN'])*48*5
    
change_per48_df.drop(columns='MIN', inplace=True)

fig = go.Figure()
for col in change_per48_df.columns[1:]:
    fig.add_trace(go.Scatter(x=change_per48_df['season_start_year'],
                             y=change_per48_df[col], name=col))

fig.show()
```


<div>                            <div id="7bd06a7d-db39-4a96-a376-5ba092f4e1aa" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("7bd06a7d-db39-4a96-a376-5ba092f4e1aa")) {                    Plotly.newPlot(                        "7bd06a7d-db39-4a96-a376-5ba092f4e1aa",                        [{"name":"POSS_est","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[93.67818784558189,95.50509185068918,95.69202043665865,97.32311110622241,98.06842250056128,98.8547733354383,101.69411712767115,101.85801956317835,100.58749266690131,99.69160126626095],"type":"scatter"},{"name":"FGM","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[36.69914638518975,37.31398414406624,37.16080473283261,37.84503552061547,38.76043903225704,39.30214311086553,40.631504924861765,40.414296113076766,40.894264716862395,40.24179793949387],"type":"scatter"},{"name":"FGA","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[81.18650571487882,82.11287131504622,82.93110349761876,83.85184579920207,84.74536824763392,85.44897975293051,88.44108849930073,87.88133168677186,87.78556419527908,87.33915276318027],"type":"scatter"},{"name":"FG3M","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[7.098653213479188,7.699573760168428,7.8382969871372605,8.494400455066147,9.641254612779495,10.430911315467498,11.283081400940667,12.182044029826425,12.60716990389641,12.36039347233673],"type":"scatter"},{"name":"FG3A","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[19.84097728516522,21.41143187446837,22.419556659406883,24.012784593119637,26.94830841035792,28.888660851718832,31.84063850552874,34.01820150580703,34.41084551961004,34.948802024003584],"type":"scatter"},{"name":"FTM","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[16.653980914758037,17.75225455963833,17.057108546898096,17.54242281867594,17.760884894747992,16.565560247858862,17.660820741969406,17.795466644454983,16.905699017631434,16.89438804730227],"type":"scatter"},{"name":"FTA","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[22.124035201388928,23.467157915513344,22.78718958121239,23.20083093569834,23.002709958544276,21.59990527686782,23.011552573116102,22.991695970390865,21.7238915021386,21.791645950419465],"type":"scatter"},{"name":"OREB","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[11.034842832969536,10.778275396985775,10.804323090839748,10.343075247764347,10.04423841310899,9.622733551722778,10.265534166573378,9.909209759136061,9.77803376958604,10.215176250684424],"type":"scatter"},{"name":"DREB","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[30.708242383831017,31.509603319689276,32.236339051857556,33.04044211813178,33.07844333909898,33.59943166120693,34.571630841128865,34.46972632554838,34.19666570669739,33.834844832686144],"type":"scatter"},{"name":"REB","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[41.743085216800544,42.28787871667505,43.0406621426973,43.38351736589612,43.12268175220797,43.22216521292971,44.83716500770224,44.37893608468444,43.97469947628343,44.05002108337057],"type":"scatter"},{"name":"AST","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[21.77529234891899,21.676480678224173,21.83368896817567,21.968003947258836,22.449461012329202,23.013553301495836,24.315556950070242,24.09508530371454,24.451910872185422,24.4005714537456],"type":"scatter"},{"name":"STL","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[7.690459266155462,7.577764097165762,7.663179659157886,7.7544779860180295,7.643411195891741,7.646430121956032,7.5455157505703765,7.5477219145985055,7.462587863855024,7.554517820168289],"type":"scatter"},{"name":"BLK","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[5.074133017971832,4.650196671851723,4.79019645541852,4.919994154537069,4.708687361853777,4.787685992816829,4.913288691344321,4.817278755373355,4.809232771217989,4.677487365711517],"type":"scatter"},{"name":"TOV","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[13.79194947506149,13.844946449802858,13.538876614146176,13.605974943077449,13.246100284276865,13.52456881240873,13.393479662772712,13.769551408570567,13.021449980267299,12.979300535580549],"type":"scatter"},{"name":"PF","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[19.83305131124545,20.617037374701,20.148704743233743,20.16797849121059,19.81982095933165,19.792587914907052,20.83644602676312,20.692352542814824,19.264236877753245,19.65020485483942],"type":"scatter"},{"name":"PTS","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[97.15092689861672,100.07979660793924,99.21701499970058,101.72689431497302,104.92301757204157,105.60075778505743,110.20691199263361,110.80610290043494,111.30139835525263,109.73837739862674],"type":"scatter"},{"name":"FG%","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[0.45203505264870647,0.45442308308647456,0.44809249082160857,0.45133216997085596,0.45737530951538735,0.45994865268730906,0.4594188698297514,0.45987350598102095,0.4658427053666028,0.46075324372116755],"type":"scatter"},{"name":"3PT%","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[0.3577773973254199,0.35960106756566934,0.34961873270800997,0.35374491542726116,0.35776845306823624,0.3610728572365401,0.3543610282495276,0.3581037059747825,0.3663719886427039,0.3536714495634886],"type":"scatter"},{"name":"FT%","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[0.7527551264116824,0.756472284524191,0.7485393706015138,0.7561118335500651,0.7721214120752227,0.7669274487791187,0.7674762789626877,0.7739953880467244,0.7782076713082074,0.7752690221629208],"type":"scatter"},{"name":"FG3A%","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[0.2443876246484275,0.2607560974493043,0.2703395434747908,0.28637156838052746,0.31799151939032744,0.338080816590769,0.36002087995310567,0.38709246722677443,0.39198751907617835,0.4001504585093366],"type":"scatter"},{"name":"PTS/FGA","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[1.1966388507937984,1.2188076607863156,1.1963788110277518,1.213174180549059,1.2380973702945826,1.2358340391002247,1.246105332517532,1.2608605351517879,1.2678781457468629,1.2564625820928432],"type":"scatter"},{"name":"FG3M/FGM","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[0.19342829228158584,0.2063455280047556,0.2109291508483374,0.224452172873215,0.24873956161218636,0.26540311773949427,0.2776929237990575,0.3014290783573664,0.30828699308286994,0.3071531120682375],"type":"scatter"},{"name":"FTA/FGA","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[0.2725087747844076,0.2857914665470146,0.2747725355163843,0.2766883747706257,0.2714332409451357,0.25278131277075955,0.26019074350603505,0.2616220706843435,0.24746541987033058,0.2495060377962152],"type":"scatter"},{"name":"TRU%","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[0.5297479651555854,0.5365646686997728,0.5291290884240456,0.5361257085615703,0.5483495453689106,0.5516765913782087,0.5545192924393539,0.560746080935249,0.5672598986059707,0.5616653190881382],"type":"scatter"},{"name":"AST_TOV","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[1.57884078594494,1.5656601314288818,1.6126662196893509,1.6145850656910028,1.6947977540964823,1.7016108698697296,1.8154771995253434,1.7498816474672558,1.8778178243774575,1.8799604329105086],"type":"scatter"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}}},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('7bd06a7d-db39-4a96-a376-5ba092f4e1aa');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>



```python
change_per100_df = change_df.copy()


for col in change_per100_df.columns[3:18]:
    change_per100_df[col] = (change_per100_df[col]/change_per100_df['POSS_est'])*100
    
change_per100_df.drop(columns=['MIN','POSS_est'], inplace=True)
change_per100_df

fig = go.Figure()

for col in change_per100_df.columns[1:]:
    fig.add_trace(go.Scatter(x=change_per100_df['season_start_year'],
                             y=change_per100_df[col], name=col))

fig.show()
```


<div>                            <div id="828d0ea0-a299-4637-9948-e39c424a080d" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("828d0ea0-a299-4637-9948-e39c424a080d")) {                    Plotly.newPlot(                        "828d0ea0-a299-4637-9948-e39c424a080d",                        [{"name":"FGM","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[39.17576463550322,39.07015157097824,38.833754960195904,38.885969725433306,39.52387327535038,39.757456099265745,39.95462674979638,39.67708805491691,40.655417122569155,40.366287057637095],"type":"scatter"},{"name":"FGA","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[86.66532474849508,85.97748007343934,86.6645966081501,86.15820522597426,86.4145319021002,86.4389010968457,86.96775290183993,86.2782646507894,87.27284264454605,87.60933885484576],"type":"scatter"},{"name":"FG3M","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[7.577701252270732,8.061951055139337,8.191170958006534,8.72804039915556,9.831150911726263,10.5517528021362,11.09511712145099,11.959828084297673,12.533536297246666,12.39863069239305],"type":"scatter"},{"name":"FG3A","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[21.179932854669296,22.419152172475364,23.4288674824742,24.673260359413607,27.479088296952764,29.223334268030314,31.310206927264673,33.39766633171866,34.20986507096131,35.056917112466365],"type":"scatter"},{"name":"FTM","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[17.77786408743333,18.58775717151486,17.82500616986,18.024930172576813,18.110707240800515,16.757471277231993,17.366610027006043,17.470854745430415,16.80695936383979,16.94665130533911],"type":"scatter"},{"name":"FTA","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[23.617061463505195,24.57163012020495,23.81305094952604,23.838973777128846,23.45577645894388,21.8501388937225,22.62820428857887,22.57229825299132,21.597010648309876,21.859059011618566],"type":"scatter"},{"name":"OREB","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[11.779522092335142,11.285550527333479,11.290725226134658,10.62756330968036,10.242071970772756,9.734212347106903,10.09452115473463,9.728453195567765,9.720924053615999,10.246777181762038],"type":"scatter"},{"name":"DREB","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[32.78056833726347,32.99258993326846,33.68759370400767,33.94922515585233,33.72996372905831,33.98867907692822,33.995703800374365,33.84095476563652,33.996936199553886,33.93951386367892],"type":"scatter"},{"name":"REB","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[44.56009042959861,44.27814046060194,44.97831893014232,44.576788465532694,43.97203569983107,43.722891424035126,44.090224955109,43.569407961204284,43.71786025316988,44.18629104544096],"type":"scatter"},{"name":"AST","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[23.244783924314525,22.696675389949643,22.81662448817039,22.572237670538563,22.891630598219034,23.280163946565587,23.9104853229056,23.655560364365172,24.309096711614732,24.476055298355],"type":"scatter"},{"name":"STL","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[8.20944495513975,7.934408470087327,8.008169985532252,7.967766235457141,7.79395752577543,7.735013559749751,7.419815387253337,7.410041886703839,7.419001772484397,7.577887930590395],"type":"scatter"},{"name":"BLK","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[5.416557615670338,4.869056279346604,5.005847335608606,5.055319439148617,4.801430717239106,4.843151050046968,4.831438464799264,4.729405476399819,4.781143901403243,4.6919573026203745],"type":"scatter"},{"name":"TOV","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[14.722690299897758,14.496553201003964,14.148386200193103,13.980209621769415,13.506998426737264,13.681250137023307,13.17035836591999,13.51837731346218,12.945396723813607,13.01945236180411],"type":"scatter"},{"name":"PF","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[21.17147200150587,21.58736981996026,21.05578359751612,20.722702205027577,20.210196568847852,20.021883867707622,20.48933273161136,20.31489776804487,19.151721915911928,19.710993308610565],"type":"scatter"},{"name":"PTS","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[103.7070946107105,104.79001136861068,103.68368704825835,104.52491002259899,106.98960470322756,106.82413627789968,108.3709806480498,108.78485893956191,110.65132990622477,110.07785611300636],"type":"scatter"},{"name":"FG%","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[0.45203505264870647,0.45442308308647456,0.44809249082160857,0.45133216997085596,0.45737530951538735,0.45994865268730906,0.4594188698297514,0.45987350598102095,0.4658427053666028,0.46075324372116755],"type":"scatter"},{"name":"3PT%","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[0.3577773973254199,0.35960106756566934,0.34961873270800997,0.35374491542726116,0.35776845306823624,0.3610728572365401,0.3543610282495276,0.3581037059747825,0.3663719886427039,0.3536714495634886],"type":"scatter"},{"name":"FT%","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[0.7527551264116824,0.756472284524191,0.7485393706015138,0.7561118335500651,0.7721214120752227,0.7669274487791187,0.7674762789626877,0.7739953880467244,0.7782076713082074,0.7752690221629208],"type":"scatter"},{"name":"FG3A%","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[0.2443876246484275,0.2607560974493043,0.2703395434747908,0.28637156838052746,0.31799151939032744,0.338080816590769,0.36002087995310567,0.38709246722677443,0.39198751907617835,0.4001504585093366],"type":"scatter"},{"name":"PTS/FGA","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[1.1966388507937984,1.2188076607863156,1.1963788110277518,1.213174180549059,1.2380973702945826,1.2358340391002247,1.246105332517532,1.2608605351517879,1.2678781457468629,1.2564625820928432],"type":"scatter"},{"name":"FG3M/FGM","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[0.19342829228158584,0.2063455280047556,0.2109291508483374,0.224452172873215,0.24873956161218636,0.26540311773949427,0.2776929237990575,0.3014290783573664,0.30828699308286994,0.3071531120682375],"type":"scatter"},{"name":"FTA/FGA","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[0.2725087747844076,0.2857914665470146,0.2747725355163843,0.2766883747706257,0.2714332409451357,0.25278131277075955,0.26019074350603505,0.2616220706843435,0.24746541987033058,0.2495060377962152],"type":"scatter"},{"name":"TRU%","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[0.5297479651555854,0.5365646686997728,0.5291290884240456,0.5361257085615703,0.5483495453689106,0.5516765913782087,0.5545192924393539,0.560746080935249,0.5672598986059707,0.5616653190881382],"type":"scatter"},{"name":"AST_TOV","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[1.57884078594494,1.5656601314288818,1.6126662196893509,1.6145850656910028,1.6947977540964823,1.7016108698697296,1.8154771995253434,1.7498816474672558,1.8778178243774575,1.8799604329105086],"type":"scatter"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}}},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('828d0ea0-a299-4637-9948-e39c424a080d');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>


### Comparte RS to Playoffs


```python
rs_change_df = rs_df.groupby('season_start_year')[total_cols].sum().reset_index()
playoffs_change_df = playoffs_df.groupby('season_start_year')[total_cols].sum().reset_index()

for i in [rs_change_df, playoffs_change_df]:
    i['POSS_est'] = i['FGA']-i['OREB']+i['TOV']+0.44*i['FTA']
    i['POSS_per_48'] = (i['POSS_est']/i['MIN'])*48*5
    
    i['FG%'] = i['FGM']/i['FGA']
    i['3PT%'] = i['FG3M']/i['FG3A']
    i['FT%'] = i['FTM']/i['FTA']
    i['FG3A%'] = i['FG3A']/i['FGA']
    i['PTS/FGA'] = i['PTS']/i['FGA']
    i['FG3M/FGM'] = i['FG3M']/i['FGM']
    i['FTA/FGA'] = i['FTA']/i['FGA']
    i['TRU%'] = 0.5*i['PTS']/(i['FGA']+0.475*i['FTA'])
    i['AST_TOV'] =  i['AST']/i['TOV']
    for col in total_cols:
        i[col] = 100*i[col]/i['POSS_est']
    i.drop(columns=['MIN','POSS_est'], inplace=True)

rs_change_df

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
      <th>season_start_year</th>
      <th>FGM</th>
      <th>FGA</th>
      <th>FG3M</th>
      <th>FG3A</th>
      <th>FTM</th>
      <th>FTA</th>
      <th>OREB</th>
      <th>DREB</th>
      <th>REB</th>
      <th>AST</th>
      <th>STL</th>
      <th>BLK</th>
      <th>TOV</th>
      <th>PF</th>
      <th>PTS</th>
      <th>POSS_per_48</th>
      <th>FG%</th>
      <th>3PT%</th>
      <th>FT%</th>
      <th>FG3A%</th>
      <th>PTS/FGA</th>
      <th>FG3M/FGM</th>
      <th>FTA/FGA</th>
      <th>TRU%</th>
      <th>AST_TOV</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2012</td>
      <td>39.270953</td>
      <td>86.735365</td>
      <td>7.573088</td>
      <td>21.109396</td>
      <td>17.662937</td>
      <td>23.460955</td>
      <td>11.812003</td>
      <td>32.747162</td>
      <td>44.559165</td>
      <td>23.410189</td>
      <td>8.250677</td>
      <td>5.430183</td>
      <td>14.753819</td>
      <td>20.983773</td>
      <td>103.777931</td>
      <td>93.838988</td>
      <td>0.452767</td>
      <td>0.358754</td>
      <td>0.752865</td>
      <td>0.243377</td>
      <td>1.196489</td>
      <td>0.192842</td>
      <td>0.270489</td>
      <td>0.530132</td>
      <td>1.586721</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2013</td>
      <td>39.077222</td>
      <td>85.994401</td>
      <td>8.025279</td>
      <td>22.311911</td>
      <td>18.477433</td>
      <td>24.441006</td>
      <td>11.307161</td>
      <td>32.985187</td>
      <td>44.292348</td>
      <td>22.799223</td>
      <td>7.958311</td>
      <td>4.883231</td>
      <td>14.558717</td>
      <td>21.448058</td>
      <td>104.657155</td>
      <td>95.735469</td>
      <td>0.454416</td>
      <td>0.359686</td>
      <td>0.756001</td>
      <td>0.259458</td>
      <td>1.217023</td>
      <td>0.205370</td>
      <td>0.284216</td>
      <td>0.536132</td>
      <td>1.566019</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2014</td>
      <td>38.900086</td>
      <td>86.650240</td>
      <td>8.135183</td>
      <td>23.240912</td>
      <td>17.771371</td>
      <td>23.688136</td>
      <td>11.288515</td>
      <td>33.604208</td>
      <td>44.892723</td>
      <td>22.846798</td>
      <td>8.021797</td>
      <td>4.972578</td>
      <td>14.215495</td>
      <td>20.960953</td>
      <td>103.706727</td>
      <td>95.659492</td>
      <td>0.448932</td>
      <td>0.350037</td>
      <td>0.750222</td>
      <td>0.268215</td>
      <td>1.196843</td>
      <td>0.209130</td>
      <td>0.273376</td>
      <td>0.529645</td>
      <td>1.607176</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2015</td>
      <td>38.926558</td>
      <td>86.096120</td>
      <td>8.670900</td>
      <td>24.515476</td>
      <td>17.996886</td>
      <td>23.782176</td>
      <td>10.603882</td>
      <td>33.942436</td>
      <td>44.546317</td>
      <td>22.690502</td>
      <td>7.988086</td>
      <td>5.045782</td>
      <td>14.043605</td>
      <td>20.630890</td>
      <td>104.520902</td>
      <td>97.493488</td>
      <td>0.452129</td>
      <td>0.353691</td>
      <td>0.756738</td>
      <td>0.284745</td>
      <td>1.214002</td>
      <td>0.222750</td>
      <td>0.276228</td>
      <td>0.536595</td>
      <td>1.615718</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016</td>
      <td>39.516445</td>
      <td>86.434227</td>
      <td>9.769173</td>
      <td>27.323490</td>
      <td>18.052073</td>
      <td>23.388341</td>
      <td>10.257879</td>
      <td>33.777035</td>
      <td>44.034914</td>
      <td>22.896756</td>
      <td>7.795428</td>
      <td>4.800256</td>
      <td>13.532781</td>
      <td>20.136476</td>
      <td>106.854135</td>
      <td>98.151085</td>
      <td>0.457185</td>
      <td>0.357538</td>
      <td>0.771841</td>
      <td>0.316119</td>
      <td>1.236248</td>
      <td>0.247218</td>
      <td>0.270591</td>
      <td>0.547724</td>
      <td>1.691948</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2017</td>
      <td>39.782703</td>
      <td>86.439951</td>
      <td>10.536996</td>
      <td>29.127708</td>
      <td>16.700692</td>
      <td>21.772593</td>
      <td>9.754285</td>
      <td>33.953813</td>
      <td>43.708098</td>
      <td>23.339648</td>
      <td>7.750757</td>
      <td>4.836313</td>
      <td>13.734393</td>
      <td>19.940143</td>
      <td>106.803093</td>
      <td>98.979263</td>
      <td>0.460235</td>
      <td>0.361752</td>
      <td>0.767051</td>
      <td>0.336970</td>
      <td>1.235576</td>
      <td>0.264864</td>
      <td>0.251881</td>
      <td>0.551772</td>
      <td>1.699358</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2018</td>
      <td>40.060963</td>
      <td>86.993122</td>
      <td>11.081358</td>
      <td>31.213318</td>
      <td>17.241016</td>
      <td>22.498864</td>
      <td>10.089962</td>
      <td>33.952838</td>
      <td>44.042800</td>
      <td>23.975453</td>
      <td>7.443993</td>
      <td>4.830132</td>
      <td>13.197341</td>
      <td>20.384863</td>
      <td>108.444300</td>
      <td>101.847754</td>
      <td>0.460507</td>
      <td>0.355020</td>
      <td>0.766306</td>
      <td>0.358802</td>
      <td>1.246585</td>
      <td>0.276612</td>
      <td>0.258628</td>
      <td>0.555099</td>
      <td>1.816688</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2019</td>
      <td>39.741774</td>
      <td>86.378550</td>
      <td>11.875237</td>
      <td>33.176460</td>
      <td>17.368831</td>
      <td>22.473502</td>
      <td>9.798838</td>
      <td>33.803237</td>
      <td>43.602075</td>
      <td>23.716035</td>
      <td>7.438668</td>
      <td>4.765339</td>
      <td>13.531948</td>
      <td>20.205627</td>
      <td>108.727615</td>
      <td>102.071250</td>
      <td>0.460088</td>
      <td>0.357942</td>
      <td>0.772858</td>
      <td>0.384082</td>
      <td>1.258734</td>
      <td>0.298810</td>
      <td>0.260175</td>
      <td>0.560143</td>
      <td>1.752596</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2020</td>
      <td>40.637565</td>
      <td>87.183600</td>
      <td>12.520406</td>
      <td>34.156188</td>
      <td>16.730698</td>
      <td>21.517093</td>
      <td>9.692393</td>
      <td>33.988197</td>
      <td>43.680589</td>
      <td>24.457861</td>
      <td>7.466502</td>
      <td>4.804198</td>
      <td>13.041271</td>
      <td>19.021868</td>
      <td>110.526234</td>
      <td>100.810750</td>
      <td>0.466115</td>
      <td>0.366563</td>
      <td>0.777554</td>
      <td>0.391773</td>
      <td>1.267741</td>
      <td>0.308099</td>
      <td>0.246802</td>
      <td>0.567359</td>
      <td>1.875420</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2021</td>
      <td>40.444286</td>
      <td>87.713064</td>
      <td>12.383811</td>
      <td>35.022979</td>
      <td>16.859678</td>
      <td>21.766578</td>
      <td>10.288949</td>
      <td>33.966643</td>
      <td>44.255592</td>
      <td>24.540976</td>
      <td>7.597520</td>
      <td>4.692395</td>
      <td>12.998590</td>
      <td>19.550702</td>
      <td>110.132061</td>
      <td>99.871250</td>
      <td>0.461098</td>
      <td>0.353591</td>
      <td>0.774567</td>
      <td>0.399290</td>
      <td>1.255595</td>
      <td>0.306194</td>
      <td>0.248157</td>
      <td>0.561599</td>
      <td>1.887972</td>
    </tr>
  </tbody>
</table>
</div>




```python
comp_change_df = round(100*(playoffs_change_df-rs_change_df)/rs_change_df,2)
comp_change_df['season_start_year'] = list(range(2012,2022))
comp_change_df
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
      <th>season_start_year</th>
      <th>FGM</th>
      <th>FGA</th>
      <th>FG3M</th>
      <th>FG3A</th>
      <th>FTM</th>
      <th>FTA</th>
      <th>OREB</th>
      <th>DREB</th>
      <th>REB</th>
      <th>AST</th>
      <th>STL</th>
      <th>BLK</th>
      <th>TOV</th>
      <th>PF</th>
      <th>PTS</th>
      <th>POSS_per_48</th>
      <th>FG%</th>
      <th>3PT%</th>
      <th>FT%</th>
      <th>FG3A%</th>
      <th>PTS/FGA</th>
      <th>FG3M/FGM</th>
      <th>FTA/FGA</th>
      <th>TRU%</th>
      <th>AST_TOV</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2012</td>
      <td>-3.82</td>
      <td>-1.27</td>
      <td>0.96</td>
      <td>5.26</td>
      <td>10.25</td>
      <td>10.48</td>
      <td>-4.33</td>
      <td>1.61</td>
      <td>0.03</td>
      <td>-11.13</td>
      <td>-7.87</td>
      <td>-3.95</td>
      <td>-3.32</td>
      <td>14.09</td>
      <td>-1.07</td>
      <td>-2.63</td>
      <td>-2.58</td>
      <td>-4.09</td>
      <td>-0.21</td>
      <td>6.62</td>
      <td>0.20</td>
      <td>4.97</td>
      <td>11.90</td>
      <td>-1.14</td>
      <td>-8.07</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2013</td>
      <td>-0.28</td>
      <td>-0.30</td>
      <td>6.99</td>
      <td>7.35</td>
      <td>9.13</td>
      <td>8.17</td>
      <td>-2.92</td>
      <td>0.34</td>
      <td>-0.49</td>
      <td>-6.88</td>
      <td>-4.59</td>
      <td>-4.44</td>
      <td>-6.53</td>
      <td>9.94</td>
      <td>1.94</td>
      <td>-3.56</td>
      <td>0.02</td>
      <td>-0.34</td>
      <td>0.89</td>
      <td>7.68</td>
      <td>2.25</td>
      <td>7.29</td>
      <td>8.50</td>
      <td>1.23</td>
      <td>-0.37</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2014</td>
      <td>-2.74</td>
      <td>0.27</td>
      <td>11.05</td>
      <td>12.98</td>
      <td>4.84</td>
      <td>8.46</td>
      <td>0.31</td>
      <td>3.98</td>
      <td>3.06</td>
      <td>-2.12</td>
      <td>-2.73</td>
      <td>10.74</td>
      <td>-7.58</td>
      <td>7.26</td>
      <td>-0.36</td>
      <td>0.55</td>
      <td>-2.99</td>
      <td>-1.71</td>
      <td>-3.34</td>
      <td>12.68</td>
      <td>-0.62</td>
      <td>14.17</td>
      <td>8.18</td>
      <td>-1.55</td>
      <td>5.90</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2015</td>
      <td>-1.64</td>
      <td>1.13</td>
      <td>10.36</td>
      <td>10.12</td>
      <td>2.45</td>
      <td>3.75</td>
      <td>3.51</td>
      <td>0.31</td>
      <td>1.08</td>
      <td>-8.19</td>
      <td>-4.00</td>
      <td>2.97</td>
      <td>-7.10</td>
      <td>7.00</td>
      <td>0.06</td>
      <td>-2.68</td>
      <td>-2.74</td>
      <td>0.22</td>
      <td>-1.26</td>
      <td>8.88</td>
      <td>-1.06</td>
      <td>12.20</td>
      <td>2.59</td>
      <td>-1.36</td>
      <td>-1.18</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016</td>
      <td>0.32</td>
      <td>-0.38</td>
      <td>10.68</td>
      <td>9.59</td>
      <td>5.47</td>
      <td>4.85</td>
      <td>-2.59</td>
      <td>-2.35</td>
      <td>-2.40</td>
      <td>-0.38</td>
      <td>-0.32</td>
      <td>0.41</td>
      <td>-3.21</td>
      <td>6.16</td>
      <td>2.13</td>
      <td>-1.40</td>
      <td>0.70</td>
      <td>1.00</td>
      <td>0.59</td>
      <td>10.01</td>
      <td>2.53</td>
      <td>10.33</td>
      <td>5.26</td>
      <td>1.92</td>
      <td>2.92</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2017</td>
      <td>-1.04</td>
      <td>-0.02</td>
      <td>2.29</td>
      <td>5.36</td>
      <td>5.55</td>
      <td>5.81</td>
      <td>-3.36</td>
      <td>1.68</td>
      <td>0.55</td>
      <td>-4.16</td>
      <td>-3.32</td>
      <td>2.31</td>
      <td>-6.31</td>
      <td>6.69</td>
      <td>0.32</td>
      <td>-2.01</td>
      <td>-1.02</td>
      <td>-2.92</td>
      <td>-0.25</td>
      <td>5.38</td>
      <td>0.34</td>
      <td>3.36</td>
      <td>5.83</td>
      <td>-0.28</td>
      <td>2.30</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2018</td>
      <td>-4.33</td>
      <td>-0.48</td>
      <td>2.03</td>
      <td>5.07</td>
      <td>11.89</td>
      <td>9.38</td>
      <td>0.74</td>
      <td>2.06</td>
      <td>1.76</td>
      <td>-4.42</td>
      <td>-5.30</td>
      <td>0.44</td>
      <td>-3.34</td>
      <td>8.36</td>
      <td>-1.10</td>
      <td>-2.41</td>
      <td>-3.87</td>
      <td>-2.89</td>
      <td>2.29</td>
      <td>5.57</td>
      <td>-0.63</td>
      <td>6.65</td>
      <td>9.90</td>
      <td>-1.70</td>
      <td>-1.12</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2019</td>
      <td>-2.30</td>
      <td>-1.64</td>
      <td>10.06</td>
      <td>9.41</td>
      <td>8.29</td>
      <td>6.21</td>
      <td>-10.14</td>
      <td>1.58</td>
      <td>-1.06</td>
      <td>-3.60</td>
      <td>-5.43</td>
      <td>-10.64</td>
      <td>-1.42</td>
      <td>7.63</td>
      <td>0.74</td>
      <td>-2.87</td>
      <td>-0.67</td>
      <td>0.59</td>
      <td>1.96</td>
      <td>11.24</td>
      <td>2.42</td>
      <td>12.64</td>
      <td>7.98</td>
      <td>1.53</td>
      <td>-2.22</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2020</td>
      <td>0.62</td>
      <td>1.44</td>
      <td>1.48</td>
      <td>2.22</td>
      <td>6.43</td>
      <td>5.24</td>
      <td>4.16</td>
      <td>0.36</td>
      <td>1.20</td>
      <td>-8.59</td>
      <td>-8.98</td>
      <td>-6.77</td>
      <td>-10.38</td>
      <td>9.64</td>
      <td>1.60</td>
      <td>-3.04</td>
      <td>-0.81</td>
      <td>-0.72</td>
      <td>1.13</td>
      <td>0.76</td>
      <td>0.15</td>
      <td>0.86</td>
      <td>3.74</td>
      <td>-0.24</td>
      <td>2.00</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2021</td>
      <td>-3.01</td>
      <td>-1.84</td>
      <td>1.87</td>
      <td>1.51</td>
      <td>8.05</td>
      <td>6.63</td>
      <td>-6.39</td>
      <td>-1.25</td>
      <td>-2.44</td>
      <td>-4.13</td>
      <td>-4.03</td>
      <td>-0.15</td>
      <td>2.50</td>
      <td>12.79</td>
      <td>-0.77</td>
      <td>-2.73</td>
      <td>-1.19</td>
      <td>0.35</td>
      <td>1.33</td>
      <td>3.42</td>
      <td>1.10</td>
      <td>5.03</td>
      <td>8.63</td>
      <td>0.19</td>
      <td>-6.47</td>
    </tr>
  </tbody>
</table>
</div>




```python
fig = go.Figure()
for col in comp_change_df.columns[1:]:
    fig.add_trace(go.Scatter(x=comp_change_df['season_start_year'],
                             y=comp_change_df[col], name=col))
    
fig.show()
```


<div>                            <div id="7f9b18a8-bb08-4638-a27e-233eab2be9cd" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("7f9b18a8-bb08-4638-a27e-233eab2be9cd")) {                    Plotly.newPlot(                        "7f9b18a8-bb08-4638-a27e-233eab2be9cd",                        [{"name":"FGM","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[-3.82,-0.28,-2.74,-1.64,0.32,-1.04,-4.33,-2.3,0.62,-3.01],"type":"scatter"},{"name":"FGA","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[-1.27,-0.3,0.27,1.13,-0.38,-0.02,-0.48,-1.64,1.44,-1.84],"type":"scatter"},{"name":"FG3M","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[0.96,6.99,11.05,10.36,10.68,2.29,2.03,10.06,1.48,1.87],"type":"scatter"},{"name":"FG3A","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[5.26,7.35,12.98,10.12,9.59,5.36,5.07,9.41,2.22,1.51],"type":"scatter"},{"name":"FTM","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[10.25,9.13,4.84,2.45,5.47,5.55,11.89,8.29,6.43,8.05],"type":"scatter"},{"name":"FTA","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[10.48,8.17,8.46,3.75,4.85,5.81,9.38,6.21,5.24,6.63],"type":"scatter"},{"name":"OREB","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[-4.33,-2.92,0.31,3.51,-2.59,-3.36,0.74,-10.14,4.16,-6.39],"type":"scatter"},{"name":"DREB","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[1.61,0.34,3.98,0.31,-2.35,1.68,2.06,1.58,0.36,-1.25],"type":"scatter"},{"name":"REB","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[0.03,-0.49,3.06,1.08,-2.4,0.55,1.76,-1.06,1.2,-2.44],"type":"scatter"},{"name":"AST","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[-11.13,-6.88,-2.12,-8.19,-0.38,-4.16,-4.42,-3.6,-8.59,-4.13],"type":"scatter"},{"name":"STL","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[-7.87,-4.59,-2.73,-4.0,-0.32,-3.32,-5.3,-5.43,-8.98,-4.03],"type":"scatter"},{"name":"BLK","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[-3.95,-4.44,10.74,2.97,0.41,2.31,0.44,-10.64,-6.77,-0.15],"type":"scatter"},{"name":"TOV","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[-3.32,-6.53,-7.58,-7.1,-3.21,-6.31,-3.34,-1.42,-10.38,2.5],"type":"scatter"},{"name":"PF","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[14.09,9.94,7.26,7.0,6.16,6.69,8.36,7.63,9.64,12.79],"type":"scatter"},{"name":"PTS","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[-1.07,1.94,-0.36,0.06,2.13,0.32,-1.1,0.74,1.6,-0.77],"type":"scatter"},{"name":"POSS_per_48","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[-2.63,-3.56,0.55,-2.68,-1.4,-2.01,-2.41,-2.87,-3.04,-2.73],"type":"scatter"},{"name":"FG%","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[-2.58,0.02,-2.99,-2.74,0.7,-1.02,-3.87,-0.67,-0.81,-1.19],"type":"scatter"},{"name":"3PT%","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[-4.09,-0.34,-1.71,0.22,1.0,-2.92,-2.89,0.59,-0.72,0.35],"type":"scatter"},{"name":"FT%","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[-0.21,0.89,-3.34,-1.26,0.59,-0.25,2.29,1.96,1.13,1.33],"type":"scatter"},{"name":"FG3A%","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[6.62,7.68,12.68,8.88,10.01,5.38,5.57,11.24,0.76,3.42],"type":"scatter"},{"name":"PTS/FGA","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[0.2,2.25,-0.62,-1.06,2.53,0.34,-0.63,2.42,0.15,1.1],"type":"scatter"},{"name":"FG3M/FGM","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[4.97,7.29,14.17,12.2,10.33,3.36,6.65,12.64,0.86,5.03],"type":"scatter"},{"name":"FTA/FGA","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[11.9,8.5,8.18,2.59,5.26,5.83,9.9,7.98,3.74,8.63],"type":"scatter"},{"name":"TRU%","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[-1.14,1.23,-1.55,-1.36,1.92,-0.28,-1.7,1.53,-0.24,0.19],"type":"scatter"},{"name":"AST_TOV","x":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],"y":[-8.07,-0.37,5.9,-1.18,2.92,2.3,-1.12,-2.22,2.0,-6.47],"type":"scatter"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}}},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('7f9b18a8-bb08-4638-a27e-233eab2be9cd');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>


**Made by** | **DataSpieler12345**
