# LIST METHODS : append(), insert(), remove(), pop(), clear(), index(), count(), sort(), reverse(), copy()

# 1 :- append() method
# The append() method adds an element to the end of a list.
# Syntax:
    # list_name.append(element)
# The append() method modifies the original list. It doesn’t return a new list.

list = [1, 2, 3, 4, 5]
list.append(6) # [1, 2, 3, 4, 5, 6]
print(list) # [1, 2, 3, 4, 5, 6]


# 2 :- sort() method
# The sort() method sorts the elements of a list in ascending order.
# Syntax:
    # list_name.sort()
# The sort() method modifies the original list. It doesn’t return a new list.

list = [5, 2, 3, 1, 4]
list.sort() # [1, 2, 3, 4, 5]
print(list) # [1, 2, 3, 4, 5]


# 3 :- sort(reverse = True) method
# The sort(reverse = True) method sorts the elements of a list in descending order.
# Syntax:
    # list_name.sort(reverse = True)
# The sort(reverse = True) method modifies the original list. It doesn’t return a new list.

list = [5, 2, 3, 1, 4]
list.sort(reverse = True) # [5, 4, 3, 2, 1]
print(list) # [5, 4, 3, 2, 1]


# 4 :- reverse() method
# The reverse() method reverses the elements of a list.
# Syntax:
    # list_name.reverse()
# The reverse() method modifies the original list. It doesn’t return a new list.

list = [1, 2, 3, 4, 5]
list.reverse() # [5, 4, 3, 2, 1]
print(list) # [5, 4, 3, 2, 1]


# 5 :- insert() method
# The insert() method adds an element at a specified index in a list.
# Syntax:
    # list_name.insert(index, element)
# The insert() method modifies the original list. It doesn’t return a new list.

list = [1, 2, 3, 4, 5]
list.insert(2, 6) # [1, 2, 6, 3, 4, 5]
print(list) # [1, 2, 6, 3, 4, 5]


# 6 :- remove() method
# The remove() method removes the first occurrence of a specified element from a list.
# Syntax:
    # list_name.remove(element)
# The remove() method modifies the original list. It doesn’t return a new list.

list = [1, 2, 3, 4, 5]
list.remove(3) # [1, 2, 4, 5]
print(list) # [1, 2, 4, 5]


# 7 :- pop() method
# The pop() method removes the element at a specified index from a list and returns the removed element.
# Syntax:
    # list_name.pop(index)
# The pop() method modifies the original list.

list = [1, 2, 3, 4, 5]
element = list.pop(2) 
print(list) # [1, 2, 4, 5]
print(element) # 3

