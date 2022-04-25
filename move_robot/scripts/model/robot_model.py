from UR import ur_library
import serial
from math import atan2
import json


class RobotModel:
    def __init__(self, payload=0, tcp_mass=0, robot_speed=0, robot_ip='192.168.0.178'):
        self.move_group = None #ur_library.MoveGroupPythonInterface()
        self.detected_tags = {}  # dict of detected tags
        self.serial_port = None #serial.Serial('/dev/ttyUSB0', 9600, timeout=0.05)

