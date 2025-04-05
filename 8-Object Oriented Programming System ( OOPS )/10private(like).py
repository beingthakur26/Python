# Private(like) members are not accessible from outside the class, while public members are accessible.
# This is achieved by prefixing the member name with a single underscore (_).
# Private members are intended for internal use only and should not be accessed directly from outside the class.

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_n0 = acc_no
        self.__acc_pass = acc_pass # Private( __ lagna se wah private ho jata hai)

    def reset_pass(self):
        print(self.__acc_pass) # Private members are not accessible from outside the class

acc1 = Account("12345", "abcdert")

print("Account Number:", acc1.acc_n0)  # Account Number: 12345
# print("Account Password:", acc1.acc_pass)  # Account Password: abcdert   
print(acc1.reset_pass())  # Account Password: abcdert


class Person:
    __name = "John Doe"  # Private member   

    def __hello(self):
        print("Hello, ")
    def welcome(self):
        print("Welcome to the private world!")
        self.__hello()

p1 = Person()

print(p1.welcome())  # Welcome to the private world!