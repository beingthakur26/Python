# Method :
# A method is a function that is defined inside a class. It is used to define the behavior of the objects of the class.
# Methods can take arguments and return values, just like regular functions.
# However, methods have access to the attributes of the class, which allows them to modify the state of the object.
# Methods are defined using the def keyword, followed by the name of the method and its parameters.

class Student:

    def __init__(self, name, mark):
        self.name = "Manas"
        self.mark = mark

    def welcome(self):
        print("Welcome to the class of OOPS", self.name)

    def get_mark(self):
        return self.mark
    
s1 = Student("Manas", 99)
print(s1.name)
s1.welcome()
print(s1.get_mark())