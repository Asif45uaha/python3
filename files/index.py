"""
File handling is an important part of any web application.

Python has several functions for creating, reading, updating, and deleting files.

"""

#open a file


"""
The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists


"""

"""


open() function returns a file object, 
which has a read() method for reading the content of the file

f= open("info.txt","r")
print(f.read())
f.close()

"""

#writing to an exisiting file

"""
Write to an Existing File
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content

"""
f = open("info.txt","a")

n=int(input("Enter a number whose table you want: \n"))

print("File writing started...")

f.write(f"\n\n\n\nTable of {n} is : "+"\n\n")

i=1
while i<=10:
    f.write(f"{n} * {i} = {i*n}"+"\n")
    i= i+1
    
print("File writing completed...")

f = open("info.txt","r")
print(f.read())

f.close()
"""
#delete files

import os
os.remove("info.txt")

"""
