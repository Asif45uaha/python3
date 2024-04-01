from numpy import random


print(random.randint(100)) #random int
print(random.rand()) #random float
print(random.randint(100,size=(5))) #generates a 1-D array of 5 shape

print(random.randint(100,size=(5,5))) #generates 2-D arr of shape(5,5)

print(random.choice([3,5,7,9]))
