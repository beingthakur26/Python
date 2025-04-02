# Question 1.
# Factorial of n natural number 

n = int(input("Enter n : "))
def fact(n):
   if(n == 1 or n == 0):
      return 1
   return fact(n-1) * n
print(fact(n))


# Question 2.
# Write a recursion function to calculate the sum of first n natural numbers.

num = int(input("Enter a number : "))
def sum(num):
   if num == 0:
       return 0
   return sum(num-1) + num
print(sum(num))


# Question 3.
# Write a recursion function to print all elements in a list . ( hint : use list & index as parameters)

def print_list(list, index = 0):
    if(index == len(list)):
        return 
    print(list[index])
    print_list(list, index + 1)

fruits = ["mango", "grape", "apple", "banana", "orange"]

print_list(fruits)