'''
This programme creates a schematic B&W heatmap of the initial user input of charges. 
Created Feb 2019
'''
import numpy as np #library for maths functions and arrays
import matplotlib . pyplot as plt #library for plotting

data_in = np.loadtxt('matrix.txt') #loads the initial input data 
dim = int(np.sqrt(len(data_in))) #dimensions are the squared length of the 1d matrix
V_in = np.reshape(data_in, (dim,dim)) #reshapes the data to a 2d matrix
V_in[abs(V_in) < 0.000002 ] = 0 #sets the empty cells to a zero potential
V_in[abs(V_in) >= 0.01 ] = 100101 #normalises all the ocuppied cells to a number bigger than the maximum potential

plt.imshow(V_in, cmap='Greys') #plots the potential as a heatmap
plt.gca().invert_yaxis() #inverts the y-axis 
plt.savefig('schematic.png', bbox_inches='tight') #saves the figure to the 'schematic.png' file 
