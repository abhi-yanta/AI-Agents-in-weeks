#print(int(input("What's x? ")) + int(input("What's y? ")))

# x = float(input("What's x? "))
# y = float(input("What's y? "))
# z = round(x + y) # it let u round the number to the nearest integer
# print(f"{z}") # it print the number as it is
# print(f"{z:.2f}") # it print the number with 2 decimal places
# print(f"{z:,}") # it print the number with comma separator


# a = round(x + y, 2) # it let u round the number to the nearest 2 decimal places
# print(z)


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    #return n*n
    #return n ** 2
    return pow(n, 2)

main()