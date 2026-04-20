#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TalkerNode(Node):
    def __init__(self):
        super().__init__('talker_node')
        self.publisher = self.create_publisher(String, 'group_info', 4)
        self.timer = self.create_timer(2.5, self.publish_info)  # Publish every 2 seconds

    def publish_info(self):
        msg = String()
        msg.data = "Titilola Mayowa, Group 4, Matric: 230410005"
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = TalkerNode()
    rclpy.spin(node)  # Keep the node running
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()