```python
import io
```


```python
import pandas as pd
```


```python
import requests
```


```python
url = 'https://storage.googleapis.com/uber-data-engineering-project/uber_data.csv'
response = requests.get(url)
```


```python
df = pd.read_csv(io.StringIO(response.text), sep=',')
```


```python
df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
```


```python
df = df.drop_duplicates().reset_index(drop=True)
df['trip_id'] = df.index
```


```python
df.head()
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
      <th>VendorID</th>
      <th>tpep_pickup_datetime</th>
      <th>tpep_dropoff_datetime</th>
      <th>passenger_count</th>
      <th>trip_distance</th>
      <th>pickup_longitude</th>
      <th>pickup_latitude</th>
      <th>RatecodeID</th>
      <th>store_and_fwd_flag</th>
      <th>dropoff_longitude</th>
      <th>dropoff_latitude</th>
      <th>payment_type</th>
      <th>fare_amount</th>
      <th>extra</th>
      <th>mta_tax</th>
      <th>tip_amount</th>
      <th>tolls_amount</th>
      <th>improvement_surcharge</th>
      <th>total_amount</th>
      <th>trip_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2016-03-01</td>
      <td>2016-03-01 00:07:55</td>
      <td>1</td>
      <td>2.50</td>
      <td>-73.976746</td>
      <td>40.765152</td>
      <td>1</td>
      <td>N</td>
      <td>-74.004265</td>
      <td>40.746128</td>
      <td>1</td>
      <td>9.0</td>
      <td>0.5</td>
      <td>0.5</td>
      <td>2.05</td>
      <td>0.00</td>
      <td>0.3</td>
      <td>12.35</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2016-03-01</td>
      <td>2016-03-01 00:11:06</td>
      <td>1</td>
      <td>2.90</td>
      <td>-73.983482</td>
      <td>40.767925</td>
      <td>1</td>
      <td>N</td>
      <td>-74.005943</td>
      <td>40.733166</td>
      <td>1</td>
      <td>11.0</td>
      <td>0.5</td>
      <td>0.5</td>
      <td>3.05</td>
      <td>0.00</td>
      <td>0.3</td>
      <td>15.35</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>2016-03-01</td>
      <td>2016-03-01 00:31:06</td>
      <td>2</td>
      <td>19.98</td>
      <td>-73.782021</td>
      <td>40.644810</td>
      <td>1</td>
      <td>N</td>
      <td>-73.974541</td>
      <td>40.675770</td>
      <td>1</td>
      <td>54.5</td>
      <td>0.5</td>
      <td>0.5</td>
      <td>8.00</td>
      <td>0.00</td>
      <td>0.3</td>
      <td>63.80</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>2016-03-01</td>
      <td>2016-03-01 00:00:00</td>
      <td>3</td>
      <td>10.78</td>
      <td>-73.863419</td>
      <td>40.769814</td>
      <td>1</td>
      <td>N</td>
      <td>-73.969650</td>
      <td>40.757767</td>
      <td>1</td>
      <td>31.5</td>
      <td>0.0</td>
      <td>0.5</td>
      <td>3.78</td>
      <td>5.54</td>
      <td>0.3</td>
      <td>41.62</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>2016-03-01</td>
      <td>2016-03-01 00:00:00</td>
      <td>5</td>
      <td>30.43</td>
      <td>-73.971741</td>
      <td>40.792183</td>
      <td>3</td>
      <td>N</td>
      <td>-74.177170</td>
      <td>40.695053</td>
      <td>1</td>
      <td>98.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>15.50</td>
      <td>0.3</td>
      <td>113.80</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
datetime_dim = df[['tpep_pickup_datetime','tpep_dropoff_datetime']].reset_index(drop=True)
datetime_dim['tpep_pickup_datetime'] = datetime_dim['tpep_pickup_datetime']
datetime_dim['pick_hour'] = datetime_dim['tpep_pickup_datetime'].dt.hour
datetime_dim['pick_day'] = datetime_dim['tpep_pickup_datetime'].dt.day
datetime_dim['pick_month'] = datetime_dim['tpep_pickup_datetime'].dt.month
datetime_dim['pick_year'] = datetime_dim['tpep_pickup_datetime'].dt.year
datetime_dim['pick_weekday'] = datetime_dim['tpep_pickup_datetime'].dt.weekday

datetime_dim['tpep_dropoff_datetime'] = datetime_dim['tpep_dropoff_datetime']
datetime_dim['drop_hour'] = datetime_dim['tpep_dropoff_datetime'].dt.hour
datetime_dim['drop_day'] = datetime_dim['tpep_dropoff_datetime'].dt.day
datetime_dim['drop_month'] = datetime_dim['tpep_dropoff_datetime'].dt.month
datetime_dim['drop_year'] = datetime_dim['tpep_dropoff_datetime'].dt.year
datetime_dim['drop_weekday'] = datetime_dim['tpep_dropoff_datetime'].dt.weekday


datetime_dim['datetime_id'] = datetime_dim.index

# datetime_dim = datetime_dim.rename(columns={'tpep_pickup_datetime': 'datetime_id'}).reset_index(drop=True)
datetime_dim = datetime_dim[['datetime_id', 'tpep_pickup_datetime', 'pick_hour', 'pick_day', 'pick_month', 'pick_year', 'pick_weekday',
                             'tpep_dropoff_datetime', 'drop_hour', 'drop_day', 'drop_month', 'drop_year', 'drop_weekday']]
#
datetime_dim.head()
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
      <th>datetime_id</th>
      <th>tpep_pickup_datetime</th>
      <th>pick_hour</th>
      <th>pick_day</th>
      <th>pick_month</th>
      <th>pick_year</th>
      <th>pick_weekday</th>
      <th>tpep_dropoff_datetime</th>
      <th>drop_hour</th>
      <th>drop_day</th>
      <th>drop_month</th>
      <th>drop_year</th>
      <th>drop_weekday</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>2016-03-01</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>2016</td>
      <td>1</td>
      <td>2016-03-01 00:07:55</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>2016</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2016-03-01</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>2016</td>
      <td>1</td>
      <td>2016-03-01 00:11:06</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>2016</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>2016-03-01</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>2016</td>
      <td>1</td>
      <td>2016-03-01 00:31:06</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>2016</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>2016-03-01</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>2016</td>
      <td>1</td>
      <td>2016-03-01 00:00:00</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>2016</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>2016-03-01</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>2016</td>
      <td>1</td>
      <td>2016-03-01 00:00:00</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>2016</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
passenger_count_dim = df[['passenger_count']].reset_index(drop=True)
passenger_count_dim['passenger_count_id'] = passenger_count_dim.index
passenger_count_dim = passenger_count_dim[['passenger_count_id','passenger_count']]

trip_distance_dim = df[['trip_distance']].reset_index(drop=True)
trip_distance_dim['trip_distance_id'] = trip_distance_dim.index
trip_distance_dim = trip_distance_dim[['trip_distance_id','trip_distance']]
```


```python
rate_code_type = {
    1:"Standard rate",
    2:"JFK",
    3:"Newark",
    4:"Nassau or Westchester",
    5:"Negotiated fare",
    6:"Group ride"
}

rate_code_dim = df[['RatecodeID']].reset_index(drop=True)
rate_code_dim['rate_code_id'] = rate_code_dim.index
rate_code_dim['rate_code_name'] = rate_code_dim['RatecodeID'].map(rate_code_type)
rate_code_dim = rate_code_dim[['rate_code_id','RatecodeID','rate_code_name']]

# rate_code_dim.head()
```


```python
rate_code_dim.head()
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
      <th>rate_code_id</th>
      <th>RatecodeID</th>
      <th>rate_code_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>Standard rate</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>Standard rate</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>1</td>
      <td>Standard rate</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>1</td>
      <td>Standard rate</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>3</td>
      <td>Newark</td>
    </tr>
  </tbody>
</table>
</div>




```python
pickup_location_dim = df[['pickup_longitude', 'pickup_latitude']].reset_index(drop=True)
pickup_location_dim['pickup_location_id'] = pickup_location_dim.index
pickup_location_dim = pickup_location_dim[['pickup_location_id','pickup_latitude','pickup_longitude']] 


dropoff_location_dim = df[['dropoff_longitude', 'dropoff_latitude']].reset_index(drop=True)
dropoff_location_dim['dropoff_location_id'] = dropoff_location_dim.index
dropoff_location_dim = dropoff_location_dim[['dropoff_location_id','dropoff_latitude','dropoff_longitude']]
```


```python
payment_type_name = {
    1:"Credit card",
    2:"Cash",
    3:"No charge",
    4:"Dispute",
    5:"Unknown",
    6:"Voided trip"
}
payment_type_dim = df[['payment_type']].reset_index(drop=True)
payment_type_dim['payment_type_id'] = payment_type_dim.index
payment_type_dim['payment_type_name'] = payment_type_dim['payment_type'].map(payment_type_name)
payment_type_dim = payment_type_dim[['payment_type_id','payment_type','payment_type_name']]
```


```python
fact_table = df.merge(passenger_count_dim, left_on='trip_id', right_on='passenger_count_id') \
             .merge(trip_distance_dim, left_on='trip_id', right_on='trip_distance_id') \
             .merge(rate_code_dim, left_on='trip_id', right_on='rate_code_id') \
             .merge(pickup_location_dim, left_on='trip_id', right_on='pickup_location_id') \
             .merge(dropoff_location_dim, left_on='trip_id', right_on='dropoff_location_id')\
             .merge(datetime_dim, left_on='trip_id', right_on='datetime_id') \
             .merge(payment_type_dim, left_on='trip_id', right_on='payment_type_id') \
             [['trip_id','VendorID', 'datetime_id', 'passenger_count_id',
               'trip_distance_id', 'rate_code_id', 'store_and_fwd_flag', 'pickup_location_id', 'dropoff_location_id',
               'payment_type_id', 'fare_amount', 'extra', 'mta_tax', 'tip_amount', 'tolls_amount',
               'improvement_surcharge', 'total_amount']]
```


```python
payment_type_dim.columns
```




    Index(['payment_type_id', 'payment_type', 'payment_type_name'], dtype='object')




```python
fact_table.columns
```




    Index(['trip_id', 'VendorID', 'datetime_id', 'passenger_count_id',
           'trip_distance_id', 'rate_code_id', 'store_and_fwd_flag',
           'pickup_location_id', 'dropoff_location_id', 'payment_type_id',
           'fare_amount', 'extra', 'mta_tax', 'tip_amount', 'tolls_amount',
           'improvement_surcharge', 'total_amount'],
          dtype='object')




```python
fact_table
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
      <th>trip_id</th>
      <th>VendorID</th>
      <th>datetime_id</th>
      <th>passenger_count_id</th>
      <th>trip_distance_id</th>
      <th>rate_code_id</th>
      <th>store_and_fwd_flag</th>
      <th>pickup_location_id</th>
      <th>dropoff_location_id</th>
      <th>payment_type_id</th>
      <th>fare_amount</th>
      <th>extra</th>
      <th>mta_tax</th>
      <th>tip_amount</th>
      <th>tolls_amount</th>
      <th>improvement_surcharge</th>
      <th>total_amount</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>N</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>9.0</td>
      <td>0.5</td>
      <td>0.5</td>
      <td>2.05</td>
      <td>0.00</td>
      <td>0.3</td>
      <td>12.35</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>N</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>11.0</td>
      <td>0.5</td>
      <td>0.5</td>
      <td>3.05</td>
      <td>0.00</td>
      <td>0.3</td>
      <td>15.35</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>N</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>54.5</td>
      <td>0.5</td>
      <td>0.5</td>
      <td>8.00</td>
      <td>0.00</td>
      <td>0.3</td>
      <td>63.80</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>N</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>31.5</td>
      <td>0.0</td>
      <td>0.5</td>
      <td>3.78</td>
      <td>5.54</td>
      <td>0.3</td>
      <td>41.62</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>2</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>N</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>98.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>15.50</td>
      <td>0.3</td>
      <td>113.80</td>
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
    </tr>
    <tr>
      <th>99995</th>
      <td>99995</td>
      <td>1</td>
      <td>99995</td>
      <td>99995</td>
      <td>99995</td>
      <td>99995</td>
      <td>N</td>
      <td>99995</td>
      <td>99995</td>
      <td>99995</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.5</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.3</td>
      <td>5.80</td>
    </tr>
    <tr>
      <th>99996</th>
      <td>99996</td>
      <td>1</td>
      <td>99996</td>
      <td>99996</td>
      <td>99996</td>
      <td>99996</td>
      <td>N</td>
      <td>99996</td>
      <td>99996</td>
      <td>99996</td>
      <td>14.0</td>
      <td>0.0</td>
      <td>0.5</td>
      <td>2.00</td>
      <td>0.00</td>
      <td>0.3</td>
      <td>16.80</td>
    </tr>
    <tr>
      <th>99997</th>
      <td>99997</td>
      <td>1</td>
      <td>99997</td>
      <td>99997</td>
      <td>99997</td>
      <td>99997</td>
      <td>N</td>
      <td>99997</td>
      <td>99997</td>
      <td>99997</td>
      <td>29.0</td>
      <td>0.0</td>
      <td>0.5</td>
      <td>8.80</td>
      <td>5.54</td>
      <td>0.3</td>
      <td>44.14</td>
    </tr>
    <tr>
      <th>99998</th>
      <td>99998</td>
      <td>2</td>
      <td>99998</td>
      <td>99998</td>
      <td>99998</td>
      <td>99998</td>
      <td>N</td>
      <td>99998</td>
      <td>99998</td>
      <td>99998</td>
      <td>5.5</td>
      <td>0.5</td>
      <td>0.5</td>
      <td>1.36</td>
      <td>0.00</td>
      <td>0.3</td>
      <td>8.16</td>
    </tr>
    <tr>
      <th>99999</th>
      <td>99999</td>
      <td>1</td>
      <td>99999</td>
      <td>99999</td>
      <td>99999</td>
      <td>99999</td>
      <td>N</td>
      <td>99999</td>
      <td>99999</td>
      <td>99999</td>
      <td>6.0</td>
      <td>0.0</td>
      <td>0.5</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.3</td>
      <td>6.80</td>
    </tr>
  </tbody>
</table>
<p>100000 rows × 17 columns</p>
</div>




```python
# CREATE OR REPLACE TABLE `data-with-darshil.uber_dataset.tbl_analysis_report` AS (
# SELECT
#   f.VendorID,
#   f.tpep_pickup_datetime,
#   f.tpep_dropoff_datetime,
#   p.passenger_count,
#   td.trip_distance,
#   rc.RatecodeID,
#   f.store_and_fwd_flag,
#   pl.pickup_latitude,
#   pl.pickup_longitude,
#   dl.dropoff_latitude,
#   dl.dropoff_longitude,
#   pt.payment_type,
#   f.fare_amount,
#   f.extra,
#   f.mta_tax,
#   f.tip_amount,
#   f.tolls_amount,
#   f.improvement_surcharge,
#   f.total_amount
# FROM
#   `data-with-darshil.uber_dataset.fact_table` f
#   JOIN `data-with-darshil.uber_dataset.passenger_count_dim` p ON f.passenger_count_id = p.passenger_count_id
#   JOIN `data-with-darshil.uber_dataset.trip_distance_dim` td ON f.trip_distance_id = td.trip_distance_id
#   JOIN `data-with-darshil.uber_dataset.rate_code_dim` rc ON f.rate_code_id = rc.rate_code_id
#   JOIN `data-with-darshil.uber_dataset.pickup_location_dim` pl ON f.pickup_location_id = pl.pickup_location_id
#   JOIN `data-with-darshil.uber_dataset.dropoff_location_dim` dl ON f.dropoff_location_id = dl.dropoff_location_id
#   JOIN `data-with-darshil.uber_dataset.payment_type_dim` pt ON f.payment_type_id = pt.payment_type_id);
```
