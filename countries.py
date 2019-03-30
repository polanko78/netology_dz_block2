import requests
import json
from pprint import pprint

class Country:

    def __init__(self, path):
        self.file = open(path, encoding='utf8')
        # self.params = {
        #     'action' : 'opensearch',
        #     'limit' : 1,
        #     'search' : country,
        #     'namespace' : 0
        # }

    def __iter__(self):
        return self

    def __next__(self):
        json_data = json.load(self.file)
#        for item in json_data:
        pprint(json_data)
        self.country = json_data['name']['common']
        if self.country == 'Zimbabwe':
            print('Bam!')
        params = {
            'action' : 'opensearch',
            'limit' : 1,
            'search' : self.country,
            'namespace' : 0,
            'format' : 'json'
        }
        try:
            response = requests.get('https://en.wikipedia.org/w/api.php', params = params)
        except ConnectionError:
            time.sleep(0.33)
            response = requests.get('https://en.wikipedia.org/w/api.php', params=params)
        self.res = response.json()
#            pprint(self.res)
#            pprint(self.res[3])
        return self.res[3]


if __name__ == '__main__':
    for i in Country('countries.json'):
        pprint(i)
        with open('country_link.json', 'w', encoding='utf8') as file:
            data = {self.country : i}
            json.dump(data, file, ensure_ascii=False, indent=1)



