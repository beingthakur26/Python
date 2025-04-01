# Question 1.
# Print numbers frpm 1 to 100.

i = 1
while i <= 100 :
    print(i)
    i += 1


# Question 2.
# Print numbers from 100 to 1.

i = 100
while i >= 1 :
    print(i)
    i -= 1


# Question 3.
# Print the multiplicatuion table of a number n.

n = int(input("Enter a number :"))
i = 1
while i <= 10 :
    print(n*i)
    i += 1


# Question 4.
# Print the elements of the following list using a loop [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
index = 0  
while index < len(num) :
    # print(index)
    print(num[index])
    index += 1


# Question 5.
# Searchfor a number x in this tuple using loop :
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x =int(input("Enter a Number from given Tuple :")) 

i = 0
while i < len(num) :
    if(num[i] == x) :
        print("Found at Index :", i)
    else:
        print("finding....")
    i += 1
