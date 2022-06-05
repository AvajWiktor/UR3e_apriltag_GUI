import rospy
from UR import ur_library
import serial
import subprocess
from math import atan2
import json
from move_robot.srv import connect
from os import system
from geometry_msgs.msg import PoseStamped, Pose
from geometry_msgs.msg import Point as Point_msg
from math import pi, cos, sin, radians, atan
from std_msgs.msg import Bool
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
        self.tag_position = None
        self.connect_service = rospy.Service("connect", connect, self.connect_handler)

    def connect_handler(self, req):
        if req.status:
            print("finished connecting")
            self.move_group = ur_library.MoveGroupPythonInterface()
            self.is_connected = True
            return True
        else:
            print("Connecting failed")
            return False

    def connect_to_robot(self):
        rc = subprocess.call("../RobotLaunch.sh")

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
            self.read_tag_info(tag_id)
            self.tag_position = position
            print(self.tag_position)
            return True
        except Exception as exc:
            print(exc)
            return False

    def read_tag_info(self, tag_id):
        f = open(f"utilities/params.json")
        data = json.load(f)
        self.tag_params = data[tag_id]
        print(self.tag_params)

    def move_to_tag(self):
        if self.tag_position is not None:
            print(self.tag_position)
            self.move_group.move_to_point(self.tag_position, False)
        else:
            print("Tag position unknown")

    def move_to_target(self):
        if self.tag_position is not None:
            target_pose = self.tag_position
            for i, position in enumerate(target_pose.position):
                target_pose.position[i] += self.tag_params['tf'][i]

            print(target_pose)
            self.move_group.move_to_point(target_pose, False)
        else:
            print("Tag position unknown")

    def go_home(self):
        self.move_group.go_to_joint_state(90.0, -90.0, 60.0, 30.0, 90.0, 90.0)

