import requests
import json
import time


class Country:

    def __init__(self, path):
        file = open(path, encoding='utf8')
        self.json_data = json.load(file)
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        number = len(self.json_data)
        if self.counter < number:
            self.country = self.json_data[self.counter]['name']['common']
            print(self.counter, self.country)
            params = {
                'action': 'opensearch',
                'limit': 1,
                'search': self.country,
                'namespace': 0,
                'format': 'json'
            }
            try:
                response = requests.get('https://en.wikipedia.org/w/api.php', params=params)
            except ConnectionError:
                time.sleep(0.33)
                response = requests.get('https://en.wikipedia.org/w/api.php', params=params)
            self.res = response.json()
            self.counter += 1
            return self.country, self.res[3]
        else:
            raise StopIteration


if __name__ == '__main__':
    data_to_file = []
    for i in Country('countries.json'):
        data = {i[0]: i[1][0]}
        data_to_file.append(data)
    with open('country_link.json', 'w', encoding='utf8') as f:
        json.dump(data_to_file, f, ensure_ascii=False, indent=1)
