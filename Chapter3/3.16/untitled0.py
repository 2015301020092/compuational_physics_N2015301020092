

import math
import pylab as pl


pl.figure(figsize=(10,7)) 




def F(Fd,Ω,TS):
    ω=0
    θ=2.0
    t=0
    dt=0.04
    pi=math.pi
    
    W=[ω]
    Theta=[θ]
    T=[t]
    pl.title('ω versus θ  comparison' ,size=15)
    pl.xlabel('θ (radians)',size=14)
    pl.ylabel('ω (radians/s)',size=14)
    pl.xlim(-4,4)
    pl.ylim(-2,1)
    
    while t<=TS:
        sin1=math.sin(θ) 
        sin2=math.sin(Ω*t)
        ω=ω+(-sin1-0.5*ω+Fd*sin2)*dt
        θ=θ+ω*dt
        
        while θ>pi:
            θ=θ-2*pi
        else:
            θ=θ
            
        while θ<-1*pi:
            θ=θ+2*pi
        else:
            θ=θ
            
        t=t+dt
        k=Ω*t
        K=[]
    
        while k>0:
           K.append(k)
           k=k-2*pi
        else:
           K.append(k)
           i=K[-1]
           j=K[-2]
    
        if abs(i)>abs(j):
            min=abs(j)
        else:
            min=abs(i)
    
        if min<0.02*Ω:
           W.append(ω) 
           Theta.append(θ)
           T.append(t)
        else:
           T.append(t)
    else:
       
        pl.scatter(Theta,W,marker = 'o', color = 'r', s=0.4)
        pl.legend('x1')
       


        return 0
    
    
F(1.2,2/3,10000)

pl.show()
