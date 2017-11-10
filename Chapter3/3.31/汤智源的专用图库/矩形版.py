# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:31:41 2017

@author: Administrator
"""

import pylab as pl
import math 
import numpy as np  


x=0.0
y=0.0
t=0.
vx=0.5
vy=0.5
dt=0.001
time=0
X=[]
Y=[]
X1=[]
Vx=[]
Vy=[]
while(t<500):
    t=t+dt
    if ((abs(x)<1)and(abs(y)<1))and(abs((x-0.4)**2+y**2>0.05))and(abs((x+0.4)**2+y**2>0.05)):
        x=x+vx*dt
        y=y+vy*dt

    elif((x-0.4)**2+y**2<0.05):
        P=np.array([x-0.4,y])
        n=P/math.sqrt(np.dot(P,P))
        V=np.array([vx,vy])
        v_1=np.dot(V,n)*n
        v_2=V-v_1
        v_1=-v_1
        [vx,vy]=v_1+v_2
        x=x+vx*dt
        y=y+vy*dt
    elif((x+0.4)**2+y**2<0.05):
        P=np.array([x+0.4,y])
        n=P/math.sqrt(np.dot(P,P))
        V=np.array([vx,vy])
        v_1=np.dot(V,n)*n
        v_2=V-v_1
        v_1=-v_1
        [vx,vy]=v_1+v_2
        x=x+vx*dt
        y=y+vy*dt

    elif(abs(x)>1)or(abs(y)>1):
        if(abs(x)>1)and(abs(y)<1):
            vx=-vx
            vy=vy
            x=x+vx*dt
            y=y+vy*dt
        elif(abs(x)<1)and(abs(y)>1):
            vx=vx
            vy=-vy
            x=x+vx*dt
            y=y+vy*dt
        elif(abs(x)>1)and(abs(y)>1):
            vx=-vx
            vy=-vy
            x=x+vx*dt
            y=y+vy*dt
    if(abs(y)<0.01):
        X1.append(x)
        Vx.append(vx)
    X.append(x)
    Y.append(y)
fig1=pl.figure(figsize=(10,4))
pl.subplot(121)
pl.plot(X,Y,'-')
pl.xlim(-1.5,1.5)
pl.ylim(-1.5,1.5)
x=np.linspace(1,1,200)
y=np.linspace(-1,1,200)
pl.plot(x,y)
x=np.linspace(-1,-1,200)
y=np.linspace(-1,1,200)
pl.plot(x,y)
x=np.linspace(-1,1,200)
y=np.linspace(-1,-1,200)
pl.plot(x,y)
x=np.linspace(-1,1,200)
y=np.linspace(1,1,200)
pl.plot(x,y)
x=math.sqrt(0.05)*np.cos(np.linspace(0,2*np.pi,200))+0.4
y=math.sqrt(0.05)*np.sin(np.linspace(0,2*np.pi,200))
pl.plot(x,y)
x=math.sqrt(0.05)*np.cos(np.linspace(0,2*np.pi,200))-0.4
y=math.sqrt(0.05)*np.sin(np.linspace(0,2*np.pi,200))
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