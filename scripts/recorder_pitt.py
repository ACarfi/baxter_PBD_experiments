import os
import sys
import time

sys.path.append(os.path.abspath("../lib"))
from backup_setup import *
from file_manager import file_check
from shutil import copyfile


[playBackDir, dataDir, file_name] = backup_setup(sys.argv[1:])

playBackPath = playBackDir + file_name
playBackPath = file_check(playBackPath)


if os.path.isfile('../.pbd2_log.txt'):
    os.remove('../.pbd2_log.txt')


command_1 = 'rosrun pbd2 pbd2'

os.system('xterm -iconic -l -lf ../.pbd2_log.txt -e ' + command_1 + ' & exit 1')

time.sleep(1)
flag = True
while flag:
    copyfile('../.pbd2_log.txt', '../.temp_pbd2_log.txt')
    with open('../.temp_pbd2_log.txt') as f:
        for line in f:
            if len(line) > 10:
                flag = not('SHUTDOWN THE LOOP' in line)
                if not flag:
                    break
    time.sleep(0.1)

print('start the recordings')
os.remove('../.temp_pbd2_log.txt')

command_1 = 'rosrun baxter_examples joint_recorder.py -f ' + playBackPath
command_2 = 'rosrun baxter_PBD_experiments baxter_status_saver.py ' + dataDir + ' ' + file_name
command = 'xterm -iconic -e ' + command_1 + '&' + 'xterm -iconic -e ' + command_2 + ' & exit 1'

os.system(command)

raw_input("Recording, press Enter to terminate...")


kill_1 = 'rosnode kill /rsdk_joint_recorder'
kill_2 = 'rosnode kill /baxter_status_saver'
kill_3 = 'rosnode kill /pbd2'

os.system(kill_1)
os.system(kill_2)
os.system(kill_3)
