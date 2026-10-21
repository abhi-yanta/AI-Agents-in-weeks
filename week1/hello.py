
# input name from user
name = input("What is your name?")

# OR

name = input("What is your name?").strip().title()

# print hello with name
#print("Hello, " + name)
print("Hello,", name) 




# .strip() removes spaces, tab and new line character from the beginning and end of the string
print(name.strip())
print(name.lstrip()) # removes spaces from the beginning of left side of the string
print(name.rstrip()) # removes spaces from the end of right side of the string

# in python different function can be chained together
print(name.strip().lower()) # converts the every character of the string to lowercase
print(name.strip().upper()) # converts the every character of the string to uppercase
print(name.strip().title()) # converts the  first letter of each word to uppercase
print(name.strip().capitalize()) # converts the first character of the string to uppercase (only for the first word)
print(name.strip().swapcase()) # converts the lowercase string to uppercase and vice versa
print(name.strip().title())

first, last = name.strip().title().split(" ")
#.split() two word string with space in btw is converted to two separate strings from the space
print("Hello,", first, last)

#f-string is a way to format strings in python 
#The f before the string lets u drop variables inside the string by using curly braces {}
print(f"Hello, {first} {last}")
