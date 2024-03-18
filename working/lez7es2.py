# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 14:57:23 2024

@author: stefa
"""
#lez 7 es 2
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import pandas as pd
import os

#def plotter(func,xmin,xmax, x_label, y_label):
def plotter(func,xmin,xmax):
    plt.rc('xtick', labelsize=10) 
    plt.rc('ytick', labelsize=10)
    hfont = {'fontname':'Helvetica'}
    x=np.linspace(xmin,xmax, num=100)
    y=func(x)
    fig = plt.figure()
    fig.set_size_inches(10, 6)
    ax = fig.add_subplot(111)
    ax.plot(x, y)
    ax.set_xlabel("ascissa")
    ax.set_ylabel("ordinata")
    ax.set_xlim()
    #plt.savefig("function.pdf")
    return(fig)


def my_function(x):
  return x * sin(x)

plotter(my_function,0, 2*np.pi)

