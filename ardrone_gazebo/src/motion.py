#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def motion_control():
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('drone_motion_control', anonymous=True)
    rate = rospy.Rate(10)  # Publish commands at 10 Hz

    while not rospy.is_shutdown():
        # Choose a motion command
        command = input("Enter motion command (forward, backward, left, right, up, down, cw, ccw, stop): ")

        twist = Twist()
        if command == "forward":
            twist.linear.x = 1.0
        elif command == "backward":
            twist.linear.x = -1.0
        elif command == "left":
            twist.linear.y = 1.0
        elif command == "right":
            twist.linear.y = -1.0
        elif command == "up":
            twist.linear.z = 1.0
        elif command == "down":
            twist.linear.z = -1.0
        elif command == "cw":  # Clockwise rotation
            twist.angular.z = 1.0
        elif command == "ccw":  # Counterclockwise rotation
            twist.angular.z = -1.0
        elif command == "stop":
            twist.linear.x = 0.0
            twist.linear.y = 0.0
            twist.linear.z = 0.0
            twist.angular.z = 0.0
        else:
            print("Invalid command.")
            continue

        pub.publish(twist)
        rate.sleep()

if __name__ == '__main__':
    try:
        motion_control()
    except rospy.ROSInterruptException:
        pass
