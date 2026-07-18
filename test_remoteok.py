import requests

url = "https://remoteok.com/api"

response = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=20
)

print("Status Code:", response.status_code)

data = response.json()

print("Total Records:", len(data))

print("\nFirst Job\n")

print("Company :", data[1]["company"])
print("Position:", data[1]["position"])
print("Location:", data[1]["location"])