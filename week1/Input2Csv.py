import csv

name = input("What's your name?")
home = input("What's your home?")

with open("csv_Input.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames = ["name", "home"])
    writer.writerow({"name": name, "home": home})

# DictWriter ---
# It denotes which coloumn contains which data
