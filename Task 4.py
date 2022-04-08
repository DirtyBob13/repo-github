from lxml import html
import requests
from pprint import pprint
import json
import pandas as pd
from pymongo import MongoClient

url = 'https://yandex.ru/news'
header = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'}


response = requests.get(url, headers=header)
dom = html.fromstring(response.text)
names = dom.xpath("//div[contains(@class, 'mg-grid__row mg-grid__row_gap_8 news-top-flexible-stories news-app__top')]")

yandex_News = []
all_news = []
all_names_list = []
for name in names:
    names_list = {}
    title = name.xpath(".//h2[contains(@class ,'mg-card__title')]//text()")
    link = name.xpath(".//a[contains(@class,'mg-card__source-link')]/@href")
    source = name.xpath(".//a[contains(@class,'mg-card__source-link')]/text()")
    time = name.xpath(".//span[contains(@class,'mg-card-source__time')]/text()")

    names_list['title'] = title
    names_list['source'] = source
    names_list['link'] = link
    names_list['time'] = time
    all_names_list.append(names_list)

    for vac in all_names_list:
        client = MongoClient('127.0.0.1', 27017)
        db = client['users0104']
        yandex = db.yandex
        yandex.insert_one(vac)

pprint(all_names_list)


with open('task4-1save.json', 'w') as ht:
    json.dump(all_names_list, ht)
pd.read_json('task4-1save.json')

