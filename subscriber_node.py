import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MessageReceiver(Node):
    def __init__(self):
        super().__init__('receiver')
        self.subscription = self.create_subscription(
            String,
            'my_msg',
            self.listener_callback,
            5
        )

    def listener_callback(self, msg):
        self.get_logger().info(f'Message Received: "{msg.data}"')

def start_receiver(args=None):
    rclpy.init()
    receive_node = MessageReceiver()
    rclpy.spin(receive_node)
    receive_node.destroy_node()
    rclpy.shutdown()
