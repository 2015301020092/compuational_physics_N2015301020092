
"""
Created on Fri Dec 15 15:06:49 2017

@author: Administrator
"""

import math
import pylab as pl
import numpy as np

r=0.5
M=100
xi=30
k=1000*10**(-4)
TS=250
xl=1.0
xy=70

#定义作图数组：
c=[] 
for c1 in range(0,M+1):
             c.append(c1/100)
else:
    c=c
#定义系统参量
h=TS+1   
    
#定义t=O状态
a=np.zeros((M+1,3))
for n in range(2,M):
    #a[n-1][1-1]=math.exp(-k*(n-xi)**2)+(n-xi)**3
    
    a[n-1][1-1]=math.exp(-k*(n-xy)**2)+math.exp(-k*(n-xi)**2)
    
#定义t=1状态：
for n in range(2,M):
    a[n-1][2-1]=a[n-1][1-1]
else:
    a=a
#定义t=3状态
for i in range(1,M-1) :
    j=1 
    a[i][j+1]=2*(1-r**2)*a[i][j]-a[i][j-1]+(r**2)*(a[i+1][j]+a[i-1][j])#最上一行始终为0
        
     
#画出t=0,1的波形
pl.figure(figsize=(7,1.2*h))
pl.subplot(h,1,1)
pl.xticks(np.linspace(0,M,0))
pl.ylim(-xl,xl)
pl.plot(c,a[:,1],label=0,color='r')
pl.legend(loc='upper right')
pl.subplot(h,1,2)
pl.xticks(np.linspace(0,M,0))
pl.ylim(-xl,xl)
pl.plot(c,a[:,2],label=1,color='g')
pl.legend(loc='upper right')


t=1 
while t<=TS-1:
    for i in range(1,M-1):
          a[i][0]=a[i][1]
          a[i][1]=a[i][2]
    else:
          for i in range(1,M-1):
               a[i][j+1]=2*(1-r**2)*a[i][j]-a[i][j-1]+(r**2)*(a[i+1][j]+a[i-1][j])
          else:
              pl.subplot(h,1,t+2)
              pl.ylim(-xl,xl)
              pl.xticks(np.linspace(0,20,0))
              pl.plot(c,a[:,2],label=t+1,color='blue')
              pl.legend(loc='upper right')
          t=t+1
else:
    pl.subplot(h,1,h)
    pl.xticks(np.linspace(0,M/100,6))
    pl.show()
