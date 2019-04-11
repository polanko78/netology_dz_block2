def to_file(old_func):
    def new_fun(data, *args, **kwargs):
        data_to_write = old_func(data, *args, **kwargs)
        if kwargs['in_file'] != False:
            with open('adv_prn.txt', 'w', encoding='utf-8') as file:
                for item in data_to_write:
                    file.writelines(item)
        return old_func
    return new_fun


@to_file
def adv_print(data, start='\n', max_line=None, in_file=False):
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
    return data_to_file

#adv_print('Привет, мир!', max_line=3)
#adv_print('Привет, мир!', start='!!!!', max_line=3)
adv_print('Привет, мир!', start='!!!!', max_line=3, in_file=True)