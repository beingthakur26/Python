# For Loop :
# A for loop in Python is used to iterate over a sequence (such as a list, tuple, dictionary, string, or range). 
# It allows you to execute a block of code multiple times.
# Syntax :
    #for variable in sequence:
        # Code to execute

list = [1, 2, 3, 4, 5]

for val in list :
    if(val == 3):
        print("3 found")
        break
    print(val)
print("END")