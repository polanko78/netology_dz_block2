import csv
import re
from pprint import pprint
from pymongo import MongoClient



def read_data(file, netology_db):
    """
    Загрузить данные в бд из CSV-файла
    """
    data = netology_db['data']
    with open(file, encoding='utf8') as cfile:
        # прочитать файл с данными и записать в коллекцию
        reader = csv.DictReader(cfile)
        for row in reader:
            data.insert_one(row)
    res = data.find({})
    pprint(list(res))





def find_cheapest(db):
    """
    Отсортировать билеты из базы по возрастания цены
    Документация: https://docs.mongodb.com/manual/reference/method/cursor.sort/
    """


def find_by_name(name, db):
    """
    Найти билеты по имени исполнителя (в том числе – по подстроке),
    и вернуть их по возрастанию цены
    """

    regex = re.compile('укажите регулярное выражение для поиска. ' \
                       'Обратите внимание, что в строке могут быть специальные символы, их нужно экранировать')


if __name__ == '__main__':
    file = 'artists.csv'
    client = MongoClient()
    netology_db = client['ndb']
    read_data(file, netology_db)
