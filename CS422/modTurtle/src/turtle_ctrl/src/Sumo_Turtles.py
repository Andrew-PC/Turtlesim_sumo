#!/usr/bin/env python
import rospy
import tf
import turtlesim.srv
import geometry_msgs.msg
import time
# Imports SetPen structure to instruct turtle not to draw its path
# through its SetPen service interface
from turtlesim.srv import SetPen
 
# Imports Twist message structure for issuing motion commands to turtle
from geometry_msgs.msg import Twist
 
import random
droprate = 30
droppacket = 0
 
# Imports Color message structure for monitoring if
# turtle is over red square
from turtlesim.msg import Color
 
def colour_update(msg):
    global droprate
    global droppacket
    if(((msg.r == 0) and (msg.g == 255) and (msg.b == 0))):
        droppacket = 1
        backup = Twist()
        backup.angular.z = 3.14
        backup.linear.x = -3
        twist_pub.publish(backup)
        return

    if((msg.r == 0) and (msg.g == 0) and (msg.b == 0)):
        dead_stop = Twist()
        time.sleep(0.25);
        twist_pub.publish(dead_stop)
        print('turtle1 has left the circle, LOSER!')
        #twist_pub2.publish(dead_stop)
        return
    droppacket = (droppacket + 1)%droprate
    if (droppacket != 0):
        return
    next_move = Twist() # initialises to zero motion
    if (random.randint(0,1) == 0):
        next_move.linear.x = 3
    else:
        next_move.angular.z = 3.14 * random.uniform(-1,1)
    twist_pub.publish(next_move)

def colour_update2(msg):
    global droprate
    global droppacket
    if(((msg.r == 0) and (msg.g == 255) and (msg.b == 0))):
        droppacket = 1
        backup = Twist()
        backup.angular.z = 3.14
        backup.linear.x = -3
        twist_pub2.publish(backup)
        return
    
    if ((msg.r == 0) and (msg.g == 0) and (msg.b == 0)):
        dead_stop = Twist()
        time.sleep(0.25);
        twist_pub2.publish(dead_stop)
        print('turtle2 has left the circle, LOSER!')
        #twist_pub2.publish(dead_stop)
        return
    droppacket = (droppacket + 1)%droprate
    if (droppacket != 0):
        return
    next_move2 = Twist() # initialises to zero motion
    if (random.randint(0,1) == 0):
        next_move2.linear.x = 3
    else:
        next_move2.angular.z = 3.14 * random.uniform(-1,1)
    twist_pub2.publish(next_move2)

def colour_update3(msg):
    global droprate
    global droppacket
    if(((msg.r == 0) and (msg.g == 255) and (msg.b == 0))):
        droppacket = 1
        backup = Twist()
        backup.angular.z = 3.14
        backup.linear.x = -3
        twist_pub3.publish(backup)
        return

    if ((msg.r == 0) and (msg.g == 0) and (msg.b == 0)):
        dead_stop = Twist()
        time.sleep(0.25);
        twist_pub3.publish(dead_stop)
        print('turtle3 has left the circle, LOSER!')
        #twist_pub2.publish(dead_stop)
        return
    droppacket = (droppacket + 1)%droprate
    if (droppacket != 0):
        return
    next_move3 = Twist() # initialises to zero motion
    if (random.randint(0,1) == 0):
        next_move3.linear.x = 3
    else:
        next_move3.angular.z = 3.14 * random.uniform(-1,1)
    twist_pub3.publish(next_move3)

def colour_update4(msg):
    global droprate
    global droppacket
    if(((msg.r == 0) and (msg.g == 255) and (msg.b == 0))):
        droppacket = 1
        backup = Twist()
        backup.angular.z = 3.14
        backup.linear.x = -3
        twist_pub4.publish(backup)
        return

    if ((msg.r == 0) and (msg.g == 0) and (msg.b == 0)):
        dead_stop = Twist()
        time.sleep(0.25);
        twist_pub4.publish(dead_stop)
        print('turtle4 has left the circle, LOSER!')
        #twist_pub2.publish(dead_stop)
        return
    droppacket = (droppacket + 1)%droprate
    if (droppacket != 0):
        return

    next_move4 = Twist() # initialises to zero motion
    if (random.randint(0,1) == 0):
        next_move4.linear.x = 3
    else:
        next_move4.angular.z = 3.14 * random.uniform(-1,1)
    twist_pub4.publish(next_move4)

def colour_update5(msg):
    global droprate
    global droppacket
    if(((msg.r == 0) and (msg.g == 255) and (msg.b == 0))):
        droppacket = 1
        backup = Twist()
        backup.angular.z = 3.14
        backup.linear.x = -3
        twist_pub5.publish(backup)
        return
        
    if ((msg.r == 0) and (msg.g == 0) and (msg.b == 0)):
        dead_stop = Twist()
        time.sleep(0.25);
        twist_pub5.publish(dead_stop)
        print('turtle5 has left the circle, LOSER!')
        #twist_pub2.publish(dead_stop)
        return

    elif(twist_pub.publish(dead_stop) and twist_pub4.publish(dead_stop) and twist_pub3.publish(dead_stop) and twist_pub2.publish(dead_stop)):
        print('turtle5 did not leave! WINNER!')
    droppacket = (droppacket + 1)%droprate
    if (droppacket != 0):
        return

    next_move5 = Twist() # initialises to zero motion
    if (random.randint(0,1) == 0):
        next_move5.linear.x = 3
    else:
        next_move5.angular.z = 3.14 * random.uniform(-1,1)
    twist_pub5.publish(next_move5)

    
if __name__=='__main__':
    # Initialise node
    rospy.init_node('random_walker',anonymous=True)
    

    listener = tf.TransformListener()


    #uses the services interface to spawn multiple turtles in the frame.
    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    spawner(4, 2, 0, 'turtle2')
    spawner(6, 4, 0, 'turtle3')
    spawner(8, 6, 0, 'turtle4')
    spawner(5, 8, 0, 'turtle5')


    #uses the service interface of eac turtlesim 
    #to instruct it not to draw a path
    set_pen = rospy.ServiceProxy('turtle2/set_pen', SetPen)
    set_pen(0,0,0,0,1)
    set_pen = rospy.ServiceProxy('turtle3/set_pen', SetPen)
    set_pen(0,0,0,0,1)
    set_pen = rospy.ServiceProxy('turtle4/set_pen', SetPen)
    set_pen(0,0,0,0,1)
    set_pen = rospy.ServiceProxy('turtle5/set_pen', SetPen)
    set_pen(0,0,0,0,1)
 
 
    # Create Color subscriber and attach to colour_update() callback
    colour_sub = rospy.Subscriber("turtle1/color_sensor",Color,\
                colour_update, queue_size=1)
    colour_sub2 = rospy.Subscriber("turtle2/color_sensor",Color,\
                colour_update2, queue_size=1)
    colour_sub3 = rospy.Subscriber("turtle3/color_sensor",Color,\
                colour_update3, queue_size=1)
    colour_sub4 = rospy.Subscriber("turtle4/color_sensor",Color,\
                colour_update4, queue_size=1)
    colour_sub5 = rospy.Subscriber("turtle5/color_sensor",Color,\
                colour_update5, queue_size=1)
                
 
    # Create a publisher endpoint for publishing Twist messages
    twist_pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1)
    twist_pub2 = rospy.Publisher('turtle2/cmd_vel', Twist, queue_size=1)
    twist_pub3 = rospy.Publisher('turtle3/cmd_vel', Twist, queue_size=1)
    twist_pub4 = rospy.Publisher('turtle4/cmd_vel', Twist, queue_size=1)
    twist_pub5 = rospy.Publisher('turtle5/cmd_vel', Twist, queue_size=1)

   
 
# This try / except block uses the service interface of the
# turtlesim node to instruct it not to draw its path
try:
    rospy.wait_for_service('turtle1/set_pen')
    set_pen = rospy.ServiceProxy('turtle1/set_pen', SetPen)
    set_pen(0,0,0,0,1)
except rospy.ServiceException, e:
    print "Service call failed: %s"%e

# Here we enter into the ros spin loop which hands control
# to ROS. This results in execution of the colour_update()
# callback whenever a Color message is received.
try:
    rospy.spin()
except KeyboardInterrupt:
        print("Keyboard input")