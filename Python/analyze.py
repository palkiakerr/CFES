#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 11:53:21 2019

@author: kk
"""
import matplotlib
import numpy as np #library for maths functions and arrays
import matplotlib . pyplot as plt #library for plottitng

N=40 #dimensions of the grid
L=1 # 1 metre grid for the x, y dimensions 
fname = 'analyze.txt' #the file should be in the same folder as program, or include the path
#load the file "fname", defined above
data = np.loadtxt(fname, delimiter=',', comments='#')
                  
V = np.reshape(data, (40,40)) #reshape the data to a 40x40 array

#manual reshaping
#V=np.zeros((40,40)) #creates a 40x40 array of 0s            
#for i in range (0,40):
#    for j in range (0,40):
#        V[i][j] = data [i*40 + j]

# Define arrays used for plotting
x = np. linspace (0,L,N)
y = np. linspace (0,L,N)
X, Y = np. meshgrid (x,y) #create the 2d grid

#Plotting
matplotlib.rcParams ['xtick.direction'] = 'out'
matplotlib.rcParams ['ytick.direction'] = 'out'
CS = plt. contour (X,Y,V,10) # Make a contour plot = Contour Set; num countour lines
plt. clabel (CS , inline =1, fontsize =10)
plt. title ('PDE solution of a point charge')
CB = plt. colorbar (CS , shrink =0.8 , extend ='both')
plt.show ()