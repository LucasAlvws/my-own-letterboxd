import requests

endpoint = "http://127.0.0.1:8000/api/film/viewset/"

data = {
    "name": "PinguinoRS-2",
    "director_name": "Lucas Alves",
    "duration": 1001,
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam convallis semper molestie. Morbi nec molestie turpis, ac tempus orci. Nulla rutrum lorem ipsum, eu volutpat metus gravida a.",
    "film_type": "comedy",
}

response = requests.post(endpoint, json=data)
print(response.status_code)
print(response.json())
from IPython import embed; embed(header='create')
