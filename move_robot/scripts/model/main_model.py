from model.robot_model import RobotModel
import rospy
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
    def __init__(self, robot_model):
        self.robot_model = robot_model
        self.tag_id = None
        self.tag_params = None

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

