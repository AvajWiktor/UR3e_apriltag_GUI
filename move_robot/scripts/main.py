#!/usr/bin/env python3
"""
Initial file for entire app
"""
from view import main_view  # , modules_view, settings_bar_view
import rospy
if __name__ == '__main__':

    rospy.init_node('Manipulator', anonymous=True)
    App = main_view.MainWindowView()
    print("Closed")