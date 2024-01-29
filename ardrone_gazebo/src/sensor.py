import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image, Range

def motion_and_sensors():
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('drone_motion_and_sensors', anonymous=True)
    rate = rospy.Rate(10)  # Publish commands at 10 Hz

    image_sub = rospy.Subscriber('/ardrone/image_raw', Image, image_callback)  # Subscribe to camera image
    sonar_sub = rospy.Subscriber('/sonar_height', Range, sonar_callback)  # Subscribe to sonar sensor

    while not rospy.is_shutdown():
        # Implement your desired motion logic here
        twist = Twist()
        # Example: Fly forward for 5 seconds
        twist.linear.x = 0.5
        for _ in range(50):  # 50 iterations at 10 Hz = 5 seconds
            pub.publish(twist)
            rate.sleep()

        # Stop the drone
        twist.linear.x = 0.0
        pub.publish(twist)

def image_callback(msg):
    # Process the received camera image
    print("Received camera image:", msg.width, "x", msg.height)  # Example processing

def sonar_callback(msg):
    # Process the sonar height data
    print("Sonar height:", msg.range)

if __name__ == '__main__':
    try:
        motion_and_sensors()
    except rospy.ROSInterruptException:
        pass
