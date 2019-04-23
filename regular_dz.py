import re
import csv

with open("phonebook_raw.csv", encoding='utf8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


for i in contacts_list:
    if i[0] != '﻿lastname':
        phone = re.compile(
            '(\+7|8)?[\s]*[\(]*(\d\d\d)[\)]*[\s-]*(\d\d\d)[\s-]*(\d\d)[\s-]*(\d+)\s*([\(]*([а-я]*.)*\s(\d+)[\)]*)*')
        res = re.sub(phone, r'+7(\2)\3-\4-\5 \7\8', i[5])
        i[5] = res
        name_line = i[0] + i[1] + i[2]
        name = re.compile('([А-Я][а-я]*)\s*([А-Я][а-я]*)\s*([А-Я][а-я]*)*')
        name_str = re.sub(name, r'\1 ,\2 ,\3 ', name_line)
        res = re.split(' ,', name_str)
        i[0] = res[0]
        i[1] = res[1]
        i[2] = res[2]
list_to_file = []
new_line = ['﻿lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email']
tmp_list = contacts_list
for it in tmp_list:
    for t in contacts_list:
        if t[0] == it[0]:
            for x in range(1, 6):
                if (t[x] == '' or ' ') and it[x] != '' and it[x] not in new_line:
                    t[x] = it[x]
            try:
                if t[7] == '':
                    t.pop()
            except IndexError:
                pass
for l in contacts_list:
    if l not in list_to_file:
        list_to_file.append(l)

with open("phonebook.csv", "w", encoding='utf8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(list_to_file)
