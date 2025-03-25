# Lists are mutable, which means that you can change the values of the elements in a list after the list has been created.
# list_name[index] = new_value

student = ['manas', 18, 'CSE', 9.36]
print(student[0]) # manas

student[0] = 'disha'
print(student) # ['disha', 18, 'CSE', 9.36]