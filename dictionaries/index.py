"""
Dictionary
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

"""

car = {
    "brand" : "Ford",
    "model":"Mustang",
    "year" : 1965
}

print(car)
print(car["brand"])
print(car["year"])
print(car["model"])
print(car.get("model")) #get method can also be used to access
print(car.keys()) #returns a list of all the keys in the dictionary.
print(car.values()) #returns a list of all the values in the dictionary.
print(car.items()) #returns each item in a dictionary, as tuples in a list


#change dictionary

car.update({"color":"white"})
print(car.items())
car.pop("model")
print(car)

#looping dictionary

for x in car.values():
    print(x)
    
    
#dictionary methods

"""
clear()	Removes all the elements from the dictionary

copy()	Returns a copy of the dictionary

fromkeys()	Returns a dictionary with the specified keys and value

get()	Returns the value of the specified key

items()	Returns a list containing a tuple for each key value pair

keys()	Returns a list containing the dictionary's keys

pop()	Removes the element with the specified key

popitem()	Removes the last inserted key-value pair

setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value

update()	Updates the dictionary with the specified key-value pairs

values()	Returns a list of all the values in the dictionary

"""
