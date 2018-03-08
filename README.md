# Recon Robot
3d reconstruction robot using ROS and RTAB-MAP


## Installation

Install ROS Kinetic and catkin workspace
ROS Kinetic

On Raspberry Pi
sudo apt-get install ros-kinetic-ros-base ros-kinetic-rospy ros-kinetic-roscpp

New Catkin tool
sudo apt-get install python-catkin-tools

Place 51-kinect.rules file in /etc/udev/rules.d and you'll no longer need to run your apps as root.

## Launch

depth_to_laser.launch -> convert depth image to 2d laser scan.

freenect.launch -> launch freenect.

rosrun teleop_twist_keyboard teleop_twist_keyboard.py -> control robot cmd_vels by keyboard.

rosrun robot_setup_tf tf_broadcaster & rosrun robot_setup_tf tf_listener -> launch tf for base_link and camera_link.

rosrun rviz rviz -d rviz.rviz run rviz with config file.

rqt -> show tf graph

## No access to /dev/mem when run with ros

Create new user group name gpio

Add current user to gpio group

Add 99-com.rules to /etc/udev/rules.d/

## To launch open loop control of an actual robot
On host machine

roslaunch nav_behaviors nav_behaviors.launch

On the Raspberry Pi:

roscore (cmd_vel wont goes to raspberry pi if you launch roscore on host machine)

roslaunch gopigo_description gopigo_interface.launch

## 3D Mapping on raspberry pi

on raspberry pi

roslaunch freenect_launch freenect.launch depth_registration:=true data_skip:=2

roslaunch rtabmap_ros rgbd_mapping.launch rtabmap_args:="--delete_db_on_start --Vis/MaxFeatures 500 --Mem/ImagePreDecimation 2 --Mem/ImagePostDecimation 2 --Kp/DetectorStrategy 6 --OdomF2M/MaxSize 1000 --Odom/ImageDecimation 2" rtabmapviz:=false

on client

ROS_NAMESPACE=rtabmap rosrun rtabmap_ros rtabmapviz _subscribe_odom_info:=false _frame_id:=camera_link



## Save map

rosrun mapserver -f mymap

adjust laser scan size to 0.05

nmap -sP 10.42.0.*

robot_pose_ekf -> better calculation base_link overtime (covariance m)

rostopic pub /syscommand std_msgs/String "data: 'reset'"

## TODO
Add IMU Sensor, Encoder motor, Nvidia Jetson
add robot_pose_ekf to help stablize odom
nvidia jetson tx2