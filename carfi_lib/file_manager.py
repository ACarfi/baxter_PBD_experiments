import os


def read_config():
    with open('../config.txt') as f:
        file_lines = f.read().splitlines()
        filtered_file_lines = []
        for j in range(len(file_lines)):
            if not(file_lines[j].startswith("#")) and len(file_lines[j].replace(' ', '')) != 0:
                filtered_file_lines.append(file_lines[j])
    return filtered_file_lines


def extension_remove(name, extension):
    name = name.split('_')
    name_end = name[-1]
    del name[-1]
    name_end = name_end.split(('.' + extension))
    name.append(name_end[0])
    return name


def dir_check(dir_name):
    if not(os.path.isdir(dir_name)):
        print('creating ' + dir_name)
        os.mkdir(dir_name)


def file_check(check_file_name):

    config_lines = read_config()
    name_structure = extension_remove(config_lines[1], 'txt')

    name = check_file_name.split('/')
    check_directory = name[0:-1]
    check_directory = '/'.join([j for j in check_directory])

    name = name[-1]
    name = extension_remove(name, 'txt')

    if os.path.isfile(check_file_name):
        if len(name_structure) == len(name):
            name.append('1')
        else:
            name[-1] = str(int(name[-1]) + 1)

        name = '_'.join(name)
        check_file_name = check_directory + '/' + name + '.txt'

        if os.path.isfile(check_file_name):
            check_file_name = file_check(check_file_name)

    return check_file_name
