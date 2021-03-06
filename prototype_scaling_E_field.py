"""
Plotter for C generated E_field
"""
import sys
import math
import numpy as np
np.set_printoptions(threshold=np.nan)
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
#Imports needed libaries 


num_lines = sum(1 for line in open('E_x.txt'))
dim = int(math.sqrt(num_lines))
#Determines the dimension of the grid form the sqrt of lines

fname = 'E_x.txt'
data = np.loadtxt(fname, delimiter=',', comments='#')
E_x = np.reshape(data, (dim,dim))
#Reads in dv/dx and froms an array from it

fname = 'E_y.txt'
data = np.loadtxt(fname, delimiter=',', comments='#')
E_y = np.reshape(data, (dim,dim))
#Reads in dv/dy and froms an array from it

E_norm = np.zeros((dim,dim))
#initialingnormalisation matrix with all zeros

for i in range (1, dim-1):
	for j in range (1, dim-1):
		  E_norm[i,j] = np.sqrt(E_x[i,j]**2 + E_y[i,j]**2)

E_scaled = (E_norm - np.min(E_norm))/np.ptp(E_norm)		   
		  
x = np. linspace (0,dim,dim)
y = np. linspace (0,dim,dim)		  
X, Y = np. meshgrid (x,y)
#Defines plotting grid/space

print(E_x)
print("xxxxxxxxxxxx")
print(E_norm/E_x)
print("xxxxxxxxxxxx")
print(E_norm/E_y)
print("xxxxxxxxxxxx")
print(E_scaled)

plt.clf()
fig =plt.quiver(X, Y,E_x/E_scaled, E_y/E_scaled, E_scaled, cmap='gist_rainbow', clim=[0,1], scale=100)
cb = plt.colorbar(fig)
plt. title ('Electric field')
plt.show()
