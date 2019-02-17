import matplotlib
import numpy as np #library for maths functions and arrays
import matplotlib . pyplot as plt #library for plottitng

fname = 'matrix.txt' #the file should be in the same folder as program, or include the path
#load the file "fname", defined above
data = np.loadtxt(fname)
print(len(data))
N = int(np.sqrt(len(data))) 
V = np.reshape(data, (N,N)) #reshape the data
V[V < 0.000002] = 0

plt.imshow(V, cmap='Greys')
plt.savefig('schematic.png', bbox_inches='tight')