# Question 1.
# Print the elements of the following list using a loop :
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for val in num :
    print(val)


# Quesion 2.
# Search for a number x in the tuple using loop :
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = int(input("Enter a number from given tuple :"))

index = 0
for el in num :
    if(el == x ):
        print("Number found at Index :", index)
    index += 1