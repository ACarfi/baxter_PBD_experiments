import os
import sys
sys.path.append(os.path.abspath("../lib"))
from backup_setup import *
from file_manager import file_check

[playBackDir, dataDir, file_name] = backup_setup(sys.argv[1:])

playBackPath = playBackDir + file_name
playBackPath = file_check(playBackPath)


command_1 = 'rosrun pbd2 pbd2'

os.system('xterm -iconic -e ' + command_1 + ' & exit 1')

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