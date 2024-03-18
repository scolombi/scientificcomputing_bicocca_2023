# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 15:55:19 2023

@author: stefa
"""

import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import time
from scipy import integrate
import scipy.interpolate as interpolate
import scipy.optimize as optimize



#es1
"""
N = 32
x = np.linspace(-5, 5, N)
f = np.exp(-x**2)
I = integrate.simps(f, x)
print(I)
"""
#es2
"""
def g(x):
    return np.tanh(x)*pow(x/5,2)+np.sin(x)*0.3*(x-3/5*x*x/3)
N = 20
x = np.linspace(-20, 20, N)
y = g(x)
fig, ax = plt.subplots()

x_fine = np.linspace(-20, 20, 10*N)

ax.scatter(x, y)
ax.plot(x_fine, g(x_fine), ls=":", label="original function")
f_interp = interpolate.interp1d(x, y, kind="cubic")
ax.plot(x_fine, f_interp(x_fine), label="interpolant")
ax.legend(frameon=False, loc="best")
fig
"""
#es3
"""
def f(x):
    return x*x*x-2*x*x-11*x+12
#prova -5, 1,  3 (sol: -3, 1, 4)
root, r = optimize.brentq(f, -5, 10, full_output=True)
print(root)
print(r.converged)
x = np.linspace(-10, 10.0, 1000)
fig, ax = plt.subplots()
ax.plot(x, f(x))
ax.scatter(np.array([root]), np.array([f(root)]))
ax.grid()
"""
#es4
"""
G=4*np.pi #G= 6.674e-11
M=1       #M= 1.98847e30
a=1       #a= 1.49598e11
e= 0.0167
x0 = a*(1-e)
y0=0
vx0=0
vy0=sqrt(G*M*(1+e)/(a*(1-e)))

def rhs(t, Y, GM=G*M):
    #RHS for orbits, Y is the solution vector, containing x, y, v_x, and v_y
    x, y, vx, vy = Y
    f = np.zeros_like(Y)
    # dx/dt = vx
    f[0] = vx
    # dy/dt = vy
    f[1] = vy
    # d(vx)/dt = -GMx/r**3
    r = np.sqrt(x**2 + y**2)
    f[2] = -GM*x/r**3
    # d(vy)/dt = -GMy/r**3
    f[3] = -GM*y/r**3
    return f

def ode_integrate(X0, dt, tmax):
    #integrate using the VODE method, storing the solution each dt 
    r = integrate.solve_ivp(rhs, (0.0, tmax), X0, method="RK45", dense_output=True)
    # get the solution at intermediate times
    ts = np.arange(0.0, tmax, dt)
    Xs = r.sol(ts)
    return ts, Xs
#anno = 3.15e7 giorno = 86400
t, X = ode_integrate([x0, y0, vx0, vy0], 0.01, 2)
fig, ax = plt.subplots()
ax.plot(X[0,:], X[1,:])
fig.set_size_inches(8.0,8.0)

"""

