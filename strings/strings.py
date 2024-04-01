
#----------------------------------slicing strings----------------------------------------#
"""
name = "Aasif Ali"
print(type(name)) #<class 'str'>
print(len(name)) #9
print(name[:5]) #general slicing from start idx to end idx
print(name[:3]) #slices from index 0 excluding last
print(name[2:]) #slices from index 2 including start index
print(name[-3:]) #negative indexing
print(name[:-5]) #negative indexing

"""

#----------------------------------Modify strings----------------------------------------#

"""
name = "Aasif, Ali, Mir "
print(name.lower()) #converts str to lowercase
print(name.upper()) #converts str to Uppercase
print(name.strip()) #removes whitespace from beginning or the end
print(name.replace("Aasif", "Ali")) #replaces string with another string
print(name.split(",")) #returns a list where the text between the specified separator becomes the list items

"""

#----------------------------------Format strings----------------------------------------#

#we can combine strings and numbers by using the format() method!
"""
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

"""
"""
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

"""

#----------------------------------string Methods----------------------------------------#

"""
txt = "hello, and Welcome to my World. Welcome again"

print (txt.capitalize()) #makes first char as an uppercase rest of the str as a lowercase
print(txt.casefold()) #makes whole string as a lowercase
print(txt.count("Welcome")) #returns the number of times a specified value appears in a str
print(txt.encode("utf-8")) #returns utf-8 encoding
print(txt.endswith("again")) #returns True if the string ends with the specified value, otherwise False.
print(txt.find("World")) #finds the first occurrence of the specified value.
# The find() method returns -1 if the value is not found
print(txt.index("World")) #same as find method, 
# but this method raises an exception if the specified value is not found
print(txt.isalnum()) #Returns True if the string is an alpha-numeric string, False otherwise
print(txt.isalpha()) #Returns True if the string is an alphabetic string, False otherwise.
print(txt.islower()) #Returns True if the string is a lowercase string, False otherwise.
print(txt.isupper()) #Returns True if the string is an uppercase string, False otherwise.
myTuple = ("He","is","only","one","person","in","district","Budgam")
print(" ".join(myTuple)) #The join() method takes all items in an iterable and joins them into one string
print(txt.startswith("World")) #returns True if the string starts with the specified value, otherwise False.

"""
