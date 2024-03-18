# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 14:56:53 2024

@author: stefa
"""
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import pandas as pd
import os
from scipy.optimize import curve_fit
import scipy.integrate as integrate
import time

#esercizio1
eps = 1

while (1+eps!=1):
    eps=eps/2
    
print(eps)

#esercizio2
names = ["Mary", "John", "Sarah"]
age = [21, 56, 98]
list1= names
list2=age
result=zip(list1, list2)
for x in range(3):
 print("my name is "+list1[x] +" and I am " +str(list2[x])+" years old" )

