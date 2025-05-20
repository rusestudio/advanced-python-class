#encapsulation

class Person:
    def __init__(self, name, age, gender):
        self.__name = name  #.__ for private attribute
        self.__age = age
        self.__gender = gender

    @property
    def Name(self):   #like getter
        return self.__name
    
    @Name.setter
    def Name(self, value):   #like setter
        if value == "cat":
            self.__name = "Not a person"
        else:
            self.__name= value

    @staticmethod
    def mymethod():
        print("my method")
    
p1 = Person("Mike", 20, 'm')
print(p1.Name)

p1.Name = "cat"
print(p1.Name)

#static method
Person.mymethod()
p1.mymethod()

#abstract class
from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):  #need to inherit abstract method in parent
    
    def go(self):
        print("driving")

    def stop(self):
        print("stopping")

class Bike(Vehicle): 
    
    def go(self):
        print("cycling")

    def stop(self):
        print("breaking")

class Boat(Vehicle): 
    
    def go(self):
        print("rowing")

    def stop(self):
        print("anchor boat")

#v1 = Vehicle() # cannot create obj with abstrct
#v1.go()
#v1.stop()

c1 = Car()
c1.go()
c1.stop()

b1 = Bike()
b1.go()
b1.stop()

b2 = Boat()
b2.go()
b2.stop()
