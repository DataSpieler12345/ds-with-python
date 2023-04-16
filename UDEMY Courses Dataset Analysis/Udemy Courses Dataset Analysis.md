### UDEMY COURSE DATASET ANALYSIS

This dataset contains all course data for all subjects.

We will analyze this data using the Pandas Library.

Herem the questions are given for the practice and learning purpose.


```python
#import pandas
import pandas as pd
```


```python
#import the dataset
data = pd.read_csv(r"E:\DATA SETS\udemy_courses.csv")
print('Dataset imported')
```

    Dataset imported
    


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
      <th>course_id</th>
      <th>course_title</th>
      <th>url</th>
      <th>is_paid</th>
      <th>price</th>
      <th>num_subscribers</th>
      <th>num_reviews</th>
      <th>num_lectures</th>
      <th>level</th>
      <th>content_duration</th>
      <th>published_timestamp</th>
      <th>subject</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1070968</td>
      <td>Ultimate Investment Banking Course</td>
      <td>https://www.udemy.com/ultimate-investment-bank...</td>
      <td>True</td>
      <td>200</td>
      <td>2147</td>
      <td>23</td>
      <td>51</td>
      <td>All Levels</td>
      <td>1.5</td>
      <td>2017-01-18T20:58:58Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1113822</td>
      <td>Complete GST Course &amp; Certification - Grow You...</td>
      <td>https://www.udemy.com/goods-and-services-tax/</td>
      <td>True</td>
      <td>75</td>
      <td>2792</td>
      <td>923</td>
      <td>274</td>
      <td>All Levels</td>
      <td>39.0</td>
      <td>2017-03-09T16:34:20Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1006314</td>
      <td>Financial Modeling for Business Analysts and C...</td>
      <td>https://www.udemy.com/financial-modeling-for-b...</td>
      <td>True</td>
      <td>45</td>
      <td>2174</td>
      <td>74</td>
      <td>51</td>
      <td>Intermediate Level</td>
      <td>2.5</td>
      <td>2016-12-19T19:26:30Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1210588</td>
      <td>Beginner to Pro - Financial Analysis in Excel ...</td>
      <td>https://www.udemy.com/complete-excel-finance-c...</td>
      <td>True</td>
      <td>95</td>
      <td>2451</td>
      <td>11</td>
      <td>36</td>
      <td>All Levels</td>
      <td>3.0</td>
      <td>2017-05-30T20:07:24Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1011058</td>
      <td>How To Maximize Your Profits Trading Options</td>
      <td>https://www.udemy.com/how-to-maximize-your-pro...</td>
      <td>True</td>
      <td>200</td>
      <td>1276</td>
      <td>45</td>
      <td>26</td>
      <td>Intermediate Level</td>
      <td>2.0</td>
      <td>2016-12-13T14:57:18Z</td>
      <td>Business Finance</td>
    </tr>
  </tbody>
</table>
</div>




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
      <th>course_id</th>
      <th>course_title</th>
      <th>url</th>
      <th>is_paid</th>
      <th>price</th>
      <th>num_subscribers</th>
      <th>num_reviews</th>
      <th>num_lectures</th>
      <th>level</th>
      <th>content_duration</th>
      <th>published_timestamp</th>
      <th>subject</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1070968</td>
      <td>Ultimate Investment Banking Course</td>
      <td>https://www.udemy.com/ultimate-investment-bank...</td>
      <td>True</td>
      <td>200</td>
      <td>2147</td>
      <td>23</td>
      <td>51</td>
      <td>All Levels</td>
      <td>1.5</td>
      <td>2017-01-18T20:58:58Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1113822</td>
      <td>Complete GST Course &amp; Certification - Grow You...</td>
      <td>https://www.udemy.com/goods-and-services-tax/</td>
      <td>True</td>
      <td>75</td>
      <td>2792</td>
      <td>923</td>
      <td>274</td>
      <td>All Levels</td>
      <td>39.0</td>
      <td>2017-03-09T16:34:20Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1006314</td>
      <td>Financial Modeling for Business Analysts and C...</td>
      <td>https://www.udemy.com/financial-modeling-for-b...</td>
      <td>True</td>
      <td>45</td>
      <td>2174</td>
      <td>74</td>
      <td>51</td>
      <td>Intermediate Level</td>
      <td>2.5</td>
      <td>2016-12-19T19:26:30Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1210588</td>
      <td>Beginner to Pro - Financial Analysis in Excel ...</td>
      <td>https://www.udemy.com/complete-excel-finance-c...</td>
      <td>True</td>
      <td>95</td>
      <td>2451</td>
      <td>11</td>
      <td>36</td>
      <td>All Levels</td>
      <td>3.0</td>
      <td>2017-05-30T20:07:24Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1011058</td>
      <td>How To Maximize Your Profits Trading Options</td>
      <td>https://www.udemy.com/how-to-maximize-your-pro...</td>
      <td>True</td>
      <td>200</td>
      <td>1276</td>
      <td>45</td>
      <td>26</td>
      <td>Intermediate Level</td>
      <td>2.0</td>
      <td>2016-12-13T14:57:18Z</td>
      <td>Business Finance</td>
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
    </tr>
    <tr>
      <th>3673</th>
      <td>775618</td>
      <td>Learn jQuery from Scratch - Master of JavaScri...</td>
      <td>https://www.udemy.com/easy-jquery-for-beginner...</td>
      <td>True</td>
      <td>100</td>
      <td>1040</td>
      <td>14</td>
      <td>21</td>
      <td>All Levels</td>
      <td>2.0</td>
      <td>2016-06-14T17:36:46Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>3674</th>
      <td>1088178</td>
      <td>How To Design A WordPress Website With No Codi...</td>
      <td>https://www.udemy.com/how-to-make-a-wordpress-...</td>
      <td>True</td>
      <td>25</td>
      <td>306</td>
      <td>3</td>
      <td>42</td>
      <td>Beginner Level</td>
      <td>3.5</td>
      <td>2017-03-10T22:24:30Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>3675</th>
      <td>635248</td>
      <td>Learn and Build using Polymer</td>
      <td>https://www.udemy.com/learn-and-build-using-po...</td>
      <td>True</td>
      <td>40</td>
      <td>513</td>
      <td>169</td>
      <td>48</td>
      <td>All Levels</td>
      <td>3.5</td>
      <td>2015-12-30T16:41:42Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>3676</th>
      <td>905096</td>
      <td>CSS Animations: Create Amazing Effects on Your...</td>
      <td>https://www.udemy.com/css-animations-create-am...</td>
      <td>True</td>
      <td>50</td>
      <td>300</td>
      <td>31</td>
      <td>38</td>
      <td>All Levels</td>
      <td>3.0</td>
      <td>2016-08-11T19:06:15Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>3677</th>
      <td>297602</td>
      <td>Using MODX CMS to Build Websites: A Beginner's...</td>
      <td>https://www.udemy.com/using-modx-cms-to-build-...</td>
      <td>True</td>
      <td>45</td>
      <td>901</td>
      <td>36</td>
      <td>20</td>
      <td>Beginner Level</td>
      <td>2.0</td>
      <td>2014-09-28T19:51:11Z</td>
      <td>Web Development</td>
    </tr>
  </tbody>
</table>
<p>3678 rows × 12 columns</p>
</div>



### What are all different subjects for which Udemy is offering courses?


```python
#data.title.unique()
data.subject.unique()
```




    array(['Business Finance', 'Graphic Design', 'Musical Instruments',
           'Web Development'], dtype=object)



### Which subject has the maximum number of courses


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
      <th>course_id</th>
      <th>course_title</th>
      <th>url</th>
      <th>is_paid</th>
      <th>price</th>
      <th>num_subscribers</th>
      <th>num_reviews</th>
      <th>num_lectures</th>
      <th>level</th>
      <th>content_duration</th>
      <th>published_timestamp</th>
      <th>subject</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1070968</td>
      <td>Ultimate Investment Banking Course</td>
      <td>https://www.udemy.com/ultimate-investment-bank...</td>
      <td>True</td>
      <td>200</td>
      <td>2147</td>
      <td>23</td>
      <td>51</td>
      <td>All Levels</td>
      <td>1.5</td>
      <td>2017-01-18T20:58:58Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1113822</td>
      <td>Complete GST Course &amp; Certification - Grow You...</td>
      <td>https://www.udemy.com/goods-and-services-tax/</td>
      <td>True</td>
      <td>75</td>
      <td>2792</td>
      <td>923</td>
      <td>274</td>
      <td>All Levels</td>
      <td>39.0</td>
      <td>2017-03-09T16:34:20Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1006314</td>
      <td>Financial Modeling for Business Analysts and C...</td>
      <td>https://www.udemy.com/financial-modeling-for-b...</td>
      <td>True</td>
      <td>45</td>
      <td>2174</td>
      <td>74</td>
      <td>51</td>
      <td>Intermediate Level</td>
      <td>2.5</td>
      <td>2016-12-19T19:26:30Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1210588</td>
      <td>Beginner to Pro - Financial Analysis in Excel ...</td>
      <td>https://www.udemy.com/complete-excel-finance-c...</td>
      <td>True</td>
      <td>95</td>
      <td>2451</td>
      <td>11</td>
      <td>36</td>
      <td>All Levels</td>
      <td>3.0</td>
      <td>2017-05-30T20:07:24Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1011058</td>
      <td>How To Maximize Your Profits Trading Options</td>
      <td>https://www.udemy.com/how-to-maximize-your-pro...</td>
      <td>True</td>
      <td>200</td>
      <td>1276</td>
      <td>45</td>
      <td>26</td>
      <td>Intermediate Level</td>
      <td>2.0</td>
      <td>2016-12-13T14:57:18Z</td>
      <td>Business Finance</td>
    </tr>
  </tbody>
</table>
</div>




```python
#data.subject.value_counts()
data.subject.value_counts()
```




    Web Development        1200
    Business Finance       1195
    Musical Instruments     680
    Graphic Design          603
    Name: subject, dtype: int64



### Show all the courses which are Free of Cost


```python
#data.head()
data.head(2)
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
      <th>course_id</th>
      <th>course_title</th>
      <th>url</th>
      <th>is_paid</th>
      <th>price</th>
      <th>num_subscribers</th>
      <th>num_reviews</th>
      <th>num_lectures</th>
      <th>level</th>
      <th>content_duration</th>
      <th>published_timestamp</th>
      <th>subject</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1070968</td>
      <td>Ultimate Investment Banking Course</td>
      <td>https://www.udemy.com/ultimate-investment-bank...</td>
      <td>True</td>
      <td>200</td>
      <td>2147</td>
      <td>23</td>
      <td>51</td>
      <td>All Levels</td>
      <td>1.5</td>
      <td>2017-01-18T20:58:58Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1113822</td>
      <td>Complete GST Course &amp; Certification - Grow You...</td>
      <td>https://www.udemy.com/goods-and-services-tax/</td>
      <td>True</td>
      <td>75</td>
      <td>2792</td>
      <td>923</td>
      <td>274</td>
      <td>All Levels</td>
      <td>39.0</td>
      <td>2017-03-09T16:34:20Z</td>
      <td>Business Finance</td>
    </tr>
  </tbody>
</table>
</div>




```python
#data[data.is_paid == False]
data.is_paid == False
```




    0       False
    1       False
    2       False
    3       False
    4       False
            ...  
    3673    False
    3674    False
    3675    False
    3676    False
    3677    False
    Name: is_paid, Length: 3678, dtype: bool




```python
#data[data.is_paid == False]
data[data.is_paid == False] #free Education = 0 price
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
      <th>course_id</th>
      <th>course_title</th>
      <th>url</th>
      <th>is_paid</th>
      <th>price</th>
      <th>num_subscribers</th>
      <th>num_reviews</th>
      <th>num_lectures</th>
      <th>level</th>
      <th>content_duration</th>
      <th>published_timestamp</th>
      <th>subject</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>95</th>
      <td>1148774</td>
      <td>Options Trading 101: The Basics</td>
      <td>https://www.udemy.com/options-trading-101-the-...</td>
      <td>False</td>
      <td>0</td>
      <td>1514</td>
      <td>66</td>
      <td>11</td>
      <td>Beginner Level</td>
      <td>0.550000</td>
      <td>2017-03-23T22:19:57Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>103</th>
      <td>133536</td>
      <td>Stock Market Investing for Beginners</td>
      <td>https://www.udemy.com/the-beginners-guide-to-t...</td>
      <td>False</td>
      <td>0</td>
      <td>50855</td>
      <td>2698</td>
      <td>15</td>
      <td>Beginner Level</td>
      <td>1.500000</td>
      <td>2013-12-25T19:53:34Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>106</th>
      <td>265960</td>
      <td>Fundamentals of Forex Trading</td>
      <td>https://www.udemy.com/fundamentals-of-forex-tr...</td>
      <td>False</td>
      <td>0</td>
      <td>17160</td>
      <td>620</td>
      <td>23</td>
      <td>All Levels</td>
      <td>1.000000</td>
      <td>2014-08-29T20:10:38Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>108</th>
      <td>923616</td>
      <td>Website Investing 101 - Buying &amp; Selling Onlin...</td>
      <td>https://www.udemy.com/cash-flow-website-invest...</td>
      <td>False</td>
      <td>0</td>
      <td>6811</td>
      <td>151</td>
      <td>51</td>
      <td>All Levels</td>
      <td>2.000000</td>
      <td>2016-08-05T17:03:15Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>112</th>
      <td>191854</td>
      <td>Stock Market Foundations</td>
      <td>https://www.udemy.com/how-to-invest-in-the-sto...</td>
      <td>False</td>
      <td>0</td>
      <td>19339</td>
      <td>794</td>
      <td>9</td>
      <td>Beginner Level</td>
      <td>2.000000</td>
      <td>2014-03-31T21:35:06Z</td>
      <td>Business Finance</td>
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
    </tr>
    <tr>
      <th>3638</th>
      <td>155640</td>
      <td>Building a Search Engine in PHP &amp; MySQL</td>
      <td>https://www.udemy.com/creating-a-search-engine...</td>
      <td>False</td>
      <td>0</td>
      <td>10110</td>
      <td>379</td>
      <td>12</td>
      <td>All Levels</td>
      <td>2.500000</td>
      <td>2014-02-03T18:07:52Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>3643</th>
      <td>366720</td>
      <td>CSS Image filters - The modern web images colo...</td>
      <td>https://www.udemy.com/super-awesome-images-wit...</td>
      <td>False</td>
      <td>0</td>
      <td>6315</td>
      <td>53</td>
      <td>16</td>
      <td>All Levels</td>
      <td>1.500000</td>
      <td>2014-12-10T19:43:40Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>3651</th>
      <td>1079078</td>
      <td>Drupal 8 Site Building</td>
      <td>https://www.udemy.com/drupal-8-site-building/</td>
      <td>False</td>
      <td>0</td>
      <td>1942</td>
      <td>23</td>
      <td>48</td>
      <td>All Levels</td>
      <td>4.500000</td>
      <td>2017-05-02T05:15:52Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>3665</th>
      <td>21386</td>
      <td>Beginner Photoshop to HTML5 and CSS3</td>
      <td>https://www.udemy.com/psd-html5-css3/</td>
      <td>False</td>
      <td>0</td>
      <td>73110</td>
      <td>1716</td>
      <td>22</td>
      <td>All Levels</td>
      <td>2.000000</td>
      <td>2012-07-27T12:54:57Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>3668</th>
      <td>270976</td>
      <td>A how to guide in HTML</td>
      <td>https://www.udemy.com/a-how-to-guide-in-html/</td>
      <td>False</td>
      <td>0</td>
      <td>7318</td>
      <td>205</td>
      <td>8</td>
      <td>Beginner Level</td>
      <td>0.583333</td>
      <td>2014-08-10T20:19:10Z</td>
      <td>Web Development</td>
    </tr>
  </tbody>
</table>
<p>310 rows × 12 columns</p>
</div>



### Show all the courses which are Paid


```python
data.is_paid == True
```




    0       True
    1       True
    2       True
    3       True
    4       True
            ... 
    3673    True
    3674    True
    3675    True
    3676    True
    3677    True
    Name: is_paid, Length: 3678, dtype: bool




```python
#data[data.is_paid == True]
data[data.is_paid == True] #Education Fee
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
      <th>course_id</th>
      <th>course_title</th>
      <th>url</th>
      <th>is_paid</th>
      <th>price</th>
      <th>num_subscribers</th>
      <th>num_reviews</th>
      <th>num_lectures</th>
      <th>level</th>
      <th>content_duration</th>
      <th>published_timestamp</th>
      <th>subject</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1070968</td>
      <td>Ultimate Investment Banking Course</td>
      <td>https://www.udemy.com/ultimate-investment-bank...</td>
      <td>True</td>
      <td>200</td>
      <td>2147</td>
      <td>23</td>
      <td>51</td>
      <td>All Levels</td>
      <td>1.5</td>
      <td>2017-01-18T20:58:58Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1113822</td>
      <td>Complete GST Course &amp; Certification - Grow You...</td>
      <td>https://www.udemy.com/goods-and-services-tax/</td>
      <td>True</td>
      <td>75</td>
      <td>2792</td>
      <td>923</td>
      <td>274</td>
      <td>All Levels</td>
      <td>39.0</td>
      <td>2017-03-09T16:34:20Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1006314</td>
      <td>Financial Modeling for Business Analysts and C...</td>
      <td>https://www.udemy.com/financial-modeling-for-b...</td>
      <td>True</td>
      <td>45</td>
      <td>2174</td>
      <td>74</td>
      <td>51</td>
      <td>Intermediate Level</td>
      <td>2.5</td>
      <td>2016-12-19T19:26:30Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1210588</td>
      <td>Beginner to Pro - Financial Analysis in Excel ...</td>
      <td>https://www.udemy.com/complete-excel-finance-c...</td>
      <td>True</td>
      <td>95</td>
      <td>2451</td>
      <td>11</td>
      <td>36</td>
      <td>All Levels</td>
      <td>3.0</td>
      <td>2017-05-30T20:07:24Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1011058</td>
      <td>How To Maximize Your Profits Trading Options</td>
      <td>https://www.udemy.com/how-to-maximize-your-pro...</td>
      <td>True</td>
      <td>200</td>
      <td>1276</td>
      <td>45</td>
      <td>26</td>
      <td>Intermediate Level</td>
      <td>2.0</td>
      <td>2016-12-13T14:57:18Z</td>
      <td>Business Finance</td>
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
    </tr>
    <tr>
      <th>3673</th>
      <td>775618</td>
      <td>Learn jQuery from Scratch - Master of JavaScri...</td>
      <td>https://www.udemy.com/easy-jquery-for-beginner...</td>
      <td>True</td>
      <td>100</td>
      <td>1040</td>
      <td>14</td>
      <td>21</td>
      <td>All Levels</td>
      <td>2.0</td>
      <td>2016-06-14T17:36:46Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>3674</th>
      <td>1088178</td>
      <td>How To Design A WordPress Website With No Codi...</td>
      <td>https://www.udemy.com/how-to-make-a-wordpress-...</td>
      <td>True</td>
      <td>25</td>
      <td>306</td>
      <td>3</td>
      <td>42</td>
      <td>Beginner Level</td>
      <td>3.5</td>
      <td>2017-03-10T22:24:30Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>3675</th>
      <td>635248</td>
      <td>Learn and Build using Polymer</td>
      <td>https://www.udemy.com/learn-and-build-using-po...</td>
      <td>True</td>
      <td>40</td>
      <td>513</td>
      <td>169</td>
      <td>48</td>
      <td>All Levels</td>
      <td>3.5</td>
      <td>2015-12-30T16:41:42Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>3676</th>
      <td>905096</td>
      <td>CSS Animations: Create Amazing Effects on Your...</td>
      <td>https://www.udemy.com/css-animations-create-am...</td>
      <td>True</td>
      <td>50</td>
      <td>300</td>
      <td>31</td>
      <td>38</td>
      <td>All Levels</td>
      <td>3.0</td>
      <td>2016-08-11T19:06:15Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>3677</th>
      <td>297602</td>
      <td>Using MODX CMS to Build Websites: A Beginner's...</td>
      <td>https://www.udemy.com/using-modx-cms-to-build-...</td>
      <td>True</td>
      <td>45</td>
      <td>901</td>
      <td>36</td>
      <td>20</td>
      <td>Beginner Level</td>
      <td>2.0</td>
      <td>2014-09-28T19:51:11Z</td>
      <td>Web Development</td>
    </tr>
  </tbody>
</table>
<p>3368 rows × 12 columns</p>
</div>



### What are Top Selling Courses?


```python
#data.sort_values('num_suscribers', ascending = False)
data.sort_values('num_subscribers', ascending = False)
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
      <th>course_id</th>
      <th>course_title</th>
      <th>url</th>
      <th>is_paid</th>
      <th>price</th>
      <th>num_subscribers</th>
      <th>num_reviews</th>
      <th>num_lectures</th>
      <th>level</th>
      <th>content_duration</th>
      <th>published_timestamp</th>
      <th>subject</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2827</th>
      <td>41295</td>
      <td>Learn HTML5 Programming From Scratch</td>
      <td>https://www.udemy.com/learn-html5-programming-...</td>
      <td>False</td>
      <td>0</td>
      <td>268923</td>
      <td>8629</td>
      <td>45</td>
      <td>All Levels</td>
      <td>10.500000</td>
      <td>2013-02-14T07:03:41Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>3032</th>
      <td>59014</td>
      <td>Coding for Entrepreneurs Basic</td>
      <td>https://www.udemy.com/coding-for-entrepreneurs...</td>
      <td>False</td>
      <td>0</td>
      <td>161029</td>
      <td>279</td>
      <td>27</td>
      <td>Beginner Level</td>
      <td>3.500000</td>
      <td>2013-06-09T15:51:55Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>3230</th>
      <td>625204</td>
      <td>The Web Developer Bootcamp</td>
      <td>https://www.udemy.com/the-web-developer-bootcamp/</td>
      <td>True</td>
      <td>200</td>
      <td>121584</td>
      <td>27445</td>
      <td>342</td>
      <td>All Levels</td>
      <td>43.000000</td>
      <td>2015-11-02T21:13:27Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>2783</th>
      <td>173548</td>
      <td>Build Your First Website in 1 Week with HTML5 ...</td>
      <td>https://www.udemy.com/build-your-first-website...</td>
      <td>False</td>
      <td>0</td>
      <td>120291</td>
      <td>5924</td>
      <td>30</td>
      <td>Beginner Level</td>
      <td>3.000000</td>
      <td>2014-04-08T16:21:30Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>3232</th>
      <td>764164</td>
      <td>The Complete Web Developer Course 2.0</td>
      <td>https://www.udemy.com/the-complete-web-develop...</td>
      <td>True</td>
      <td>200</td>
      <td>114512</td>
      <td>22412</td>
      <td>304</td>
      <td>All Levels</td>
      <td>30.500000</td>
      <td>2016-03-08T22:28:36Z</td>
      <td>Web Development</td>
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
    </tr>
    <tr>
      <th>1569</th>
      <td>726314</td>
      <td>Create Beautiful Image Maps for Your Website</td>
      <td>https://www.udemy.com/how-to-create-hotspot-im...</td>
      <td>True</td>
      <td>20</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>Intermediate Level</td>
      <td>0.616667</td>
      <td>2016-01-18T17:56:36Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>1473</th>
      <td>185526</td>
      <td>MicroStation - Células</td>
      <td>https://www.udemy.com/microstation-celulas/</td>
      <td>True</td>
      <td>20</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
      <td>Beginner Level</td>
      <td>0.616667</td>
      <td>2014-04-15T21:48:55Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>1472</th>
      <td>181268</td>
      <td>Photoshop: Creando elemental de aire</td>
      <td>https://www.udemy.com/photoshop-creando-elemen...</td>
      <td>True</td>
      <td>20</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>Beginner Level</td>
      <td>1.000000</td>
      <td>2014-04-01T21:50:32Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>1471</th>
      <td>188584</td>
      <td>Letras en Adobe Illustrator</td>
      <td>https://www.udemy.com/letras-en-adobe-illustra...</td>
      <td>True</td>
      <td>40</td>
      <td>0</td>
      <td>0</td>
      <td>13</td>
      <td>Beginner Level</td>
      <td>2.500000</td>
      <td>2014-04-04T21:23:23Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>2405</th>
      <td>1265814</td>
      <td>ABRSM Grade III Piano Class - Handel Sonatina ...</td>
      <td>https://www.udemy.com/abrsm-grade-iii-piano-cl...</td>
      <td>True</td>
      <td>20</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>Beginner Level</td>
      <td>0.516667</td>
      <td>2017-07-06T16:12:34Z</td>
      <td>Musical Instruments</td>
    </tr>
  </tbody>
</table>
<p>3678 rows × 12 columns</p>
</div>



### Which are Least Selling Courses?


```python
#data.sort_values('num_suscribers')
data.sort_values('num_subscribers')
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
      <th>course_id</th>
      <th>course_title</th>
      <th>url</th>
      <th>is_paid</th>
      <th>price</th>
      <th>num_subscribers</th>
      <th>num_reviews</th>
      <th>num_lectures</th>
      <th>level</th>
      <th>content_duration</th>
      <th>published_timestamp</th>
      <th>subject</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>885</th>
      <td>1032648</td>
      <td>beginning accounting</td>
      <td>https://www.udemy.com/beginning_accounting/</td>
      <td>True</td>
      <td>20</td>
      <td>0</td>
      <td>0</td>
      <td>12</td>
      <td>Intermediate Level</td>
      <td>0.633333</td>
      <td>2016-12-26T16:52:47Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>456</th>
      <td>1247992</td>
      <td>Introduction to Project Management for Finance...</td>
      <td>https://www.udemy.com/introduction-to-project-...</td>
      <td>True</td>
      <td>50</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
      <td>Beginner Level</td>
      <td>2.000000</td>
      <td>2017-07-03T21:40:32Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>457</th>
      <td>1251582</td>
      <td>Best Practices in Corporate Budgeting</td>
      <td>https://www.udemy.com/best-practices-corporate...</td>
      <td>True</td>
      <td>50</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
      <td>Intermediate Level</td>
      <td>2.000000</td>
      <td>2017-06-29T22:01:56Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>458</th>
      <td>1258666</td>
      <td>Financial Statement Auditing Cycles</td>
      <td>https://www.udemy.com/financial-statement-audi...</td>
      <td>True</td>
      <td>50</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
      <td>Intermediate Level</td>
      <td>2.000000</td>
      <td>2017-06-29T23:20:10Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>459</th>
      <td>1168172</td>
      <td>Case studies on credit appraisal for bankers</td>
      <td>https://www.udemy.com/case-studies-on-credit-a...</td>
      <td>True</td>
      <td>20</td>
      <td>0</td>
      <td>0</td>
      <td>15</td>
      <td>Beginner Level</td>
      <td>3.500000</td>
      <td>2017-05-01T20:16:26Z</td>
      <td>Business Finance</td>
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
    </tr>
    <tr>
      <th>3232</th>
      <td>764164</td>
      <td>The Complete Web Developer Course 2.0</td>
      <td>https://www.udemy.com/the-complete-web-develop...</td>
      <td>True</td>
      <td>200</td>
      <td>114512</td>
      <td>22412</td>
      <td>304</td>
      <td>All Levels</td>
      <td>30.500000</td>
      <td>2016-03-08T22:28:36Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>2783</th>
      <td>173548</td>
      <td>Build Your First Website in 1 Week with HTML5 ...</td>
      <td>https://www.udemy.com/build-your-first-website...</td>
      <td>False</td>
      <td>0</td>
      <td>120291</td>
      <td>5924</td>
      <td>30</td>
      <td>Beginner Level</td>
      <td>3.000000</td>
      <td>2014-04-08T16:21:30Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>3230</th>
      <td>625204</td>
      <td>The Web Developer Bootcamp</td>
      <td>https://www.udemy.com/the-web-developer-bootcamp/</td>
      <td>True</td>
      <td>200</td>
      <td>121584</td>
      <td>27445</td>
      <td>342</td>
      <td>All Levels</td>
      <td>43.000000</td>
      <td>2015-11-02T21:13:27Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>3032</th>
      <td>59014</td>
      <td>Coding for Entrepreneurs Basic</td>
      <td>https://www.udemy.com/coding-for-entrepreneurs...</td>
      <td>False</td>
      <td>0</td>
      <td>161029</td>
      <td>279</td>
      <td>27</td>
      <td>Beginner Level</td>
      <td>3.500000</td>
      <td>2013-06-09T15:51:55Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>2827</th>
      <td>41295</td>
      <td>Learn HTML5 Programming From Scratch</td>
      <td>https://www.udemy.com/learn-html5-programming-...</td>
      <td>False</td>
      <td>0</td>
      <td>268923</td>
      <td>8629</td>
      <td>45</td>
      <td>All Levels</td>
      <td>10.500000</td>
      <td>2013-02-14T07:03:41Z</td>
      <td>Web Development</td>
    </tr>
  </tbody>
</table>
<p>3678 rows × 12 columns</p>
</div>



###  Show all courses of Graphic Design where the price is below 100?


```python
data.subject == 'Graphic Design'
```




    0       False
    1       False
    2       False
    3       False
    4       False
            ...  
    3673    False
    3674    False
    3675    False
    3676    False
    3677    False
    Name: subject, Length: 3678, dtype: bool




```python
#data[(data.subject == 'Graphic Design') & (data.price < '100')]
data[(data.subject == 'Graphic Design') & (data.price < 100)]
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
      <th>course_id</th>
      <th>course_title</th>
      <th>url</th>
      <th>is_paid</th>
      <th>price</th>
      <th>num_subscribers</th>
      <th>num_reviews</th>
      <th>num_lectures</th>
      <th>level</th>
      <th>content_duration</th>
      <th>published_timestamp</th>
      <th>subject</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1196</th>
      <td>1197206</td>
      <td>Illustrator CC MasterClass</td>
      <td>https://www.udemy.com/illustrator-cc-masterclass/</td>
      <td>True</td>
      <td>95</td>
      <td>462</td>
      <td>50</td>
      <td>86</td>
      <td>All Levels</td>
      <td>12.0</td>
      <td>2017-05-02T16:41:21Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>1198</th>
      <td>1219520</td>
      <td>Adobe Illustrator T-Shirt Design for Merch by ...</td>
      <td>https://www.udemy.com/merchbyamazondesign/</td>
      <td>True</td>
      <td>20</td>
      <td>390</td>
      <td>44</td>
      <td>15</td>
      <td>All Levels</td>
      <td>1.0</td>
      <td>2017-06-13T20:41:14Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>1202</th>
      <td>28556</td>
      <td>Discover How to Draw and paint Comics</td>
      <td>https://www.udemy.com/learn-to-draw-and-paint/</td>
      <td>True</td>
      <td>65</td>
      <td>8901</td>
      <td>424</td>
      <td>85</td>
      <td>All Levels</td>
      <td>62.0</td>
      <td>2012-11-21T22:03:54Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>1203</th>
      <td>317278</td>
      <td>Typographic Logos: Typography and Lettering fo...</td>
      <td>https://www.udemy.com/typographic-logos-typogr...</td>
      <td>True</td>
      <td>25</td>
      <td>4235</td>
      <td>427</td>
      <td>20</td>
      <td>Intermediate Level</td>
      <td>1.5</td>
      <td>2014-10-16T19:30:01Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>1204</th>
      <td>573064</td>
      <td>Photoshop in Ease: Create World Amazing  Graph...</td>
      <td>https://www.udemy.com/photoshop-knights-become...</td>
      <td>True</td>
      <td>20</td>
      <td>14440</td>
      <td>182</td>
      <td>26</td>
      <td>All Levels</td>
      <td>3.0</td>
      <td>2015-08-13T21:17:34Z</td>
      <td>Graphic Design</td>
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
    </tr>
    <tr>
      <th>1793</th>
      <td>456388</td>
      <td>Adobe Photoshop CC | The Essential Guide</td>
      <td>https://www.udemy.com/adobe-photoshop-cc-the-e...</td>
      <td>True</td>
      <td>20</td>
      <td>254</td>
      <td>5</td>
      <td>81</td>
      <td>All Levels</td>
      <td>4.5</td>
      <td>2015-05-12T00:19:27Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>1794</th>
      <td>955242</td>
      <td>Learn to Composite a 2D Action Shot in Photoshop</td>
      <td>https://www.udemy.com/3dmotive-learn-to-compos...</td>
      <td>True</td>
      <td>20</td>
      <td>40</td>
      <td>2</td>
      <td>8</td>
      <td>Beginner Level</td>
      <td>1.5</td>
      <td>2016-09-10T21:38:26Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>1795</th>
      <td>496430</td>
      <td>Infographic Design: How To Create Your Own Inf...</td>
      <td>https://www.udemy.com/infographic-design-how-t...</td>
      <td>True</td>
      <td>20</td>
      <td>84</td>
      <td>8</td>
      <td>13</td>
      <td>All Levels</td>
      <td>2.0</td>
      <td>2015-05-12T20:38:58Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>1796</th>
      <td>793246</td>
      <td>Autodesk Inventor 2016 : Complete Guide</td>
      <td>https://www.udemy.com/learn-autodesk-inventor-...</td>
      <td>True</td>
      <td>20</td>
      <td>23</td>
      <td>4</td>
      <td>83</td>
      <td>Beginner Level</td>
      <td>7.5</td>
      <td>2016-03-22T20:35:56Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>1797</th>
      <td>547190</td>
      <td>Amazing Graphic Design for Beginners</td>
      <td>https://www.udemy.com/amazing-graphic-design-f...</td>
      <td>True</td>
      <td>20</td>
      <td>32</td>
      <td>10</td>
      <td>5</td>
      <td>Beginner Level</td>
      <td>0.7</td>
      <td>2015-07-08T19:58:01Z</td>
      <td>Graphic Design</td>
    </tr>
  </tbody>
</table>
<p>485 rows × 12 columns</p>
</div>



###  Show all courses of Graphic Design where the price == 100?


```python
#data[(data.subject == 'Graphic Design') & (data.price == '100')]
data[(data.subject == 'Graphic Design') & (data.price == 100)]
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
      <th>course_id</th>
      <th>course_title</th>
      <th>url</th>
      <th>is_paid</th>
      <th>price</th>
      <th>num_subscribers</th>
      <th>num_reviews</th>
      <th>num_lectures</th>
      <th>level</th>
      <th>content_duration</th>
      <th>published_timestamp</th>
      <th>subject</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1248</th>
      <td>1160004</td>
      <td>Design a logo for FREE in Inkscape</td>
      <td>https://www.udemy.com/logoinkscape/</td>
      <td>True</td>
      <td>100</td>
      <td>1148</td>
      <td>26</td>
      <td>42</td>
      <td>All Levels</td>
      <td>2.000000</td>
      <td>2017-05-01T18:32:43Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>1288</th>
      <td>927186</td>
      <td>Learn Blender 3D  - The introduction course</td>
      <td>https://www.udemy.com/learn-blender-3d-in-unde...</td>
      <td>True</td>
      <td>100</td>
      <td>739</td>
      <td>12</td>
      <td>15</td>
      <td>Beginner Level</td>
      <td>1.500000</td>
      <td>2016-08-19T00:52:30Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>1338</th>
      <td>638040</td>
      <td>Adobe Photoshop Essentials: Master Adobe Photo...</td>
      <td>https://www.udemy.com/adobe-photoshop-cs6-esse...</td>
      <td>True</td>
      <td>100</td>
      <td>1373</td>
      <td>5</td>
      <td>63</td>
      <td>Beginner Level</td>
      <td>2.500000</td>
      <td>2015-11-18T17:47:26Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>1347</th>
      <td>1246168</td>
      <td>Illustrator para criação de peças gráficas, De...</td>
      <td>https://www.udemy.com/aula-de-illustrator-como...</td>
      <td>True</td>
      <td>100</td>
      <td>33</td>
      <td>3</td>
      <td>41</td>
      <td>Beginner Level</td>
      <td>1.500000</td>
      <td>2017-06-13T04:15:20Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>1376</th>
      <td>654038</td>
      <td>How To Sell Your Art Online With ETSY</td>
      <td>https://www.udemy.com/how-to-sell-your-art-onl...</td>
      <td>True</td>
      <td>100</td>
      <td>1338</td>
      <td>38</td>
      <td>35</td>
      <td>Beginner Level</td>
      <td>3.000000</td>
      <td>2015-11-11T01:26:13Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>1380</th>
      <td>1243016</td>
      <td>Photoshop - Tratamento de pele profissional</td>
      <td>https://www.udemy.com/como-fazer-retoque-de-pe...</td>
      <td>True</td>
      <td>100</td>
      <td>50</td>
      <td>5</td>
      <td>16</td>
      <td>Intermediate Level</td>
      <td>1.500000</td>
      <td>2017-06-06T14:22:28Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>1381</th>
      <td>1266468</td>
      <td>Indesign - Para quem quer trabalhar com Design...</td>
      <td>https://www.udemy.com/indesign-como-criar-layo...</td>
      <td>True</td>
      <td>100</td>
      <td>27</td>
      <td>7</td>
      <td>12</td>
      <td>Intermediate Level</td>
      <td>2.500000</td>
      <td>2017-06-27T02:48:29Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>1417</th>
      <td>978462</td>
      <td>Blender Modelling Series - Volume Two</td>
      <td>https://www.udemy.com/blender-modelling-series...</td>
      <td>True</td>
      <td>100</td>
      <td>1526</td>
      <td>3</td>
      <td>24</td>
      <td>Beginner Level</td>
      <td>2.000000</td>
      <td>2016-10-12T20:22:14Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>1452</th>
      <td>1027080</td>
      <td>Logo Portfolio in 1 Hour in Wordpress</td>
      <td>https://www.udemy.com/logoportfolio/</td>
      <td>True</td>
      <td>100</td>
      <td>734</td>
      <td>9</td>
      <td>36</td>
      <td>All Levels</td>
      <td>1.000000</td>
      <td>2016-12-06T22:13:44Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>1489</th>
      <td>482924</td>
      <td>Mastering Retouching and Restoration (15 proje...</td>
      <td>https://www.udemy.com/mastering-beauty-retouch...</td>
      <td>True</td>
      <td>100</td>
      <td>4927</td>
      <td>15</td>
      <td>22</td>
      <td>All Levels</td>
      <td>2.500000</td>
      <td>2015-04-26T12:27:22Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>1507</th>
      <td>1161864</td>
      <td>Diseño impreso - Preimpresión para offset en I...</td>
      <td>https://www.udemy.com/diseno-impreso/</td>
      <td>True</td>
      <td>100</td>
      <td>33</td>
      <td>9</td>
      <td>29</td>
      <td>All Levels</td>
      <td>1.500000</td>
      <td>2017-05-31T18:37:31Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>1540</th>
      <td>490392</td>
      <td>Getting Started with Illustrator CC</td>
      <td>https://www.udemy.com/getting-started-with-ill...</td>
      <td>True</td>
      <td>100</td>
      <td>92</td>
      <td>10</td>
      <td>57</td>
      <td>Beginner Level</td>
      <td>5.500000</td>
      <td>2015-05-01T21:29:51Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>1577</th>
      <td>1012262</td>
      <td>Icon &amp; Logo Symbol Design in Adobe Illustrator</td>
      <td>https://www.udemy.com/icondesign/</td>
      <td>True</td>
      <td>100</td>
      <td>1043</td>
      <td>27</td>
      <td>30</td>
      <td>All Levels</td>
      <td>2.000000</td>
      <td>2016-11-23T22:57:18Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>1585</th>
      <td>727510</td>
      <td>How To Become An Etsy Wholesale Seller</td>
      <td>https://www.udemy.com/how-to-become-an-etsy-wh...</td>
      <td>True</td>
      <td>100</td>
      <td>1013</td>
      <td>0</td>
      <td>25</td>
      <td>Beginner Level</td>
      <td>2.500000</td>
      <td>2016-03-29T22:34:30Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>1614</th>
      <td>575040</td>
      <td>Typography From A to Z</td>
      <td>https://www.udemy.com/typography-from-a-to-z/</td>
      <td>True</td>
      <td>100</td>
      <td>317</td>
      <td>15</td>
      <td>76</td>
      <td>All Levels</td>
      <td>6.000000</td>
      <td>2015-08-07T22:16:26Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>1628</th>
      <td>950894</td>
      <td>photoshop - CURSO DE PHOTOSHOP DO BÁSICO AO AV...</td>
      <td>https://www.udemy.com/photoshop-do-basico-ao-a...</td>
      <td>True</td>
      <td>100</td>
      <td>1110</td>
      <td>183</td>
      <td>77</td>
      <td>All Levels</td>
      <td>10.000000</td>
      <td>2017-02-06T17:22:18Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>1632</th>
      <td>908664</td>
      <td>Word Swag : Create Stunning Images with the Wo...</td>
      <td>https://www.udemy.com/word-swag/</td>
      <td>True</td>
      <td>100</td>
      <td>2416</td>
      <td>19</td>
      <td>14</td>
      <td>All Levels</td>
      <td>1.000000</td>
      <td>2016-08-09T17:56:53Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>1657</th>
      <td>757900</td>
      <td>Canva : Book Cover Design</td>
      <td>https://www.udemy.com/canva-book-cover-design/</td>
      <td>True</td>
      <td>100</td>
      <td>3377</td>
      <td>20</td>
      <td>15</td>
      <td>Beginner Level</td>
      <td>2.000000</td>
      <td>2016-02-26T01:08:20Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>1665</th>
      <td>1269190</td>
      <td>7 Secrets To Designing In Black and White</td>
      <td>https://www.udemy.com/secrets-to-designing-in-...</td>
      <td>True</td>
      <td>100</td>
      <td>1000</td>
      <td>1</td>
      <td>12</td>
      <td>All Levels</td>
      <td>1.500000</td>
      <td>2017-06-27T19:55:18Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>1672</th>
      <td>1147664</td>
      <td>Photoshop CC Eğitim Seti (YENİ)</td>
      <td>https://www.udemy.com/photoshop-cc-egitim-seti...</td>
      <td>True</td>
      <td>100</td>
      <td>27</td>
      <td>5</td>
      <td>202</td>
      <td>All Levels</td>
      <td>16.000000</td>
      <td>2017-03-30T22:26:26Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>1693</th>
      <td>983444</td>
      <td>Adobe Illustrator Vectors For Hand Letterers</td>
      <td>https://www.udemy.com/adobe-illustrator-vector...</td>
      <td>True</td>
      <td>100</td>
      <td>23</td>
      <td>2</td>
      <td>9</td>
      <td>Beginner Level</td>
      <td>0.616667</td>
      <td>2016-10-21T18:50:38Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>1706</th>
      <td>996868</td>
      <td>How to Design a Logo in Adobe Illustrator</td>
      <td>https://www.udemy.com/logoworkshop/</td>
      <td>True</td>
      <td>100</td>
      <td>972</td>
      <td>44</td>
      <td>24</td>
      <td>All Levels</td>
      <td>1.000000</td>
      <td>2016-11-14T15:26:17Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>1745</th>
      <td>771044</td>
      <td>Make Money With Photoshop: Logos, Business Car...</td>
      <td>https://www.udemy.com/make-money-with-photosho...</td>
      <td>True</td>
      <td>100</td>
      <td>32</td>
      <td>4</td>
      <td>21</td>
      <td>All Levels</td>
      <td>5.000000</td>
      <td>2016-08-14T22:05:04Z</td>
      <td>Graphic Design</td>
    </tr>
  </tbody>
</table>
</div>



### List out all the courses that are related with 'Python'


```python
#data[data.course_title.str.contains('Python')]
data[data.course_title.str.contains('Python')]
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
      <th>course_id</th>
      <th>course_title</th>
      <th>url</th>
      <th>is_paid</th>
      <th>price</th>
      <th>num_subscribers</th>
      <th>num_reviews</th>
      <th>num_lectures</th>
      <th>level</th>
      <th>content_duration</th>
      <th>published_timestamp</th>
      <th>subject</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>14</th>
      <td>1196544</td>
      <td>Python Algo Trading: Sentiment Trading with News</td>
      <td>https://www.udemy.com/hedge-fund-strategy-trad...</td>
      <td>True</td>
      <td>200</td>
      <td>294</td>
      <td>19</td>
      <td>42</td>
      <td>All Levels</td>
      <td>7.0</td>
      <td>2017-04-28T16:41:44Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>30</th>
      <td>1170894</td>
      <td>Python Algo Stock Trading: Automate Your Trading!</td>
      <td>https://www.udemy.com/algorithmic-stock-tradin...</td>
      <td>True</td>
      <td>95</td>
      <td>1165</td>
      <td>21</td>
      <td>41</td>
      <td>Beginner Level</td>
      <td>2.5</td>
      <td>2017-05-28T23:41:03Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>41</th>
      <td>1035472</td>
      <td>Python for Finance: Investment Fundamentals &amp; ...</td>
      <td>https://www.udemy.com/python-for-finance-inves...</td>
      <td>True</td>
      <td>195</td>
      <td>3811</td>
      <td>278</td>
      <td>103</td>
      <td>All Levels</td>
      <td>6.5</td>
      <td>2017-03-30T22:17:09Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>147</th>
      <td>1070886</td>
      <td>Python Algo Trading: FX Trading with Oanda</td>
      <td>https://www.udemy.com/python-algo-trading-fx-t...</td>
      <td>True</td>
      <td>200</td>
      <td>453</td>
      <td>42</td>
      <td>33</td>
      <td>Intermediate Level</td>
      <td>3.0</td>
      <td>2017-03-14T00:39:45Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>334</th>
      <td>815482</td>
      <td>Stock Technical Analysis with Python</td>
      <td>https://www.udemy.com/stock-technical-analysis...</td>
      <td>True</td>
      <td>50</td>
      <td>409</td>
      <td>35</td>
      <td>46</td>
      <td>All Levels</td>
      <td>8.0</td>
      <td>2016-04-12T00:40:03Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>536</th>
      <td>529828</td>
      <td>Python for Trading &amp; Investing</td>
      <td>https://www.udemy.com/python-for-trading-inves...</td>
      <td>True</td>
      <td>95</td>
      <td>638</td>
      <td>25</td>
      <td>36</td>
      <td>All Levels</td>
      <td>5.0</td>
      <td>2015-06-17T22:23:31Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>762</th>
      <td>1088656</td>
      <td>Quantitative Trading Analysis with Python</td>
      <td>https://www.udemy.com/quantitative-trading-ana...</td>
      <td>True</td>
      <td>50</td>
      <td>256</td>
      <td>17</td>
      <td>49</td>
      <td>All Levels</td>
      <td>5.5</td>
      <td>2017-01-27T17:11:28Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>863</th>
      <td>902888</td>
      <td>Investment Portfolio Analysis with Python</td>
      <td>https://www.udemy.com/investment-portfolio-ana...</td>
      <td>True</td>
      <td>50</td>
      <td>209</td>
      <td>13</td>
      <td>37</td>
      <td>All Levels</td>
      <td>7.0</td>
      <td>2016-07-13T21:40:32Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>1682</th>
      <td>546848</td>
      <td>Learn to code in Python and learn Adobe Photos...</td>
      <td>https://www.udemy.com/learn-to-code-in-python-...</td>
      <td>True</td>
      <td>50</td>
      <td>1132</td>
      <td>1</td>
      <td>29</td>
      <td>All Levels</td>
      <td>2.0</td>
      <td>2015-07-08T00:15:12Z</td>
      <td>Graphic Design</td>
    </tr>
    <tr>
      <th>2497</th>
      <td>16646</td>
      <td>Web Programming with Python</td>
      <td>https://www.udemy.com/web-programming-with-pyt...</td>
      <td>True</td>
      <td>50</td>
      <td>35267</td>
      <td>217</td>
      <td>53</td>
      <td>All Levels</td>
      <td>4.0</td>
      <td>2012-04-25T00:01:43Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>2528</th>
      <td>391546</td>
      <td>Learn Python and Django: Payment Processing</td>
      <td>https://www.udemy.com/learn-django-code-accept...</td>
      <td>True</td>
      <td>70</td>
      <td>17714</td>
      <td>198</td>
      <td>23</td>
      <td>All Levels</td>
      <td>3.5</td>
      <td>2015-02-09T15:37:56Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>2553</th>
      <td>938560</td>
      <td>The Complete Ethical Hacking Course 2.0: Pytho...</td>
      <td>https://www.udemy.com/penetration-testing-ethi...</td>
      <td>True</td>
      <td>195</td>
      <td>7827</td>
      <td>268</td>
      <td>66</td>
      <td>All Levels</td>
      <td>11.0</td>
      <td>2016-09-26T15:08:29Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>2570</th>
      <td>47963</td>
      <td>Coding for Entrepreneurs: Learn Python, Django...</td>
      <td>https://www.udemy.com/coding-for-entrepreneurs/</td>
      <td>True</td>
      <td>195</td>
      <td>23412</td>
      <td>799</td>
      <td>251</td>
      <td>All Levels</td>
      <td>45.0</td>
      <td>2013-04-08T00:46:14Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>2681</th>
      <td>477702</td>
      <td>Python for Beginners: Python Programming Langu...</td>
      <td>https://www.udemy.com/python-course/</td>
      <td>True</td>
      <td>150</td>
      <td>6153</td>
      <td>125</td>
      <td>84</td>
      <td>Beginner Level</td>
      <td>5.0</td>
      <td>2015-06-14T18:18:57Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>2960</th>
      <td>270808</td>
      <td>Projects in Django and Python</td>
      <td>https://www.udemy.com/projects-in-django-and-p...</td>
      <td>True</td>
      <td>60</td>
      <td>1764</td>
      <td>53</td>
      <td>28</td>
      <td>All Levels</td>
      <td>6.5</td>
      <td>2014-10-21T07:58:07Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>3133</th>
      <td>574082</td>
      <td>Web Scraping with Python, Ruby &amp; import. io</td>
      <td>https://www.udemy.com/web-scraping-with-python...</td>
      <td>True</td>
      <td>75</td>
      <td>973</td>
      <td>50</td>
      <td>46</td>
      <td>All Levels</td>
      <td>4.5</td>
      <td>2015-08-09T22:16:41Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>3138</th>
      <td>631128</td>
      <td>Complete Python Web Course: Build 8 Python Web...</td>
      <td>https://www.udemy.com/the-complete-python-web-...</td>
      <td>True</td>
      <td>110</td>
      <td>7489</td>
      <td>941</td>
      <td>173</td>
      <td>All Levels</td>
      <td>16.0</td>
      <td>2015-11-08T20:57:35Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>3160</th>
      <td>368340</td>
      <td>Professional Python Web Development Using Flask</td>
      <td>https://www.udemy.com/python-flask-course/</td>
      <td>True</td>
      <td>120</td>
      <td>3420</td>
      <td>489</td>
      <td>102</td>
      <td>Beginner Level</td>
      <td>14.5</td>
      <td>2015-03-04T00:10:36Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>3192</th>
      <td>1035940</td>
      <td>Professional RESTful API Design using Python F...</td>
      <td>https://www.udemy.com/restful-api-flask-course/</td>
      <td>True</td>
      <td>120</td>
      <td>578</td>
      <td>25</td>
      <td>36</td>
      <td>Intermediate Level</td>
      <td>4.5</td>
      <td>2017-01-11T21:15:25Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>3194</th>
      <td>1063722</td>
      <td>Learn Python Django - A Hands-On Course</td>
      <td>https://www.udemy.com/learn-python-django-a-ha...</td>
      <td>True</td>
      <td>50</td>
      <td>1339</td>
      <td>21</td>
      <td>18</td>
      <td>Beginner Level</td>
      <td>2.0</td>
      <td>2017-01-18T21:53:34Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>3197</th>
      <td>76052</td>
      <td>Try Django 1.9 | Build a Blog and Learn Python...</td>
      <td>https://www.udemy.com/try-django/</td>
      <td>True</td>
      <td>50</td>
      <td>7407</td>
      <td>172</td>
      <td>147</td>
      <td>All Levels</td>
      <td>20.0</td>
      <td>2014-03-04T07:12:21Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>3200</th>
      <td>822444</td>
      <td>Python and Django Full Stack Web Developer Boo...</td>
      <td>https://www.udemy.com/python-and-django-full-s...</td>
      <td>True</td>
      <td>200</td>
      <td>11832</td>
      <td>1883</td>
      <td>191</td>
      <td>All Levels</td>
      <td>31.5</td>
      <td>2017-02-24T18:40:55Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>3203</th>
      <td>970600</td>
      <td>REST APIs with Flask and Python</td>
      <td>https://www.udemy.com/rest-api-flask-and-python/</td>
      <td>True</td>
      <td>110</td>
      <td>5151</td>
      <td>737</td>
      <td>115</td>
      <td>Intermediate Level</td>
      <td>12.5</td>
      <td>2016-11-06T19:00:38Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>3284</th>
      <td>599504</td>
      <td>Advanced Scalable Python Web Development Using...</td>
      <td>https://www.udemy.com/advanced-python-flask/</td>
      <td>True</td>
      <td>120</td>
      <td>1299</td>
      <td>56</td>
      <td>71</td>
      <td>Intermediate Level</td>
      <td>14.0</td>
      <td>2016-08-11T22:09:24Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>3326</th>
      <td>186096</td>
      <td>Core: A Web App Reference Guide for Django, Py...</td>
      <td>https://www.udemy.com/coding-for-entrepreneurs...</td>
      <td>True</td>
      <td>195</td>
      <td>2497</td>
      <td>98</td>
      <td>154</td>
      <td>All Levels</td>
      <td>26.0</td>
      <td>2014-05-29T00:58:43Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>3333</th>
      <td>1038538</td>
      <td>Introduction to QGIS Python Programming</td>
      <td>https://www.udemy.com/introduction-to-qgis-pyt...</td>
      <td>True</td>
      <td>85</td>
      <td>197</td>
      <td>26</td>
      <td>28</td>
      <td>Beginner Level</td>
      <td>3.5</td>
      <td>2016-12-22T00:11:22Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>3343</th>
      <td>523312</td>
      <td>Python Web Programming</td>
      <td>https://www.udemy.com/python-web-programming/</td>
      <td>True</td>
      <td>100</td>
      <td>1020</td>
      <td>46</td>
      <td>60</td>
      <td>Beginner Level</td>
      <td>6.0</td>
      <td>2015-07-01T21:46:36Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>3392</th>
      <td>70640</td>
      <td>Python Programming: Create an Digital Marketpl...</td>
      <td>https://www.udemy.com/coding-for-entrepreneurs...</td>
      <td>True</td>
      <td>195</td>
      <td>4198</td>
      <td>145</td>
      <td>161</td>
      <td>All Levels</td>
      <td>26.0</td>
      <td>2013-10-20T19:53:28Z</td>
      <td>Web Development</td>
    </tr>
    <tr>
      <th>3507</th>
      <td>394832</td>
      <td>Fun and creative web engineering with Python a...</td>
      <td>https://www.udemy.com/web-engineering-with-pyt...</td>
      <td>False</td>
      <td>0</td>
      <td>10917</td>
      <td>319</td>
      <td>25</td>
      <td>All Levels</td>
      <td>2.0</td>
      <td>2015-06-09T19:51:50Z</td>
      <td>Web Development</td>
    </tr>
  </tbody>
</table>
</div>




```python
len(data[data.course_title.str.contains('Python')]) #total python courses are 29 
```




    29



### courses that published in year == 2015?


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
      <th>course_id</th>
      <th>course_title</th>
      <th>url</th>
      <th>is_paid</th>
      <th>price</th>
      <th>num_subscribers</th>
      <th>num_reviews</th>
      <th>num_lectures</th>
      <th>level</th>
      <th>content_duration</th>
      <th>published_timestamp</th>
      <th>subject</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1070968</td>
      <td>Ultimate Investment Banking Course</td>
      <td>https://www.udemy.com/ultimate-investment-bank...</td>
      <td>True</td>
      <td>200</td>
      <td>2147</td>
      <td>23</td>
      <td>51</td>
      <td>All Levels</td>
      <td>1.5</td>
      <td>2017-01-18T20:58:58Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1113822</td>
      <td>Complete GST Course &amp; Certification - Grow You...</td>
      <td>https://www.udemy.com/goods-and-services-tax/</td>
      <td>True</td>
      <td>75</td>
      <td>2792</td>
      <td>923</td>
      <td>274</td>
      <td>All Levels</td>
      <td>39.0</td>
      <td>2017-03-09T16:34:20Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1006314</td>
      <td>Financial Modeling for Business Analysts and C...</td>
      <td>https://www.udemy.com/financial-modeling-for-b...</td>
      <td>True</td>
      <td>45</td>
      <td>2174</td>
      <td>74</td>
      <td>51</td>
      <td>Intermediate Level</td>
      <td>2.5</td>
      <td>2016-12-19T19:26:30Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1210588</td>
      <td>Beginner to Pro - Financial Analysis in Excel ...</td>
      <td>https://www.udemy.com/complete-excel-finance-c...</td>
      <td>True</td>
      <td>95</td>
      <td>2451</td>
      <td>11</td>
      <td>36</td>
      <td>All Levels</td>
      <td>3.0</td>
      <td>2017-05-30T20:07:24Z</td>
      <td>Business Finance</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1011058</td>
      <td>How To Maximize Your Profits Trading Options</td>
      <td>https://www.udemy.com/how-to-maximize-your-pro...</td>
      <td>True</td>
      <td>200</td>
      <td>1276</td>
      <td>45</td>
      <td>26</td>
      <td>Intermediate Level</td>
      <td>2.0</td>
      <td>2016-12-13T14:57:18Z</td>
      <td>Business Finance</td>
    </tr>
  </tbody>
</table>
</div>




```python
#data.dtypes
data.dtypes #published_timestamp = object. to Datetime
```




    course_id                int64
    course_title            object
    url                     object
    is_paid                   bool
    price                    int64
    num_subscribers          int64
    num_reviews              int64
    num_lectures             int64
    level                   object
    content_duration       float64
    published_timestamp     object
    subject                 object
    dtype: object




```python
#data['published_timestamp'] = pd.to_datetime(data.published_timestamp)
data['published_timestamp'] = pd.to_datetime(data['published_timestamp'])
```


```python
#data.dtypes
data.dtypes
```




    course_id                            int64
    course_title                        object
    url                                 object
    is_paid                               bool
    price                                int64
    num_subscribers                      int64
    num_reviews                          int64
    num_lectures                         int64
    level                               object
    content_duration                   float64
    published_timestamp    datetime64[ns, UTC]
    subject                             object
    Year                                 int64
    dtype: object




```python
data.head(1)
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
      <th>course_id</th>
      <th>course_title</th>
      <th>url</th>
      <th>is_paid</th>
      <th>price</th>
      <th>num_subscribers</th>
      <th>num_reviews</th>
      <th>num_lectures</th>
      <th>level</th>
      <th>content_duration</th>
      <th>published_timestamp</th>
      <th>subject</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1070968</td>
      <td>Ultimate Investment Banking Course</td>
      <td>https://www.udemy.com/ultimate-investment-bank...</td>
      <td>True</td>
      <td>200</td>
      <td>2147</td>
      <td>23</td>
      <td>51</td>
      <td>All Levels</td>
      <td>1.5</td>
      <td>2017-01-18 20:58:58+00:00</td>
      <td>Business Finance</td>
      <td>2017</td>
    </tr>
  </tbody>
</table>
</div>




```python
#data['Year'] = data['published_timestamp'].dt.year
data['year'] = data['published_timestamp'].dt.year
```


```python
#data[data.year == 2015]
data[data.year == 2015]
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
      <th>course_id</th>
      <th>course_title</th>
      <th>url</th>
      <th>is_paid</th>
      <th>price</th>
      <th>num_subscribers</th>
      <th>num_reviews</th>
      <th>num_lectures</th>
      <th>level</th>
      <th>content_duration</th>
      <th>published_timestamp</th>
      <th>subject</th>
      <th>Year</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>403100</td>
      <td>Trading Stock Chart Patterns For Immediate, Ex...</td>
      <td>https://www.udemy.com/trading-chart-patterns-f...</td>
      <td>True</td>
      <td>95</td>
      <td>2917</td>
      <td>148</td>
      <td>23</td>
      <td>All Levels</td>
      <td>2.5</td>
      <td>2015-01-30 22:13:03+00:00</td>
      <td>Business Finance</td>
      <td>2015</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>8</th>
      <td>476268</td>
      <td>Options Trading 3 : Advanced Stock Profit and ...</td>
      <td>https://www.udemy.com/day-trading-stock-option...</td>
      <td>True</td>
      <td>195</td>
      <td>5172</td>
      <td>34</td>
      <td>38</td>
      <td>Expert Level</td>
      <td>2.5</td>
      <td>2015-05-28 00:14:03+00:00</td>
      <td>Business Finance</td>
      <td>2015</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>10</th>
      <td>592338</td>
      <td>Forex Trading Secrets of the Pros With Amazon'...</td>
      <td>https://www.udemy.com/trading-with-amazons-aws...</td>
      <td>True</td>
      <td>200</td>
      <td>4284</td>
      <td>93</td>
      <td>76</td>
      <td>All Levels</td>
      <td>5.0</td>
      <td>2015-09-11 16:47:02+00:00</td>
      <td>Business Finance</td>
      <td>2015</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>15</th>
      <td>504036</td>
      <td>Short Selling: Learn To Sell Stocks Before The...</td>
      <td>https://www.udemy.com/short-selling-learn-to-s...</td>
      <td>True</td>
      <td>75</td>
      <td>2276</td>
      <td>106</td>
      <td>19</td>
      <td>Intermediate Level</td>
      <td>1.5</td>
      <td>2015-06-22 21:18:35+00:00</td>
      <td>Business Finance</td>
      <td>2015</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>17</th>
      <td>564966</td>
      <td>The Complete Chart Pattern Trading Course: A P...</td>
      <td>https://www.udemy.com/make-money-trading-stock...</td>
      <td>True</td>
      <td>200</td>
      <td>2666</td>
      <td>115</td>
      <td>52</td>
      <td>All Levels</td>
      <td>4.0</td>
      <td>2015-08-10 21:07:35+00:00</td>
      <td>Business Finance</td>
      <td>2015</td>
      <td>2015</td>
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
    </tr>
    <tr>
      <th>3659</th>
      <td>577796</td>
      <td>Simple Javascript: Learn by Doing, Beginners W...</td>
      <td>https://www.udemy.com/simple-javascript-learn-...</td>
      <td>True</td>
      <td>25</td>
      <td>2753</td>
      <td>10</td>
      <td>18</td>
      <td>All Levels</td>
      <td>2.0</td>
      <td>2015-09-07 17:55:11+00:00</td>
      <td>Web Development</td>
      <td>2015</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>3667</th>
      <td>523216</td>
      <td>The Fastest Way to Create a Website Using Godaddy</td>
      <td>https://www.udemy.com/create-your-own-website/</td>
      <td>True</td>
      <td>30</td>
      <td>1454</td>
      <td>14</td>
      <td>12</td>
      <td>Beginner Level</td>
      <td>0.5</td>
      <td>2015-11-09 20:44:25+00:00</td>
      <td>Web Development</td>
      <td>2015</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>3669</th>
      <td>679992</td>
      <td>Building Better APIs with GraphQL</td>
      <td>https://www.udemy.com/building-better-apis-wit...</td>
      <td>True</td>
      <td>50</td>
      <td>555</td>
      <td>89</td>
      <td>16</td>
      <td>All Levels</td>
      <td>2.5</td>
      <td>2015-11-29 22:02:02+00:00</td>
      <td>Web Development</td>
      <td>2015</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>3671</th>
      <td>667122</td>
      <td>Build A Stock Downloader With Visual Studio 20...</td>
      <td>https://www.udemy.com/csharpyahoostockdownloader/</td>
      <td>True</td>
      <td>20</td>
      <td>436</td>
      <td>36</td>
      <td>22</td>
      <td>Intermediate Level</td>
      <td>1.5</td>
      <td>2015-11-19 17:22:47+00:00</td>
      <td>Web Development</td>
      <td>2015</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>3675</th>
      <td>635248</td>
      <td>Learn and Build using Polymer</td>
      <td>https://www.udemy.com/learn-and-build-using-po...</td>
      <td>True</td>
      <td>40</td>
      <td>513</td>
      <td>169</td>
      <td>48</td>
      <td>All Levels</td>
      <td>3.5</td>
      <td>2015-12-30 16:41:42+00:00</td>
      <td>Web Development</td>
      <td>2015</td>
      <td>2015</td>
    </tr>
  </tbody>
</table>
<p>1014 rows × 14 columns</p>
</div>




```python
#We have 2 Year and year columns...drop one
data = data.drop('Year', axis=1)
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
      <th>course_id</th>
      <th>course_title</th>
      <th>url</th>
      <th>is_paid</th>
      <th>price</th>
      <th>num_subscribers</th>
      <th>num_reviews</th>
      <th>num_lectures</th>
      <th>level</th>
      <th>content_duration</th>
      <th>published_timestamp</th>
      <th>subject</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1070968</td>
      <td>Ultimate Investment Banking Course</td>
      <td>https://www.udemy.com/ultimate-investment-bank...</td>
      <td>True</td>
      <td>200</td>
      <td>2147</td>
      <td>23</td>
      <td>51</td>
      <td>All Levels</td>
      <td>1.5</td>
      <td>2017-01-18 20:58:58+00:00</td>
      <td>Business Finance</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1113822</td>
      <td>Complete GST Course &amp; Certification - Grow You...</td>
      <td>https://www.udemy.com/goods-and-services-tax/</td>
      <td>True</td>
      <td>75</td>
      <td>2792</td>
      <td>923</td>
      <td>274</td>
      <td>All Levels</td>
      <td>39.0</td>
      <td>2017-03-09 16:34:20+00:00</td>
      <td>Business Finance</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1006314</td>
      <td>Financial Modeling for Business Analysts and C...</td>
      <td>https://www.udemy.com/financial-modeling-for-b...</td>
      <td>True</td>
      <td>45</td>
      <td>2174</td>
      <td>74</td>
      <td>51</td>
      <td>Intermediate Level</td>
      <td>2.5</td>
      <td>2016-12-19 19:26:30+00:00</td>
      <td>Business Finance</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1210588</td>
      <td>Beginner to Pro - Financial Analysis in Excel ...</td>
      <td>https://www.udemy.com/complete-excel-finance-c...</td>
      <td>True</td>
      <td>95</td>
      <td>2451</td>
      <td>11</td>
      <td>36</td>
      <td>All Levels</td>
      <td>3.0</td>
      <td>2017-05-30 20:07:24+00:00</td>
      <td>Business Finance</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1011058</td>
      <td>How To Maximize Your Profits Trading Options</td>
      <td>https://www.udemy.com/how-to-maximize-your-pro...</td>
      <td>True</td>
      <td>200</td>
      <td>1276</td>
      <td>45</td>
      <td>26</td>
      <td>Intermediate Level</td>
      <td>2.0</td>
      <td>2016-12-13 14:57:18+00:00</td>
      <td>Business Finance</td>
      <td>2016</td>
    </tr>
  </tbody>
</table>
</div>




```python
#data['month'] = data['published_timestamp'].dt.month
data['month'] = data['published_timestamp'].dt.month
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
      <th>course_id</th>
      <th>course_title</th>
      <th>url</th>
      <th>is_paid</th>
      <th>price</th>
      <th>num_subscribers</th>
      <th>num_reviews</th>
      <th>num_lectures</th>
      <th>level</th>
      <th>content_duration</th>
      <th>published_timestamp</th>
      <th>subject</th>
      <th>year</th>
      <th>month</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1070968</td>
      <td>Ultimate Investment Banking Course</td>
      <td>https://www.udemy.com/ultimate-investment-bank...</td>
      <td>True</td>
      <td>200</td>
      <td>2147</td>
      <td>23</td>
      <td>51</td>
      <td>All Levels</td>
      <td>1.5</td>
      <td>2017-01-18 20:58:58+00:00</td>
      <td>Business Finance</td>
      <td>2017</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1113822</td>
      <td>Complete GST Course &amp; Certification - Grow You...</td>
      <td>https://www.udemy.com/goods-and-services-tax/</td>
      <td>True</td>
      <td>75</td>
      <td>2792</td>
      <td>923</td>
      <td>274</td>
      <td>All Levels</td>
      <td>39.0</td>
      <td>2017-03-09 16:34:20+00:00</td>
      <td>Business Finance</td>
      <td>2017</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1006314</td>
      <td>Financial Modeling for Business Analysts and C...</td>
      <td>https://www.udemy.com/financial-modeling-for-b...</td>
      <td>True</td>
      <td>45</td>
      <td>2174</td>
      <td>74</td>
      <td>51</td>
      <td>Intermediate Level</td>
      <td>2.5</td>
      <td>2016-12-19 19:26:30+00:00</td>
      <td>Business Finance</td>
      <td>2016</td>
      <td>12</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1210588</td>
      <td>Beginner to Pro - Financial Analysis in Excel ...</td>
      <td>https://www.udemy.com/complete-excel-finance-c...</td>
      <td>True</td>
      <td>95</td>
      <td>2451</td>
      <td>11</td>
      <td>36</td>
      <td>All Levels</td>
      <td>3.0</td>
      <td>2017-05-30 20:07:24+00:00</td>
      <td>Business Finance</td>
      <td>2017</td>
      <td>5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1011058</td>
      <td>How To Maximize Your Profits Trading Options</td>
      <td>https://www.udemy.com/how-to-maximize-your-pro...</td>
      <td>True</td>
      <td>200</td>
      <td>1276</td>
      <td>45</td>
      <td>26</td>
      <td>Intermediate Level</td>
      <td>2.0</td>
      <td>2016-12-13 14:57:18+00:00</td>
      <td>Business Finance</td>
      <td>2016</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>



### Max | Min number of subscribers for Each Level of courses?


```python
data.head(2)
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
      <th>course_id</th>
      <th>course_title</th>
      <th>url</th>
      <th>is_paid</th>
      <th>price</th>
      <th>num_subscribers</th>
      <th>num_reviews</th>
      <th>num_lectures</th>
      <th>level</th>
      <th>content_duration</th>
      <th>published_timestamp</th>
      <th>subject</th>
      <th>year</th>
      <th>month</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1070968</td>
      <td>Ultimate Investment Banking Course</td>
      <td>https://www.udemy.com/ultimate-investment-bank...</td>
      <td>True</td>
      <td>200</td>
      <td>2147</td>
      <td>23</td>
      <td>51</td>
      <td>All Levels</td>
      <td>1.5</td>
      <td>2017-01-18 20:58:58+00:00</td>
      <td>Business Finance</td>
      <td>2017</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1113822</td>
      <td>Complete GST Course &amp; Certification - Grow You...</td>
      <td>https://www.udemy.com/goods-and-services-tax/</td>
      <td>True</td>
      <td>75</td>
      <td>2792</td>
      <td>923</td>
      <td>274</td>
      <td>All Levels</td>
      <td>39.0</td>
      <td>2017-03-09 16:34:20+00:00</td>
      <td>Business Finance</td>
      <td>2017</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
# the levels
data.level.unique() 
```




    array(['All Levels', 'Intermediate Level', 'Beginner Level',
           'Expert Level'], dtype=object)




```python
#create the grouping level
data.groupby('level')
```




    <pandas.core.groupby.generic.DataFrameGroupBy object at 0x00000185E331E9D0>




```python
#data.groupby('level')['num_subscriber'].max()
data.groupby('level')['num_subscribers'].max()
```




    level
    All Levels            268923
    Beginner Level        161029
    Expert Level            5172
    Intermediate Level     29167
    Name: num_subscribers, dtype: int64




```python
#data.groupby('level')['num_subscriber'].min()
data.groupby('level')['num_subscribers'].min()
```




    level
    All Levels            0
    Beginner Level        0
    Expert Level          1
    Intermediate Level    0
    Name: num_subscribers, dtype: int64




```python
#data.groupby('level').max()
data.groupby('level').max()
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
      <th>course_id</th>
      <th>course_title</th>
      <th>url</th>
      <th>is_paid</th>
      <th>price</th>
      <th>num_subscribers</th>
      <th>num_reviews</th>
      <th>num_lectures</th>
      <th>content_duration</th>
      <th>published_timestamp</th>
      <th>subject</th>
      <th>year</th>
      <th>month</th>
    </tr>
    <tr>
      <th>level</th>
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
      <th>All Levels</th>
      <td>1277924</td>
      <td>６時間でインターバンク市場を攻略！最短距離でトレード基礎力</td>
      <td>https://www.udemy.com/zombie-apocalypse-photos...</td>
      <td>True</td>
      <td>200</td>
      <td>268923</td>
      <td>27445</td>
      <td>544</td>
      <td>76.5</td>
      <td>2017-07-06 21:16:13+00:00</td>
      <td>Web Development</td>
      <td>2017</td>
      <td>12</td>
    </tr>
    <tr>
      <th>Beginner Level</th>
      <td>1282064</td>
      <td>７日でマスター  ビギナー向け Adobe Illustrator　どきどきセミナー</td>
      <td>https://www.udemy.com/zprzqgfl/</td>
      <td>True</td>
      <td>200</td>
      <td>161029</td>
      <td>5924</td>
      <td>779</td>
      <td>78.5</td>
      <td>2017-07-06 21:46:30+00:00</td>
      <td>Web Development</td>
      <td>2017</td>
      <td>12</td>
    </tr>
    <tr>
      <th>Expert Level</th>
      <td>1275790</td>
      <td>[Value Investing] Where White People Keep Thei...</td>
      <td>https://www.udemy.com/working-capital-manageme...</td>
      <td>True</td>
      <td>200</td>
      <td>5172</td>
      <td>249</td>
      <td>157</td>
      <td>12.5</td>
      <td>2017-07-04 18:08:01+00:00</td>
      <td>Web Development</td>
      <td>2017</td>
      <td>12</td>
    </tr>
    <tr>
      <th>Intermediate Level</th>
      <td>1276182</td>
      <td>株式投資で本当のテクニカル分析ができるようになる</td>
      <td>https://www.udemy.com/youtubedownloader/</td>
      <td>True</td>
      <td>200</td>
      <td>29167</td>
      <td>3326</td>
      <td>320</td>
      <td>31.5</td>
      <td>2017-07-05 04:41:54+00:00</td>
      <td>Web Development</td>
      <td>2017</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>



**By-**: **DataSpieler12345**
