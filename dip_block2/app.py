from dip_block2.class_vk import VK_USER
import webbrowser
from pprint import pprint
import time
from datetime import datetime
from operator import itemgetter
import requests
import random
from pymongo import MongoClient
import json


def get_user_data():
    redirect_url = 'https://oauth.vk.com/blank.html'
    app = '6971041'
    display = 'popup'
    settings = 'friends, groups, status'
    user_data = input('Введите имя или id пользователя :')
    webbrowser.open(
        'http://oauth.vk.com/authorize?client_id=' + app + '&scope=' + settings + '&redirect_uri=' + redirect_url + '&display=' + display + '&response_type=token')
    token = input('Введите token :')
    params = {
        'user_ids': user_data,
        'access_token': token,
        'fields': 'bdate, books, interests, music, movies, relation, sex',
        'v': 5.92
    }
    response = requests.get('https://api.vk.com/method/users.get', params)
    res = response.json()
    try:
        for i in res['response']:
            user_id = i['id']
            bdate = i['bdate']
            age = int(datetime.strftime(datetime.now(), "%Y")) - int(bdate[-4:])
            books = i['books']
            interests = i['interests']
            movies = i['movies']
            music = i['music']
            relation = i['relation']
            sex = i['sex']
    except KeyError:
        print('{}'.format(res['error']['error_msg']))
    return user_id, token, age, books, interests, movies, music, relation, sex

def get_friend_list(x_user):
    friend_list = []
    response_fr = requests.get('https://api.vk.com/method/friends.get', x_user.params)
    r_fr = response_fr.json()
    try:
        if r_fr['error']['error_code'] == 30:
            pass
        elif r_fr['error']['error_code'] == 6:
            time.sleep(0.3)
            response_fr = requests.get('https://api.vk.com/method/friends.get', x_user.params)
            r_fr = response_fr.json()
    except KeyError:
        pass
    try:
        for x in r_fr['response']['items']:
            friend_list.append(x)
    except KeyError:
        pass
    x_user.friend_list(friend_list)


def search(token):
    if user.sex == 1:
        s = 2,
    elif user.sex == 0:
        s = 0
    else:
        s = 1
    offset = random.randint(1, 1000)
    params = {
        'sex': s,
        'offset': offset,
        'age_from': user.age - 2,
        'age_to': user.age + 2,
        'count': 1000,
        'access_token': token,
        'fields': 'bdate, books, interests, music, movies, relation, sex',
        'v': 5.92
    }
    response = requests.get('https://api.vk.com/method/users.search', params)
    res = response.json()
    return res['response']['items']

def get_photo(list):
    big_res = []
    for x in list:
        params = {
            'owner_id': x[0],
            'album_id': 'profile',
            'extended': 1,
            'count': 1000,
            'access_token': token,
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
            my_res = {'id': x[0], 'photo': 'нет фото'}
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
    client = MongoClient()
    tindvk_db = client['tvk']
    data = tindvk_db['data']
    if tindvk_db['data']:
        data.drop()
    for item in big_res:
        data.insert_one(item)
    pprint(data.find())
#    pprint(list(data.find().sort()))

def data_analyse(data):
    for item in data:
        counter = 0
        try:
            b = item['books'].split(', ')
            for book in b:
                if book in user.books:
                    counter += 3
        except KeyError:
            pass
        try:
            m = item['music'].split(', ')
            for music in m:
                if music in user.music:
                    counter += 1
        except KeyError:
            pass
        try:
            i = item['interests'].split(', ')
            for interest in i:
                if interest in user.interests:
                    counter += 2
        except KeyError:
            pass
        try:
            age_tmp = int(datetime.strftime(datetime.now(), "%Y")) - int(item['bdate'][-4:])
        except Exception:
            pass
        else:
            if age_tmp == user.age:
                counter += 3
            elif abs(age_tmp - user.age) == 1:
                counter += 2
            elif abs(age_tmp - user.age) == 2:
                counter += 1
        user_id = item['id']
        tmp_user = VK_USER(token, user_id)
        get_friend_list(tmp_user)
        set1 = set(tmp_user.fr_list)
        set2 = set(user.fr_list)
        if set1 & set2:
            counter += 10
            print('есть общие друзья!!!!!!!!!!')
        user_count = [item['id'], counter]
        yield user_count


if __name__ == '__main__':
    list = []
    user_id, token, age, books, interests, movies, music, relation, sex = get_user_data()
    user = VK_USER(token, user_id)
    user.user_stat(age, books, interests, movies, music, relation, sex)
    get_friend_list(user)
    data = search(token)
    for item in data_analyse(data):
        list.append(item)
    itogo = sorted(list, key=itemgetter(1))
#    pprint(itogo)
    get_photo(itogo[-10:])
#    to_bd(itogo[-3:])







