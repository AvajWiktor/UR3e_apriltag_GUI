import rospy
from UR import ur_library
import serial
import subprocess
from math import atan2
import json

from os import system
from geometry_msgs.msg import PoseStamped, Pose
from geometry_msgs.msg import Point as Point_msg
from math import pi, cos, sin, radians, atan
from std_msgs.msg import String
from UR.ur_library import MoveGroupPythonInterface
import tf
from tf.transformations import quaternion_from_euler
from tf.transformations import euler_from_quaternion
from tf.transformations import *
from geometry_msgs.msg import Quaternion


class MainModel:
    """
    Module responsible for detecting aruco tags and storing their position
    """
    def __init__(self):
        self.tag_id = None
        self.tag_params = None
        self.move_group = None  #
        self.detected_tags = {}  # dict of detected tags
        self.serial_port = None  # serial.Serial('/dev/ttyUSB0', 9600, timeout=0.05)
        self.is_connected = False

    def connect_to_robot(self):
        rc = subprocess.call("/home/wiktor/Desktop/RobotLaunch.sh")
        self.move_group = ur_library.MoveGroupPythonInterface()
        self.is_connected = True

    def detect_tag(self, tag_id):
        try:
            listener = tf.TransformListener()
            listener.waitForTransform('/base_link', f'/tag_{tag_id}', rospy.Time(), rospy.Duration(1))
            (transform, orientation) = listener.lookupTransform(
                '/base_link',
                f"/tag_{tag_id}",
                rospy.Time(0)
            )
            (xo, yo, zo, wo) = orientation
            (x, y, z) = transform
            position = Pose([x, y, z], [xo, yo, zo, wo])
            # Create object which represents parameters of box with given tag id
            self.tag_id = tag_id
            return position
        except Exception as exc:
            print(exc)
            return False

    def read_tag_info(self, tag_id):
        f = open(f"utilities/tags_params.json")
        data = json.load(f)
        self.tag_params = data[tag_id]

    def connect_to_robot(self):
        self.robot_model.connect_to_robot()

    def move_to_tag(self):
        pass

    def move_to_target(self):
        pass

