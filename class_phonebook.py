from class_contact import Contact


class Phonebook:

    def __init__(self, phone_name):
        self.phone_name = phone_name

    def contact_def(self, *args, **kwargs):
        return Contact(*args, **kwargs)


    def new_contact(self, *args, **kwargs):
        name = input('Введите имя: ').capitalize()
        suname = input('Введите фамилию: ').capitalize()
        phnumber = input('Введите телефон: ')
        favorite = input('Внести контакт в избранное? да/нет ')
        if favorite == 'да':
            favorite = True
        elif favorite == 'нет':
            favorite = False
        else:
            print('Вы ввели некоректно данные, наверное вы имели ввиду НЕТ')
            favorite = False
        print('Дополнительная информация: ')
        check = input('Xотите добавить email ? да/нет ')
        if check == 'да':
            email = input('Введите email: ')
            kwargs = {'email': email}
        check = input('Xотите добавить telegram ? да/нет ')
        if check == 'да':
            snet = input('Введите telegram: ')
        check = input('Xотите добавить второй номер ? да/нет ')
        if check == 'да':
            phnumber2 = input('Введите второй номер: ')

        return Contact(name, suname, phnumber, favorite, email, snet, phnumber2)


    def list_contact(self):
        for item in my_book.__dict__.keys():
            print(my_book.__dict__[item])


    def del_cont(self):
        tel_del = input('Номер телефона: ')
        for item in my_book.__dict__.keys():
            tmp = my_book.__dict__[item]
            try:
                if tel_del == tmp.phnumber:
                    name_to_del = item
            except AttributeError:
                pass
        my_book.__dict__.pop(name_to_del)


    def search_favorite(self):
        for item in my_book.__dict__.keys():
            tmp = my_book.__dict__[item]
            try:
                if tmp.favorite:
                    print(tmp)
            except AttributeError:
                pass

    def search_name(self):
        name = input('Введите имя: ').capitalize()
        suname = input('Введите фамилию: ').capitalize()
        suname.capitalize()
        for item in my_book.__dict__.keys():
            tmp = my_book.__dict__[item]
            try:
                if name == tmp.name:
                    if suname == tmp.surname:
                        print(tmp)
            except AttributeError:
                pass




my_book = Phonebook('My book')

my_book.jhon = my_book.contact_def('Jhon', 'Smith', '+71234567809', email='jhony@smith.com')
my_book.ivan = my_book.contact_def('Ivan', 'Ivanov', '+71234544444', favorite=True, phnumber2='+755598665')
my_book.bill = my_book.contact_def('Bill', 'Murrey', '+71235442398', favorite=True, phnumber2='+7565593212', email='bill@murrey.com')

my_book.list_contact()
#my_book.del_cont()
print('_-_-_-_-_-____-__-_')
#my_book.list_contact()
#my_book.search_favorite()
#my_book.search_name()
my_book.new_contact()


