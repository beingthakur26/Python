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


# Encapsulation :
# Encapsulation is the concept of wrapping data and methods into a single unit called a class.
# It restricts direct access to some components of the object and can prevent the accidental modification of data.
# Encapsulation is achieved in Python using private and public access modifiers.
# Private members are defined by prefixing the member name with an underscore (_).
# Public members are accessible from outside the class.
# Encapsulation allows for data hiding and protects the integrity of the object.
# It also provides a clear interface for interacting with the object.