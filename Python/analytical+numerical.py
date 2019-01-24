import matplotlib
import numpy as np #library for maths functions and arrays
import matplotlib . pyplot as plt #library for plottitng

N=101
L=101
V0 = 8
r0 = 15
r1 = 50
c1 = -V0 / np.log(r0/r1)
c2 = (V0 / np.log(r0/r1))*np.log(r0)

x = np. linspace (-L/2,L/2,N)
y = np. linspace (-L/2,L/2,N)
X, Y = np. meshgrid (x,y) #create the 2d grid

def potential(i,j):
    r = np.sqrt(i**2 + j**2)
    V_potential = c1 * np.log(r) +c2
    V_potential [np.where(r<=r0)] = 0
    V_potential [np.where(r>=r1)] = 0
    return V_potential

V_anal = potential(X,Y)

fname = 'analyze_num.txt' #the file should be in the same folder as program, or include the path
#load the file "fname", defined above
data = np.loadtxt(fname, delimiter=',', comments='#')        
V_num = np.reshape(data, (101,101)) #reshape the data to a 40x40 array

#Plotting
matplotlib.rcParams ['xtick.direction'] = 'out'
matplotlib.rcParams ['ytick.direction'] = 'out'
CS = plt. contour (X,Y,V_anal,30) # Make a contour plot = Contour Set; num countour lines
plt. clabel (CS , inline =1, fontsize =10)
plt. title ('Analytical Solution')
CB = plt. colorbar (CS , shrink =0.8 , extend ='both')
plt.show ()
plt.clf()

matplotlib.rcParams ['xtick.direction'] = 'out'
matplotlib.rcParams ['ytick.direction'] = 'out'
CS = plt. contour (X,Y,V_num,30) # Make a contour plot = Contour Set; num countour lines
plt. clabel (CS , inline =1, fontsize =10)
plt. title ('Numerical Solution')
CB = plt. colorbar (CS , shrink =0.8 , extend ='both')
plt.show ()

error = np.abs(V_num - V_anal) 
plt.imshow(np.abs(V_num - V_anal), cmap = 'OrRd', vmin = 0, vmax = 0.1)
plt.colorbar()
plt.show()
