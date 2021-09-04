#!/usr/bin/env python3 import rospy # Python library for ROS from sensor_msgs.msg import LaserScan # LaserScan type message is defined in sensor_msgs from geometry_msgs.msg import Twist # def callback(dt): #print '-------------------------------------------' #print 'Range data at 0 deg: {}'.format(dt.ranges[0]) #print 'Range data at 15 deg: {}'.format(dt.ranges[15]) #print 'Range data at 345 deg: {}'.format(dt.ranges[345]) #print '-------------------------------------------' thr1 = 1 # Laser scan range threshold thr2 = 0.1 if dt.ranges[0]>thr1 : # Checks if there are obstacles in front and # 15 degrees left and right (Try changing the # the angle values as well as the thresholds) move.linear.x = 0.5 # go forward (linear velocity) move.angular.z = 0 # do not rotate (angular velocity) elif dt.ranges[0]<thr1 and dt.ranges[90]>thr2 and dt.ranges[270]<thr2:# obstacle in front move.linear.x = 0.0 move.angular.z = 5.0 move.angular.z = 0.0 move.linear.x=0.5 move.linear.x = 0.0 move.angular.z = 5.0 elif dt.ranges[0]<thr1 and dt.ranges[90]>thr2 and dt.ranges[270]>thr2: move.linear.x = 0.0 move.angular.z = 5.0 move.angular.z = 0.0 move.linear.x=0.5 move.linear.x = 0.0 move.angular.z = 5.0 elif dt.ranges[0]<thr1 and dt.ranges[90]<thr2 and dt.ranges[270]>thr2: move.linear.x = 0.0 move.angular.z = -5.0 move.angular.z = 0.0 move.linear.x=0.5 move.linear.x = 0.0 move.angular.z = -5.0 else: move.linear.x = 0.0 move.angular.z =0.0 move.angular.z =0.0 move.linear.x=-0.5 move.linear.x = 0.0 move.angular.z =0.0 pub.publish(move) # publish the move object move = Twist() # Creates a Twist message type object rospy.init_node('obstacle_avoidance_node') # Initializes a node pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10) # Publisher object which will publish "Twist" type messages # on the "/cmd_vel" Topic, "queue_size" is the size of the # outgoing message queue used for asynchronous publishing sub = rospy.Subscriber("/scan", LaserScan, callback) # Subscriber object which will listen "LaserScan" type messages # from the "/scan" Topic and call the "callback" function # each time it reads something from the Topic rospy.spin() # Loops infinitely until someone stops the program execution