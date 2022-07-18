# Covid Analysis - Delaware North Data and Analytics Recruiting Project 2022-05-10
 
Data Source: https://healthdata.gov/resource/j8mb-icvb.json
Data Dictionary: https://healthdata.gov/dataset/COVID-19-Diagnostic-Laboratory-Testing-PCR-Testing/j8mb-icvb
## Pre-requisites:
Please install the following libraries 
pip install pandas
pip install sodapy
 
## Challenges:
The path given had a limit of 1000 data records. Therefore, it has been increased to 200,000. Although we can also apply best practice for ETL implementation i.e. fetching the data state/date wise by making required changes to the API link and scripting accordingly.
 
## About the data :
Used Sodapy python library to fetch data from API. 
state (string) - Abbreviation of state associated with the test. Typically patient's state of residence, but provider or lab state used when patient is unavailable.
state_name (string) - Name of state associated with the test. Typically patient's state of residence, but provider or lab state used when patient is unavailable.
state_fips (string) - Numerical identifier of state associated with the test. Typically patient's state of residence, but provider or lab state used when patient is unavailable.
fema_region (string) - Region associated with the test. Typically that of patient's state of residence, but provider or lab state used when patient is unavailable.
overall_outcome (string) - Outcome of test -- Positive, Negative or Inconclusive.
date (date) - Typically the date the test completed or the date that the result was reported back to the patient. If neither are available, it can be the date the specimen was collected, arrived at the testing facility, or the date the test was ordered.
new_results_reported (long) - The number of tests completed with the specified outcome in the specified state on the listed date. (Large spikes may result from states submitting tests for several proceeding days at once with a single date).
total_results_reported (long) - The cumulative number of tests completed with the specified outcome in the specified state up through the listed date.
 
## Data quality testing:
Checked for null records (if any). 
### Problem Statement 1- The total number of PCR tests performed as of yesterday in the United States.
Solution: Fetched all the records before today’s date and took the sum of new_results_reported.
In all there were 928,413,010 tests performed in the United States.
 
### Problem Statement 2- The 7-day rolling average number of new cases per day for the last 30 days.
Solution: As seen in the graph below, the 7-day rolling average per day decreased overtime in the past month and a sudden dip can be seen in the last three days of July, 2022. We can conclude that last week of July 2022 saw less number of test cases. Below graph has been created using library matplotlib.

### Problem Statement 3- The 10 states with the highest test positivity rate (positive tests / tests performed) for tests performed in the last 30 days
Solution: There are 2 ways to solve this problem. In case there is large amount of data in the database we can use cumulative column to calculate ratio i.e. 
Positivity rate = (Cumulative of positive cases latest date-Cumulative of positive cases 30 days ago) / Cumulative of positive, negative, inconclusive cases  latest date-Cumulative of positive, negative, inconclusive cases 30 days ago)
Please see the below chart for top 10 states with hightest test positivity rate with Iowa having the most positivity rate in the last 30 days followed by Missouri and Nevada. One of the key points to note is that all the tests performed in Iowa were positive which can be data quality issue or the remaining cases were not reported.
Below graph has been created using library matplotlib.

 

