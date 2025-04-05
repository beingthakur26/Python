# Inheritance :
# Inheritance is a mechanism in which one class acquires the property of another class.

class Car:
    color = "red"
    @staticmethod
    def start():
        print("Car started.....")

    @staticmethod
    def stop():
        print("Car stopped.....")

class Toyota(Car):
    def __init__(self, name):
        self.name = name

car1 = Toyota("Fortuner")

print(car1.start())  # Car started.....
print(car1.color)  # red


# Multi-Level Inheritance:
# In multi-level inheritance, a class is derived from another derived class.
# This means that a derived class can inherit properties and methods from its parent class, and it can also be a parent class for another derived class.
# This creates a chain of inheritance.

class Car:
    @staticmethod
    def start():
        print("Car started.....")

    @staticmethod
    def stop():
        print("Car stopped.....")

class Toyota(Car):
    def __init__(self, brand):
        self.name = brand

class Fortuner(Toyota):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("Diesel")
car1.start()  # Car started.....



# Multiple Inheritance:
# In multiple inheritance, a class can inherit from multiple parent classes.
# This allows a derived class to inherit properties and methods from multiple base classes.
# However, it can lead to ambiguity if the same method or property is defined in multiple parent classes.
# Python resolves this ambiguity using the Method Resolution Order (MRO) algorithm.
# The MRO determines the order in which base classes are searched when looking for a method or property.

class A:
    varA = "wlcome  to class a"

class B:
    varB = "wlcome  to class b"

class C(A, B):  # Inheriting from both A and B
    varC = "wlcome  to class c"

c1 = C()

print(c1.varA)  # wlcome  to class a
print(c1.varB)  # wlcome  to class b
print(c1.varC)  # wlcome  to class c
