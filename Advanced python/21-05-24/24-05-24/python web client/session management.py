import requests

url = 'https://jsonplaceholder.typicode.com/posts'

session = requests.Session()

# make the 1st request
response = session.get(url)
# print(response.json())

import json
print(json.dumps(response.json(), indent=4))

# make the 2nd request
response = session.post(url, json={'title':'new post', 'body':'content'})
print("=====================================================================")
print(response.json())

# close the session
session.close()