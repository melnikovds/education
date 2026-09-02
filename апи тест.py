import requests

url = "https://api.shop.dev/items"

r = requests.get(url)
print(r.status_code)

for item in r.json():
    print(item['name'], item['price'])

