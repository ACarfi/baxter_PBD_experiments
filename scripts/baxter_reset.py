import os
open_gripper = 'rostopic pub -1 /robot/end_effector/left_gripper/command baxter_core_msgs' \
               '/EndEffectorCommand' \
               ' \'{ id :  65538,  command : release, args : "{ }", sender : "foo", "sequence" : 1 }\''

close_gripper = 'rostopic pub -1 /robot/end_effector/left_gripper/command baxter_core_msgs' \
                '/EndEffectorCommand' \
                ' \'{ id :  65538,  command : grip, args : "{ }", sender : "foo", "sequence" : 1 }\''

untuck = 'rosrun custom_baxter_tools tuck_arms.py -u'

print 'reaching untuck position'
os.system('xterm -iconic -e ' + untuck)

print 'opening gripper'
os.system('xterm -iconic -e ' + open_gripper)
