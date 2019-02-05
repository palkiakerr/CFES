import matplotlib
import numpy as np #library for maths functions and arrays
import matplotlib . pyplot as plt #library for plottitng

N=500
d = 10
h = 10
R0 = 2
V0 = 1

x = np.linspace( -d/2, d/2, N)
y = np.linspace( -h/2, h/2, N)
X, Y = np.meshgrid(x,y)

def potential(x,y):
    r = x**2 + y**2 
    V_potential = ((2*V0) / d) * r * x/r - R0*R0*x/r*r
    V_potential [np.where (np.abs(r) < R0) ] = 0
    return V_potential

V_anal = potential(X,Y)

#Plotting
matplotlib.rcParams ['xtick.direction'] = 'out'
matplotlib.rcParams ['ytick.direction'] = 'out'
CS = plt. contour (X,Y,V_anal,40) # Make a contour plot = Contour Set; num countour lines
plt. clabel (CS , inline =1, fontsize =10)
plt. title ('Analytical Solution')
plt.xlabel("x")
plt.ylabel("y")
CB = plt. colorbar (CS , shrink =0.8 , extend ='both')
plt.show ()
plt.clf()