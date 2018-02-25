#include <ros/ros.h>
#include <tf/transform_broadcaster.h>

int main(int argc, char** argv) {
    ros::init(argc, argv, "robot_tf_publisher");
    ros::NodeHandle n;
    ros::Rate r(100);
    tf::TransformBroadcaster broadcaster;
    //  0.02 in x, 0.11 in z
    while(n.ok()) {
        broadcaster.sendTransform(
            tf::StampedTransform(tf::Transform(tf::Quaternion(0, 0, 0, 1), tf::Vector3(0.0, 0.0, 0.14)), 
                ros::Time::now(), "base_link", "camera_link"));
        broadcaster.sendTransform( 
        tf::StampedTransform(
            tf::Transform(tf::Quaternion(0, 0, 0, 1), tf::Vector3(0, 0, 0)),
            ros::Time::now(), "base_laser", "camera_link"));
        broadcaster.sendTransform( 
        tf::StampedTransform(
            tf::Transform(tf::Quaternion(0, 0, 0, 1), tf::Vector3(0, 0, 0)),
            ros::Time::now(), "base_footprint", "base_laser"));
        r.sleep();
    }
}