# Abstraction :
# Abstraction is the concept of hiding the complex implementation details and showing only the essential features of the object.
# It allows the user to interact with the object without needing to understand its internal workings.
# Abstraction is achieved in Python using abstract classes and interfaces.
# An abstract class is a class that cannot be instantiated and can contain abstract methods (methods without implementation).

class Car:
    def __init__(self):
        self.acc = False
        self.brake = False
        self.clutch = False

    def start(self):
        self.clutch
        self.acc
        print("Car started.....")

car1 = Car()
car1.start()
