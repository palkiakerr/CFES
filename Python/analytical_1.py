import matplotlib
import numpy as np #library for maths functions and arrays
import matplotlib . pyplot as plt #library for plottitng

N=100
L=100
V0 = 8
r0 = 15
r1 = 50
c1 = -V0 / np.log(r0/r1)
c2 = (V0 / np.log(r0/r1))*np.log(r0)

x = np. linspace (-L/2,L/2,N)
y = np. linspace (-L/2,L/2,N)
X, Y = np. meshgrid (x,y) #create the 2d grid

def potential(i,j):
    return -c1 * np.log(np.sqrt(i**2 + j**2)) +c2

V=potential(X,Y)


#Plotting
matplotlib.rcParams ['xtick.direction'] = 'out'
matplotlib.rcParams ['ytick.direction'] = 'out'
CS = plt. contour (X,Y,V,10) # Make a contour plot = Contour Set; num countour lines
plt. clabel (CS , inline =1, fontsize =10)
plt. title ('PDE solution of a point charge')
CB = plt. colorbar (CS , shrink =0.8 , extend ='both')
plt.show ()
