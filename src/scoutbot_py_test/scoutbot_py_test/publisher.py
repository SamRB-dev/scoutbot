import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class scoutBotPublisher(Node):
    def __init__(self):
        super().__init__("scoutbot_publisher")
        self.publisher = self.create_publisher(String, 'scoutbot_topic', 10)
        self.counter = 0
        self.frequency = 1.5  # Frequency in seconds
        self.timer = self.create_timer(self.frequency, self.timerCallback)
        self.get_logger().info("Scoutbot Publisher COunter Frequency: " + str(self.frequency) + " seconds")
        
    def timerCallback(self):
        msg = String()
        msg.data = f"Hello from Soutbot! Count: {self.counter}"
        self.publisher.publish(msg)
        self.get_logger().info(f"Published: {msg.data}")
        self.counter += 1
        
def main():
    rclpy.init()
    publisher = scoutBotPublisher()
    rclpy.spin(publisher)
    publisher.destroy_node()
    rclpy.shutdown()