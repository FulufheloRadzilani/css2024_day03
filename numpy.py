# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 14:09:58 2024

@author: radzi
"""

import numpy as np
import matplotlib.pyplot as plt
 
#Conventional python - for loops

print("using just python")
for i in range (1,11):
    print(i)

#numpy - arange
print("using numpy:")
for i in np.arange(1,11,0.5):
    print(i)

"""
#squaring the numbers from 1 to 5

squares=[]
for i in range(1,6):
    squares.append(i**2)
print(squares)

squares = np.arange(1,6)**2
print(squares)

x=np.arange(1,6)
y = x**2
print("shape of x:")
print("x.shape")
print("shape of y:")
print("y.shape")
print(x*y)
print("calculating dot product")
print(x.dot(y))
print("calculate cross product")
print(np.matmul(x,y))
plt.plot(x,y,"r*")
plt.show()
"""

alist = [1, 2, 5, 6, 15, 22]
data = np.array(alist)
print(data)
data2 = data.reshape([2,3])
data3 = np.reshape(alist, [2, 3])
print("data 2")
print(data2)
print("data 3")
print(data3)
alist2 = [[1,2,5],[6,15,22]]
#Multiply two 2x3 matrices
data4 = np.matmul(data2.T[0,:],data3)
print("data4:")
print(data4)
#cross product of matrices
print("cross product")
crossdata = np.cross(data2[0,:], data3 [1,:])
print(crossdata)

a = np.array([[1,2,3],[4,5,6],[7,8,-9]])
b = np.array([3,-4,2])
d = np.linalg.det(a)
if(d>0):
    print(f"d = {d}, this matrix is solvable")
sol = np.linalg.solve(a,b)

