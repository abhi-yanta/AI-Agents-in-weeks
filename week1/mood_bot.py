# feeling = input("How are you feeling? ")

# if feeling.lower() == "happy" :
#     print("I'm glad to hear that!")
# elif feeling.lower() == "tired":
#     print("Have a good sleep!")
# elif feeling.lower() == "stressed":
#     print("Take a deep breath and relax!")
# elif feeling.lower() == "bored":
#     print("Do something interesting!")
# else:
#     print("I'm not sure what you're feeling!")

# # if feeling.lower() == "great": # lower() is used to convert the string to lowercase
# #     print("I'm glad to hear that!")

feeling = input("How are you feeling? ")

if happy in feeling.lower():
    print("I'm glad to hear that!")
elif tired in feeling.lower():
    print("Have a good sleep!")
elif stressed in feeling.lower():
    print("Take a deep breath and relax!")
elif bored in feeling.lower():
    print("Do something interesting!")
elif sad in feeling.lower():
    print("its okay")
else:
    print("I'm not sure what you're feeling!")