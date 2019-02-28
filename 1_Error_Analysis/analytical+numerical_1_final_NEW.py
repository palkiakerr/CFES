'''
This programme generates the analytical solution to the First problem 
(Charged outer shell with a ground wire inside),
plots the numerical solution, 
compares both and 
calculates the error.
''' 
import numpy as np #library for maths functions and arrays
import matplotlib . pyplot as plt #library for plottitng

### Numerical ###
fname = '1_201_500000.txt'
data = np.loadtxt(fname) #loads the output from the numerical solver
dim = int(np.sqrt(len(data))) #dimensions are the squared length of the 1d matrix
V_num = np.reshape(data, (dim,dim)) #reshape the data

### Defines plotting space in Polar Coord ###
x = np. linspace (-dim/2,dim/2,dim) 
y = np. linspace (-dim/2,dim/2,dim)
X, Y = np. meshgrid (x,y)

### Analytical Solution ###
V0 = np.max(V_num)
r0 = 10 #inner radius 
r1 = 100 #outer radius
c1 = -V0 / np.log(r0/r1) #1st constant
c2 = (V0 / np.log(r0/r1))*np.log(r0) #2nd constant

#function to calculate the analytical potential at each point of the grid
def potential(i,j):
    r = np.sqrt(i**2 + j**2)
    V_potential = c1 * np.log(r) + c2
    V_potential [np.where(r<=r0)] = 0.01 #ground is actually not zero
    V_potential [np.where(r>=r1)] = V0 #outside the shell is uniform 
    return V_potential

#calculating the analytical values of the potential
V_anal = potential(X,Y) 

### Plotting ###
plt.subplot(1,3,1) #2 rows, 2 columns, 1st image
plt. title ('Analytical Solution')
plt.gca().set_aspect('equal', adjustable='box')
plt.contour (X,Y,V_anal,50) # Make a contour plot = Contour Set; num countour lines
plt.colorbar()

plt.subplot(1,3,2) #2 rows, 2 columns, 1st image
plt.title ('Numerical Solution')
plt.gca().set_aspect('equal', adjustable='box')
plt.contour (X,Y,V_num,50) # Make a contour plot = Contour Set; num countour lines
plt.colorbar()

### Error Analysis ###
err_array = np.abs(V_num - V_anal) #takes absolute difference at each point
#err_array[err_array >=100  ] = 0 #hardcoded truncating of the error for edges
err_max = np.max(err_array)
err_avr = np.average(err_array)

plt.subplot(1,3,3) #2 rows, 2 columns, 1st image
plt.gca().set_aspect('equal', adjustable='box')
plt.title ('Difference between \n Analytical and \n Numerical Solutions')
plt.imshow(err_array, cmap = 'OrRd', vmin = 0, vmax = err_max) #defines normalisation values
plt.colorbar()

print("The biggest error is " + str(err_max))
print("The average error is " + str(err_avr))

plt.show()

plt.clf()
plt.gca().set_aspect('equal', adjustable='box')
plt.title ('Difference between \n Analytical and \n Numerical Solutions')
plt.imshow(err_array, cmap = 'OrRd', vmin = 0, vmax = err_max) #defines normalisation values
plt.colorbar()
plt.savefig("error_"+str(fname)+".png")

### Tolerance Plots ###
### IDEA: maybe make them as a heatmap and on an animation yey
#plt.clf()
#plt.subplot(1,3,1) #2 rows, 2 columns, 1st image
#plt.title ('Numerical Solution \n Lower Band')
#plt.gca().set_aspect('equal', adjustable='box')
#plt.contour (X,Y,V_num - err_max,50) # Make a contour plot = Contour Set; num countour lines
#plt.colorbar()
#
#plt.subplot(1,3,2) #2 rows, 2 columns, 1st image
#plt.title('Numerical Solution')
#plt.gca().set_aspect('equal', adjustable='box')
#plt.contour(X,Y,V_num,50) # Make a contour plot = Contour Set; num countour lines
#plt.colorbar()
#
#plt.subplot(1,3,3) #2 rows, 2 columns, 1st image
#plt.title('Numerical Solution \n Upper Band')
#plt.gca().set_aspect('equal', adjustable='box')
#plt.contour(X,Y,V_num + err_max,50) # Make a contour plot = Contour Set; num countour lines
#plt.colorbar()
#
#plt.show()