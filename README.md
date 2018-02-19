# Installation

Install ROS Kinetic and catkin workspace
ROS Kinetic

On Raspberry Pi
sudo apt-get install ros-kinetic-ros-base ros-kinetic-rospy ros-kinetic-roscpp

New Catkin tool
sudo apt-get install python-catkin-tools

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

# No access to /dev/mem when run with ros

Create new user group name gpio

Add current user to gpio group

Add 99-com.rules to /etc/udev/rules.d/

# To launch open loop control of an actual robot
On host machine

roslaunch nav_behaviors nav_behaviors.launch

On the Raspberry Pi:

roscore (cmd_vel wont goes to raspberry pi if you launch roscore on host machine)

roslaunch gopigo_description gopigo_interface.launch