# TUPLUES :
# Tuples are similar to lists, but they are immutable, meaning that the values inside a tuple cannot be changed. Also, tuples are written using parentheses, ( and ), instead of square brackets, [ and ].
# Tuples are often used to store related pieces of information. For example, a tuple might contain an x-coordinate and a y-coordinate, representing a point on a graph.
# Here is an example of a tuple:
# point = (2.0, 3.0)

tup = (2, 1, 3, 4, 5)
print(type(tup)) # <class 'tuple'>
print(tup[0]) # 2
print(tup[1]) # 1
print(tup[2]) # 3
print(tup[1:3]) # (1, 3)

tup1 = (1,)
print(type(tup1)) # <class 'tuple'>
print(tup1) # (1,)
# The comma is necessary to distinguish the tuple from the parentheses that are used for grouping in mathematical expressions.
# Without the comma, Python will interpret (1) as an integer in parentheses.
# This is why we need to put a comma after the single element 1 to make it a tuple.
