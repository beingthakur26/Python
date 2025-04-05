class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("John")
print(s1.name)  # Output: John
del s1.name  # Deleting the name attribute of the object s1
print(s1.name)  # Raises AttributeError: 'Student' object has no attribute 'name'