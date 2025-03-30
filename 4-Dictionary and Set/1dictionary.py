# Dictionary :
# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
# Example:
# Create and print a dictionary:

info = {
    "name" : "manas",
    "subject" : "python",
    "learning" : "python",
    "age" : 20,
    "adult" : True,
    "mark" : 90.5,
    "topics" : ("dict", "set"),
}
print(info) # Output: {'name': 'manas', 'subject': 'python', 'learning': 'python', 'age': 20, 'adult': True, 'mark': 90.5, 'topics': ('dict', 'set')}
print(type(info)) # Output: <class 'dict'>

# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:

print(info["name"]) # Output: manas
print(info["age"]) # Output: 20
print(info["mark"]) # Output: 90.5
print(info["topics"]) # Output: ('dict', 'set')

# Change Values
# You can change the value of a specific item by referring to its key name:

info["name"] = "Manas Singh" 
info["surname"] = "Singh" 
print(info)