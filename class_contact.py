
class Contact:

    def __init__(self, name, surname, phnumber, favorite=False, *args, **kwargs):
        self.name = name
        self.surname = surname
        self.phnumber = phnumber
        self.favorite = favorite
        try:
            self.email = kwargs['email']
        except KeyError:
            pass
        try:
            self.snet = kwargs['telegram']
        except KeyError:
            pass
        try:
            self.phnumber2 = kwargs['phnumber2']
        except KeyError:
            pass

    def __str__(self):
        data = ['Имя:    ' + self.name + '\n' + 'Фамилия:    ' + self.surname + '\n'
                + 'Телефон:  ' + self.phnumber + '\n' + 'В избранных:    ' + str(self.favorite) + '\n'
                + 'Дополнительная информация:' + '\n']
        try:
            data_tmp = ['      email :' + self.email + '\n']
            data[0] += data_tmp[0]
        except AttributeError:
            pass
        try:
            data_tmp = ['      telegram :' + self.snet + '\n']
            data[0] += data_tmp[0]
        except AttributeError:
            pass
        try:
            data_tmp = ['      доп.телефон :' + self.phnumber2 + '\n']
            data[0] += data_tmp[0]
        except AttributeError:
            pass
        return data[0]


#if __name__ == '__main__':

#    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com', phnumber2='+755598665')
#    print(jhon)
