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
import math


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

        self.lw = tk.Canvas(bg="black", width=400, height=300)

        self.lw.pack()

        self.direction = 1
        self.food_coords = []
        self.snake_body = []
        self.snake_coords = []

        self.circ = self.lw.create_oval(0, 0, 20, 20, fill="green")
        self.snake_body.append(self.circ)
        self.x1 = 0
        self.y1 = 0
        self.speed = 2
        self.root.after(1000, self.snake_coords_inc)
        self.root.after(1000, self.update_snake_pos)

        self.root.bind('<Down>', self.change_diretion_down)
        self.root.bind('<Right>', self.change_diretion_right)
        self.root.bind('<Left>', self.change_diretion_left)
        self.root.bind('<Up>', self.change_diretion_up)

        self.root.after(3000, self.food_generator)

        self.root.mainloop()

    def snake_coords_inc(self):
        self.check_collisions()
        if self.direction == 1:
            self.x1 += self.speed
        elif self.direction == 2:
            self.y1 += self.speed
        elif self.direction == 3:
            self.x1 -= self.speed
        elif self.direction == 4:
            self.y1 -= self.speed
        self.snake_coords.insert(0, (self.x1, self.y1))
        self.root.after(10, self.snake_coords_inc)

    def update_snake_pos(self):
        m = 0
        for part in self.snake_body:
            x = self.snake_coords[m][0]
            y = self.snake_coords[m][1]
            self.lw.coords(part, x, y, x + 20, y + 20)
            m += 1
        self.root.after(10, self.update_snake_pos)

    def check_collisions(self):
        if self.x1 > 380:
            sys.exit()
        if self.y1 > 380:
            sys.exit()
        if self.x1 < 0:
            sys.exit()
        if self.y1 < 0:
            sys.exit()
        for food in self.food_coords:
            if math.isclose(self.x1, food[0]):
                print("HIT")
                self.grow()

    def change_diretion_down(self, event):
        self.direction = 2

    def change_diretion_right(self, event):
        self.direction = 1

    def change_diretion_up(self, event):
        self.direction = 4

    def change_diretion_left(self, event):
        self.direction = 3

    def grow(self):
        print(self.x1 - 20, self.y1 - 20, self.x1, self.y1, self.x1)
        m = self.lw.create_oval(10, 10, 30, 30, fill="red")
        self.lw.tag_lower(m)  # lowers the level of element
        self.snake_body.append(m)

    def food_generator(self):
        x = random.randint(0, 380)
        y = random.randint(0, 280)
        self.food = self.lw.create_oval(x, y, x+20, y+20, fill="red")
        self.lw.tag_lower(self.food)  # lowers the level of element
        self.root.after(5000, self.food_generator)
        print(self.lw.coords(self.food)[0:2])
        self.food_coords.append(self.lw.coords(self.food)[0:2])

    def __del__(self):
        print("Instance deleted.")
