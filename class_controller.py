"""Pah Tum Controller Class

This class is dedicated to playing with a reali life friend or opponent. As always we tried
to be as descriptive as possible, so our commenting in docstrings is relatively shorter
"""

import random
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox
import sys
import os
import time


__author__ = "6785468: Robert am Wege, 6770541: Niels Heissel"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni"
__credits__ = ""
__email__ = "uni.goethe.horde@gmail.com"


class SnakeGame():
    move_list = []

    def __init__(self, tic=0):
        """The Constructor

        Called from the main.py, and handed over a tk root, which is the basis for the window.
        In the constructor we bind every widget to its belonging root window
        """
        self.root = tk.Tk()
        self.tic = tic
        self.root.attributes("-topmost", True)  # put the root to foreground
        self.root.geometry('+900+50')  # sets the default window position
        self.root.geometry('400x300')
        self.root.title("Snake")

        self.lw = tk.Canvas(bg="black")

        self.lw.pack(fill=X)

        self.direction = 1

        self.circ = self.lw.create_oval(0, 0, 80, 80, fill="green")
        self.x1 = 0
        self.y1 = 0
        self.speed = 2
        self.root.after(1000, self.animation)

        self.root.bind('<Down>', self.change_diretion_down)
        self.root.bind('<Right>', self.change_diretion_right)
        self.root.bind('<Left>', self.change_diretion_left)
        self.root.bind('<Up>', self.change_diretion_up)

        self.root.mainloop()

    def animation(self):
        if self.direction == 1:
            self.x1 += self.speed
        elif self.direction == 2:
            self.y1 += self.speed
        elif self.direction == 3:
            self.x1 -= self.speed
        elif self.direction == 4:
            self.y1 -= self.speed
        print("heyyy", self.x1)
        self.lw.coords(self.circ, self.x1, self.y1, self.x1 + 20, self.y1 + 20)
        self.root.after(50, self.animation)

    def change_diretion_down(self, event):
        self.direction = 2

    def change_diretion_right(self, event):
        self.direction = 1

    def change_diretion_up(self, event):
        self.direction = 4

    def change_diretion_left(self, event):
        self.direction = 3


    def __del__(self):
        print("Instance deleted.")
