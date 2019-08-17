# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 01:01:29 2019

@author: mega top
"""

x = [0,1,2,3,4,5]
y = [0,2,4,6,8,10]
plt.figure(figsize=(5,3),dpi=100)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.plot(x,y,'b*--',label='3x')
z =np.arange(0,10,1)
plt.plot(z[:4],z[:4]**2,'g',label='x2')
plt.plot(z[:5],z[:5]**2,'g--')
plt.title('Our First Graph' , fontdict={'fontname':'comic sans MS', 'fontsize':20 })
plt.legend()
