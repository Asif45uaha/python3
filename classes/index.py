"""
class MyClass:
    x=5
obj = MyClass()
print(obj.x)

"""

#----------------------------The __init__() Function---------------------------------------
"""
To understand the meaning of classes we have to understand the built-in __init__() function
All classes have a function called __init__(), which is always executed when the class is being initiated.
Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created

"""

"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age= age

p1 = Person("Aasif",24)
p2 = Person("Arshid",22)

print(p1.name,p1.age) #Aasif 24
print(p2.name,p2.age) #Arshid 22

"""

#The __init__() function is called automatically every time the class is being used to create a new object.


#--------------------The __str__() Function------------------------------

"""
The __str__() function controls what should be returned when the class object is represented as a string.
If the __str__() function is not set, the string representation of the object is returned

"""

#class Person without __str__() func

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

# print(p1) #<__main__.Person object at 0x00000209D9C373E0>

#class Person with __str__() func

class Person:
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Email: {self.email}"
        
p1 = Person("Aasif",24,"asif1510@gmail.com")
print(p1) #Name: Aasif, Age: 24, Email: asif1510@gmail.com


"""
The self Parameter
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class

It does not have to be named self , we can call it whatever you like, but it has to be the first parameter of any function in the class

"""

class Animal:
    def __init__(dog,name,age,wild):
       dog.name = name
       dog.age = age
       dog.wild = wild
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Wild: {self.wild}"

dog = Animal("Golden Retreiver",5,False)
dog.age = 10 #modifies age of dog object
print(dog)
# del dog #deletes dog obj

