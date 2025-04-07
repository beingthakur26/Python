# Question 1.
# Define a Circle class to create a circle with radius r using constructor.
# Define an Area() method of the class which calculate the area of the circle.
# Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return 22/7 * self.radius ** 2

    def Perimeter(self):
        return 2 * 22/7 * self.radius   
    
area = Circle(7)
print("Area of Circle:", area.Area()) # Output: Area of Circle: 154.0

perimeter = Circle(7)
print("Perimeter of Circle:", perimeter.Perimeter()) # Output: Perimeter of Circle: 44.0


# Question 2.
# Define an Employee class with attributes role, deparatment & salary . This class aslo has a showDetails() method.
# Define an Engineer class that inherits properties from Employeee & has additional attributes : name and age. 


class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        # print(f"Role: {self.role}, Department: {self.department}, Salary: {self.salary}")
        print("Role:", self.role)
        print("Department:", self.department)
        print("Salary:", self.salary)
    
class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "Engineering", 60000)  # Call the constructor of Employee


    def showDetails(self):
        super().showDetails()
        print(f"Name: {self.name}, Age: {self.age}")


e1 = Employee("Manager", "HR", 50000)
print("\nEmployee Details:")
e1.showDetails() # Output: Role: Manager, Department: HR, Salary: 50000

engg1 = Engineer("Alice", 30)
print("\nEngineer Details:")
# print(engg1.name) # Output: Alice
# print(engg1.age) # Output: 30
engg1.showDetails() # Output: Role: Engineer, Department: Engineering, Salary: 60000, Name: Alice, Age: 30


# Question 3.
# Create a class called Order with store item & its price.
# Use Dunder function __gt__() to convey that : order1 > order2 if price of order1 > price of order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2r):
        return self.price > odr2.price
    
odr1 = Order("Laptop", 1000)
odr2 = Order("Phone", 800)

print(odr1 > odr2)  # Output: True (1000 > 800)
print(odr2 > odr1)  # Output: False (800 > 1000)