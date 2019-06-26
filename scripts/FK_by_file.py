#!/usr/bin/python

import rospy
import numpy as np
import os
from os import walk
from baxter_pykdl import baxter_kinematics

def main():
    rospy.init_node('fk_by_file')
    kin = baxter_kinematics('left')

    f = []
    loadpath = '/home/alessandro/eXperimentsData/'

    print '\n'
    for exp_name in os.listdir(loadpath):
        exp_path = loadpath  + exp_name
        if os.path.isdir(exp_path):
            for dir_name in os.listdir(exp_path):
                dir_load = exp_path +'/' +dir_name 
                if os.path.isdir(dir_load) and dir_load.find('_pose') < 0:
                    dir_save = dir_load + '_pose'

                    try:
                        os.stat(dir_save)
                    except:
                        os.mkdir(dir_save)

                    for files in os.listdir(dir_load):
                        loadname = dir_load +'/'+files
                        savename = dir_save +'/'+files
                        if os.path.isfile(loadname):
                            print loadname
                            print savename
                            print '\n'
                            input_file = open(loadname,'r')
                            output_file = open(savename,'w')
                            output_file.write("time,x,y,z,quat1,quat2,quat3,quat4,gripper"+"\n")
                            string_content = input_file.readlines()
                            for item in string_content:
                                string_list = item.split(',')
                                line = []
                                for item in string_list:
                                    if item == 'time':
                                        break
                                    line.append(float(item))
                                if line:
                                    angles = {'left_s0': line[1], 'left_s1': line[2], 'left_w0': line[5], 'left_w1': line[6], 'left_w2': line[7], 'left_e0': line[3], 'left_e1': line[4]}
                                    r = kin.forward_position_kinematics(angles)
                                    output_file.write(str(line[0])+","+str(r[0])+","+str(r[1])+","+str(r[2])+","+str(r[3])+","+str(r[4])+","+str(r[5])+","+str(r[6])+","+str(line[8])+"\n")

        
if __name__ == "__main__":
    main()
