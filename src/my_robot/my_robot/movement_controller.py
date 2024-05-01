import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MovementController(Node):
    def __init__(self):
        super().__init__('movement_controller')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(1.0, self.publish_movement)

    def publish_movement(self):
        # Commande de mouvement simple
        twist = Twist()
        twist.linear.x = 2.0  # Avancer à une vitesse linéaire de 0.5 m/s
        twist.angular.z = 1.0  # Pas de rotation
        self.publisher.publish(twist)
        self.get_logger().info("Published movement command")

def main(args=None):
    rclpy.init(args=args)
    node = MovementController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

