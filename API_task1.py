import requests
import getpass
from pprint import pprint
import json
main_link = 'https://api.github.com/user/repos' #Ссылка на репозитории

username = input('Введите имя вашего пользователя!') #Запрос имени пользователя.
password = getpass.getpass()  #Запрос пароля пользователя.

r = requests.get(main_link, auth=(username, password))
data = json.loads(r.text) #Получение данных о репозиториях пользователя.
# pprint(data)

#Вывод ссылок публичных репозиториев пользователя.
for repo in data:
    if not repo['private']:
        print(repo['html_url'])