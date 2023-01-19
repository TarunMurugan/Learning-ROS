#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def talker():
    p=rospy.Publisher("chat",String,queue_size=2)
    rospy.init_node("talker")
    rate=rospy.Rate(10)
    x=0
    while not rospy.is_shutdown():
        x+=1
        hstr="hello world {}".format(x)
        rospy.loginfo(hstr)
        p.publish(hstr)
        rate.sleep()






if __name__ == "__main__":
    rospy.loginfo("begin")
    try:
        talker()
    except rospy.RosInterruptException:
        pass
