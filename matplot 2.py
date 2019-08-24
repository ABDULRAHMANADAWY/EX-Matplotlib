# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 01:01:29 2019

@author: mega top
"""
 import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
fifa =pd.read_csv('fifa_data.csv')
# Histogram
Bins = [40,50,60,70,80,90,100]
# resize our Graph
plt.figure(figsize=(8,5))
# plot our figure in histogram and determine color  
plt.hist(fifa.Overall, Bins=Bins, color='g')
# X axis Tickmarks (scale of our graph)
plt.xticks(Bins)
# X , Y Labels
plt.ylabel('Number of Players')
plt.xlabel('Skill Level')
# write a title 
plt.title('Distribution of Player Skills in FIFA 2018')
# save figure
plt.savefig('histogram.png', dpi=300)
plt.show()
  
