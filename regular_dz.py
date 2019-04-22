from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding='utf8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
new_contacts_list = []
tmp_dic = {'﻿"lastname':[],
           'firstname':[],
           'surname':[],
           'organization':[],
           'position':[],
           'phone':[],
           'email':[]
           }
for i in contacts_list:
#  if i[0] == '﻿"lastname':
#    new_contacts_list.append(i)
  if i[0] != '﻿"lastname':
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
new_list = []
new_line = [12]
tmp_list = contacts_list
for i in tmp_list:
    for t in contacts_list:
            if t[0] in i:
                i.remove(t[0])
                i[0] = t[0]






        new_list.append(new_line)

#            if t[1] == '':
#                print('!')
#                t[1] = i[1]
#            if t[1] == '':
#                print('!')
#                t[2] = i[2]
#            if t[1] == '':
#                print('!')
#                t[3] = i[3]
#            if t[1] == '':
#                t[4] = i[4]
#            if t[1] == '':
#                t[5] = i[5]
#            if t[1] == '':
#                t[6] = i[6]
#        print(t)






#      for x in new_contacts_list:
#        if x[0] == i[0]:
#          if x[1] == '':
#              x[1] = i[1]
#          if x[1] == '':
#              x[2] = i[2]
#          if x[1] == '':
#              x[3] = i[3]
#          if x[1] == '':
#              x[4] = i[4]
#          if x[1] == '':
#              x[5] = i[5]
#          if x[1] == '':
#              x[6] = i[6]


pprint(new_list)



# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
#with open("phonebook.csv", "w") as f:
#  datawriter = csv.writer(f, delimiter=',')
#  # Вместо contacts_list подставьте свой список
#  datawriter.writerows(contacts_list)

#phone = re.compile('(\+7|8)?[\s]*[\(]*(\d\d\d)[\)]*[\s-]*(\d\d\d)[\s-]*(\d\d)[\s-]*(\d+)\s*([\(]*([а-я]*.)*\s(\d+)[\)]*)*')
#res = re.sub(phone, r'+7(\2)\3-\4-\5 \7\8', data)
# (\+7|8)?[\s]*[\(]*(\d\d\d)[\)]*[\s-]*(\d\d\d)[\s-]*(\d\d)[\s-]*(\d+)\s*([\(]*([а-я]*.)*\s(\d+)[\)]*)*

# +7($2)$3-$4-$5 $7$8