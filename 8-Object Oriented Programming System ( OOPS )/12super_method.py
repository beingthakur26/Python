# Super Method :
# The super() function in Python is used to call methods from a parent class in a child class.
# It allows you to access inherited methods that have been overridden in a child class.
# The super() function returns a temporary object of the superclass that allows you to call its methods.
# It is commonly used in the __init__ method to initialize the parent class's attributes.

class Car : # Base class
    # Constructor of the base class
    def __init__(self, type):
        self.type = type

    @staticmethod 
    def start():
        print("Car started.....")

    @staticmethod
    def stop():
        print("Car stopped.....")

class Toyota(Car): # Inheriting from Car class
    def __init__(self, name, type):
        super().__init__(type) # Calling the constructor of the parent class
        # Initializing the attributes of the child class
        self.name = name
        super().start()  # Calling the start method from the parent class
        

car1 = Toyota("prius", "hybrid")
print(car1.type) # hybrid
