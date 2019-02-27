'''
This programme generates the analytical solution to the Second problem 
(Capacitor with a ground wire),
plots the numerical solution, 
compares both and 
calculates the error.
''' 
import numpy as np #library for maths functions and arrays
import matplotlib . pyplot as plt #library for plotting

data = np.loadtxt('output_2_51_20000_bigger.txt')      
dim = int(np.sqrt(len(data))) #get the dimensions automatically                 
V_num = np.reshape(data, (dim,dim)) #reshape the data to a NxN array

# dimensions of the problem, hardcoded ####
d = dim #distance between plates
h = dim #height of the plates
R0 = 5 #radius of the ground wire
V0 = np.max(V_num) #potential of the plates

### generating space grid in polar coordinates ###
x = np.linspace( -dim/2, dim/2, dim) 
y = np.linspace( -dim/2, dim/2, dim)
X, Y = np.meshgrid(x,y)

def potential(x,y):
    r = x**2 + y**2 #r.sin(thetha) = x so just substitute
    V_potential = (-(2*V0) / d) * (x - R0*R0*x/(r*r))
    V_potential [np.where (np.abs(r) < R0) ] = 0 
    return V_potential

V_anal = potential(X,Y)

### Plotting ###
plt.subplot(1,3,1) #2 rows, 2 columns, 1st image
plt. title ('Analytical Solution')
plt.gca().set_aspect('equal', adjustable='box')
plt.contour (X,Y,V_anal,50) # Make a contour plot = Contour Set; num countour lines
plt.colorbar()

plt.subplot(1,3,2) #2 rows, 2 columns, 1st image
plt. title ('Numerical Solution')
plt.gca().set_aspect('equal', adjustable='box')
CS = plt.contour (X,Y,V_num,50) # Make a contour plot = Contour Set; num countour lines
CB = plt.colorbar()

### Error Analysis ###
err_array = np.abs(V_num - V_anal) #takes absolute difference at each point
err_max = np.max(err_array)
err_avr = np.average(err_array)

plt.subplot(1,3,3) #2 rows, 2 columns, 1st image
plt.gca().set_aspect('equal', adjustable='box')
plt.title ('Difference between \n Analytical and \n Numerical Solutions')
plt.imshow(err_array, cmap = 'OrRd', vmin = 0, vmax = 0.1) #defines normalisation values
plt.colorbar()

print("The biggest error is " + str(err_max))
print("The average error is " + str(err_avr))

plt.show()


