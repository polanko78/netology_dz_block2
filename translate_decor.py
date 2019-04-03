import requests
# import json
import time


def logger(old_func):
    def newfun(*args, **kwargs):
        start = time.asctime()
        res = old_func(*args, **kwargs)
        t = str(args)
        with open('my_log.log', 'a', encoding='utf-8') as file:
            line = [start, '  функция: ', old_func.__name__, '\n']
            line2 = ['аргументы: ', t, '\n']
            line3 = ['результат: ', str(res), '\n']
            file.writelines(line)
            file.writelines(line2)
            file.writelines(line3)
            file.writelines('\n')
        return old_func(*args, **kwargs)
    return newfun


@logger
def translate_it(my_text, from_lang, to_lang='ru'):
    params = {
        'key': API_KEY,
        'text': my_text,
        'lang': '{}-{}'.format(from_lang, to_lang),
    }
    response = requests.get(URL, params=params)
    json_ = response.json()
    return json_['text']


def file_send_and_write(x):
    with open(x + '.txt', encoding='UTF-8') as file:
        my_text = file.read()
    param = {
        'key': API_KEY,
        'text': my_text
    }
    res = requests.post('https://translate.yandex.net/api/v1.5/tr.json/detect', params=param)
    resj = res.json()
    new_text = translate_it(my_text, resj['lang'])
    with open(x + '-ru.txt', 'w', encoding='UTF-8') as nfile:
        nfile.write(new_text[0])


if __name__ == '__main__':
    API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    list_of_texts = ['de', 'es', 'fr']
    for x in list_of_texts:
        file_send_and_write(x)
