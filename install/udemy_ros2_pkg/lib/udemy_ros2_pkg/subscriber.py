#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SubscriberNode(Node):
    def __init__(self):
        super().__init__("subscriber_node")
        self.subscriber=self.create_subscription(String,'topic',self.subscriber_callback,10)

    def subscriber_callback(self,msg):
        print("Recived:"+msg.data)

def main():
    rclpy.init()
    node=SubscriberNode()
    print("Weatting for data to br published ....")
    try:
        rclpy.spin(node)
    except:
        print("Terminating the node ... ")
        rclpy.shutdown()
if __name__=='__main__':
    main()
