"""
thislist = ["apple", "banana", "cherry"]
print(type(thislist)) #<class 'list'>
print(len(thislist)) #3 returns length of a list
#access list
print(thislist[-1]) #cherry
print(thislist[:2]) #["apple", "banana"]
print(thislist[1:]) #['banana', 'cherry']
#change list
thislist[1:2] = ["orange", "mango"]
thislist.insert(2,"watermelon") #nserts an item at the specified index
print(thislist)

"""
#add items in  list
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange") #appends item at an end
# print(thislist)
# thislist.insert(2,"Kiwi")
# print(thislist)
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical) #merges two lists
# print(thislist)
# thislist.remove("apple") #removes specified item
# print(thislist) # ["banana", "cherry"]
# thislist.pop(1) #removes the specified index
# print(thislist)

# looping through lists

# thislist = ["apple", "banana", "cherry"]

#for in loop

# for x in thislist:
#     print(x)

#for loop with indices

# for i in range(len(thislist)):
#     print(thislist[i]+ " has index of: ",i)

#while loop

# i=0
# while i<len(thislist):
#     print(thislist[i])
#     i=i+1

#list comprehension

# [print(x) for x in thislist]

#sorting lists

"""
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort() #sorts by alphabetically
thislist.sort(reverse=True) #sorts lists alphabetically but in descending order
print(thislist)

"""

# thislist = [100,50,65,82,23,1]
# thislist.sort()
# print(thislist)


"""
list methods

append():Adds an element at the end of the list
clear():Removes all the elements from the list
copy():Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
x= thislist.index("mango")
print(x) returns the index number

insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

"""