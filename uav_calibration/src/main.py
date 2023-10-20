#!/usr/bin/env python3.8

import numpy as np
import rospy
import time
from mavros_msgs.msg import Thrust

#rospy node
rospy.init_node('thrust_publisher')
thrust_pub = rospy.Publisher('/mavros/setpoint_attitude/att_throttle', Thrust, queue_size=10)
thrust_param = Thrust()

for i in range(0, 5):
    #
    thrust_param.thrust = 0.1 * i
    thrust_pub.publish(thrust_param)
    time.sleep(1.0)
    print(i)
    
    #
    print("thrust:",thrust_param.thrust)
    print("################")
#    
thrust_param.thrust = 0.0
thrust_pub.publish(thrust_param)

print("thrust:",thrust_param.thrust)
print("end!")

rospy.spin()