import requests

endpoint_func = "http://127.0.0.1:8000/api/film/viewset/5/"

response = requests.delete(endpoint_func)
print(response.status_code)
from IPython import embed; embed(header='delete')
