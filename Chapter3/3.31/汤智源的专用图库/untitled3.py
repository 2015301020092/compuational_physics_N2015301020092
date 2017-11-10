# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 15:30:31 2017

@author: Administrator
"""

import pylab as pl
import math 
import numpy as np  

pl.figure(figsize=(5,5)) 
x=-0.5
y=0.4
t=0.
vx=0.01
vy=0.01
dt=0.001
time=0
X=[]
Y=[]
V1=[]
V2=[]
while(t<5000):
    dt=0.001
    x=x+vx*dt
    y=y+vy*dt
    vx=vx
    vy=vy
    t=t+dt
    if ((x**2)/4+y**2<1)and((x-0.3)**2+y**2>0.2):
        x=x+vx*dt
        y=y+vy*dt
        t=t+dt

    else:
        if(abs(X[-1]-X[-2])<0.0001)and(abs(Y[-1]-Y[-2])<0.0001):
            P=np.array([x,y])
            n=P/math.sqrt(np.dot(P,P))
            V=np.array([vx,vy])
            v_1=np.dot(V,n)*n
            v_2=V-v_1
            v_1=-v_1
            [vx,vy]=v_1+v_2
            x=x+vx*dt*10
            y=y+vy*dt*10
        else:
            x=X[-2]
            y=Y[-2]
            vx=V1[-2]
            vy=V2[-2]
            dt=0.0001
            x=x+vx*dt
            y=y+vy*dt
    X.append(x)
    Y.append(y)
    V1.append(vx)
    V2.append(vy)
pl.plot(X,Y,'-')
x=math.sqrt(0.2)*(np.cos(np.linspace(0,2*np.pi,200)))+0.3
y=math.sqrt(0.2)*(np.sin(np.linspace(0,2*np.pi,200)))
pl.plot(x,y)
x=2*np.cos(np.linspace(0,2*np.pi,200))
y=np.sin(np.linspace(0,2*np.pi,200))
pl.plot(x,y)
pl.ylabel('y')
pl.xlabel('x')
pl.xlim(-2,2)
pl.ylim(-2,2)
pl.show()
        
        
        
        
        