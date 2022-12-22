#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def talker():
    p=rospy.Publisher("chat",String,queue_size=2)
    rospy.init_node("talker")
    rate=rospy.Rate(10)
    while not rospy.is_shutdown():
        hstr="hello world {}".format(rospy.get_time())
        rospy.loginfo(hstr)
        p.publish(hstr)
        rate.sleep()






if __name__ == "__main__":
    rospy.loginfo("begin")
    try:
        talker()
    except rospy.RosInterruptException:
        pass