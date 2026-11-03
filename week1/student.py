# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append({"name": name, "house": house})


# for student in students:
#     print(f"{student['name']} is in {student['house']}")


# Using dictionary comprehension

import csv
students = []

with open("student.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

# def get_name(student):
#     return student["name"]

# for student in sorted(students, key = get_name):
#     print(f"{student['name']} is in {student['house']}")

                  # OR

# def get_house(student):
#     return student["house"]

# for student in sorted(students, key = get_house, reverse = True):
#     print(f"{student['name']} is in {student['house']}")

                  #OTHERWISE

for student in sorted(students, key = lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
