#!/usr/bin/env python
import rospy
import os
import sys
sys.path.append(os.path.abspath("../carfi_lib"))

from exist_check import *
from baxter_interface import Limb
from baxter_interface import Gripper


def time_stamp(start_time):
    return rospy.get_time() - start_time


def main():
    rospy.init_node('baxter_status_saver')

    start_time = rospy.get_time()

    file_dir = str(sys.argv[1])
    file_name = str(sys.argv[2])

    dir_1 = file_dir + '/' + 'Baxter_Joints_Position'
    dir_2 = file_dir + '/' + 'Baxter_Joints_Torque'
    dir_3 = file_dir + '/' + 'Baxter_Gripper_Pose'
    dir_4 = file_dir + '/' + 'Baxter_Gripper_Velocity'

    file_1 = dir_1 + '/' + file_name
    file_2 = dir_2 + '/' + file_name
    file_3 = dir_3 + '/' + file_name
    file_4 = dir_4 + '/' + file_name

    dir_check(dir_1)
    dir_check(dir_2)
    dir_check(dir_3)
    dir_check(dir_4)

    file_1 = file_check(file_1)
    file_2 = file_check(file_2)
    file_3 = file_check(file_3)
    file_4 = file_check(file_4)

    right_arm = Limb('right')
    left_arm = Limb('left')

    right_gripper = Gripper('right')
    left_gripper = Gripper('left')

    joints_left = left_arm.joint_names()
    joints_right = right_arm.joint_names()

    rate = rospy.Rate(10)

    with open(file_1, 'w') as f1, open(file_2, 'w') as f2, \
            open(file_3, 'w') as f3, open(file_4, 'w') as f4:

        f1.write('time,')
        f2.write('time,')
        f3.write('time,')
        f4.write('time,')

        f1.write(','.join([j for j in joints_left]) + ',')
        f1.write('left_gripper,')
        f1.write(','.join([j for j in joints_right]) + ',')
        f1.write('right_gripper\n')

        f2.write(','.join([j for j in joints_left]) + ',')
        f2.write(','.join([j for j in joints_right]) + '\n')

        f3.write('left_point_x,left_point_y,left_point_z,left_orientation_x,left_orientation_y'
                 ',left_orientation_z,left_orientation_w,')
        f3.write('right_point_x,right_point_y,right_point_z,right_orientation_x,right_orientation_y'
                 ',right_orientation_z,right_orientation_w\n')

        f4.write('left_lin_x,left_lin_y,left_lin_z,left_ang_x,left_ang_y,left_ang_z,')
        f4.write('right_lin_x,right_lin_y,right_lin_z,right_ang_x,right_ang_y,right_ang_z\n')

        while not rospy.is_shutdown():
            angles_left = [left_arm.joint_angle(j) for j in joints_left]
            angles_right = [right_arm.joint_angle(j) for j in joints_right]

            effort_left = [left_arm.joint_effort(j) for j in joints_left]
            effort_right = [right_arm.joint_effort(j) for j in joints_right]

            left_vel = left_arm.endpoint_velocity()
            left_linear_vel = left_vel['linear']
            left_angular_vel = left_vel['angular']

            right_vel = right_arm.endpoint_velocity()
            right_linear_vel = right_vel['linear']
            right_angular_vel = right_vel['angular']

            left_pose = left_arm.endpoint_pose()
            left_pose_p = left_pose['position']
            left_pose_o = left_pose['orientation']

            right_pose = right_arm.endpoint_pose()
            right_pose_p = right_pose['position']
            right_pose_o = right_pose['orientation']

            f1.write("%f," % (time_stamp(start_time),))
            f2.write("%f," % (time_stamp(start_time),))
            f3.write("%f," % (time_stamp(start_time),))
            f4.write("%f," % (time_stamp(start_time),))

            f1.write(','.join([str(x) for x in angles_left]) + ',')
            f1.write(str(left_gripper.position()) + ',')
            f1.write(','.join([str(x) for x in angles_right]) + ',')
            f1.write(str(right_gripper.position()) + '\n')

            f2.write(','.join([str(x) for x in effort_left]) + ',')
            f2.write(','.join([str(x) for x in effort_right]) + '\n')

            f3.write(','.join([str(x) for x in left_pose_p]) + ',')
            f3.write(','.join([str(x) for x in left_pose_o]) + ',')
            f3.write(','.join([str(x) for x in right_pose_p]) + ',')
            f3.write(','.join([str(x) for x in right_pose_o]) + '\n')

            f4.write(','.join([str(x) for x in left_linear_vel]) + ',')
            f4.write(','.join([str(x) for x in left_angular_vel]) + ',')
            f4.write(','.join([str(x) for x in right_linear_vel]) + ',')
            f4.write(','.join([str(x) for x in right_angular_vel]) + '\n')

            rate.sleep()


if __name__ == '__main__':
    main()
