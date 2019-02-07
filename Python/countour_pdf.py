# point_charge .py - Iterative solution of 2-D PDE , electrostatics
import matplotlib
import numpy as np
import matplotlib . pyplot as plt
# Set dimensions of the problem
L = 1.0
N = 40
ds = L/N
# Define arrays used for plotting
x = np. linspace (0,L,N)
print(x)
y = np.copy(x)
X, Y = np. meshgrid (x,y)
print(X)

# Make the charge density matrix
k=9e9 #electric constant
#these are the charge values
q1q=1e-6
q2q=-1e-6
q3q=5e-5
rho0 = 10.0
rho = np. zeros ((N,N))
rho[int( round(N/4.0)) , int(round (N /4.0))] = k*q1q
rho[int( round(3.0*N/4.0)) , int(round (2.0*N /4.0))] = k*q2q

rho[int( round(2.0*N/4.0)) , int(round (3.0*N /4.0))] = k*q2q
# Make the initial guess for solution matrix
V = np. zeros ((N,N))
# Solver
iterations = 0
eps = 1e-8 # Convergence threshold
error = 1e4 # Large dummy error

while iterations < 1e4 and error > eps:
    V_temp = np.copy(V)
    error = 0 # we make this accumulate in the loop
    for j in range (1,N -1):
        for i in range (1,N -1):
            V[i,j] = 0.25*( V[i+1,j] + V[i-1,j] + V[i,j -1] + V[i,j+1] + rho[i,j]* ds **2)
            error += abs(V[i,j]- V_temp [i,j])
    iterations += 1
    error /= float(N)
print (" iterations =",iterations)

print(V_temp)
print(rho)
#Plotting
matplotlib.rcParams ['xtick.direction'] = 'out'
matplotlib.rcParams ['ytick.direction'] = 'out'
CS = plt. contour (X,Y,V,50) # Make a contour plot = Controur Set
plt. clabel (CS , inline =1, fontsize =10)
plt. title ('PDE solution of a point charge')
CB = plt. colorbar (CS , shrink =0.8 , extend ='both')
plt.show ()