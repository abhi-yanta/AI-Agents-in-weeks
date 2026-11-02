# with open("names.txt") as file:
#     lines = file.readlines()

# for line in lines:
#     print("hello", line.rstrip())  # rstrip() removes the newline character

# names = []

# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())
    
# for name in sorted(names, reverse = False): # reverse = False is the default value used for sorting A to Z 
#     print(f"Hello, {name}")                    # reverse = True is used for sorting Z to A

 #OR

with open("names.txt") as file:
    for line in sorted(file):
        print("Hello,", line.rstrip())
        # this is a more efficient way to read the file
