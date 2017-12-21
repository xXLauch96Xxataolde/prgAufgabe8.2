"""Snake Controller Class

This class is dedicated to playing with a reali life friend or opponent. As always we tried
to be as descriptive as possible, so our commenting in docstrings is relatively shorter
"""

import random
import tkinter as tk
from tkinter import messagebox
import sys

__author__ = "6770541: Niels Heissel"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__credits__ = "If you would like to thank somebody \
              i.e. an other student for her code or leave it out"
__email__ = "niels.heissel@stud.uni-frankfurt.de"


class SnakeGame():
    move_list = []

    def __init__(self):
        """The Constructor

        Called from the main.py, and handed over a tk root, which is the basis for the window.
        In the constructor we bind every widget to its belonging root window
        """

        self.root = tk.Tk()
        self.root.attributes("-topmost", True)  # put the root to foreground
        self.root.geometry('+900+50')  # sets the default window position
        self.root.geometry('405x340')
        self.root.title("Snake")

        self.game_state = False
        self.speed = 1
        self.direction = 1
        self.food_coords = []
        self.snake_body = []
        self.snake_coords = []
        self.foods = []
        self.score = 0
        self.blocks = []
        self.steps_per_body = int(20 / self.speed)
        self.key_pressed = False
        self.score_var = tk.StringVar(self.root)
        self.score_var.set("Score")
        self.speed_var = tk.StringVar(self.root)
        self.speed_var.set("Speed")

        self.lw = tk.Canvas(bg="black", width=400, height=300)
        self.lw.grid(rowspan=3, columnspan=3)

        self.label_1 = tk.Label(self.root, textvariable=self.score_var, bg="red", relief=tk.RIDGE, bd="5", width=10,
                                height=1)
        self.label_1.grid(row=3, column=0)

        self.start_button = tk.Button(self.root, text="Start", command=self.start)
        self.start_button.grid(row=3, column=1)

        self.label_2 = tk.Label(self.root, textvariable=self.speed_var, bg="blue", relief=tk.RIDGE, bd="5", width=10,
                                height=1)
        self.label_2.grid(row=3, column=2)

        self.circ = self.lw.create_oval(0, 0, 20, 20, fill="green")
        self.snake_body.append(self.circ)
        self.x1 = 0
        self.y1 = 0

        self.root.bind('<Down>', self.change_diretion_down)
        self.root.bind('<Right>', self.change_diretion_right)
        self.root.bind('<Left>', self.change_diretion_left)
        self.root.bind('<Up>', self.change_diretion_up)

        self.instructions()

        self.root.mainloop()

        sys.exit()

    def start(self):
        self.delete_instructions()
        self.game_state = True
        self.snake_coords_inc()
        self.update_snake_pos()
        self.root.after(3000, self.food_generator)
        self.root.after(4000, self.inc_speed)
        self.root.after(5000, self.block_generator)
        self.root.after(30000, self.block_destructor)
        self.start_button.destroy()


    def instructions(self):
        self.text = self.lw.create_text(200, 115, text="Welcome to Snake. \nThe original game "
                                                      "with some small changes. \nTo navigate "
                                                      "with the snake, use the arrow keys\n"
                                                      "(<up>, <down>, <right>, <left>). \n"
                                                      "But don't turn to quickly or you will bite"
                                                      " yourself...\n"
                                                      "Be careful, your speed increases every "
                                                      "10 seconds. \n\nEat the red ovals to score, "
                                                      "hit the grey to slow down, but \nwatch out,"
                                                      " you might get torn apart.",
                                        fill="white", font=("Purisa", 15))

    def delete_instructions(self):
        self.lw.delete(self.text)

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
        self.root.after(1, self.snake_coords_inc)

    def update_snake_pos(self):
        m = 0
        for part in self.snake_body:
            x = self.snake_coords[m][0]
            y = self.snake_coords[m][1]
            self.lw.coords(part, x, y, x + 20, y + 20)
            m += self.steps_per_body
        self.speed_var.set(self.speed)
        self.root.after(1, self.update_snake_pos)

    def check_collisions(self):
        if self.game_state == True:
            if self.x1 > 380:
                self.game_state = False
                self.lw.delete("all")
                self.lw.create_text(200,100, text="GAME OVER \nYou lost...", fill="grey", font=("Purisa", 30))
                return
            if self.y1 > 280:
                self.game_state = False
                self.lw.delete("all")
                self.lw.create_text(200,100, text="GAME OVER \nYou lost...", fill="grey", font=("Purisa", 30))
                return
            if self.x1 < 0:
                self.game_state = False
                self.lw.delete("all")
                self.lw.create_text(200,100, text="GAME OVER \nYou lost...", fill="grey", font=("Purisa", 30))
                return
            if self.y1 < 0:
                self.game_state = False
                self.lw.delete("all")
                self.lw.create_text(200,100, text="GAME OVER \nYou lost...", fill="grey", font=("Purisa", 30))
                return
            for food in self.foods:
                if self.x1 == self.lw.coords(food)[0] and self.y1 == self.lw.coords(food)[1]:
                    self.grow()
                    self.lw.delete(food)
                    self.foods.remove(food)
                    self.score += 1
                    self.score_var.set(self.score)

            for part in self.snake_coords[1:len(self.snake_body) * self.steps_per_body]:
                if part[0] == self.x1 and part[1] == self.y1:
                    self.game_state = False
                    self.lw.delete("all")
                    self.lw.create_text(200,100, text="GAME OVER. You lost...", fill="grey", font=("Purisa", 30))
                    return

            for block in self.blocks:
                try:
                    if self.x1 == self.lw.coords(block)[0] and self.y1 == self.lw.coords(block)[1]:
                        self.label_3 = tk.Label(self.root, text="Watch out for obstacles..", bg="grey")
                        self.label_3.grid(row=3, column=1)
                        self.root.after(2000, self.delete_message)
                        self.dec_speed()
                except IndexError:
                    None

    def delete_message(self):
        try:
            self.label_3.destroy()
        except AttributeError:
            None

    def change_diretion_down(self, event):
        if self.key_pressed is False and self.game_state is True:
            if self.direction == 4:
                return
            if self.snake_coords[0][0] % 20 == 0 and self.snake_coords[0][1] % 20 == 0:
                self.direction = 2
                return
            else:
                self.keep_change_down()
                self.key_pressed = True

    def keep_change_down(self):
        if self.snake_coords[0][0] % 20 == 0 and self.snake_coords[0][1] % 20 == 0:
            self.direction = 2
            self.key_pressed = False
            return
        else:
            self.root.after(10, self.keep_change_down)

    def change_diretion_right(self, event):
        if self.key_pressed is False and self.game_state is True:
            if self.direction == 3:
                return
            if self.snake_coords[0][0] % 20 == 0 and self.snake_coords[0][1] % 20 == 0:
                self.direction = 1
                return
            else:
                self.keep_change_right()
                self.key_pressed = True

    def keep_change_right(self):
        if self.snake_coords[0][0] % 20 == 0 and self.snake_coords[0][1] % 20 == 0:
            self.direction = 1
            self.key_pressed = False
            return
        else:
            self.root.after(10, self.keep_change_right)

    def change_diretion_up(self, event):
        if self.key_pressed is False and self.game_state is True:
            if self.direction == 2:
                return
            if self.snake_coords[0][0] % 20 == 0 and self.snake_coords[0][1] % 20 == 0:
                self.direction = 4
                self.key_pressed = False
                return
            else:
                self.keep_change_up()
                self.key_pressed = True

    def keep_change_up(self):
        if self.snake_coords[0][0] % 20 == 0 and self.snake_coords[0][1] % 20 == 0:
            self.direction = 4
            self.key_pressed = False
            return
        else:
            self.root.after(10, self.keep_change_up)

    def change_diretion_left(self, event):
        if self.key_pressed is False and self.game_state is True:
            if self.direction == 1:
                return
            if self.snake_coords[0][0] % 20 == 0 and self.snake_coords[0][1] % 20 == 0:
                self.direction = 3
                return
            else:
                self.keep_change_left()
                self.key_pressed = True

    def keep_change_left(self):
        if self.snake_coords[0][0] % 20 == 0 and self.snake_coords[0][1] % 20 == 0:
            self.direction = 3
            self.key_pressed = False
            return
        else:
            self.root.after(10, self.keep_change_left)

    def grow(self):

        l = len(self.snake_body)

        print(self.snake_coords)

        x = self.snake_coords[l * self.steps_per_body - 1][0]
        y = self.snake_coords[l * self.steps_per_body - 1][1]
        print(x)
        print(self.x1)
        m = self.lw.create_oval(x, y, x + 20, y + 20, fill="darkgreen")
        self.snake_body.append(m)

    def food_generator(self):
        """Randomly positions food on the field."""
        while True:
            x = random.randrange(0, 380, 20)
            y = random.randrange(0, 280, 20)
            # Check if random coordinates are in snake or next to head.
            if x in range(self.x1 - 40, self.x1 + 40) and y in range(self.y1 - 40, self.y1 + 40):
                continue
            if (x, y) in self.snake_coords[len(self.snake_body) * self.steps_per_body]:
                continue
            else:
                break
        food = self.lw.create_oval(x, y, x + 20, y + 20, fill="red")
        self.lw.tag_lower(food)  # lowers the level of element
        if self.game_state is True:
            self.root.after(5000, self.food_generator)
        self.food_coords.append(self.lw.coords(food)[0:2])
        self.foods.append(food)

    def block_generator(self):
        """Randomly positions blocks on the field."""
        while True:
            x = random.randrange(0, 380, 20)
            y = random.randrange(0, 280, 20)
            # Check if random coordinates are in snake or next to head.
            if x in range(self.x1 - 60, self.x1 + 60) and y in range(self.y1 - 60, self.y1 + 60):
                continue
            if (x, y) in self.snake_coords[len(self.snake_body) * self.steps_per_body]:
                continue
            else:
                break
        block = self.lw.create_oval(x, y, x + 20, y + 20, fill="grey")
        self.lw.tag_lower(block)  # lowers the level of element
        if self.game_state is True:
            self.root.after(5000, self.block_generator)
        self.blocks.append(block)

    def block_destructor(self):
        """Randomly positions blocks on the field."""
        random_block = random.choice(self.blocks)
        self.lw.delete(random_block)
        self.root.after(5000, self.block_destructor)

    def inc_speed(self):
        if self.x1 % 20 == 0 and self.y1 % 20 == 0:
            if self.speed == 1:
                self.speed = 2
            elif self.speed == 2:
                self.speed = 4
            elif self.speed == 4:
                self.speed = 5
        else:
            self.root.after(5, self.inc_speed)
            return
        self.steps_per_body = int(20 / self.speed)
        if self.game_state is True:
            self.root.after(10000, self.inc_speed)

    def dec_speed(self):
        if self.x1 % 20 == 0 and self.y1 % 20 == 0:
            if self.speed == 5:
                self.speed = 4
            elif self.speed == 4:
                self.speed = 2
            elif self.speed == 2:
                self.speed = 1
        else:
            self.root.after(5, self.inc_speed)
            return
        self.steps_per_body = int(20 / self.speed)

    def __del__(self):
        print("Instance deleted.")
