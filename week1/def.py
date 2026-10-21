# def is used to define a function in python

# def hello():
#     print("Hello", name )

# name = input("What's your name? ")
# hello()


# def hello(to):
#     print("Hello", to )

# name = input("What's your name? ")
# hello(name)


# def hello(to = "World"):
#     print("Hello", to )

# hello()
# name = input("What's your name? ")
# hello(name)


# There is a problem if we define any function anywhere in the down and run program 
# with main function then we might have encounter to error for that we must have to define 
# main part of the program like def main():

def main():
    name = input("What's your name? ")
    hello(name)


def hello(to = "World"):
    print("Hello", to )

main()
  