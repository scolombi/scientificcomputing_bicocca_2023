# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 15:25:55 2024

@author: stefa
"""
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import os, sys
import time

def GameOfLife():
    fig, ax = plt.subplots()
    plt.ion()
    x=20
    y=20
    #valore iniziale
    a=zeros((x,y))
    a[0:2,5:7]=1
    a[18:20,6:8]=1
    a[1,:]=1
    a[18,:]=1
    tetto=50
    #iterazione
    num=0
    while(num<tetto):
        ax.imshow(a, cmap='Greys')
        ax.set_title(f"Initial condition: {len(a[a==1])} live cells")
        ax.set_xticks(np.arange(a.shape[1]+1)-.5, labels="")
        ax.set_yticks(np.arange(a.shape[0]+1)-.5, labels="")
        ax.grid(visible=True, which="major", axis="both")
        plt.show()
        ax.imshow(a, cmap='Greys')
        ax.set_title(f"Step {num}/{tetto}: {len(a[a==1])} live cells")
        fig.canvas.draw()
        fig.canvas.flush_events()
        time.sleep(0.1)
        b=zeros((x,y))
        b[:,1:]=a[:,:-1]
        c=zeros((x,y))
        c[:,:-1]=a[:,1:]
        d=zeros((x,y))
        d[1:,:]=a[:-1,:]
        e=zeros((x,y))
        e[:-1,:]=a[1:,:]
        f=zeros((x,y))
        f[1:,1:]=a[:-1,:-1]
        g=zeros((x,y))
        g[:-1,:-1]=a[1:,1:]
        h=zeros((x,y))
        h[1:,:-1]=a[:-1,1:]
        i=zeros((x,y))
        i[:-1,1:]=a[1:,:-1]
        tot=b+c+d+e+f+g+h+i
        #a[tot[:,:]==2]=a[tot[:,:]==2])
        a[tot[:,:]==3]=1
        a[tot[:,:]>3]=0
        a[tot[:,:]<2]=0
        num=num+1
        
if __name__ == "__main__":
    GameOfLife()