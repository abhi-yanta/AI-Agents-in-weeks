# dictionary is a collection of key-value pairs
# dictionary is unordered
# dictionary is mutable
# dictionary is indexed
# dictionary is iterable
# dictionary is dynamic
# dictionary is heterogeneous

# dictionary is data structure that allows you to--
# associate one value to the another value. something in 2 Dimensional


students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])

for student in students:
    print(student, students[student], sep=", ")