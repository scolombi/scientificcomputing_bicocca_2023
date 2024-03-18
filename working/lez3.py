# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 11:18:47 2023

@author: stefa
"""

import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import time

"""
#lez3es1
a = np.array([0.39, 0.72, 1.00, 1.52, 5.20, 9.54, 19.22, 30.06, 39.48])
P = np.array([0.24, 0.62, 1.00, 1.88, 11.86, 29.46, 84.01, 164.8, 248.09])
names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", 
     "Uranus", "Neptune", "Pluto"]
plt.plot(names,a)
plt.plot(names,P)

#lez3es5
x=linspace(0,2*pi,100)
y=tanh(x)
z=zeros(100)
n=range(99)
for i in n:
    z[i]=(y[i]-y[i+1])/(x[i]-x[i+1])
a=zeros(100)
for i in n:
    a[i]=(z[i]-z[i+1])/(x[i]-x[i+1])

fig = plt.figure()
ax1 = fig.add_subplot(311)
ax1.plot(x,y)
ax2 = fig.add_subplot(312)
ax2.plot(x,z)
ax3 = fig.add_subplot(313)
ax3.plot(x,a)
"""
#lez3es7
N = 1024
x = np.linspace(-2, 2, N)
y = np.linspace(-2, 2, N)

xv, yv = np.meshgrid(x, y, indexing="ij")
fig, ax = plt.subplots()
c = xv + 1j*y

z = np.zeros((N, N), dtype=np.complex128)
matrice = np.zeros((N, N))
for j in range(30):
    z = (z)**2 + c
    matrice[np.abs(z) <= 2]=j
    ax.set_title(f"step {j}")
    ax.imshow(matrice)
    fig.canvas.draw()
    time.sleep(0.1)
    fig.canvas.flush_events()

