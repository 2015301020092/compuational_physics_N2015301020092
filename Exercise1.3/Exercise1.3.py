
import numpy as np   #cooperate with Gao DuoQi
import pylab as pl
N=1500
Time=0
deltat=0.0001
a=10
b=0.02
x=[0]
y=[0]
while Time<=0.9999:
    Time=Time+deltat
    N=N+(a*N-b*N**2)*deltat
    x.append(Time)
    y.append(N)
else:
    plot=pl.plot(x,y,'--',label='N')
    pl.title('model of population')
    pl.xlabel('Time')
    pl.ylabel('N')
    pl.xlim(0,1)
    pl.ylim(400,1500)
    pl.legend(loc='best')
    pl.show()
