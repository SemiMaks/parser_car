'''
name: parser_car
author: Maksim Semizorov
email: semimaks@gmail.com
link:
github:
'''

import requests
from bs4 import BeautifulSoup

URL = 'https://auto.ru/moskovskaya_oblast/cars/volkswagen/passat/used/?year_from=2000'
HEADERS = {'user-agent': 'Mozilla/5.0 (Linux; Android 9; Unspecified Device) \\'
                         'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 \\'
                         'Chrome/71.1.2222.33 Mobile Safari/537.36', 'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):  # функция получает html
    soup = BeautifulSoup(html, 'html.parser')  # указываем тип документа html
    items = soup.find_all('a', class_='Link')

    cars = []
    for item in items:
        cars.append({
            'title': item.find('div', class_='ListingItemHeader__titleLink')
        })
    print(cars)
    print(items, '\n')


def parse():
    html = get_html(URL)
    print(html.status_code)  # если 200, то всё ОК
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')

parse()
