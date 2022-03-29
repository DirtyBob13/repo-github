import json
import requests

url = 'https://www.wine-searcher.com/ws-api'  #тут два необходимых параметра это api_key и winename
api_key = '4325g5g54g6343543'  # запросил key у администрации сайта ждать 48 часов, не дождался, указал рандомный, но суть ясна.
winename = 'Ferrer Bobet Seleccio Especial Vinyes Velles, Priorat DOCa, Spain' # нашел в поиске имя вина
params = {'name': winename,
          'api_key': api_key}

response = requests.get(url, params=params)
j_data = response.json()
print(j_data)

with open('task1-2save.json', 'w') as file:
    json.dump(j_data, file)