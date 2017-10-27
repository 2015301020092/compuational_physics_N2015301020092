# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 23:19:55 2017

@author: 李弘禹
"""

import pylab as pl
import math   
g=9.8
l=9.8
m=1
dt=0.0001
q=0.5
F=0.5
D=0.6667
t=0
x=0.2
w=0
E=0
pi=math.pi
X=[0]
Y=[0]
while t<=500:
    w=w-((g/l)*math.sin(x)+q*w-F*math.sin(D*t))*dt
    E=E+0.5*m*l*l*(w*w+x*x)*dt*dt
    x=x+w*dt
    if x<-1*pi:        
         x=x+2*pi
    elif x>pi:
         x=x-2*pi
    else:
         x=x
    X.append(t)
    Y.append(E)  
    t=t+dt  
pl.plot(X, Y,'r,',label='E versus t  F='+str(F)+'dt='+str(dt))
pl.title('')
pl.xlabel('t')
pl.ylabel('E')
pl.xlim(0, 500)
pl.ylim(-2, 10)
        
pl.legend(loc = 'best')