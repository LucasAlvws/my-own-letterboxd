import requests

endpoint = "http://127.0.0.1:8000/api/film/viewset/"

response = requests.get(endpoint)
print(response.status_code)
print(response.json())
from IPython import embed; embed(header='list')
