"""
Slicing arrays
Slicing in python means taking elements from one given index to another given index.

We pass slice instead of index like this: [start:end].

We can also define the step, like this: [start:end:step].

If we don't pass start its considered 0

If we don't pass end its considered length of array in that dimension

If we don't pass step its considered 1

"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])
print(arr[1:])
print(arr[:5])
print(arr[-3:-1])

arr2 = np.array([1,2,4,5,6,7,8,9,10])

#using step
print(arr[1:5:2]) # determines the step of the slicing
print(arr2[0:6:3]) #[1 5]
print(arr2[::2]) #[ 1  4  6  8 10]
print(arr2[1:6:3]) #[2 6]

#slicing 2-D array

arr3 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr3[1,1:4]) #[7 8 9]
print(arr3[0:2,2]) #[3 8]
print(arr3[0:2,1:4]) #[[2 3 4][7 8 9]]