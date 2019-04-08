from class_contact import Contact


class Phonebook:

    def __init__(self, phone_name):
        self.phone_name = phone_name

    def new_contact(self, x, *args, **kwargs):

        x = Contact(*args, **kwargs)
        print(x)
        return x



my_book = Phonebook('My book')
print(dir(my_book))
print(my_book.__dict__)
#jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com', phnumber2='+755598665')
my_book.new_contact('jhon', 'Jhon', 'Smith', '+71234567809')

my_book.new_contact('ivan', 'Ivan', 'Ivanov', '+71234544444')
