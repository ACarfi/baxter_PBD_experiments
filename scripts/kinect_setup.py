import os
import time


workspace_src_path = os.path.abspath("../..")
print workspace_src_path
kinect_driver_command = '. ' + workspace_src_path + \
                        '/kinect_calibration/emarolab_kincect_driver/baxterisedRemoteTerminal.sh & exit 1'

print kinect_driver_command
os.system(kinect_driver_command)
time.sleep(10)
os.system('xterm -e rostopic pub -1 /tilt_angle std_msgs/Float64 -- -50')
#os.system(kinect_driver_command)
