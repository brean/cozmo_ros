#!/usr/bin/env python3
import time
import pycozmo
import rclpy


class CozmoRos(object):
    def __init__(self, node):
        self.ros_node = node
        self.cli = pycozmo.Client()
        self.connect_and_wait()

    def connect_and_wait(self):
        self.cli.start()
        self.cli.connect()
        self.cli.wait_for_robot()

    def term(self):
        """Terminate: stop all motors and disconnect"""
        self.cli.send(pycozmo.protocol_encoder.StopAllMotors())
        self.cli.disconnect()
        self.cli.stop()

    @staticmethod
    def on_camera_image(image):
        image.save("camera.png", "PNG")

    def setup_camera(self):
        pkt = pycozmo.protocol_encoder.EnableCamera(enable=True)
        self.cli.send(pkt)
        pkt = pycozmo.protocol_encoder.EnableColorImages(enable=True)
        self.cli.send(pkt)
        time.sleep(2.0)

    def get_image(self):
        """make sure to call setup_camera first"""
        self.cli.add_handler(
            pycozmo.client.EvtNewRawCameraImage,
            CozmoRos.on_camera_image,
            one_shot=True)
        time.sleep(1)


def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('cozmo_driver')
    app = CozmoRos(node)
    # see pycozmo/examples/rc.py
    # TODO: use threading and run thread or does rclpy have sth. else?


if __name__ == '__main__':
    main()
