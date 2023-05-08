#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("Recived data %s", data.data)

  
def listener():
    rospy.init_node('subscriber',anonymous=True)
    rospy.Subscriber('vision_topic',String,callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass