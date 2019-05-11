from dip_block2.class_vk import VK_USER
import webbrowser
from urllib.parse import urlparse
import urllib.request
import requests


def get_user_data():
    redirect_url = 'https://oauth.vk.com/blank.html'
    app = '6971041'
    secret = 'BpbkowvhUyXAS8gTQOFE'
    display = 'popup'
    settings = 'friends, groups, status'
    user_data = input('Введите имя или id пользователя :')
    webbrowser.open(
        'http://oauth.vk.com/authorize?client_id=' + app + '&        scope=' + settings + '&redirect_uri=' + redirect_url + '&display=' + display + '&response_type=token')
    token = input('Введите token :')
    params = {
        'user_ids': user_data,
        'access_token': token,
        'v': 5.92
    }
    response = requests.get('https://api.vk.com/method/users.get', params)
    res = response.json()
    try:
        for i in res['response']:
            user_id = i['id']
#            x = False
    except KeyError:
        print('{}'.format(res['error']['error_msg']))
    return user_id, token
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

if __name__ == '__main__':
    user_id, token = get_user_data()
    user = VK_USER(token, user_id)
    response_gr = requests.get('https://api.vk.com/method/groups.get', user.params)
    r = response_gr.json()
    print(r)