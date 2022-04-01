from bs4 import BeautifulSoup as bs
import requests
import re
import json
import pandas as pd
import time

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}
base_url = 'https://spb.hh.ru'
url = base_url + '/search/vacancy?clusters=true&area=2&no_magic=true&ored_clusters=true&items_on_page=100&enable_snippets=true&salary=&text=Python+junior'

response = requests.get(url, headers=headers)
html_file = ''

'''with open('response.html', 'w', encoding='utf-8') as f:
    #f.write(response.text)
with open('response.html', 'r', encoding='utf-8') as f:
    html_file = f.read()'''

dom = bs(response.text, 'html.parser')
vacancies = dom.find_all('div', {'class': 'vacancy-serp-item'})


vacancies_list = []
for vacancy in vacancies:
    vacancy_data = {}
    vacancy_link = vacancy.find('a', {'class': 'bloko-link'})['href']
    vacancy_name = vacancy.find('span', {'class': 'g-user-content'}).getText()
    salary = vacancy.find('span', {'class': 'bloko-header-section-3'})
    if not salary:
        salary_min = None
        salary_max = None
        salary_currency = None
    else:
        salary = salary.getText().replace(u'\xa0', u'')
        salaries = salary.split('-')
        for i in salaries:
            if 'руб' in i:
                salary_currency = 'руб'
            elif '$' in i:
                salary_currency = 'Бакс'
            else:
                salary_currency = None

        salaries[0] = re.sub(r'[^0-9]', '', salaries[0])
        salary_min = int(salaries[0])

        if len(salaries) > 1:
            salaries[1] = re.sub(r'[^0-9]', '', salaries[1])
            salary_max = int(salaries[1])
        else:
            salary_max = None

    vacancy_data['Вакансия'] = vacancy_name
    vacancy_data['Минимальный оклад'] = salary_min
    vacancy_data['Максимальный оклад'] = salary_max
    vacancy_data['Валюта'] = salary_currency
    vacancy_data['Линк'] = vacancy_link
    vacancy_data['Сайт'] = base_url
    vacancies_list.append(vacancy_data)

    time.sleep(1)
    next = dom.find('a', {'class': 'bloko-button'})['href']
    response = requests.get(base_url + next, headers=headers).text
    dom = bs(response, 'html.parser')


print(vacancies_list)

with open('task2-1save.json', 'w') as ht:
    json.dump(vacancies_list, ht)
pd.read_json('task2-1save.json')
