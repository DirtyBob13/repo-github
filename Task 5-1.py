from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import exceptions
from pymongo import MongoClient
import time
import re
from pprint import pprint

login = "study.ai_172@mail.ru"
pwd = "NextPassword172#"
link = "https://account.mail.ru/login/"

options = Options()
options.add_argument("start-maximized")
s = Service('./chromedriver')
driver = webdriver.Chrome(service=s, options=options)

driver.get(link)

login1 = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.NAME, 'username')))
login1.send_keys(login)
login1.submit()

password1 = WebDriverWait(driver, 35).until(EC.visibility_of_element_located((By.NAME, 'password')))
password1.send_keys(pwd)
password1.submit()

inbox = WebDriverWait(driver, 35).until(EC.visibility_of_element_located((By.CLASS_NAME, 'nav__item_active')))
title = inbox.get_attribute('title')
regex = r"Входящие, (\d*) "
all_emails = int(re.search(regex, title).group(1))
print(f"Общее количество писем: {all_emails}")

urls = WebDriverWait(driver, 35).until(EC.visibility_of_element_located((By.CLASS_NAME, 'js-letter-list-item')))
lists = driver.find_elements(by=By.CLASS_NAME, value='js-letter-list-item')
all_url = set()

for z in lists:
    all_url.add(z.get_attribute('href'))

while len(all_url) != all_emails:
    actions = ActionChains(driver)
    actions.move_to_element(lists[-1])
    actions.perform()
    time.sleep(1)
    lists = driver.find_elements(by=By.CLASS_NAME, value='js-letter-list-item')
    for z in lists:
        all_url.add(z.get_attribute('href'))
    pprint(f"Собрано Писем: {len(all_url)}")
    if len(all_url) >= all_emails:
        break

emails = []
for x in all_url:
    try:
        driver.get(x)
        email = {}
        letters = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.CLASS_NAME, 'letter__author')))
        email['sender'] = letters.find_element(by=By.CLASS_NAME, value='letter-contact').get_attribute('title'),
        email['title'] = driver.find_element(By.XPATH, "//h2[@class='thread-subject']").text,
        email['date'] = letters.find_element(by=By.CLASS_NAME, value='letter__date').text,
        email['text'] = driver.find_element(by=By.CLASS_NAME, value='letter-body').text.replace('\n', ' ')
        emails.append(email)
        pprint(emails)
    except exceptions.InvalidArgumentException:
        pprint('Все входящие письма собраны, вся собранная информацию будет сохранена в базу данных')
        break
    except exceptions.WebDriverException:
        pprint('chrome не обнаружен или закрыт, вся собранная информацию будет сохранена в базу данных')
        break
    except exceptions.NoSuchWindowException:
        pprint('Вы прекратили сбор писем самостоятельно, вся собранная информацию будет сохранена в базу данных')
        break

client = MongoClient('127.0.0.1', 27017)
db = client['users0104']
hh = db.hh
hh.insert_many(emails)



