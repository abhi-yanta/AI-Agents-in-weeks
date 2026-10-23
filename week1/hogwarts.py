# What we have done here is we have created a list of dictionaries
# each dictionary contains the name, house, and patronus of a student
# we have then printed the name, house, and patronus of each student

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}, # None is used to represent a null value
]                                                              # None is a built-in constant in Python

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ") 







