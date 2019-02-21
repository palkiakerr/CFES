import matplotlib
import numpy as np #library for maths functions and arrays
import matplotlib . pyplot as plt #library for plottitng

### Loading the Input Schematic ###
data_in = np.loadtxt('matrix.txt')
dim = int(np.sqrt(len(data_in))) 
V_in = np.reshape(data_in, (dim,dim)) #reshape the data
V_in[abs(V_in) < 0.000002 ] = 0

### Loading the Output data ###
data = np.loadtxt('output.txt')
V = np.reshape(data, (dim,dim)) #reshape the data

### Calculating the E-field ###
E_x = np.zeros((dim,dim))
E_y = np.zeros((dim,dim))

for i in range (1, len(V)-1):
    for j in range (1, len(V)-1):
        E_y[i,j] = - (V[i+1, j] - V[i-1, j])*dim/(2)
        E_x[i,j] =  - (V[i, j+1] - V[i, j-1])*dim/(2)

E_norm = np.zeros((dim,dim))
#initialing normalisation matrix with all zeros.

for i in range (1, dim-1):
    for j in range (1, dim-1):
        E_norm[i,j] = np.sqrt(E_x[i,j]**2 + E_y[i,j]**2)


### Defines plotting grid/space ###
x = np. linspace (0,dim,dim)
y = np. linspace (0,dim,dim)
X, Y = np. meshgrid (x,y)

###### Plots ########
### Input Charges ###
plt.subplot(2,2,1) #2 rows, 2 columns, 1st image
plt.imshow(V_in, cmap='Greys')
plt.gca().invert_yaxis()
plt. colorbar ()
plt.title("Charges")

### Potential HeatMap ###
plt.subplot(2,2,2)
plt.imshow(V, cmap='hot', interpolation='nearest')
CB = plt. colorbar()
plt.gca().invert_yaxis()
plt. title ('Potential')

### Electri Field ###
plt.subplot(2,2,3)
#Comment in for binary colours
h=int(round(dim/35))
skip = (slice(None, None, h), slice(None, None, h))
fig =plt.quiver(X[skip], Y[skip], E_x[skip]/E_norm[skip], E_y[skip]/E_norm[skip], E_norm[skip], cmap='gist_rainbow', clim=[0,np.amax(E_norm)], scale=30, headwidth=5)
plt.colorbar()
plt.gca().set_aspect('equal', adjustable='box')
plt. title('Electric field')

### Equipotential ###
plt.subplot(2,2,4)
matplotlib.rcParams ['xtick.direction'] = 'out'
matplotlib.rcParams ['ytick.direction'] = 'out'
CS = plt. contour (X,Y,V,20) #number shows the density of countour lines
plt. clabel (CS , inline =1, fontsize =10)
plt. colorbar()
plt.gca().set_aspect('equal', adjustable='box')
plt. title ('Equipotential Lines')

### Plot and Save ###
plt.suptitle("Classical Field Equation Solver")
plt.show()
plt.savefig('final.png', bbox_inches='tight')
