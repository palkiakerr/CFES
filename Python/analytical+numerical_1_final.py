import matplotlib
import numpy as np #library for maths functions and arrays
import matplotlib . pyplot as plt #library for plottitng

### Numerical ###
data = np.loadtxt('output_1_200.txt') #loads the output from the numerical solver
dim = int(np.sqrt(len(data))) #dimensions are the squared length of the 1d matrix
V_num = np.reshape(data, (dim,dim)) #reshape the data

### Defines plotting grid/space ###
x = np. linspace (-dim/2,dim/2,dim)
y = np. linspace (-dim/2,dim/2,dim)
X, Y = np. meshgrid (x,y)

### Analytical ###
V0 = np.max(V_num)
#r0 = 15 #inner radius 
#r1 = 50 #outer radius
r0 = 10 #inner radius 
r1 = 90 #outer radius
c1 = -V0 / np.log(r0/r1) #1st constant
c2 = (V0 / np.log(r0/r1))*np.log(r0) #2nd constant

#function to calculate the analytical potential at each point of the grid
def potential(i,j):
    r = np.sqrt(i**2 + j**2)
    V_potential = c1 * np.log(r) + c2
    V_potential [np.where(r<=r0)] = 0
    V_potential [np.where(r>=r1)] = 0.01
    return V_potential

#calculating the analytical values of the potential
V_anal = potential(X,Y) 

### Plotting ###
matplotlib.rcParams ['xtick.direction'] = 'out'
matplotlib.rcParams ['ytick.direction'] = 'out'
CS = plt. contour (X,Y,V_anal,30) # Make a contour plot = Contour Set; num countour lines
plt. clabel (CS , inline =1, fontsize =10)
plt. title ('Analytical Solution')
CB = plt. colorbar (CS , shrink =0.8 , extend ='both')
plt.show()
plt.clf()

matplotlib.rcParams ['xtick.direction'] = 'out'
matplotlib.rcParams ['ytick.direction'] = 'out'
CS = plt. contour (X,Y,V_num,30) # Make a contour plot = Contour Set; num countour lines
plt. clabel (CS , inline =1, fontsize =10)
plt. title ('Numerical Solution')
CB = plt. colorbar (CS , shrink =0.8 , extend ='both')
plt.show()

### HeatMap of the error ###
err = np.abs(V_num - V_anal)
err[err >= 10  ] = 0 
plt.imshow(err, cmap = 'OrRd', vmin = 0, vmax = 0.1)
print("The biggest error is " + str(np.max(err)))
plt.colorbar()
plt.show()
