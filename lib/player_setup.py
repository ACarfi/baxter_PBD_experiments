import fnmatch
import os
import sys
from file_manager import read_config
from file_manager import extension_remove

# This function receives as input the terminal inputs and matches them with the number of input required by
# the configuration file (config.txt). If the number of inputs is correct creates the file name otherwise
# returns and error. Once the name of the file to be played the function checks if exist different versions
# of the same function, differentiate by a number located at the end of the file name. If this is the case
# all the alternatives are displayed and the user is required to select one version. The name of the selected
# file is returned as output.


def player_setup(terminal_input):
    config_lines = read_config()

    playback_dir = config_lines[0] + 'PlayBack/'

    temp = extension_remove(config_lines[1], 'txt')
    indices = [i for i, x in enumerate(temp) if x == "#"]

    if len(terminal_input) == len(indices):
        for j in range(len(terminal_input)):
            temp[indices[j]] = terminal_input[j]
    else:
        print('inserted ' + str(len(terminal_input)) + ' arguments but are required '
              + str(len(indices)) + ', shutting down ...')
        sys.exit()

    file_name = '_'.join([j for j in temp]) + '*'

    possible_files = []
    ids = 1
    for files in os.listdir(playback_dir):
        if fnmatch.fnmatch(files, file_name):
            possible_files.append(files)
            print(str(ids) + ': ' + files)
            ids += 1

    key_input = raw_input("These are the possible files to be played press the corresponding id: ")

    print 'It is going to be reproduced: ' + possible_files[int(key_input)-1]
    playback_file = playback_dir + possible_files[int(key_input)-1]

    return [playback_file]
