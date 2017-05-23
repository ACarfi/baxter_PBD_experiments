import sys
import os
sys.path.append(os.path.abspath("../lib"))
from dir_format import *

[playBackDir, dataDir, file_name] = dir_format(sys.argv[1], sys.argv[2])

playBackPath = playBackDir + '/' + file_name

command_1 = 'rosrun baxter_interface joint_trajectory_action_server.py --mode velocity'
command_2 = 'rosrun baxter_examples joint_trajectory_file_playback.py -f ' + playBackPath
command = 'xterm -iconic -e ' + command_2 + '&' + 'xterm -iconic -e ' + command_1 + ' & exit 1'
os.system(command)

raw_input("Press Enter to terminate...")

kill_1 = 'rosnode kill /rsdk_joint_trajectory_file_playback'
kill_2 = 'rosnode kill /rsdk_velocity_joint_trajectory_action_server'

os.system(kill_1)
os.system(kill_2)

command_rest = 'rosrun baxter_tools tuck_arms.py -u'
os.system(command_rest)
