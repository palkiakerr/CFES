import matplotlib
import numpy as np #library for maths functions and arrays
import matplotlib . pyplot as plt #library for plottitng


fname = 'output.txt' #the file should be in the same folder as program, or include the path
#load the file "fname", defined above
data = np.loadtxt(fname, delimiter='\n', comments='#')
dim = int(np.sqrt(len(data)))
V = np.reshape(data, (dim,dim)) #reshape the data


fname = 'output.txt' #the file should be in the same folder as program, or include the path
#load the file "fname", defined above
data = np.loadtxt(fname, delimiter='\n', comments='#')
#reshape the data



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



x = np. linspace (0,dim,dim)
y = np. linspace (0,dim,dim)
X, Y = np. meshgrid (x,y)
#Defines plotting grid/space.

plt.subplot(2,1,2)
plt.imshow(V, cmap='hot', interpolation='nearest')
plt. title ('Heat map')


plt.subplot(2,2,2)
matplotlib.rcParams ['xtick.direction'] = 'out'
matplotlib.rcParams ['ytick.direction'] = 'out'
CS = plt. contour (X,Y,V,50) # Make a contour plot = Controur Set
plt. clabel (CS , inline =1, fontsize =10)
plt. title ('Potential field')
CB = plt. colorbar (CS , shrink =0.8 , extend ='both')



plt.subplot(2,2,1)

#Comment in for binary colours
h=int(round(dim/35))

skip = (slice(None, None, h), slice(None, None, h))


fig =plt.quiver(X[skip], Y[skip], E_x[skip]/E_norm[skip], E_y[skip]/E_norm[skip], E_norm[skip], cmap='binary', clim=[0,np.amax(E_norm)], scale=30, headwidth=5)
#fig =plt.quiver(X, Y, 1.25*E_x/E_norm, 1.25*E_y/E_norm, E_norm, cmap='binary', clim=[0,np.amax(E_norm)], scale=80, headwidth=1)
cb = plt.colorbar(fig)
plt. title ('Electric field')
plt.suptitle("Insert catchy title here")
plt.show()
#may wish to scale arrows between 0 and 1
#Also dividing by 0 warning

