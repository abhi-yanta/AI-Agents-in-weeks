import csv

students = []

# with open ("data.csv") as file:
#     reader = csv.reader(file)
#     for name, home in reader:
#         students.append({"name": name, "home": home})

with open ("data.csv") as file:
    reader = csv.DictReader(file) # DictReader() define coloum title in the first line of csv file
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})


for student in sorted(students, key = lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")