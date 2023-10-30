#!/usr/bin/env python3.8

import numpy as np
import rospy
import time

from mavros_msgs.msg import Thrust
from mavros_msgs.msg import State
from mavros_msgs.srv import CommandBool, SetMode

#rospy node
rospy.init_node('thrust_publisher')
thrust_pub = rospy.Publisher('/mavros/setpoint_attitude/att_throttle', Thrust, queue_size=10)
thrust_param = Thrust()

# offboard
auto_offboard = rospy.get_param('~auto_offboard', True)

# mavros
mavros_state = None
def mavros_state_cb(msg: State):
    global mavros_state
    mavros_state = msg
rospy.Subscriber("/mavros/state", State, mavros_state_cb, queue_size=1, tcp_nodelay=True)

#
if mavros_state == None or  not mavros_state.connected:
    print("mavros not connected!!")

# offboard mode 
if auto_offboard and mavros_state.mode != "OFFBOARD":
    print("set OFFBOARD mode!!")
else:    
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