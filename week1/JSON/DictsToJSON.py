import json  #json is a module that allows you to convert Python dictionaries to JSON strings
food_ratings = {"organic dog food": 2, "human food": 10} #dictionary
print(json.dumps(food_ratings) )# to convert the dictionary to a JSON string


# output:
#'{"organic dog food": 2, "human food": 10}'


# When Dict doesnt contain string key
# OR they cant directly translated to JSON

numbers_present = {1: True, 2: True, 3: False}
json.dumps(numbers_present)


# Output: '{"1": true, "2": true, "3": false}'

# When you convert a dictionary to JSON, 
# the dictionary keys will always be strings in JSON.


dog_id = 1
dog_name = "Frieda"
dog_registry = {dog_id: {"name": dog_name}}
json.dumps(dog_registry)


# '{"1": {"name": "Frieda"}}'


>>> json.dumps(True)
 # 'true'

>>> json.dumps(["eating", "sleeping", "barking"])
 # '["eating", "sleeping", "barking"]'

