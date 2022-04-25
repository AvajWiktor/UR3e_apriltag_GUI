import os
import tkinter as tk
import ttkbootstrap.constants

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from threading import *
from PIL import ImageTk, Image
from model.main_model import MainModel
from controller.main_controller import MainController
from tkinter import filedialog as fd
import webview

import time
import json


class MainWindowView:
    def __init__(self, robot_model):
        self.root = ttk.Window(themename='cyborg', title='AprilTag detector')
        self.root.minsize(width=1200, height=800)
        self.robot_model = robot_model
        self.model = MainModel(self.robot_model)
        self.controller = MainController(self.robot_model, self.model)
        self.refresher = Thread(name='refresher', target=self.refresh)
        self.tag_id = 0
        """
        *Code here*
        """
        self.create_layout()
        self.add_components()

        """
        """
        self.root.mainloop()

    def refresh(self):
        pass

    def executor(self):
        pass

    def detector(self):
        if self.controller.detect_tag(self.tag_id):
            self.add_image(self.tag_id)

    def walker(self):
        pass

    def target_walker(self):
        pass

    def create_layout(self):
        """Packs basic frames to root frame"""
        self.left_frame = ttk.Frame(self.root, padding=(5, 5, 5, 5))
        self.center_frame = ttk.Frame(self.root, padding=(5, 5, 5, 5))
        self.right_frame = ttk.Frame(self.root, padding=(5, 5, 5, 5))

        self.left_frame.pack(side=LEFT, fill='both', expand=False)
        self.center_frame.pack(side=LEFT, fill='both', expand=True)
        self.right_frame.pack(side=RIGHT, fill='both', expand=False)

        self.menu_label_frame = ttk.LabelFrame(self.left_frame, text='Menu', padding=50)
        self.menu_label_frame.pack(fill='both')

        self.image_label_frame = ttk.LabelFrame(self.center_frame, text='Detected Tag', padding=50)
        self.image_label_frame.pack(fill='both', expand=True)

    def add_components(self):
        ttk.Label(self.menu_label_frame, text='Tag id').pack()
        self.tag_id = ttk.StringVar()
        ttk.Entry(self.menu_label_frame, textvariable=self.tag_id, width=10).pack()
        ttk.Button(self.menu_label_frame, text='Detect', width=10, command=self.detector).pack(pady=5)
        ttk.Button(self.menu_label_frame, text='Go to tag', width=10, command=self.walker).pack(pady=5)
        ttk.Button(self.menu_label_frame, text='Go to target', width=10, command=self.target_walker).pack(pady=5)
        ttk.Button(self.menu_label_frame, text='Execute', width=10, command=self.executor).pack(pady=5)

    def add_image(self, img_name):
        img = Image.open(f'utilities/{img_name}')
        img.resize((50,50),Image.ANTIALIAS)
        test = ImageTk.PhotoImage(img)
        img_label=tk.Label(self.image_label_frame, image=test)
        img_label.image = test

        # Position image
        img_label.pack()#place(x= 10, y = 10)
        # Create a Label Widget to display the text or Image

