#include <ros/ros.h>
#include <mavros_msgs/TimesyncStatus.h>

ros::Time sent_time; // 记录发送时间

// 时间同步回调函数
void timesyncCallback(const mavros_msgs::TimesyncStatus::ConstPtr& msg)
{
    ros::Time received_time = ros::Time::now(); // 记录接收时间
    double delay = (received_time - sent_time).toSec(); // 计算通信延时
    ROS_INFO("Communication delay: %f seconds", delay); // 输出通信延时
}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "delay_node"); // 初始化ROS节点
    ros::NodeHandle nh; // 创建节点句柄

    // 订阅mavros/time_sync话题，注册时间同步回调函数
    ros::Subscriber timesync_sub = nh.subscribe<mavros_msgs::TimesyncStatus>("mavros/time_sync", 1, timesyncCallback);

    // 发布mavros/time_sync话题
    ros::Publisher timesync_pub = nh.advertise<mavros_msgs::TimesyncStatus>("mavros/time_sync", 1);

    ros::Rate rate(10); // 设置循环频率为10Hz

    while (ros::ok())
    {
        mavros_msgs::TimesyncStatus msg;
        msg.header.stamp = ros::Time::now(); // 设置消息时间戳为当前时间
        timesync_pub.publish(msg); // 发布时间同步消息
        sent_time = ros::Time::now(); // 记录发送时间
        ros::spinOnce(); // 处理ROS回调函数
        rate.sleep(); // 按照循环频率休眠
    }

    return 0;
}
