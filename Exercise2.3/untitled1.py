# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 21:12:02 2017

@author: 高多奇
"""


import numpy as np
import pylab as pl   
V=4
TIME=0
deta=0.0001
x=[0]
y=[0]
while TIME<=100:
    TIME=TIME+deta
    V=V+400*deta/(70*V)-2*0.33*(0.00001)*V*deta/105-0.5*1.29*0.33*V*V*deta/(70)
    x.append(TIME)
    y.append(V)
else:
    pl.plot(x, y,'r--',label='with air resistance',linewidth=2)
    
    
import numpy as np
import pylab as pl   
V=4
TIME=0
deta=0.0001
x=[0]
y=[0]
while TIME<=100:
    TIME=TIME+deta
    V=V+400*deta/(70*V)-2*0.33*(0.00001)*V*deta/105
    x.append(TIME)
    y.append(V)
else:
    pl.plot(x, y,'m--',label='without -B2*V^2 term',linewidth=2)
    
    import numpy as np
import pylab as pl   
V=4
TIME=0
deta=0.0001
x=[0]
y=[0]
while TIME<=100:
    TIME=TIME+deta
    V=V+400*deta/(70*V)
    x.append(TIME)
    y.append(V)
else:
    pl.plot(x, y,'b:',label='without air resistance',linewidth=2)
   
   
import numpy as np
import pylab as pl   
V=4
TIME=0
deta=0.0001
x=[0]
y=[0]
while TIME<=100:
    TIME=TIME+deta
    V=V+400*deta/(70*V)-0.165*(0.001)*V*deta/105-0.5*1000*0.165*V*V*deta/(70)
    x.append(TIME)
    y.append(V)
else:
    plot1=pl.plot(x, y,'g--',label='with water resistance',linewidth=2)
    pl.title('velocity')
    pl.xlabel('T/s')
    pl.ylabel('V m/s')
    pl.xlim(0, 100)
    pl.ylim(0, 40)
    pl.legend(loc = 'best')
    pl.show()

    