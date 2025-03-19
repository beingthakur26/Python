
# Conditional statement : if, elif, else

"""
age = int(input("Enter your age: "))
if(age >=18):
    print("You are eligible to vote.")
elif(age >=18):
    print("You are not eligible to vote.")
else:
    print("Invalid age.")  
"""  
# Output:    
# Enter your age: 21
# You are eligible to vote.


# Practice problem:
A = int (input("A :"))
C = input ("M/F :")

if ((A == 1 or A == 2) and C == "M"):
    print("fee is 100")
elif (A == 3 or A == 4 or C == "F"):
    print("fee is 200") 
elif (A == 5  and C == "M"):
    print("fee is 300")      
else:
    print(" no fee ")   
# Output:
# A :5
# M/F :M
# fee is 300     

# Output: 
# A :2
# M/F :F
# fee is 200