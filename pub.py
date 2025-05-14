#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from tutorials.msg import *

def talk_to_me():
    pub =rospy.Publisher('talking_topic',posisi, queue_size=10)
    rospy.init_node('pub', anonymous=True)
    rate=rospy.Rate(1)
    rospy.loginfo("sudah dipublish")
    while not rospy.is_shutdown():
        msg = posisi()
        msg.massage = "my posisi : "
        msg.x = 2.0
        msg.y = 1.5
        pub.publish(msg)
        rate.sleep()






if __name__ == '__main__':
    try:
        talk_to_me()
    except rospy.ROSInterruptException:
        pass