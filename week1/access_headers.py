import requests

response = requests.get("https://api.github.com")
response.headers
#The .headers attribute returns a dictionary-like object, 
# allowing you to access header values by key. 