"""
The shape of an array is the number of elements in each dimension.

"""

import numpy as np

arr = np.array([[1, 2, 3,4,5],[6,7,8,9,10]])
print(arr.shape) #(2,5)
arr2 = np.array([1,2,3,4],ndmin=5)
print(arr2.shape)

"""
Reshaping arrays
Reshaping means changing the shape of an array.

The shape of an array is the number of elements in each dimension.

By reshaping we can add or remove dimensions or change number of elements in each dimension.

"""

#Reshape From 1-D to 2-D

arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newArr = arr3.reshape(4,3)
print(newArr) #[[ 1  2  3][ 4  5  6][ 7  8  9][10 11 12]]


#Reshape From 1-D to 3-D
newArr2 = arr3.reshape(2,2,3)
print(newArr2)

#Flattening array : Convert the array into a 1D array
arr4 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr4.reshape(-1))