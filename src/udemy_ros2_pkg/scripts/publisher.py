import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PublisherNode(Node):
    def __init__(self):# Constructor of the class
        # Create a node with the name 'publisher_node' and a namespace of 'udemy_ros2_pkg'
        super().__init__('publisher_node')
        # Create a publisher with the topic name 'topic' and a queue size of 10 messages
        self.publisher_ = self.create_publisher(String, 'topic', 10)
         # Create a timer with a period of 0.5 seconds and the callback function timer_callback 
        self.timer_ = self.create_timer(0.5, self.timer_callback)

        
    def timer_callback(self):
        # Create a message object of type String 
        msg = String()
        # Assign the message to the data field of the message object 
        msg.data = 'Hello World'
        # Publish the message to the topic 'topic'
        self.publisher_.publish(msg)
        # Print the message to the console using the get_logger() function
        self.get_logger().info('Publishing: "%s"' % msg.data)            


def main():
    rclpy.init() # Initialize the ROS 2 client library
    node = PublisherNode() # Create an instance of the PublisherNode class
    print('Publisher Node is running ...')
    try:
        rclpy.spin(node) # Keep the node running until it is shutdown by the user 
    except KeyboardInterrupt:
        rclpy.shutdown() # Shutdown the ROS 2 node 

if __name__=='__main__':
    main()