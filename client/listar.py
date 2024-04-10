import requests

authendpoint = "http://127.0.0.1:8000/api/api-token-auth/"
responseauth = requests.post(authendpoint, data={"username":"", "password":""})
auth = responseauth.json().get('token')

print(auth)
hearders = {
    'Authorization' : f'Bearer {auth}'
}
endpoint = "http://127.0.0.1:8000/api/film/viewset/"

response = requests.get(endpoint, headers=hearders)
print(response.status_code)
print(response.json())
from IPython import embed; embed(header='list')
