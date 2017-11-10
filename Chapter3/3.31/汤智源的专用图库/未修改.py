# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 15:30:31 2017

@author: Administrator
"""

import pylab as pl
import math 
import numpy as np  


x=0.6
y=0.6
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
    if ((x**2)/4+y**2<1)and((abs(x)>0.5)or(abs(y)>0.5)):
        x=x+vx*dt
        y=y+vy*dt
        t=t+dt

    elif((x**2)/4+y**2>1):
        P=np.array([x/4,y])
        n=P/math.sqrt(np.dot(P,P))
        V=np.array([vx,vy])
        v_1=np.dot(V,n)*n
        v_2=V-v_1
        v_1=-v_1
        [vx,vy]=v_1+v_2
        x=x+vx*dt
        y=y+vy*dt

    elif(abs(x)<0.5)or(abs(y)<0.5):
        if(abs(X[-2]-0.2)>0.5)and(abs(Y[-2])<0.5):
            vx=-vx
            vy=vy
            x=x+vx*dt
            y=y+vy*dt
        elif(abs(Y[-2])>0.5)and(abs(X[-2]-0.2)<0.5):
            vx=vx
            vy=-vy
            x=x+vx*dt
            y=y+vy*dt
        elif(abs(Y[-2])>0.5)and(abs(X[-2]-0.2)>0.5):
            vx=-vx
            vy=-vy
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
pl.ylim(-1.2,1.2)
x=np.linspace(0.5,0.5,200)
y=np.linspace(-0.5,0.5,200)
pl.plot(x,y)
x=np.linspace(-0.5,-0.5,200)
y=np.linspace(-0.5,0.5,200)
pl.plot(x,y)
x=np.linspace(-0.5,0.5,200)
y=np.linspace(-0.5,-0.5,200)
pl.plot(x,y)
x=np.linspace(-0.5,0.5,200)
y=np.linspace(0.5,0.5,200)
pl.plot(x,y)
x=2*np.cos(np.linspace(0,2*np.pi,200))
y=np.sin(np.linspace(0,2*np.pi,200))
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
        
        
        
        
        