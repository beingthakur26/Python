# Polymorphism :
# Polymorphism is a core concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different underlying forms (data types). In Python, polymorphism is often achieved through method overriding and operator overloading.

# Operator Overloading
# Operator overloading is a feature that allows us to define the behavior of operators for user-defined classes.
# It enables us to use standard operators like +, -, *, /, etc., with objects of our classes.
# This can make our code more intuitive and easier to read.
# In Python, we can overload operators by defining special methods in our classes. These special methods are also known as dunder (double underscore) methods.
# For example, we can overload the + operator by defining the __add__ method in our class. When we use the + operator with objects of that class, Python will automatically call the __add__ method.

class Complex :
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        # print(f"{self.real} + {self.img}i")
        print(self.real,"i +", self.img,"i")

    # def add(self, num2):
    #     # Adding two complex numbers
    #     real = self.real + num2.real
    #     img = self.img + num2.img
    #     return Complex(real, img)
    
    def __add__(self, num2):
        # Adding two complex numbers
        real = self.real + num2.real
        img = self.img + num2.img
        return Complex(real, img)
    
    def __sub__(self, num2):
        # Subtracting two complex numbers
        real = self.real - num2.real
        img = self.img - num2.img
        return Complex(real, img)

num1 = Complex(2, 3)
num1.showNumber()  # Output: 2 i + 3 i

num2 = Complex(4, 5)
num2.showNumber()  # Output: 4 i + 5 i

# num3 = num1.add(num2)
# num3.showNumber()  # Output: 6 i + 8 i

num3 = num1 + num2  # Using the overloaded + operator
num3.showNumber()  # Output: 6 i + 8 i
# The __add__ method is called when we use the + operator with Complex objects.
# This allows us to add complex numbers using the + operator, making the code more intuitive.

num4 = num1 - num2  # Using the overloaded - operator
num4.showNumber()  # Output: -2 i + -2 i
# The __sub__ method is called when we use the - operator with Complex objects.
# This allows us to subtract complex numbers using the - operator, making the code more intuitive.

