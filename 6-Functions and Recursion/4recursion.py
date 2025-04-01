# Recursion :
# Recursion is a technique where a function calls itself to solve a problem. 
# It is commonly used for problems that can be broken down into smaller subproblems of the same type.

def show(n):
    if(n == 0):
        return
    print(n)
    show(n - 1)

show(10) # 10 to 1 will be printed
