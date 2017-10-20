# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 19:50:37 2017

@author: 高多奇
"""

import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

g=9.8
w=2000*math.pi/60
dt=0.0001
S0=0.00041
m=0.150
B=0.00004
x=[0]
y=[0]
z=[1.8]
v=30
vx=30
vy=0
vz=0
ax=-B*v*vx/m
az=-g+S0*vz*w/m
ay=0
X=[0] 
Y=[0]
Z=[2]
v1=30
vx1=30
vy1=0
vz1=0
ax1=-B*v1*vx1/m
az1=-g
ay1=S0*vx1*w/m
i=0
j=0
while z[i]>=0:
    x.append(x[i]+vx*dt)
    y.append(y[i]+vy*dt)
    z.append(z[i]+vz*dt)
    vx=vx+ax*dt
    vy=vy+ay*dt
    vz=vz+az*dt
    v=(vx**2+vy**2+vz**2)**0.5
    i=i+1

while Z[j]>=0:
    x.append(X[j]+vx1*dt)
    y.append(Y[j]+vy1*dt)
    z.append(Z[j]+vz1*dt)
    vx1=vx1+ax1*dt
    vy1=vy1+ay1*dt
    vz1=vz1+az1*dt
    v1=(vx1**2+vy1**2+vz1**2)**0.5
    j=j+1

fig = plt.figure(figsize=(8,5))
ax = Axes3D(fig)


plt.xlabel("x(m)")
plt.ylabel("y(m)")
ax.set_zlabel("z(m)")
plt.title("trajectory of baseball")
ax.set_zlim(-1,1)

ax.plot(x, y, z,color="green",label="trajectory(back spin)",linewidth=2)
ax.plot(x1, y1, z1, color="blue",label="trajectory(side spin)",linewidth=2)
ax.scatter(x[0],y[0],z[0],label="initial position",color="red")
ax.scatter(x[-1],y[-1],z[-1],label="final position",color="black")
plt.legend()

plt.show()
    




