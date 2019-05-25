from pprint import pprint
from pymongo import MongoClient
import time
import requests
import json
from operator import itemgetter
from dip_block2.class_vk import Vk_User


def get_photo(list, user):
    big_res = []
    for x in list:
        params = {
            'owner_id': x[0],
            'album_id': 'profile',
            'extended': 1,
            'count': 1000,
            'access_token': user.token,
            'v': 5.92
        }
        response = requests.get('https://api.vk.com/method/photos.get', params)
        res = response.json()
        try:
            if res['error']['error_code'] == 6:
                time.sleep(0.3)
                response = requests.get('https://api.vk.com/method/photos.get', params)
                res = response.json()
        except KeyError:
            pass
        res = sort_photo(response.json())
        if res == []:
            my_res = {'id': 'https://vk.com/id' + str(x[0]), 'photo': 'нет фото'}
        else:
            photo_list = []
            for pho in res:
                photo_list.append(pho[1])
            my_res = {'id': 'https://vk.com/id' + str(x[0]), 'photo': photo_list}
        big_res.append(my_res)
#    pprint(big_res)
    to_file(big_res)
    to_bd(big_res)


def sort_photo(res):
    line = []
    list = []
    try:
        for item in res['response']['items']:
            for ph_size in item['sizes']:
                if ph_size['type'] == 'x':
                    line_tmp = [item['likes']['count'], ph_size['url']]
                elif ph_size['type'] == 'm':
                    line_tmp = [item['likes']['count'], ph_size['url']]
                elif ph_size['type'] == 's':
                    line_tmp = [item['likes']['count'], ph_size['url']]
                elif ph_size['type'] == 'o':
                    line_tmp = [item['likes']['count'], ph_size['url']]
            line.append(line_tmp)
        sorted_list = sorted(line, key=itemgetter(0))
        list = sorted_list[-3:]
    except KeyError:
        pass
    return list


def to_file(big_res):
    with open('search_result.json', 'w', encoding='utf8') as f:
        json.dump(big_res, f, ensure_ascii=False, indent=1)
    print('Готово')


def to_bd(big_res):
    global data
    client = MongoClient()
    tindvk_db = client['tvk']
    data = tindvk_db['data']
    if tindvk_db['data']:
        data.drop()
    for item in big_res:
        data.insert_one(item)
    pprint(data.find())

def show_bd():
    print('результаты')
    pprint(list(data.find()))
