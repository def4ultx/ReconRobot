# Installation

Install ROS Kinetic and catkin workspace

Place 51-kinect.rules file in /etc/udev/rules.d and you'll no longer need to run your apps as root.

# Launch

depth_to_laser.launch -> convert depth image to 2d laser scan.

freenect.launch -> launch freenect.

rosrun teleop_twist_keyboard teleop_twist_keyboard.py -> control robot cmd_vels by keyboard.

rosrun robot_setup_tf tf_broadcaster & rosrun robot_setup_tf tf_listener -> launch tf for base_link and camera_link.

rosrun rviz rviz -d rviz.rviz run rviz with config file.

rqt -> show tf graph

# Better hardware

Hokuyo laser scan, encoder motors, Nvidia Jetson, ZED camera