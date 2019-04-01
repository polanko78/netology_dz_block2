import hashlib


def hash_gen(path):
    data = True
    with open(path, 'rb') as file:
        while data:
            data = file.readline()
            data_hash = hashlib.md5(data).hexdigest()
            yield data_hash
    return


if __name__ == '__main__':
    p = 'DE.txt'
    for item in hash_gen(p):
        print(item)
