import requests

city = input()
url = f'https://wttr.in/{city}'
res = requests.get(url)
print(res.text)
