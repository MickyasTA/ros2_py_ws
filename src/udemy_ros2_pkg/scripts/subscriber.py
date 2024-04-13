import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SubscriberNode(Node):
    super().__init__("subscriber_node")
    self.subscriber=self.create_subscriber(String,'topic',10)
    self.timer=self.create_timer(self.timer_callback())

    def timer_callback(self):
        


def main():
    rclpy.init()

    try:
        pass
    except:
        pass

if __name__=='__main__':
    main()
