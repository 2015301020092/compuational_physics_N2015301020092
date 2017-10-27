
import pylab as pl
import math   
g=9.8
l=9.8
m=1
dt=0.04
q=0.5
F=1.2
D=2.0/3.0
t=0
x=0.2
w=0
E=9.8
pi=math.pi
X=[0]
Y=[0]
while t<=500:
    w=w-((g/l)*math.sin(x)+q*w-F*math.sin(D*t))*dt
    x=x+w*dt
    if x<-1*pi:        
         x=x+2*pi
    elif x>pi:
         x=x-2*pi
    else:
        x=x
    X.append(t)
    Y.append(x) 
    t=t+dt   
pl.plot(X, Y,'r,',label='θ versus t  F='+str(F))
pl.title('')
pl.xlabel('θ(radians)')
pl.ylabel('t/s)')
pl.xlim(0, 100)
pl.ylim(-4, 4)
pl.legend(loc = 'best')

