# Dictionary Method : keys(), values(), items(), get(), update(), pop(), popitem(), clear(), copy()

student = {
    "name": "John",
    "class": "XII",
    "roll_no": 12,
    "subjects" :{
        "phy" : 90,
        "maths" : 80,
        "chem" : 85,
    }
}

# 1:
# keys() : Returns a list containing the dictionary's keys
print(student.keys()) # Output: dict_keys(['name', 'class', 'roll_no', 'subjects'])
print(list(student.keys())) # Output: ['name', 'class', 'roll_no', 'subjects']
print(len(list(student.keys()))) # Output: 4

#2:
# values() : Returns a list containing the dictionary's values
print(student.values()) # Output: dict_values(['John', 'XII', 12, {'phy': 90, 'maths': 80, 'chem': 85}])
print(list(student.values())) # Output: ['John', 'XII', 12, {'phy': 90, 'maths': 80, 'chem': 85}]
print(len(list(student.values()))) # Output: 4

#3:
# items() : Returns a list containing a tuple for each key value pair
print(student.items()) # Output: dict_items([('name', 'John'), ('class', 'XII'), ('roll_no', 12), ('subjects', {'phy': 90, 'maths': 80, 'chem': 85})])
print(list(student.items())) # Output: [('name', 'John'), ('class', 'XII'), ('roll_no', 12), ('subjects', {'phy': 90, 'maths': 80, 'chem': 85})]
print(len(list(student.items()))) # Output: 4
pair = list(student.items())
print(pair[0]) # Output: ('name', 'John')

#4:
# get() : Returns the value of the specified key
print(student["name"]) # Output: John
'''print(student("name1"))''' # Output: Error
print(student.get("name")) # Output: John
print(student.get("name1")) # Output: None

#5:
# update() : Updates the dictionary with the specified key-value pairs
student.update({"name" : "Manas", "surname" : "Singh"})
print(student) # Output: {'name': 'Manas', 'class': 'XII', 'roll_no': 12, 'subjects': {'phy': 90, 'maths': 80, 'chem': 85}, 'surname': 'Singh'}

new_dic = {"city" : "Delhi"}
student.update(new_dic)
print(student)
print(list(student))

