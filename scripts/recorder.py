import sys
import os
sys.path.append(os.path.abspath("../carfi_lib"))
from dir_format import *

[playBackDir, dataDir, file_name] = dir_format(sys.argv[1:])

playBackPath = playBackDir + '/' + file_name

command_1 = 'rosrun baxter_examples joint_recorder.py -f ' + playBackPath
command_2 = 'rosrun baxter_PBD_experiments baxter_status_saver.py ' + dataDir + ' ' + file_name
command = 'xterm -iconic -e ' + command_1 + '&' + 'xterm -iconic -e ' + command_2 + ' & exit 1'
os.system(command)

raw_input("Recording, press Enter to terminate...")

kill_1 = 'rosnode kill /rsdk_joint_recorder'
kill_2 = 'rosnode kill /baxter_status_saver'

os.system(kill_1)
os.system(kill_2)
