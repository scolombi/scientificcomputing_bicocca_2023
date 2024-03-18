# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 11:34:58 2024
numba
@author: stefa
"""
import os, sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numba import njit
giorni=10000000
# 0-bull 1-bear 2-stagnant
def market(ndays):
    day = 0
    lista=[0]
    for i in range(ndays):
        rand =  np.random.uniform(0,1)
        if (day==0):
            if (0.9<rand<0.975):
                day=1
            if (rand>0.975):
                day =2
        elif (day==1):
            if (0.8<rand<0.95):
                day=0
            if (rand>0.95):
                day =2
        elif (day==2):
            if (0.5<rand<0.75):
                day=0
            if (rand>0.75):
                day =2
        #print(day)
        lista.append(day)
    #plt.plot(lista)
    return(sum(lista))

%timeit market(giorni)


c_market = njit(market)

%timeit c_market(giorni)
print(market(giorni))
print(c_market(giorni))
