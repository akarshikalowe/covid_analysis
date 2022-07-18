# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 16:10:38 2022

@author: mayan
"""

import pandas as pd
import matplotlib.pyplot as plt

# Read CSV into pandas
dataFrame = pd.read_csv(r"rolling_average.csv")

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

# Labelling x and y axis
plt.xlabel('Dates')
plt.ylabel('Rolling average') 
plt.title('Rolling Average')
plt.legend() 

fig, ax = plt.subplots(figsize =(30, 9))

# Remove x, y Ticks
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')

# Add Plot Title
ax.set_title('The 7-day rolling average number of new cases per day for the last 30 days ',
             loc ='left', )
# plot a line graph
plt.plot(dataFrame["date"], dataFrame["new_results_reported"],marker='o',label='Square')
