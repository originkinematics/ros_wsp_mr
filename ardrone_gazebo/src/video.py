
import rospy
from geometry_msgs.msg import Twist
import time

def takeoff_and_rectangle():
    global pub  # Make `pub` accessible globally
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('drone_takeoff_rectangle_land', anonymous=True)
    
    # Takeoff
    takeoff(5.0)

    # Rectangle motion
    side_length = 2.0
    turn_duration = 2.0
    forward_duration = 5.0
    rectangle_motion(side_length, turn_duration, forward_duration)

    # Landing
    land(5.0)

def takeoff(duration):
    twist = Twist()
    twist.linear.z = 1.0  # Upward velocity
    start_time = time.time()
    while time.time() - start_time < duration:

        pub.publish(twist)
        rate = rospy.Rate(10)  # Publish commands at 10 Hz

        rate.sleep()

def land(duration):
    twist = Twist()
    twist.linear.z = -1.0  # Downward velocity
    start_time = time.time()
    while time.time() - start_time < duration:
        pub.publish(twist)
        rate = rospy.Rate(10)  # Publish commands at 10 Hz

        rate.sleep()

def rectangle_motion(side_length, turn_duration, forward_duration):
    # Move forward along one side
    move_forward(forward_duration)

    # Turn 90 degrees
    turn(turn_duration)

    # Repeat for the other three sides
    for _ in range(3):
        move_forward(forward_duration)
        turn(turn_duration)

def move_forward(duration):
    twist = Twist()
    twist.linear.x = 0.5  # Forward velocity
    start_time = time.time()
    while time.time() - start_time < duration:
        pub.publish(twist)
        rate = rospy.Rate(10)  # Publish commands at 10 Hz

        rate.sleep()

def turn(duration):
    twist = Twist()
    twist.angular.z = 1.0  # Counterclockwise turn
    start_time = time.time()
    while time.time() - start_time < duration:
        pub.publish(twist)
        rate = rospy.Rate(10)  # Publish commands at 10 Hz

        rate.sleep()

if __name__ == '__main__':
    try:
        takeoff_and_rectangle()
    except rospy.ROSInterruptException:
        pass
