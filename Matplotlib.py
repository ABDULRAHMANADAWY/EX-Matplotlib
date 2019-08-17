# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 01:01:29 2019

@author: mega top
"""
  # Basic Graph
x = [0,1,2,3,4,5]
y = [0,2,4,6,8,10]
# resize our Graph
plt.figure(figsize=(5,3),dpi=100)
# X,Y Labels
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
#plt.plot(x,y, label='2x', color='red', linewidth=2, marker='.', linestyle='--', markersize=10, markeredgecolor='blue')
plt.plot(x,y,'b*--',label='3x')
# Select The wanted plot points
z =np.arange(0,10,1)
# part of the graph as line
plt.plot(z[:4],z[:4]**2,'g',label='x2')
# part of the graph as --
plt.plot(z[:5],z[:5]**2,'g--')
# Add title with fontdict  
plt.title('Our First Graph' , fontdict={'fontname':'comic sans MS', 'fontsize':20 })
# Add a Legned
plt.legend()

