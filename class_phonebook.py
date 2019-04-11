from class_contact import Contact


class Phonebook:

    def __init__(self, phone_name):
        self.phone_name = phone_name
        self.contacts = {}

    def contact_def(self, name, *args, **kwargs):
        cont = Contact(name, *args, **kwargs)
        self.contacts[name] = cont

    def list_contact(self):
        for item in self.contacts.keys():
            print(self.contacts[item])

    def del_cont(self):
        name_to_del = None
        tel_del = input('Номер телефона: ')
        for item in self.contacts.keys():
            if tel_del == self.contacts[item].phnumber:
                name_to_del = item
        if not name_to_del:
            print('Нет такого номера')
            return
        self.contacts.pop(name_to_del)

    def search_favorite(self):
        for item in self.contacts.keys():
            if self.contacts[item].favorite:
                print(self.contacts[item])

    def search_name(self):
        name = input('Введите имя: ').capitalize()
        suname = input('Введите фамилию: ').capitalize()
        for item in self.contacts.keys():
            if name == self.contacts[item].name:
                if suname == self.contacts[item].surname:
                    print(self.contacts[item])
