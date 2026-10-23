# lists are ordered collections of items
# lists are mutable
# lists are indexed
# lists are iterable
# lists are dynamic
# lists are heterogeneous

# students = ["Hermione", "Harry", "Ron"]
# print(students[0])
# print(students[1])
# print(students[2])


# students = ["Hermione", "Harry", "Ron"]
# for student in students:
#     print(student) # this is a better way to print the list of students
 

 students = ["Hermione", "Harry", "Ron"]

 for i in range(len(students)):  # len(students) is the length of the list students
    print(i+1, students[i])       # len() is used to get the length of the list