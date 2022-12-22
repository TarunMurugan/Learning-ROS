#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
def received(d):
    rospy.loginfo(rospy.get_caller_id() + ": {}".format(d) )

def listener():
    rospy.init_node("listner",anonymous=True)
    rospy.Subscriber("chat",String,received)
    rospy.spin()
if __name__=="__main__":
    listener()