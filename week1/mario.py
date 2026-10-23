# def main():
#     print_column(3)

# # def print_column(height):
# #     for _ in range(height):
# #         print("#")


# def print_column(height):
#     print("#\n" * height, end="")
    

# main()

# print("================================================")

# def main():
#     print_row(4)

# def print_row(width):
#     print("?" * width)

# main()

print("================================================")

print("SQUARE BLOCK MADE WITH #")

# def print_square(size):

#     # For each row in square
#     for i in range(size):

#         # For each brick in row
#         for j in range(size):

#             # Print brick
#             print("#", end="")
        
#         # Print new line
#         print()

# main()


# OR 

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print row(size)

def print_row(width):
    print("#" * width)

main()
