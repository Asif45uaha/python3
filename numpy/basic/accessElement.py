#Accessing array elements
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr[0])
print(arr[1:])
print(arr[:3])

#accessing 2-D array

arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print(arr2[0,0])
print(arr2[0,1])
print(arr2[0,2])
print(arr2[1,0])
print(arr2[1,1])
print(arr2[1,2])

# accessing 3-D array

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3[0,1,2])