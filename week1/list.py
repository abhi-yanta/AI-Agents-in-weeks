# list: ordered, mutable, can contain duplicates

# names = []

# for _ in range(3):
#     names.append(input("Enter a name: "))

# for name in sorted(names):
#     print(f"Hello, {name}")


# open(): read, write, append
# syntax: open(filename, mode)

name = input("Enter a name: ")

# file = open("names.txt", "w")
# file.write(name)
# file.close()

# it came with an prblm that if we add more names, it will write without even leaving the space.
# this can be solved by using the newline character \n

#  OR we can write it as:

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
    file.close()
