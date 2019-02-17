import matplotlib
import numpy as np #library for maths functions and arrays
import matplotlib . pyplot as plt #library for plottitng

L=1 #arbitrary dimension

fname = 'output.txt' #the file should be in the same folder as program, or include the path
#load the file "fname", defined above
data = np.loadtxt(fname, delimiter='\n', comments='#')
print(len(data))
dim = int(np.sqrt(len(data)))
V = np.reshape(data, (dim,dim)) #reshape the data
print(V)


E_x = np.zeros((dim,dim))
E_y = np.zeros((dim,dim))

for i in range (1, len(V)-1):
      for j in range (1, len(V)-1):
          E_y[i,j] = - (V[i+1, j] - V[i-1, j])*dim/(2*L)
          E_x[i,j] =  - (V[i, j+1] - V[i, j-1])*dim/(2*L)

E_norm = np.zeros((dim,dim))
#initialing normalisation matrix with all zeros.

for i in range (1, dim-1):
    for j in range (1, dim-1):
        E_norm[i,j] = np.sqrt(E_x[i,j]**2 + E_y[i,j]**2)


x = np. linspace (0,dim,dim)
y = np. linspace (0,dim,dim)
X, Y = np. meshgrid (x,y)
#Defines plotting grid/space.


plt.clf()
fig =plt.quiver(X, Y, 1.25*E_x/E_norm, 1.25*E_y/E_norm, E_norm, cmap='gist_rainbow', clim=[0,1], scale=40)
cb = plt.colorbar(fig)
plt. title ('Electric field')
plt.show()
#may wish to scale arrows between 0 and 1
#Also dividing by 0 warning
