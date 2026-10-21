# Match or Switch statement in python

name = input("What's your name? ")

# match name:
#     case "Harry":
#         print("Gryffindor")
#     case "Hermione":
#         print("Gryffindor")
#     case "Ron":
#         print("Gryffindor")
#     case "Draco":
#         print("Slytherin")
#     case _:                    # _ is a wildcard character that matches any other case not defined above 
#         print("Who?")          # _ this is used to match any other case not defined above 


match name: 
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?") 