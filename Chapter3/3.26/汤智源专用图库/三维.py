import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

sigma=10
b=8.0/3.0
dt=0.001
x=1.
y=0.
z=0.
t=0.
X=[0] 
Y=[0]
Z=[0]
r=10

while (t<=50):
        a_x=sigma*(y-x)
        a_y=-x*z+r*x-y
        a_z=x*y-b*z
        x=x+a_x*dt
        y=y+a_y*dt
        z=z+a_z*dt
        t=t+dt
        
        X.append(x)
        Y.append(y)
        Z.append(z)


fig = plt.figure(figsize=(8,5))
ax = Axes3D(fig)


plt.xlabel("x")
plt.ylabel("y")
ax.set_zlabel("z")
plt.title("three dimension")
ax.set_zlim(-25,30)
ax.set_ylim(-25,25)
ax.set_xlim(-25,25)

ax.plot(X, Y, Z,color="b",label="r="+str(r),linewidth=2)
ax.scatter(X[0],Y[0],Z[0],label="initial position",color="red")
ax.scatter(X[-1],Y[-1],Z[-1],label="final position",color="black")
plt.legend()

plt.show()