# El método get se encarga de obtener recursos por parte del servidor
import requests

URL = "https://httpbin.org/get"

response = requests.get(URL)

print(response)
print(response.text)

payload = response.json('origin')

print(payload)