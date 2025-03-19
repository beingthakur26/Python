# Type conversion
# Type conversion is the process of converting the value of one data type (integer, string, float, etc.) to another data type.

a = "2"
b = 2.45
sum = a + b # 2.0 + 2.45 = 4.45
print(sum) # it is not possible to add string and float, so it will give an error error


# Type casting 
# Type casting is the process of converting the value of one data type to another data type.

# In this example, we are converting the string to float.
a = "2"
b = 2.45
c = float(a) # 2.0 
sum = c + b # 2.0 + 2.45 = 4.45
print(sum) # 4.45

# In this example, we coverting the string and float to integer
d = int(a) # 2
e = int(b) # 2
add = d + e # 2 + 2 = 4
print(add) # 4
