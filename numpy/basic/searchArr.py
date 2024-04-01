import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)

print(x)

y = np.searchsorted(arr,[2,4,6],side="right") #performs a binary search in the array
print(y)