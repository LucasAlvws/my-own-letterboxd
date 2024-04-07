import requests

endpoint_func = "http://127.0.0.1:8000/api/film/funcview/3/"
endpoint = "http://127.0.0.1:8000/api/film/classview/3/update"

data = {
    "name": "Lucas Alves o Filme A volta de quem morreu ",
    "director_name": "Lucas Alves Segundo",
    "duration": 6969,
    "description": "oies teste",
    "film_type": "comedy",
}

response = requests.put(endpoint, json=data)
print(response.status_code)
print(response.json())
from IPython import embed; embed(header='put')
