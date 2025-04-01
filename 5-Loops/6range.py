# Rane() :
# The range() function in Python is used to generate a sequence of numbers. 
# It is commonly used in loops to iterate over a specific range of values.
# Syntax :
    # range(start, stop, step)
# start (optional) → The starting number (default is 0).
# stop (required) → The number up to but not including this value.
# step (optional) → The difference between consecutive numbers (default is 1).
# Can be used with list(), tuple(), or loops.

# seq = range(5)
# for i in seq :
#     print(i)

for i in range(10) : #range(stop)
    print(i) # output : 1 to 9 print hoga (last number nhi print hota hai)

for i in range(2, 10) : # range(start, stop)
    print(i) # output : 2 to 9 

for i in range(2, 10, 2) : # range(start, stop, step)
    print(i) # output : 2, 4, 6, 8 