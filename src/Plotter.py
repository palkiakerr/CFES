import matplotlib
import numpy as np #library for maths functions and arrays
import matplotlib . pyplot as plt #library for plottitng

### Load data from Input ###
fname = 'matrix.txt' #the file should be in the same folder as program, or include the path
#load the file "fname", defined above
data_in = np.loadtxt(fname)
dim = int(np.sqrt(len(data_in))) 
V_in = np.reshape(data_in, (dim,dim)) #reshape the data to 2D grid
V_in[abs(V_in) < 0.000002 ] = 0

### Load data from Output ###
fname = 'output.txt' #the file should be in the same folder as program, or include the path
#load the file "fname", defined above
data_out = np.loadtxt(fname, delimiter='\n', comments='#')
V = np.reshape(data_out, (dim,dim)) #reshape the data

### Calculate E-field ###
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


### Generate coordinates for plotting ###
x = np. linspace (0,dim,dim)
y = np. linspace (0,dim,dim)
X, Y = np. meshgrid (x,y)


### Plotting Final Output ###
plt.suptitle("Classical Field Equation Solver")
### Plot Input ###
plt.subplot(2,2,1) ## 2 rows, 2 columns, 1st graph
plt.title('Charges')
plt.imshow(V_in, cmap='Greys')
plt.gca().invert_yaxis()
plt.savefig('schematic.png', bbox_inches='tight')

### Plot Potential on a Heatmap ###
plt.subplot(2,2,2) ## 2 rows, 2 columns, 2nd graph
plt.title('Potential')
plt.imshow(V, cmap='hot', interpolation='nearest')
plt.gca().invert_yaxis()
#plt.axes().set_aspect('equal', 'datalim')
plt.colorbar()

### Plot Equipotential Lines ###
plt.subplot(2,2,3)
plt. title ('Equipotential Lines')
matplotlib.rcParams ['xtick.direction'] = 'out'
matplotlib.rcParams ['ytick.direction'] = 'out'
CS = plt.contour (X,Y,V,30)
plt.clabel (CS , inline =1, fontsize =10)
CB = plt. colorbar (CS , shrink =0.8 , extend ='both')

### Plot E-field ###
plt.subplot(2,2,4)
plt.title ('Electric Field Lines')
h=int(round(dim/35)) 
skip = (slice(None, None, h), slice(None, None, h))
plt.quiver(X[skip], Y[skip], E_x[skip]/E_norm[skip], E_y[skip]/E_norm[skip], E_norm[skip], cmap='gist_rainbow', clim=[0,np.amax(E_norm)], scale=30, headwidth=5)
#fig =plt.quiver(X, Y, 1.25*E_x/E_norm, 1.25*E_y/E_norm, E_norm, cmap='binary', clim=[0,np.amax(E_norm)], scale=80, headwidth=1)
plt.colorbar()

### Show and safe the final graph output ###
plt.show()
plt.savefig('final_output.png', bbox_inches='tight')

