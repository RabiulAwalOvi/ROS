#!/usr/bin/env python

import rospy
from rospy import Time
from geometry_msgs.msg import Twist
import sys

def draw_triangle():

        rospy.init_node('drawing_a_triangle', anonymous= True)
        pub=rospy.Publisher('turtle1/cmd_vel',Twist,queue_size=(10))

        motion = Twist()

        motion.linear.x=0
        motion.linear.y=0
        motion.angular.z=0
        pub.publish(motion)

        motion.linear.x=1
        motion.linear.y=0
        motion.angular.z=0
        t_present = Time.now().to_sec()    
        while Time.now().to_sec () - t_present < 3:
            pub.publish(motion) 

        

        motion.linear.x=-.5
        motion.linear.y=1
        motion.angular.z=0

        t_present = Time.now().to_sec()    
        while Time.now().to_sec () - t_present < 2:
            pub.publish(motion)
        

        motion.linear.x=-.7
        motion.linear.y=-1
        motion.angular.z=0

        t_present = Time.now().to_sec()    
        while Time.now().to_sec () - t_present < 1.2:
            pub.publish(motion)


def draw_sqr():

        #rospy.init_node('Draw_squre', anonymous=True)
        pub=rospy.Publisher('turtle2/cmd_vel',Twist,queue_size=(10))

        motion = Twist()

        rospy.sleep(2)

        motion.linear.x=.5
        motion.linear.y=0
        motion.angular.z=0
        t_present = Time.now().to_sec()    
        while Time.now().to_sec () - t_present < 2:
            pub.publish(motion) 

        rospy.sleep(2)
        

        motion.linear.x=0
        motion.linear.y=.5
        motion.angular.z=0

        t_present = Time.now().to_sec()    
        while Time.now().to_sec () - t_present < 2:
            pub.publish(motion)
        
        rospy.sleep(2)

        motion.linear.x=-.5
        motion.linear.y=0
        motion.angular.z=0

        t_present = Time.now().to_sec()    
        while Time.now().to_sec () - t_present < 2:
            pub.publish(motion)

        rospy.sleep(2)

        motion.linear.x=0
        motion.linear.y=-.5
        motion.angular.z=0

        t_present = Time.now().to_sec()    
        while Time.now().to_sec () - t_present < 2:
            pub.publish(motion)

        rospy.sleep(2)



def draw_circle():
        #rospy.init_node('draw_circle',anonymous=True)
        pub = rospy.Publisher('/turtle3/cmd_vel',Twist,queue_size=10)
        rate = rospy.Rate(10)

        vel = Twist()


        vel.linear.x= 2
        vel.linear.y= 0
        vel.linear.z= 0

        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 2
        t_present = Time.now().to_sec()    
        while Time.now().to_sec () - t_present < 4:
                pub.publish(vel) 
        
draw_triangle()
draw_sqr()
draw_circle()








