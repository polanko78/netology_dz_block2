from dip_block2.class_vk import VK_USER
import webbrowser
from pprint import pprint
from datetime import datetime
from urllib.parse import urlparse
import urllib.request
import requests

# общие друзья - 2 за друга
# возраст
#


def get_user_data():
    redirect_url = 'https://oauth.vk.com/blank.html'
    app = '6971041'
    secret = 'BpbkowvhUyXAS8gTQOFE'
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
    pprint(res)
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
#            x = False
    except KeyError:
        print('{}'.format(res['error']['error_msg']))
    return user_id, token, age, books, interests, movies, music, relation, sex
#    request = urllib.request.urlopen(
#        'http://oauth.vk.com/authorize?client_id=' + app + '&        scope=' + settings + '&redirect_uri=' + redirect_url + '&display=' + display + '&response_type=token')
#    o = urlparse(request)
#    print(o.geturl())
 #   params = {
#        'client_id': '6971041',
#        'scope': settings,
#        'redirect_uri': redirect_url,
#        'display': display,
#        'response_type': 'token'
#    }
#     s = requests.Session()
#     r = s.get('http://oauth.vk.com/authorize?client_id=6971041&scope=friends, groups, status&redirect_uri=https://oauth.vk.com/blank.html&isplay=popup&response_type=token')
#     print(r.text)

def search(token):
    if user.sex == 1:
        s = 2,
    elif user.sex == 0:
        s = 0
    else:
        s = 1

    params = {
        'sex': s,
        'age_from': user.age - 2,
        'age_to': user.age + 2,
        'count': 1000,
        'access_token': token,
        'fields': 'bdate, books, interests, music, movies, relation, sex',
        'v': 5.92
    }
    response = requests.get('https://api.vk.com/method/users.search', params)
    res = response.json()
    pprint(res)
    return res['response']['items']

def data_analyse(data):

    pass



if __name__ == '__main__':
    user_id, token, age, books, interests, movies, music, relation,sex = get_user_data()
    user = VK_USER(token, user_id, age, books, interests, movies, music, relation, sex)
    data = search(token)
    for item in data_analyse(data):
        print(item)


