import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SubscriberNode(Node):
    def __init__(self):
        super().__init__("scoutbot_subscriber")
        self.subscription = self.create_subscription(
            String,
            '/scoutbot_topic',
            self.listener_callback,
            10
        )
        self.subscription
        
    def listener_callback(self, msg):
        self.get_logger().info(f"I heard: {msg.data}")
        
def main():
    rclpy.init()
    Subscriber = SubscriberNode()
    rclpy.spin(Subscriber)
    Subscriber.destroy_node()
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()