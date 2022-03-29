import json
import requests

url = 'https://api.github.com'
user = 'Dirtybob13'

#"user_repositories_url": "https://api.github.com/users/{user}/repos{?type,page,per_page,sort}",
response = requests.get(f'{url}/users/{user}/repos')

y = 'full_name'
print('\nСписок всех доступных репозиториев')
for x in response.json():
    print(x[y])

with open('task1-1save.json', 'w') as file:
    json.dump(response.json(), file)