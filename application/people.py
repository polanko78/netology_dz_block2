import json
from os import path


def get_employees():
    with open(path.join('application', 'db', 'ivanov.json')) as file:
        json_data = json.load(file)
        name = json_data['name']
        salary = json_data['salary']
    return name, salary
