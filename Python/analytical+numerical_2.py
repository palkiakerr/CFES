import matplotlib
import numpy as np #library for maths functions and arrays
import matplotlib . pyplot as plt #library for plottitng

fname = 'problem_2.txt' #the file should be in the same folder as program, or include the path
#load the file "fname", defined above
data = np.loadtxt(fname, delimiter=',', comments='#')      
N = int(np.sqrt(len(data))) #get the dimensions automatically                 
V_num = np.reshape(data, (N,N)) #reshape the data to a NxN array

#put some arbitrary dimensions 
d = 10 #distance between plates
h = 10 #height of the plates
R0 = 1 #radius of the ground wire
V0 = 1 #potential of the plates

x = np.linspace( -d/2, d/2, N)
y = np.linspace( -h/2, h/2, N)
X, Y = np.meshgrid(x,y)

def potential(x,y):
    r = x**2 + y**2 
    V_potential = (-(2*V0) / d) * (x - R0*R0*x/(r*r))
    V_potential [np.where (np.abs(r) < R0) ] = 0
    return V_potential

V_anal = potential(X,Y)


#Plotting
plt. title ('Analytical Solution')
matplotlib.rcParams ['xtick.direction'] = 'out'
matplotlib.rcParams ['ytick.direction'] = 'out'
CS = plt. contour (X,Y,V_anal,30) # Make a contour plot = Contour Set; num countour lines
plt. clabel (CS , inline =1, fontsize =10)
CB = plt. colorbar (CS , shrink =0.8 , extend ='both')
plt.show()

plt.clf()
plt. title ('Numerical Solution')
matplotlib.rcParams ['xtick.direction'] = 'out'
matplotlib.rcParams ['ytick.direction'] = 'out'
CS = plt. contour (X,Y,V_num,30) # Make a contour plot = Contour Set; num countour lines
plt. clabel (CS , inline =1, fontsize =10)
CB = plt. colorbar (CS , shrink =0.8 , extend ='both')
plt.show()

error = np.abs(V_num - V_anal) 
plt.imshow(np.abs(V_num - V_anal), cmap = 'OrRd', vmin = 0, vmax = 0.1)
plt.colorbar()
plt.show()
