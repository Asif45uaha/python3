"""
olymorphism is often used in Class methods, where we can have multiple classes with the same method name.

"""

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Car is moving")
    

class Boat:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Boat is sailing")

class Plane:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Plane is flying")
        
car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1,boat1,plane1):
    x.move
