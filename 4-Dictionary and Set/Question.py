# Question 1.
# Store following word meaning in a python dictionary
# table : "a piece of furniture", "list of facts & figures"
# cat : "a small animal"

meaning = {
    "cat": "a small animal",
    "table" : ["a piece of furniture", "list of facts & figures"]
}
print(meaning) # {'cat': 'a small animal', 'table': ['a piece of furniture', 'list of facts & figures']}
print(type(meaning))  # <class 'dict'>



# Question 2.
# you are given a list subjects for student. Assume one classroom is required for 1 subject. how many classrooms are needed by all students
# "python", "java", "c++", "python", "javascript","java", "python", "java", "c++", "c"

list_set = {"python", "java", "c++", "python", "javascript","java", "python", "java", "c++", "c"}
print(list_set) # {'java', 'c++', 'python', 'c', 'javascript'}
no_classroom = print(len(list_set)) #5



# Questuon 3.
# WAP to enter marks of 3 subjects from the user and store them in dictionary. Start with an empty dictionary & add one by one. use subject name as key & marks as value 

dic_mark = {}

x = int(input("Enter phy :"))
dic_mark.update({"phy": x})

x = int(input("Enter math :"))
dic_mark.update({"math": x})

x = int(input("Enter chem :"))
dic_mark.update({"chem": x})

print(dic_mark) 
# Enter phy :39
# Enter math :40
# Enter chem :38
# n{'phy': 39, 'math': 40, 'chem': 38}



# Question 4.
# Figure out a way tp store 9 & 9.0 as separate values in the set. ( You can take help og built-in data types)

values = {
    ("float",9.0),
    ("int",9)
}
print(values) # {('float', 9.0), ('int', 9)}
print(type(values))