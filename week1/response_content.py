import requests

response = requests.get("https://api.github.com")
print(response.content) # gives response content in bytes


print(type(response.content))


print(response.text) 
# gives response content in string or text

type(response.text)