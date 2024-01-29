import rospy
from geometry_msgs.msg import Twist
import math

def spiral_motion():
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('drone_spiral_motion', anonymous=True)
    rate = rospy.Rate(10)  # Publish commands at 10 Hz

    radius = 1.0  # Initial radius of the spiral
    velocity = 0.5  # Linear velocity
    angular_velocity = 0.2  # Angular velocity

    while not rospy.is_shutdown():
        angle = rospy.get_time() * angular_velocity  # Calculate current angle based on time
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)

        twist = Twist()
        twist.linear.x = velocity * x  # Set linear velocities based on spiral coordinates
        twist.linear.y = velocity * y
        twist.linear.z = 0.0  # Maintain constant altitude
        twist.angular.z = angular_velocity  # Constant angular velocity for spiral motion

        pub.publish(twist)
        rate.sleep()

if __name__ == '__main__':
    try:
        spiral_motion()
    except rospy.ROSInterruptException:
        pass
