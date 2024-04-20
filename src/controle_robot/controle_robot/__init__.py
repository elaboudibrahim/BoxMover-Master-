import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Control(Node):
    def __init__(self):
        super.__init__("contole_node")
        self.publishers=self.create_publisher(Twist,'cmd1',1)
        self.timers=self.create_timer(0.5,self.callbackTimer)

    def callbackTimer(self):
        msg=Twist()
        msg.linear.x=0.2
        msg.angular.z=0.0
        self.publishers.publish(msg)
        self.get_logger().info('Sending command: Linear=%.2f, Angular=%.2f' % (msg.linear.x, msg.angular.z))

    def main(args=None):
        rclpy.init(args=args)
        node = Control()
        rclpy.spin(node)
        rclpy.shutdown()

    if __name__ == '__main__':
        main()