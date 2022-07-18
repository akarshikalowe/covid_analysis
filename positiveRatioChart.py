# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 15:49:01 2022

@author: mayan
"""

import pandas as pd
from matplotlib import pyplot as plt
 
# Read CSV into pandas
data = pd.read_csv(r"ratio.csv")
data.head()
df = pd.DataFrame(data)
 
name = df['state_name'].head(12)
price = df['ratio'].head(12)
 
# Figure Size
fig, ax = plt.subplots(figsize =(16, 9))
 
# Horizontal Bar Plot
ax.barh(name, price)
 
# Remove axes splines
for s in ['top', 'bottom', 'left', 'right']:
    ax.spines[s].set_visible(False)
 
# Remove x, y Ticks
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')
 
# Add padding between axes and labels
ax.xaxis.set_tick_params(pad = 5)
ax.yaxis.set_tick_params(pad = 10)
 
# Add x, y gridlines
ax.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)
 
# Show top values
ax.invert_yaxis()
 
# Add annotation to bars
for i in ax.patches:
    plt.text(i.get_width()+0.2, i.get_y()+0.5,
             str(round((i.get_width()), 2)),
             fontsize = 10, fontweight ='bold',
             color ='grey')
 
# Add Plot Title
ax.set_title('Top 10 countries with the Positive test records',
             loc ='left', )
plt.xlabel('ratio')
plt.ylabel('states')  
