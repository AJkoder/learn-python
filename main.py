import requests

url = "https://httpbin.org/headers"

headers = {
    "User-Agent": "my-custom-script",
    "Authorization": "Bearer test123"
}

response = requests.get(url, headers=headers)

print(response.json())