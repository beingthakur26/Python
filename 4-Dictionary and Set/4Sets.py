# Set:
# syntax
   # set_name = {item1, item2, item3, ...}
# A set is a collection of unique elements.
# Sets are unordered, meaning that the items have no specific order.
# Sets are mutable, meaning that you can add or remove items from a set.
# Sets are iterable, meaning that you can loop through the items in a set.
# Sets are not indexed, meaning that you cannot access items in a set by index.
# Sets are not subscriptable, meaning that you cannot use square brackets to access items in a set.
# Sets are hashable if they contain only immutable elements (e.g., numbers, strings, tuples).
# Sets are not hashable if they contain mutable elements (e.g., lists, dictionaries).
# Sets are not sliceable, meaning that you cannot use slicing to access items in a set.
# Sets are not callable, meaning that you cannot call a set like a function.
# Sets automatically remove duplicates.

collection = {1, 2, 2, 2, "hello", "world", "world", 4, 5}
print(collection)  # {1, 2, 4, 5, 'hello', 'world'}
print(type(collection))  # <class 'set'>
print(len(collection))  # 6


#Empty set :
# An empty set is created using the set() constructor.
# An empty set cannot be created using curly braces {} because that creates an empty dictionary.
# Syntax:
# empty_set = set()
collection = set() #empty set
print(type(collection))  # <class 'set'>