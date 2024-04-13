import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SubscriberNode(Node):
    def __init__(self):
        super().__init__("subscriber_node")
        self.subscriber=self.create_subscriber(String,'topic',10)
        self.timer=self.create_timer(0.5,self.timer_callback())

    def timer_callback(self):
        self.msg=String()
        self.msg.data='Hello world'
        self.subscriber.subscribe(msg)
        self.get_logger().info('subscriber: "%s"' % msg.data)

def main():
    rclpy.init()
    node=SubscriberNode()
    print("the subscriber node is running")
    try:
        rclpy.spin(node)
    except:
        rclpy.shutdown()
if __name__=='__main__':
    main()
