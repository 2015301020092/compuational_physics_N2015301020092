# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 18:43:19 2017

@author: Administrator
"""

import pylab as pl
import math 
import numpy as np  
x=0
y=0
t=0.
vx=0.6
vy=1.
dt=0.001
time=0
X=[]
Y=[]
X1=[]
Vx=[]
Vy=[]
while(t<1000):
    if ((x**2)/4+(y**2)/3<1)and((x-0.5)**2+y**2>0.2)and((x+0.5)**2+y**2>0.2):
        x=x+vx*dt
        y=y+vy*dt
        t=t+dt

    elif((x**2)/4+(y**2)/3>1):
        P=np.array([x/4,y/3])
        n=P/math.sqrt(np.dot(P,P))
        V=np.array([vx,vy])
        v_1=np.dot(V,n)*n
        v_2=V-v_1
        v_1=-v_1
        [vx,vy]=v_1+v_2
        x=x+vx*dt
        y=y+vy*dt

    elif((x-0.5)**2+y**2<0.2):
        P=np.array([x-0.5,y])
        n=P/math.sqrt(np.dot(P,P))
        V=np.array([vx,vy])
        v_1=np.dot(V,n)*n
        v_2=V-v_1
        v_1=-v_1
        [vx,vy]=v_1+v_2
        x=x+vx*dt
        y=y+vy*dt
    elif((x+0.5)**2+y**2<0.2):
        P=np.array([x+0.5,y])
        n=P/math.sqrt(np.dot(P,P))
        V=np.array([vx,vy])
        v_1=np.dot(V,n)*n
        v_2=V-v_1
        v_1=-v_1
        [vx,vy]=v_1+v_2
        x=x+vx*dt
        y=y+vy*dt
    if(abs(y)<0.01)and(abs(vx),0.95):
        X1.append(x)
        Vx.append(vx)
    X.append(x)
    Y.append(y)
fig1=pl.figure(figsize=(10,4))
pl.subplot(121)
pl.plot(X,Y,'-')
pl.xlim(-2,2)
pl.ylim(-2,2)
x=math.sqrt(0.2)*np.cos(np.linspace(0,2*np.pi,200))+0.5
y=math.sqrt(0.2)*np.sin(np.linspace(0,2*np.pi,200))
pl.plot(x,y)
x=math.sqrt(0.2)*np.cos(np.linspace(0,2*np.pi,200))-0.5
y=math.sqrt(0.2)*np.sin(np.linspace(0,2*np.pi,200))
pl.plot(x,y)
x=2*np.cos(np.linspace(0,2*np.pi,200))
y=math.sqrt(3)*np.sin(np.linspace(0,2*np.pi,200))
pl.plot(x,y)
pl.ylabel('y')
pl.xlabel('x')
pl.title('billiard')
pl.subplot(122)
pl.plot(X1,Vx,'.')
pl.xlabel('x')
pl.ylabel('vx')
pl.title('phase space plot')
pl.xlim(-2,2)
pl.ylim(-1,1)
pl.show()
