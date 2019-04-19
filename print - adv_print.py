def to_file(old_func):
    def new_fun(*args, in_file=False, **kwargs):
        data_to_write = old_func(*args, **kwargs)
        if in_file != False:
            with open('adv_prn.txt', 'w', encoding='utf-8') as file:
                for item in data_to_write:
                    file.writelines(item)
        return old_func
    return new_fun


@to_file
def adv_print(*args, start='\n', max_line=None):
    data = ''
    for n in args:
        data += (n + ' ')
    data_to_file = []
    if str(max_line).isdigit():
        if start != '\n':
            line = start + data
            start_point = 0
            end_point = max_line
            while len(line) > start_point:
                print(line[start_point:end_point])
                data_to_file.append(line[start_point:end_point] + '\n')
                start_point += max_line
                end_point += max_line
        else:
            line = data
            print(start)
            data_to_file.append(start)
            start_point = 0
            end_point = max_line
            while len(line) > start_point:
                print(line[start_point:end_point])
                data_to_file.append(line[start_point:end_point] + '\n')
                start_point += max_line
                end_point += max_line
    else:
        if start != '\n':
            line = start + data
            print(line)
            data_to_file.append(line)
        else:
            print(start)
            print(data)
            data_to_file.append(start)
            data_to_file.append(data)
    return data_to_file


#adv_print('Привет, мир!', max_line=3)
#print('___________________')
#adv_print('Привет, мир!', start='!!!!', max_line=3)
#print('___________________')
adv_print('Привет, мир!', 'buga-buga', start='!!!!', max_line=3, in_file=True)

adv_print('hello', 'buga-buga', '12312312312312')

