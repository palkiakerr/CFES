
"""
This programme plots the error in the 1st analytical solution
as dependent of number of iterations 
on a 101 grid
"""

import numpy as np #library for maths functions and arrays
import matplotlib . pyplot as plt #library for plottitng

num_iter = [1000, 2000, 5000, 7000, 10000, 50000, 100000]

err_max_arr = [10.466935677703123,
               2.758843466829113,
               1.63775473983579,
               1.63775473983579,
               1.63775473983579,
               1.63775473983579,
               1.63775473983579]

plt.plot(num_iter, err_max_arr, '.')
plt.title('Error Dependence with Iterations')
plt.xlabel('Number of Iterations')
plt.ylabel('Maximum Observed Error')
plt.xscale('log')
plt.show()