from class_phonebook import Phonebook
from class_contact import Contact


def menu():
    print('Приветсвуем Вас в записной книге {}'.format(my_book.__dict__['phone_name']))
    print('Доступны следующие опции' + '\n'
          'Нажмите 1 для вывода контактов' + '\n'
          'Нажмите 2 для добавления нового контакта' + '\n'
          'Нажмите 3 для удаления контакта' + '\n'
          'Нажмите 4 для для поиска избранных' + '\n'
          'Нажмите 5 для поиска по имени и фамилии'
          )
    while True:
        x = input()
        if int(x) == 1:
            my_book.list_contact()
        elif int(x) == 2:
            data_for_new_user()
        elif int(x) == 3:
            my_book.del_cont()
        elif int(x) == 4:
            my_book.search_favorite()
        elif int(x) == 5:
            my_book.search_name()
        else:
            print('Вы ввели неверную команду')


def start():
    global counter
    print('Заводим трех пользователей по-умолчанию')
    cont = Contact('Jhon', 'Smith', '+71234567809', email='jhony@smith.com')
    counter += 1
    my_book.contact_def(counter, cont)
    cont = Contact('Ivan', 'Ivanov', '+71234544444', favorite=True, phnumber2='+755598665')
    counter += 1
    my_book.contact_def(counter, cont)
    cont = Contact('Bill', 'Murrey', '+71235442398', favorite=True, phnumber2='+7565593212',
                        email='bill@murrey.com')
    counter += 1
    my_book.contact_def(counter, cont)
    print('Готово')


def data_for_new_user():
    global counter
    counter += 1
    kwargs = {}
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
        kwargs['snet'] = snet
    check = input('Xотите добавить второй номер ? да/нет ')
    if check == 'да':
        phnumber2 = input('Введите второй номер: ')
        kwargs['phnumber2'] = phnumber2
    args = (suname, phnumber, favorite)
    cont = Contact(name, *args, **kwargs)
    return my_book.contact_def(counter, cont)


if __name__ == '__main__':
    counter = 0
    book_name = input('Введите название вашей телефонной книги :')
    my_book = Phonebook(book_name)
    start()
    menu()
