# Nested Dictionary :
# A dictionary can also contain many dictionaries, this is called nested dictionary.
# Example:

student = {
    "name": "John",
    "class": "XII",
    "roll_no": 12,
    "subjects": {
        "subject1": "Maths",
        "subject2": "Physics",
        "subject3": "Chemistry",
    },
    "marks": {
        "Maths": 90,
        "Physics": 80,
        "Chemistry": 85,
    }
}
print(student["subjects"]) # Output: {'subject1': 'Maths', 'subject2': 'Physics', 'subject3': 'Chemistry'}
print(student["marks"]) # Output: {'Maths': 90, 'Physics': 80, 'Chemistry': 85}
print(student["subjects"]["subject1"]) # Output: Maths