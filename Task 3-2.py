from bs4 import BeautifulSoup as bs
import requests
import re
import json
import pandas as pd
import time
from pymongo import MongoClient
from pprint import pprint



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


for vacancy in vacancies:
    vacancies_list = []
    vacancy_data = {}
    vacancy_link = vacancy.find('a', {'class': 'bloko-link'})['href']
    vacancy_name = vacancy.find('span', {'class': 'g-user-content'}).getText()
    salary = vacancy.find('span', {'class': 'bloko-header-section-3'})
    if salary is None:
        min_salary = None
        max_salary = None
        currency = None
    else:
        salary = salary.text.replace('\u202f', '').split()
        for i in salary:
            if 'руб' in i:
                currency = 'руб'
            elif 'USD' in i:
                currency = '$'
            else:
                currency = None
        if 'от' in salary:
            min_salary = int(salary[1])
            max_salary = None
        if 'до' in salary:
            min_salary = None
            max_salary = int(salary[1])
        if 'от' not in salary:
            min_salary = int(salary[0])
            max_salary = int(salary[2])

    vacancy_data['Вакансия'] = vacancy_name
    vacancy_data['Минимальный оклад'] = min_salary
    vacancy_data['Максимальный оклад'] = max_salary
    vacancy_data['ден.ед.'] = currency
    vacancy_data['Линк'] = vacancy_link
    vacancy_data['Адрес сайта'] = base_url
    vacancies_list.append(vacancy_data)

# -1-
    for vac in vacancies_list:
        client = MongoClient('127.0.0.1', 27017)
        db = client['users0104']
        hh = db.hh
        try:
            hh.insert_one(vac)
        except DuplicateKeyError:
            print(f"Document with id = {vac['_id']} already exists")
        #pprint(vacancies_list) # для задачи №1
# -2-
        k = 30000
        for doc in hh.find({'$or': [{'Минимальный оклад': {'$gt': k}}, {'Максимальный оклад': {'$gt': k}}]}):
            pprint(doc)

