# Iterate on the 1-D array

import numpy as np

# arr = np.array([1, 2, 3])

# for x in arr:
#   print(x)

#Iterating 2-D Arrays

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
      print(y)
    
#Iterating 3-D Arrays

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
    for y in x:
        for z in y:
            print(z)
            
#Iterating arrays using nditer()
"""
The function nditer() is a helping function that can be used from very basic to very advanced iterations.
In basic for loops, iterating through each scalar of an array we need to use n for loops which can be difficult to write for arrays with very high dimensionality.
"""

arr2 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr2):
    print(x)
    
#Iterating With Different Step Size

arr3 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr3[:, ::2]):
  print(x)
  
# Enumerated Iteration Using ndenumerate()

"""
Enumeration means mentioning sequence number of somethings one by one.

Sometimes we require corresponding index of the element while iterating, the ndenumerate() method can be used for those usecases.

"""

arr5 = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr5):
  print(idx, x)
  
arr6 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr6):
  print(idx, x)