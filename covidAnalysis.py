# -*- coding: utf-8 -*-
# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
from sodapy import Socrata
from datetime import datetime, date, timedelta
import datetime
import positiveRatioChart as chart
import rollingAverageChart as chart_rolling


client = Socrata("healthdata.gov", None)

results = client.get("j8mb-icvb", limit=200000)

# Convert to pandas DataFrame
df = pd.DataFrame.from_records(results)

# Check non-null values and dtypes
df.info() 

# fetch today's date 
now = datetime.datetime.now()

# change the data types
df['new_results_reported'] = df['new_results_reported'].astype(int)
df['total_results_reported'] = df['total_results_reported'].astype(int)
df['date'] = pd.to_datetime(df['date'],format='%Y-%m-%dT%H:%M:%S')

# fetch all the records before today
df = df.loc[(df['date']) < now]

# 1 The total number of PCR tests performed as of yesterday in the United States.
total_tests_performed_usa= df['new_results_reported'].sum()  
print("The total number of PCR tests performed as of yesterday in the United States = " + str(total_tests_performed_usa))

# 2 The 7-day rolling average number of new cases per day for the last 30 days.
df_records_37_days = df[df.date > now - pd.to_timedelta("37day")]
df_records_37_days = df_records_37_days[['new_results_reported', 'date']]

df_records_sum = df_records_37_days.groupby('date')['new_results_reported'].sum().reset_index().rename(columns={'sum':'new_results_reported','date' : 'date'})
df_records_sum = df_records_sum.set_index('date')

df_rolling = df_records_sum.new_results_reported.rolling(7).mean().reset_index()
df_rolling_30 = df_rolling[df_rolling.date > now - pd.to_timedelta("30day")]
# read data to csv
df_rolling_30.to_csv("rolling_average.csv")
chart_rolling.plt.show()

# The 10 states with the highest test positivity rate 
# (positive tests / tests performed) for tests performed in the last 30 days

df_last_30d_records = df[df.date > now - pd.to_timedelta("30day")]
df_total_records = df_last_30d_records.groupby(['state_name'])['new_results_reported'].sum().reset_index()

df_filtered_records = df_last_30d_records.groupby(['state_name','overall_outcome'])['new_results_reported'].sum().reset_index()

df_positive_records = df_filtered_records[df_filtered_records.overall_outcome.str.contains('Positive')].rename(columns={'new_results_reported':'positive_results_reported'})

df_join = pd.merge(df_positive_records, df_total_records, how='inner', on='state_name')
df_join['ratio'] = (df_join['positive_results_reported'] / df_join['new_results_reported']).round(2)
df_final_ratio = df_join.nlargest(10, ['ratio'])
df_final_ratio.to_csv("ratio.csv")
chart.plt.show()




























