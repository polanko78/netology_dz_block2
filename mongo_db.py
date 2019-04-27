import csv
import re
from pprint import pprint
from pymongo import MongoClient
from datetime import datetime


def read_data(file, data):
    """
    Загрузить данные в бд из CSV-файла
    """
    with open(file, encoding='utf8') as cfile:
        # прочитать файл с данными и записать в коллекцию
        reader = csv.DictReader(cfile)
        for row in reader:
            data.insert_one({'Дата': datetime.strptime(row['Дата'] +
                             '.2017', '%d.%m.%Y'), 'Исполнитель': row['Исполнитель'],
                             'Место': row['Место'], 'Цена': int(row['Цена'])})


def find_cheapest(data):
    """
    Отсортировать билеты из базы по возрастания цены
    Документация: https://docs.mongodb.com/manual/reference/method/cursor.sort/
    """
    pprint(list(data.find().sort('Цена', 1)))


def find_by_name(name, data):
    """
    Найти билеты по имени исполнителя (в том числе – по подстроке),
    и вернуть их по возрастанию цены
    """
    regex = re.compile('\s*(\D+)*(\d+)*\s*\-*\s*(\D+)*(\d+)*\s*' + name
                       + '\s*(\D+)*(\d+)*\s*\-*\s*(\D+)*(\d+)*\s*(\D+)*(\d+)*\s*\-*\s*(\D+)*(\d+)*')
    for item in list(data.find().sort('Цена', 1)):
        if re.match(regex, item['Исполнитель']):
            print(item)


def find_by_date(date1, date2, data):
    for item in list(data.find()):
        if datetime.strptime(date1 + '.2017', '%d.%m.%Y') <= item['Дата'] \
                <= datetime.strptime(date2 + '.2017', '%d.%m.%Y'):
            print(item)


def menu():
    while True:
        command = input('''
            1. Сортировка по стоймости билетов
            2. Поиск по имени испольнителя
            3. Поиск по дате
            ''')
        if command == '1':
            find_cheapest(data)
            pass
        elif command == '2':
            name = input('Введите имя для поиска: ')
            find_by_name(name, data)
            pass
        elif command == '3':
            print('Поиск по дате')
            d1 = input('Введите c какой даты ищем (формат: день месяц): ')
            d2 = input('По какую дату ищем (формат: день месяц): ')
            regex = re.compile('(\d{2}).*(\d{2})')
            date1 = re.sub(regex, r'\1.\2', d1)
            date2 = re.sub(regex, r'\1.\2', d2)
            find_by_date(date1, date2, data)
            pass
        else:
            print('Не верная команда')
            pass


if __name__ == '__main__':
    file = 'artists.csv'
    client = MongoClient()
    netology_db = client['ndb']
    data = netology_db['data']
    data.drop()
    read_data(file, data)
    menu()
