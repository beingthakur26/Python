# Set Methods:

collection = set()

# 1. add()
#add() method adds an element to a set. If the element already exists, it will not be added again.
# Syntax:
   # set_name.add(item)
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(4)
collection.add(5)
collection.add("Hello")
collection.add("Manas")
collection.add("Singh")
collection.add((1, 2, 3, 4, 5))  # Adding a tuple to the set
print(collection)  # {1, 2, 3, 4, 5, 'Hello', 'Manas', 'Singh', (1, 2, 3, 4, 5)}
print(len(collection))  # 9
# Note: Sets can only contain immutable elements. You cannot add a list or dictionary to a set.


# 2. remove()
#remove() method removes an element from a set. If the element does not exist, it will raise a KeyError.
# Syntax:
   # set_name.remove(item)
collection.remove(1)
print(collection)  # {2, 3, 4, 5, 'Hello', 'Manas', 'Singh', (1, 2, 3, 4, 5)}
print(len(collection))  # 8
# Note: If you want to remove an element without raising an error if it doesn't exist, you can use discard() method.


# 3. clear()
#clear() method removes all elements from a set. The set will be empty after this method is called.
# Syntax:
   # set_name.clear()
collection.clear()
print(collection)  # set()
print(len(collection))  # 0
# Note: After calling clear(), the set will be empty, and you can add elements to it again.
# Note: The clear() method does not delete the set itself; it just removes all elements from it.


# 4. pop
#pop() method removes and returns an arbitrary element from a set. If the set is empty, it will raise a KeyError.
# Syntax:
   # item = set_name.pop()
coll = {"Manas", "Singh", 1, 2, 3, 4, 5}
print(coll)  
print(len(coll))  # 7
print(type(coll))  # <class 'set'>
print(coll.pop()) # gives random element from the set and removes it
print(coll.pop())  # Another random element from the set
print(coll)  # Remaining elements after pop
# Note: The pop() method does not remove the last element of the set. It removes an arbitrary element.
# Note: The pop() method is not guaranteed to remove the same element each time it is called, as sets are unordered collections.
# Note: If you want to remove a specific element, use the remove() or discard() method instead.
# Note: If the set is empty, the pop() method will raise a KeyError.


# 5. union()
#union() method returns a new set that contains all elements from both sets. It does not modify the original sets.
# Syntax:
   # new_set = set1.union(set2)
   # or
   # new_set = set1 | set2
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# print(set1 | set2)  # {1, 2, 3, 4, 5}
print(set1.union(set2))  # {1, 2, 3, 4, 5}
# Note: The union() method can also be used to combine multiple sets by chaining them together.
# Note: The union() method returns a new set, so the original sets remain unchanged.


# 6. intersection()
#intersection() method returns a new set that contains only the elements that are present in both sets.
# It does not modify the original sets.
# Syntax:
   # new_set = set1.intersection(set2)
   # or
   # new_set = set1 & set2
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# print(set1 & set2)  # {3}
print(set1.intersection(set2))  # {3}
# Note: The intersection() method can also be used to find the common elements between multiple sets by chaining them together.
# Note: The intersection() method returns a new set, so the original sets remain unchanged.
# Note: The intersection() method can also be used with more than two sets by chaining them together.