"""
Joining NumPy Arrays
Joining means putting contents of two or more arrays in a single array.

In SQL we join tables based on a key, whereas in NumPy we join arrays by axes.

We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0.

"""

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2),axis=0)

print(arr)

arr3 = np.array([[1, 2], [3, 4]])

arr4 = np.array([[5, 6], [7, 8]])

print(np.concatenate((arr3,arr4),axis=1))


#Joining Arrays Using Stack Functions

"""
Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, ie. stacking.

We pass a sequence of arrays that we want to join to the stack() method along with the axis. If axis is not explicitly passed it is taken as 0
"""

arr5 = np.array([1,2,3])
arr6 = np.array([4,5,6])

print(np.stack((arr5,arr6),axis=1)) 

"""


NumPy provides a helper function: hstack() to stack along rows.

"""

a1 = np.array([1, 2, 3])

a2 = np.array([4, 5, 6])

print(np.hstack((a1,a2))) #Stacking Along Rows
print(np.vstack((a1,a2))) #Stacking Along cols
print(np.dstack((a1,a2))) #Stacking Along Height (depth)