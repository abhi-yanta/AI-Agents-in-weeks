import requests
Response = requests.get("https://api.github.com")
print(Response)

# <Response [200]>

print(Response.status_code)


# Sometimes, you might want to use this information to make decisions in your code:

# if response.status_code == 200:
#     print("Success!")
# elif response.status_code == 404:
#     print("Not Found.")

# OR

if response:
    print("Success!")
else:
    raise Exception(f"Non-success status code: {response.status_code}")