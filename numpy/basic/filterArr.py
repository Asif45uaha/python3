"""
Filtering Arrays
Getting some elements out of an existing array and creating a new array out of them is called filtering.

In NumPy, you filter an array using a boolean index list

"""

import numpy as np

arr = np.array([41, 42, 43, 44])

x = arr >= 43
newarr = arr[x]

print(newarr)

arr1 = np.array([1, 2, 3, 4, 5, 6, 7,8,9,10])
filter = arr1 % 2 != 0
newArr = arr1[filter]
print(newArr)