import json
dog_registry = {1: {"name": "Frieda"}}
dog_json = json.dumps(dog_registry)
dog_json


#'{"1": {"name": "Frieda"}}'


# DESERIALISING
# (JSON to Python file)

new_dog_registry = json.loads(dog_json)



new_dog_registry == dog_registry
# False

new_dog_registry
# {'1': {'name': 'Frieda'}}

dog_registry
# {1: {'name': 'Frieda'}}



dog_data = {
    "name": "Frieda",
    "is_dog": True,
    "hobbies": ["eating", "sleeping", "barking",],
    "age": 8,
    "address": {
        "work": None,
        "home": ("Berlin", "Germany",),
    },
}


dog_data_json = json.dumps(dog_data)
dog_data_json
#'{"name": "Frieda", "is_dog": true, "hobbies": ["eating", "sleeping", "barking"],
#"age": 8, "address": {"work": null, "home": ["Berlin", "Germany"]}}'

new_dog_data = json.loads(dog_data_json)
new_dog_data
#{'name': 'Frieda', 'is_dog': True, 'hobbies': ['eating', 'sleeping', 'barking'],
#'age': 8, 'address': {'work': None, 'home': ['Berlin', 'Germany']}}