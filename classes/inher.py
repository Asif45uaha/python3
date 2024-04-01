"""
Python Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.

"""

class Person:
    def __init__(self,name,age,email,profession):
        self.name = name
        self.age = age
        self.email = email
        self.profession = profession
    
    def printOutput(self):
        print(f"Your name is: {self.name}\n Your Email is: {self.email}\n Your Age is: {self.age}\n Your Profession is {self.profession}")

x = Person("John Doe", 28,"john123@gmail.com","ML Engineer")
x.printOutput()


class Student(Person):
    #when we add __init__() in child class 
    #the child class will no longer inherit the parent's __init__() function
    # The child's __init__() function overrides the inheritance of the parent's __init__() function
    #To keep the inheritance of the parent's __init__() function,
    # add a call to the parent's __init__() function or add super() function to inherit parent properties of a child class
    def __init__(self, name, age, email, profession,year):
        # Person.__init__(self, name, age, email, profession)
                   #or
        super().__init__(name, age, email, profession)
        self.graduationyear=year

x= Student("Irfan",17,"irfan123@gmail.com","Student",2023)
x.printOutput()
print(x.graduationyear)

"""
in above example class Student Inherited parent class Person

"""