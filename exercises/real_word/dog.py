import requests

# https://www.learnpython.dev/02-introduction-to-python/190-apis/
api_url = "http://shibe.online/api/shibes?count=1"

params = {"count": 10}
response = requests.get(api_url, params=params)

status_code = response.status_code
print("status_code: ", status_code)

response_json = response.json()

print(response_json)
