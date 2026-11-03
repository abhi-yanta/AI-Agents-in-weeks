import json

with open("hello_frieda.json", encoding="utf-8") as f:
    data = json.load(f)
print(data["name"])
