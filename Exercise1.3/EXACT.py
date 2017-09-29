# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 23:33:55 2017

@author: 高多奇
"""

import numpy as np
import matplotlib.pyplot as plt
N=1500
a=10.0
b=0.02
x=np.arange(0,1,0.01)
y=np.exp(a*x)*a*N/(a-b*N+np.exp(a*x)*b*N)
plt.plot(x,y)
plt.show()