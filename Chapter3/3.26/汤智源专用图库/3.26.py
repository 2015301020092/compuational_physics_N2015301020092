import pylab as pl
import math   
pl.figure(figsize=(7,7)) 

r=[20,30,40]
for i in range(len(r)):
    sigma=10
    b=8.0/3.0
    dt=0.0001
    x=1.
    y=0.
    z=0.
    t=0.
    X=[0]
    Y=[0]
    while(t<=50):
        a_x=sigma*(y-x)
        a_y=-x*z+r[i]*x-y
        a_z=x*y-b*z
        x=x+a_x*dt
        y=y+a_y*dt
        z=z+a_z*dt
        t=t+dt
       
        X.append(t)
        Y.append(z)
    pl.plot(X, Y,'-',label='z versus t r='+str(r[i]))
    pl.title('t versus z')
    pl.ylabel('z')
    pl.xlabel('t')
    pl.xlim(0,30)
    pl.ylim(0,40)
    pl.legend(loc = 'best')


    
