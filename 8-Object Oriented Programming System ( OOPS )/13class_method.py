class Person:
    name = "anonymous"

    # def changeName(self, name):
        # self.name = name
        # Person.name = name  # This will change the class variable
        # self.__class__.name = name  # This will change the class variable

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("John")
print(p1.name)  # Output: John
# print(Person.name)  # Output: anonymous
print(Person.name)  # Output: John