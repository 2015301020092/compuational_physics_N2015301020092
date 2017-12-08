# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 18:22:12 2017

@author: Administrator
"""

import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

V1=100
V2=0
V_bonrdary=0.
n=30
V_n=0
V=[]
for j in range (n):
    V.append([0.0]*n)
for j in [0,n-1]:
    V[j]=[V_bonrdary]*n
for j in range(0,30):
    V[16][j]=V2
V[15][15]=V1
counter=0;
while(True):
    dV=0
    alpha=2./(1.+(math.pi)/30)
    for j in range(1,29):
        for i in range(1,29):
            if(((j==15)and(i==15))or((j==16)and(i in range(0,30)))):
                continue
            V_n=1./4.*(V[j-1][i]+V[j+1][i]+V[j][i-1]+V[j][i+1])
            V[i][j]=alpha*(V_n-V[i][j])+V[i][j]
            dV=dV+abs(alpha*(V_n-V[i][j]))
    counter=counter+1
    if(counter>=10)and(dV<abs(V1-V2)*n*n*10**(-5)):
        break

def Ele_field(x1,x2,y1,y2):
    dx=abs(x1-x2)/float(n-1)
    Ex=[]
    Ey=[]
    for j in range(n):
        Ex.append([0.0]*n)
        Ey.append([0.0]*n)
    for j in range(n-1):
        for i in range(n-1):
            Ex[i][j]=-(V[j][i+1]-V[j][i-1])/(2*dx)
            Ey[i][j]=-(V[j+1][i]-V[j-1][i])/(2*dx)
            
            
fig = plt.figure(figsize=(8,5))
ax = Axes3D(fig)
x=np.linspace(-1,1,30)
y=np.linspace(-1,1,30)
x,y=np.meshgrid(x,y)
ax.set_xlabel("x(m)")
ax.set_ylabel("y(m)")
ax.set_zlabel("Electric potential/V")
ax.set_title("Potential near lighting rod")
ax.set_zlim(-10,100)
ax.plot_surface(x,y,V, rstride=1, cstride=1, cmap=cm.coolwarm)


plt.legend()

plt.show()
    
