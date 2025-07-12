import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MessageBroadcaster(Node):
    def __init__(self):
        super().__init__('sender')
        self.publisher_ = self.create_publisher(String, 'my_msg', 10)
        self.timer = self.create_timer(5.0, self.broadcast_message)

    def broadcast_message(self):
        text_msg = String()
        text_msg.data = input("Type a message to send : ")
        self.publisher_.publish(text_msg)
        self.get_logger().info(f'You have typed: {text_msg.data}')

def start_node(args=None):
    rclpy.init()
    publishing_node = MessageBroadcaster()
    rclpy.spin(publishing_node)
    publishing_node.destroy_node()
    rclpy.shutdown()
