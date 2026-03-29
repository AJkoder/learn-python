import requests
import csv

username = input("Enter username: ")

url = f"https://api.github.com/users/{username}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # TXT FILE
    with open("report.txt", "w") as f:
        f.write("\n--- GitHub Profile Report ---\n")
        f.write(f"Username       : {data['login']}\n")
        f.write(f"Public Repos   : {data['public_repos']}\n")
        f.write(f"Followers      : {data['followers']}\n")
        f.write("------------------------------\n")

    # CSV FILE
    with open("report.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Username", "Public Repos", "Followers"])
        writer.writerow([data["login"], data["public_repos"], data["followers"]])

    print("Report generated successfully!")

else:
    print("User not found!")