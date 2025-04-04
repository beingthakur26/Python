# __init__ Function :
# The __init__ function is a special method in Python classes. It is called when an object of the class is created.
# The __init__ function is used to initialize the attributes of the class. It is similar to a constructor in other programming languages.
# The __init__ function can take arguments, which can be used to set the initial values of the attributes.
# The __init__ function is defined using the def keyword, followed by the name of the class and the parameters.
# The first parameter of the __init__ function is always self, which refers to the instance of the class.
# The self parameter is used to access the attributes and methods of the class.
# The __init__ function can also have default values for its parameters. This allows you to create objects with different initial values.
# The __init__ function can also call other methods of the class to perform additional initialization tasks.
# This can be useful for setting up complex objects with multiple attributes.

# Syntax :  
# class ClassName:
#     def __init__(self, arg1, arg2, ...):
#         # Initialization code
#         self.attribute1 = arg1
#         self.attribute2 = arg2
#         # Additional initialization code
#         # Call other methods if needed
#         self.some_method()
#
#     def some_method(self):
#         # Method code
#         pass

# Creating Class
class Student:
    college_name = "XYZ College"
    ''' name = "anonymous" ''' # class attribute

    def __init__(self, fullname, marks): # Constructor
        # This is the constructor method, it is called when an object of the class is created.
        self.name = fullname # object atribute > class attribute
        self.marks = marks
        print("Adding now student in Database...") 

s1 = Student("Manas", 40) # Creating Object of Class
print(s1.name, s1.marks) # Manas

s2 = Student("Tejas", 50) # Creating Object of Class
print(s2.name, s2.marks) # Tejas

print(s2.college_name) # XYZ College