"""Docstring: This program lets you play Snake.

It is automatically started by starting the program.
"""

import sys
from scr.snake import class_controller

__author__ = "6770541: Niels Heissel"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__credits__ = "If you would like to thank somebody \
              i.e. an other student for her code or leave it out"
__email__ = "niels.heissel@stud.uni-frankfurt.de"


def manuel():
    print("This is the manuel.\n"
          "Welcome to Snake. \nThe original game "
          "with some small changes. \nTo navigate "
          "with the snake, use the arrow keys on the "
          "bottom right of your keyboard\n"
          "(<up>, <down>, <right>, <left>). \n"
          "But don't turn to quickly or you will bite"
          " yourself...\n"
          "Be careful, your speed increases every "
          "10 seconds. \n\nEat the red ovals to score, "
          "hit the grey to slow down, but \nwatch out,"
          " you might get torn apart.\n\n")


def menue():
    """This procedure prints the Menu"""

    print("...Welcome to the Menue....................")
    print("...........................................")
    print("...Press 1 to start Snake......")
    print("...Press 2 to see the manuel...")
    print("...Press 3 to exit.........................")
    print("...........................................")
    print("...........................................")


def main():
    while (True):
        menue()
        inp = ""
        inp = input()
        if (inp == "1"):
            game = class_controller.SnakeGame()
        elif inp == "2":
            manuel()
        elif (inp == "3"):
            sys.exit()
        else:
            print("Wrong Input. Choose a number between 1 and 3, please\n")


if __name__ == '__main__':
    main()
