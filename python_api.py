import requests
import json

response = requests.get('https://api.chucknorris.io/jokes/random')
print(response.text)

jokes = []
for i in range(10):
    response = requests.get('https://api.chucknorris.io/jokes/random')
    data = response.json()['value']
    jokes.append(data)
print(jokes)

#will run <Response [200]>
# 200 = Suceess
# 300 = redirect
# 400 = error\ not available
# 404 = not found
