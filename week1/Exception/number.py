# # TYPE ERROR
# x = int(input("What's x? "))
# print(f"x is {x}")

# # input = Cat
# # Solution --
# try:
#     x = int(input("What's x? "))
#     print(f"x is {x}")

# except ValueError:
#     print("x is not an integer")

# # if anyone input string or something rather than int then it shows x is not an int


# # NAME ERROR--
# try:
#     x = int(input("What's x? ")) # Error is here it can't convert input to int   

# except ValueError:
#     print("x is not an integer")

#  print(f"x is {x}")
# # input = Cat 
#  # Solution--
# try:
#     x = int(input("What's x? ")) # Error is here it can't convert input to int   

# except ValueError:
#     print("x is not an integer")

# else:
#     print(f"x is {x}")


                        # BETTER WAY

# while True:
#     try:
#         x = int(input("What's x? "))
#     except:
#         print("x is not an interger")
#     else:
#         break

# print(f"x is {x}")

                        # OR

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
    try:
        x = int(input("What's x? "))
    except:
        print("x is not an interger")
    else:
        break
    return x


main()