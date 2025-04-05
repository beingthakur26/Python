# Static Method ;
# Static method is a method that belongs to the class rather than an instance of the class.
# It does not require an instance of the class to be called. Static methods are defined using the @staticmethod decorator.
# They can be called on the class itself or on an instance of the class. Static methods do not have access to the instance (self) or class (cls) variables. They are used for utility functions that do not require access to the instance or class variables.
# Static methods are similar to regular functions, but they are defined inside a class. They can be called using the class name or the instance of the class.
# Static methods are useful for defining utility functions that are related to the class but do not require access to the instance or class variables. They can be used for tasks such as data validation, formatting, and other operations that do not depend on the state of the object.
# Static methods can also be used to create factory methods, which are methods that return an instance of the class. Factory methods can be used to create objects with different initial values or configurations. They can also be used to create objects of subclasses based on certain conditions.

# Syntax '
# class ClassName:
#     @staticmethod
#     def method_name(args):
#         # Method code
#         pass


class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    @staticmethod
    def welcome():
        print("Welcome to the class of OOPS")

    def get_avg(self):
        sum = 0
        for val in self.mark:
            sum += val
        print("Hii", self.name, "Your avg score is : ", sum/3)

s1 = Student("Tony Stark", [90, 80, 70])
s1.get_avg() # Hii Tony Stark Your avg score is :  80.0


s1.name = "Ironman"
s1.get_avg() # Hii Ironman Your avg score is :  80.0

s1.welcome() # Welcome to the class of OOPS