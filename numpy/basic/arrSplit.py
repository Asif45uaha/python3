"""
Splitting NumPy Arrays
Splitting is reverse operation of Joining.

Joining merges multiple arrays into one and Splitting breaks one array into multiple.

We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.

"""
import numpy as np

a = np.array([1,2,3,4,5,6])
print(np.array_split(a,3)) #Splits the array in 3 parts

two_d_arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

print(np.array_split(two_d_arr,3))