import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
import numpy as np

x = np.linspace(-1,1,100)
y = np.linspace(-1,1,100)
X, Y = np.meshgrid(x,y)

k=9e9 #electric constant
q1q=1e-6
q1x=0
q1y=0

def potential(x,y):
    r = np.sqrt( (q1x-x)**2 + (q1y-y)**2 )
    V=k*q1q/r
    return V
    
V=potential(X,Y)

#plt.contourf(X, Y, V, 20, cmap='RdGy') #can twick the number for more lines 
plt.imshow(V, extent=[-1, 1, -1, 1], origin='lower',
           cmap='RdGy') #threat the plot as an image
#doesn't accept an x and y grid, 
#so you must manually specify the extent [xmin, xmax, ymin, ymax] 
#of the image on the plot.
plt.colorbar() 
plt.axis(aspect='image')
plt.show()
