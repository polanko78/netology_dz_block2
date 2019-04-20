def adv_print(data, start='\n', in_file=False, max_line = None):
    if start == '\n':
        line = data
    else:
        line = str(start) + str(data)
    if len(line) <= max_line:
        print(line)
    else:

        print(line[0:max_line])
        print(line[max_line:])
    return

adv_print('Привет', max_line=100)