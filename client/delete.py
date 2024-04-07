import requests

endpoint_func = "http://127.0.0.1:8000/api/film/funcview/4/"
endpoint = "http://127.0.0.1:8000/api/film/classview/4/delete/"

response = requests.delete(endpoint)
print(response.status_code)
from IPython import embed; embed(header='delete')
