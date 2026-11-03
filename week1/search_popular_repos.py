import requests

response = requests.get(
    "https://api.github.com/search/repositories",
    params={"q": "language:python", "sort": "stars", "order": "desc"},
)

json_response = response.json()
popular_repositories = json_response["items"]
for repo in popular_repositories[:3]:
    print(f"Name: {repo['name']}")
    print(f"Description: {repo['description']}")
    print(f"Stars: {repo['stargazers_count']}\n")

    # By passing a dictionary to the params parameter of get(), 
    # you’re able to modify the results that come back from the search API.

    # List of Tuples

import requests

requests.get(
    "https://api.github.com/search/repositories",
    [("q", "language:python"), ("sort", "stars"), ("order", "desc")],
)


#  values as bytes


requests.get(
    "https://api.github.com/search/repositories",
    params=b"q=language:python&sort=stars&order=desc",
)
