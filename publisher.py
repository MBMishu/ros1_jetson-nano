#!/usr/bin/env python
import rospy
from std_msgs.msg import String

  
def talk_to_me():
    
    pub = rospy.Publisher('talking_topic',String,queue_size=10)
    rospy.init_node('publisher',anonymous=True)
    rate = rospy.Rate(1)
    rospy.loginfo("Publisher node started vision, now publishing")

    while not rospy.is_shutdown():
        msg = "hello mishu - %s" % rospy.get_time()
        pub.publish(msg)
        rate.sleep()
    

if __name__ == '__main__':
    try:
        talk_to_me()
    except rospy.ROSInterruptException:
        pass