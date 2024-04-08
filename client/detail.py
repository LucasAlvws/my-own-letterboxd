import requests

endpoint = "http://127.0.0.1:8000/api/film/viewset/3/"

response = requests.get(endpoint)
print(response.status_code)
print(response.json())
from IPython import embed; embed(header='detail')
