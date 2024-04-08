import requests

endpoint_func = "http://127.0.0.1:8000/api/film/viewset/2/"

data = {
    "name": "Lucas Alves o Filme A volta de quem morreu denovo e denv",
    "director_name": "Lucas Alves Segundo",
    "duration": 69696565,
    "description": "oies testasdasdasdasdasdasdasdasde",
    "film_type": "comedy",
}

response = requests.put(endpoint_func, json=data)
print(response.status_code)
print(response.json())
from IPython import embed; embed(header='put')
