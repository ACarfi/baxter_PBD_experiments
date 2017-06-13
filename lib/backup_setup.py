from file_manager import dir_check
from file_manager import extension_remove
from file_manager import read_config
import sys

# This function receives the terminal inputs and matches them with the number of input required by
# the configuration file (config.txt). If the number of inputs is correct creates the file name otherwise
# returns and error. Furthermore this function checks if the PlayBack and Data folders exist in the
# path indicated by the configuration files, if not the two folder are created.


def backup_setup(terminal_input):

    config_lines = read_config()

    dir_check(config_lines[0])
    playback_dir = config_lines[0]+'PlayBack/'
    data_dir = config_lines[0]+'Data/'

    dir_check(playback_dir)
    dir_check(data_dir)

    temp = extension_remove(config_lines[1], 'txt')
    indices = [i for i, x in enumerate(temp) if x == "#"]

    if len(terminal_input) == len(indices):
        for j in range(len(terminal_input)):
            temp[indices[j]] = terminal_input[j]
    else:
        print('inserted ' + str(len(terminal_input)) + ' arguments but are required '
              + str(len(indices)) + ', shutting down ...')
        sys.exit()

    file_name = '_'.join([j for j in temp]) + '.txt'

    return [playback_dir, data_dir, file_name]
