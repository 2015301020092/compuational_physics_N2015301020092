
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 19:45:39 2017

@author: Administrator
"""

import pylab as pl
import math 
x_e=0.0
y_e=0.0
x_j=0.0
y_j=0.0
x_s=0.0
y_s=0.0
rej=0.0
res=0.0
rsj=0.0
v_e1=0.0
v_e2=0.0
x_e1=0.0
y_e2=0.0
v_j1=0.0
v_j2=0.0
x_j1=0.0
y_j2=0.0
x_s1=0.0
y_s2=0.0
v_sx=0.0
v_sy=0.0

v_s1=0.0
v_s2=0.0
dt=0.0001
t=0
m_e=6*10**24
m_j=1.9*10**27
m_s=2*10**30

kb=4*(math.pi)**2
X_E=[]
Y_E=[]
X_S=[]
Y_S=[]
X_J=[]
Y_J=[]

def orbit(theta_e,r_e,v_ex1,v_ey1,theta_j,r_j,v_jx,v_jy,T):
    
    t=0
    v_s1=0.0
    v_s2=0.0
    v_ex=2*math.pi*v_ex1
    v_ey=2*math.pi*v_ey1
    x_e=r_e*(math.cos(theta_e))
    y_e=r_e*(math.sin(theta_e))
    x_j=r_j*(math.cos(theta_j))
    y_j=r_j*(math.sin(theta_j))
    x_s=-(m_e*x_e+m_j*x_j)/m_s
    y_s=-(m_e*y_e+m_j*y_j)/m_s
    v_sx=-(m_e*v_ex+m_j*v_jx)/m_s
    v_sy=-(m_e*v_ey+m_j*v_jy)/m_s
    while(t<T):
        rej=math.sqrt((x_e-x_j)**2+(y_e-y_j)**2)
        res=math.sqrt((x_e-x_s)**2+(y_e-y_s)**2)
        rsj=math.sqrt((x_j-x_s)**2+(y_j-y_s)**2)
        v_e1=v_ex-((kb*(m_j/m_s)*(x_e-x_j))/(rej**3))*dt-((kb*(m_s/m_s)*(x_e-x_s))/(res**3))*dt
        v_e2=v_ey-((kb*(m_j/m_s)*(y_e-y_j))/(rej**3))*dt-((kb*(m_s/m_s)*(y_e-y_s))/(res**3))*dt
        x_e1=x_e+v_e1*dt
        y_e2=y_e+v_e2*dt
        v_j1=v_jx-((kb*(m_e/m_s)*(x_j-x_e))/(rej**3))*dt-((kb*(m_s/m_s)*(x_j-x_s))/(rsj**3))*dt
        v_j2=v_jy-((kb*(m_e/m_s)*(y_j-y_e))/(rej**3))*dt-((kb*(m_s/m_s)*(y_j-y_s))/(rsj**3))*dt
        x_j1=x_j+v_j1*dt
        y_j2=y_j+v_j2*dt
        v_s1=v_sx-((kb*(m_e/m_s)*(x_s-x_e))/(res**3))*dt-((kb*(m_j/m_s)*(x_s-x_j))/(rsj**3))*dt
        v_s2=v_sy-((kb*(m_e/m_s)*(y_s-y_e))/(res**3))*dt-((kb*(m_j/m_s)*(y_s-y_j))/(rsj**3))*dt
        x_s1=x_s+v_s1*dt
        y_s2=y_s+v_s2*dt
        
        v_ex=v_e1
        v_ey=v_e2
        v_jx=v_j1
        v_jy=v_j2
        v_sx=v_s1
        v_sy=v_s2
        
        x_e=x_e1
        y_e=y_e2
        x_j=x_j1
        y_j=y_j2
        x_s=x_s1
        y_s=y_s2
        t=t+dt
        X_E.append(x_e)
        Y_E.append(y_e)
        X_S.append(x_s)
        Y_S.append(y_s)
        X_J.append(x_j)
        Y_J.append(y_j)
    
    pl.figure(figsize=(7,7))
    pl.plot(X_E,Y_E,'b-',label='Earth orbit')
    pl.plot(X_J,Y_J,'g-',label='Jupiter orbit')
    pl.plot(X_S,Y_S,'r-',label='Sun orbit')
    pl.xlim(-7,7)
    pl.ylim(-7,7)
    pl.ylabel('$y$'+' (AU)',fontsize=10)
    pl.xlabel('$x$'+' (AU)',fontsize=10)
    pl.title('orbit versus time')

    pl.legend(loc = 'best')
    pl.show()
orbit(0,4,0,1,0,5.2,0,2.75535903,50)
#orbit(theta_e,r_e,v_ex,ve_y,theta_j,r_j,v_jx,v_jy,T)

