# Question 1. 
# WAP to find the sum of first n natural numbers. (using while)

n = 5
sum = 0
i = 1
while i <= n :
    sum += i
    i += 1
print("Total sum : ", sum)



# Question 2.
# WAP to find the factorial of first n natural numbers. (using while)

n = int(input("Enter a Number :"))
fact = 1
i = 1
while i <= n :
    fact *= i 
    i += 1
print("Factorial : ", fact)



# Question 3.
# WAP to find the factorial of first n natural numbers. (using for)

n = int(input("Enter a Number :"))
fact = 1

for i in range(1, n+1) :
    fact *= i
print("Factorinal of n : ", fact)