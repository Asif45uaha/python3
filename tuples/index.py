"""
Tuple
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.

"""

"""
thisTuple = ("apple", "banana", "cherry")
print(thisTuple)
print(len(thisTuple))

#access tuple items

print(thisTuple[-1])
print(thisTuple[:1])
print(thisTuple[1:])
print(thisTuple[-2:-1])

"""



"""
#tuples are unchangeable
#we can convert tuple into a list to make modifications

thisList = list(thisTuple)
thisList.insert(3,"papaya")
thisTuple = tuple(thisList)
print(thisTuple)

"""

# unpacking in a Tuple

"""
fruits = ("apple", "banana", "cherry")
(first,*rest) = fruits

print(first) #apple
print(rest) #['banana', 'cherry']

animals = ("cat","dog","bird","fish","horse","donkey")
(first,*second,last) = animals
print(first) #cat
print(second) #['dog', 'bird', 'fish', 'horse']
print(last) #donkey

"""

#looping through the tuples

"""
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

for i in range(len(thistuple)):
  print(thistuple[i])

i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

"""

#tuple methods

"""
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found

"""




thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)
y = thistuple.index(5)


print(x) #2
print(y)