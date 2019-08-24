# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 01:01:29 2019

@author: mega top
"""
 import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

Bins = [40,50,60,70,80,90,100]
plt.figure(figsize=(8,5))
plt.hist(fifa.Overall, Bins=Bins, color='g')
plt.xticks(Bins)
plt.ylabel('Number of Players')
plt.xlabel('Skill Level')
plt.title('Distribution of Player Skills in FIFA 2018')
plt.savefig('histogram.png', dpi=300)
plt.show()
  
