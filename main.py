import requests

url = "https://httpbin.org/post"

data = {
    "name": "yourname",
    "goal": "become pro"
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())