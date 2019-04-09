import hashlib
import time


def logger(old_func):
    def newfun(*args, **kwargs):
        s = []
        start = time.asctime()
        res = old_func(*args, **kwargs)
        print(dir(res))
        t = res.__
        print(t)
        with open('my_log.log', 'a', encoding='utf-8') as file:
            line = [start, '  fun: ', old_func.__name__, '   arg: ', '\n']
            file.writelines(line)
        return old_func(*args, **kwargs)
    return newfun


@logger
def hash_gen(path):
    data = True
    with open(path, 'rb') as file:
        while data:
            data = file.readline()
            data_hash = hashlib.md5(data).hexdigest()
            yield data_hash


if __name__ == '__main__':
    p = 'DE.txt'
    res = []
    for item in hash_gen(p):
        t = item
        res.append(t)
    print(res)
