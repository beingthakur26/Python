# Slicing in Python
# Slicing is a way to access a subset of elements from a list. You can slice a list by specifying two indices. The first index is the position of the first element you want to include in the slice, and the second index is the position of the first element you don’t want to include in the slice. The slice will include all elements from the first index up to, but not including, the second index.

# Syntax:
# list_name[start_index:end_index]

# If you don’t specify a start index, Python will start at the beginning of the list. If you don’t specify an end index, Python will go to the end of the list.
# You can also use negative indices to slice a list. When you use a negative index, Python counts from the end of the list. For example, an index of -1 refers to the last element in the list, -2 refers to the second-to-last element, and so on.
# You can also omit both the start and end indices to get a copy of the entire list.
# Let’s look at some examples of slicing a list:


marks = [84 , 89 , 90 , 45 , 67]
print(marks[:4]) # [84, 89, 90, 45]
print(marks[2:]) # [90, 45, 67]
print(marks[1:4]) # [89, 90, 45]
print(marks[-3:]) # [90, 45, 67]
print(marks[:-2]) # [84, 89, 90]
print(marks[:]) # [84, 89, 90, 45, 67]