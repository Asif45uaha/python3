"""
Set
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.

"""
#set doesn't allow duplicates

"""
fruits = {"apple", "banana", "cherry"}
print(fruits)
print(len(fruits)) #3
print(type(fruits)) #<class 'set'>

"""

#accessing set items

#we can't access set items by indiex,ās set is unindexed

# for x in fruits:
#     print(x)
# print("banana" in fruits)

"""
add method

fruits.add("orange") #adds item to the set
print(fruits)

update method

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical) #add items from another set into the current set
print(thisset)

#remove method : removes an item in a set
fruits.remove("banana") | fruits.discard("banana")
print(fruits)

"""

"""
#loop through the sets
fruits = {"apple", "banana", "cherry"}

# for x in fruits:
#     print(x)

"""

#set join operations

"""
union() or | : 
# The union() method returns a new set with all items from both sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

print(set1.union(set2))
print(set1 | set2)

"""

"""
intersection() or &:

The intersection() method will return a new set, 
that only contains the items that are present in both sets


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print(set1.intersection(set2))
print(set1 & set2)

"""



"""

difference() or -:

The difference() method will return a new set that will contain only the items from the first set that are not present in the other set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print(set1.difference(set2)) #{'banana', 'cherry'}
print(set1 - set2)
"""

 

"""
symmetric_difference() or ^ :
The symmetric_difference() method will keep only the elements that are NOT present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print(set1.symmetric_difference(set2))
print(set1 ^ set2)

"""

#set methods

"""

add()	 	Adds an element to the set

clear()	 	Removes all the elements from the set

copy()	 	Returns a copy of the set

difference()	-	Returns a set containing the difference between two or more sets

difference_update()	-=	Removes the items in this set that are also included in another, specified set

discard()	 	Remove the specified item

intersection()	&	Returns a set, that is the intersection of two other sets

intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)

isdisjoint()	 	Returns whether two sets have a intersection or not

issubset()	<=	Returns whether another set contains this set or not
 	<	Returns whether all items in this set is present in other, specified set(s)

issuperset()	>=	Returns whether this set contains another set or not
 	>	Returns whether all items in other, specified set(s) is present in this set

pop()	 	Removes an element from the setremove()	 	Removes the specified elementsymmetric_difference()	^	Returns a set with the symmetric differences of two setssymmetric_difference_update()	^=	Inserts the symmetric differences from this set and anotherunion()	|	Return a set containing the union of sets

update()	|=	Update the set with the union of this set and others

"""



