import requests 

# https://api.nasa.gov/?search=NeoWs
URL = 'https://api.nasa.gov/neo/rest/v1/neo/browse'

r = requests.get(url = URL, params = {'api_key': 'DEMO_KEY'}) 

data = r.json() 

print(data)