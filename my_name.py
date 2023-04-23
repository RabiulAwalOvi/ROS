#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def my_name():
    rospy.init_node('my_name_letter',anonymous= True)
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)

    motion = Twist()

    motion.linear.x=0
    motion.linear.y=1
    t_present = rospy.Time.now().to_sec()    
    while rospy.Time.now().to_sec () - t_present < 4:
            pub.publish(motion) 

    motion.linear.x=1
    motion.linear.y=0
    t_present = rospy.Time.now().to_sec()    
    while rospy.Time.now().to_sec () - t_present < 2:
            pub.publish(motion) 

    motion.linear.x=0
    motion.linear.y=-1
    t_present = rospy.Time.now().to_sec()    
    while rospy.Time.now().to_sec () - t_present < 2:
            pub.publish(motion) 
    

    motion.linear.x=-1
    motion.linear.y=0
    t_present = rospy.Time.now().to_sec()    
    while rospy.Time.now().to_sec () - t_present < 2:
            pub.publish(motion) 

    motion.linear.x=0
    pub.publish(motion)
    
    motion.linear.x=1
    motion.linear.y=-1
    t_present = rospy.Time.now().to_sec()    
    while rospy.Time.now().to_sec () - t_present < 2:
            pub.publish(motion) 


my_name()
    
