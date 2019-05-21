from dip_block2.class_vk import VK_USER
from dip_block2.photo_file_work import *
import webbrowser
import time
from datetime import datetime
from operator import itemgetter
import requests
import random


def get_user_data():
    global token
    redirect_url = 'https://oauth.vk.com/blank.html'
    app = '6971041'
    display = 'popup'
    settings = 'friends, groups, status'
    user_data = input('Введите имя или id пользователя :')
    webbrowser.open(
        'http://oauth.vk.com/authorize?client_id=' + app + '&scope=' + settings + '&redirect_uri=' \
        + redirect_url + '&display=' + display + '&response_type=token'
    )
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


def search(user):
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
        'access_token': user.token,
        'fields': 'bdate, books, interests, music, movies, relation, sex',
        'v': 5.92
    }
    response = requests.get('https://api.vk.com/method/users.search', params)
    res = response.json()
    pprint(res)
    return res['response']['items']


def data_analyse(data, user):
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


def menu():
    while True:
        print('___VKinder___')
        command = input('''
                    1. Ввод VK id или имени
                    2. Вывод результатов из БД
                    ''')
        if command == '1':
            list = []
            user_id, token, age, books, interests, movies, music, relation, sex = get_user_data()
            user = VK_USER(token, user_id)
            user.user_stat(age, books, interests, movies, music, relation, sex)
            get_friend_list(user)
            data = search(user)
            for item in data_analyse(data, user):
                list.append(item)
            itogo = sorted(list, key=itemgetter(1))
            get_photo(itogo[-10:], user)
        elif command == '2':
            show_bd()


if __name__ == '__main__':
    menu()
