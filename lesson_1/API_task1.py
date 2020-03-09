import requests
import getpass
from pprint import pprint
import json
#Первое задание!
url = 'https://api.github.com'
user='antonbelovalex'

r = requests.get(f'{url}/users/{user}/repos')
with open('data.json', 'w') as f:
    json.dump(r.json(), f)

for i in r.json():
    print(i['name'])


