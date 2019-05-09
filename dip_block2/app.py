import webbrowser
from urllib.parse import urlparse
import urllib.request
import requests


def main():
    redirect_url = 'https://oauth.vk.com/blank.html'
    app = '6971041'
    secret = 'BpbkowvhUyXAS8gTQOFE'
    display = 'popup'
    settings = 'friends, groups, status'
#    res = webbrowser.open(
 #       'http://oauth.vk.com/authorize?client_id=' + app + '&        scope=' + settings + '&redirect_uri=' + redirect_url + '&display=' + display + '&response_type=token')
#    request = urllib.request.urlopen(
#        'http://oauth.vk.com/authorize?client_id=' + app + '&        scope=' + settings + '&redirect_uri=' + redirect_url + '&display=' + display + '&response_type=token')
#    o = urlparse(request)
#    print(o.geturl())
    params = {
        'client_id': '6971041',
        'scope': settings,
        'redirect_uri': redirect_url,
        'display': display,
        'response_type': 'token'
    }
    s = requests.Session()
    r = s.get('http://oauth.vk.com/authorize?client_id=6971041&scope=friends, groups, status&redirect_uri=https://oauth.vk.com/blank.html&isplay=popup&response_type=token')
    print(r.text)

if __name__ == '__main__':
    main()