#!/bin/bash
myvariable=$(whoami)
source /home/$myvariable/sai_ws/devel_isolated/setup.bash

roslaunch ur_robot_driver ur3e_bringup.launch robot_ip:=150.254.47.146 &
sleep 10
roslaunch ur3e_moveit_config ur3e_moveit_planning_execution.launch &
#roslaunch ur3e_moveit_config moveit_rviz.launch config:=true &
roslaunch realsense2_camera rs_camera.launch &
sleep 10
rosservice call /connect "status: true" &
sleep 5
roslaunch apriltag_ros continuous_detection.launch && fg
#sleep 10
#rosrun move_robot main.py && fg
