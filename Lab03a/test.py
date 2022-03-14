import numpy as np
import matplotlib.pyplot as plt
from pyparsing import alphanums
from scipy.linalg import lstsq

plt.style.use(['seaborn-colorblind', 'seaborn-darkgrid'])
plt.rcParams["figure.figsize"] = [12,4.5]

Lab03 = np.genfromtxt('data/mystery_data_1.csv', delimiter=',')
Lab03 = np.array(Lab03)
Lab03 = np.delete(Lab03,0,0)
Lab03 = np.delete(Lab03,0,0)

row,col = np.shape(Lab03)

x = Lab03[:,0]
y = Lab03[:,1]

plt.plot( x, y)
plt.xlabel( "X")
plt.ylabel("Y")

one = np.ones(row)
x2 = x**2
#print(one)
#print (x)
#print(x2)

Ahat = one
Ahat = np.c_[Ahat,x]
Ahat = np.c_[Ahat,x2]
print (Ahat)