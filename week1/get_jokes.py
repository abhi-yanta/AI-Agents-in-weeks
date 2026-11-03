import requests

def get_jokes():
    r = requests.get("https://official-jaoke-api.appspot.com/random_joke", timeout = 5)
    data = r.json()
    print(data["setup"])
    print(data["punchline"])




get_jokes()