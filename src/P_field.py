import matplotlib
import numpy as np #library for maths functions and arrays
import matplotlib . pyplot as plt #library for plottitng

L=1 #arbitrary dimension

fname = 'output.txt' #the file should be in the same folder as program, or include the path
#load the file "fname", defined above
data = np.loadtxt(fname, delimiter='\n', comments='#')
print(len(data))
N = int(np.sqrt(len(data))) 
V = np.reshape(data, (N,N)) #reshape the data

plt.imshow(V, cmap='hot', interpolation='nearest')
plt.show()

