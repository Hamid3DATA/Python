import requests
query_params = {"q": "norwegian forest cat"}
dog_api_endpoint = "https://api.thedogapi.com/v1/breeds"
cat_api_endpoint = "https://api.thecatapi.com/v1/breeds/search"
random_user_api_endpoint = "https://randomuser.me/api"

print(requests.get(cat_api_endpoint, params=query_params).json())
