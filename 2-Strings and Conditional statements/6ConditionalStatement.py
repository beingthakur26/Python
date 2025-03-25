'''
#Conditional Statement
#Conditional statements are used to perform different actions based on different conditions.

age = int(input("Enter your age: "))
#if statement is used to check if a condition is true or false.
if age >= 18:
    print("You are an adult")
# elif is short for else if. It allows us to check for multiple expressions.
elif age >= 13:
    print("You are a teenager")    
# else statement is used to execute some statements if the condition is false.
else:
    print("You are a child")

'''

'''
# Grade students based on marks
marks = input("Enter your marks: ")
marks = int(marks)

if marks >= 90:
    print("Grade A")

elif 90 > marks >= 80:
    print ("Grade B")

elif 80 > marks >= 70:
    print("Grade c")

else:
    print("Grade D")
'''


#Nested if statement
#Nested if statements are if statements that are nested inside another if statement.
#They are used to check for multiple conditions.
age = int (input("Enter your age: "))
if(age >= 13):
    if(age < 18):
        print("You are a teenager")
    else:
        print("You are an adult")
else:
      print("Your name is Manas")