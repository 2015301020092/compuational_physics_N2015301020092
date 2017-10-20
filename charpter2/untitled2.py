# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 22:36:28 2017

@author: 高多奇
"""

import numpy as np
import pylab as pl
import math   
g=9.8
w=2000*math.pi/60
dt=0.0001
S0=0.00041
m=0.150
B=0.00004
x=0
y=1.8
X=[0]
Y=[0]
v=60
vx=60
vy=0
ax=-B*v*vx/m
ay=-g-S0*vx*w/m
while y>=0:
    vx=vx+ax*dt
    vy=vy+ay*dt
    v=(vx**2+vy**2)**0.5
    x=x+vx*dt
    y=y+vy*dt
    X.append(x)
    Y.append(y)
else:
    pl.plot(X, Y,'r--',label='trajectory(back spin)',linewidth=2)
    pl.title('trajectory(back spin)')

    pl.xlabel('m')
    pl.ylabel('m')
    pl.xlim(0, 30)
    pl.ylim(0, 3)
    pl.legend(loc = 'best')
g=9.8
w=2000*math.pi/60
dt=0.0001
S0=0.00041
m=0.150
B=0.00004
x=0
y=1.8
X=[0]
Y=[0]

vy=0
ax=-B*v*vx/m
ay=-g
while y>=0:
    vx=vx+ax*dt
    vy=vy+ay*dt
    v=(vx**2+vy**2)**0.5
    x=x+vx*dt
    y=y+vy*dt
    X.append(x)
    Y.append(y)
else:
    pl.plot(X, Y,'b--',label='trajectory(without spin)',linewidth=2)
    pl.title('trajectory(back spin)')

    pl.xlabel('m')
    pl.ylabel('m')
    pl.xlim(0, 30)
    pl.ylim(0, 3)
    pl.legend(loc = 'best')
    pl.show()