#requests
import requests
r=requests.get("https://jsonplaceholder.typicode.com/users/1")
data=r.json()
try:
    print("Email:",data["email"])
except:
    "Not found"
print(r.status_code)


