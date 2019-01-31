import matplotlib
import numpy as np #library for maths functions and arrays
import matplotlib . pyplot as plt #library for plottitng

N=40
L=1


fname = 'pos_point_charge_example_100.txt' #the file should be in the same folder as program, or include the path
#load the file "fname", defined above
data = np.loadtxt(fname, delimiter=',', comments='#')        
V = np.reshape(data, (N,N)) #reshape the data
print(V)


E_x = np.zeros((N-1,N-1))
E_y = np.zeros((N-1,N-1))

for i in range (1, len(V)-1):
      for j in range (1, len(V)-1):
          E_y[i,j] = - (V[i+1, j] - V[i-1, j])*N/(2*L)
          E_x[i,j] =  - (V[i, j+1] - V[i, j-1])*N/(2*L)

plt.clf()
plt.quiver(E_x, E_y, color='b')
plt.show()