"""Docstring: This program lets you play two games.

It is automatically started by starting the program.
"""

__author__ = "6770541: Niels Heissel"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__credits__ = "If you would like to thank somebody \
              i.e. an other student for her code or leave it out"
__email__ = "niels.heissel@stud.uni-frankfurt.de"

import sys

from scr.snake import class_controller


def menue():
    """a procedure for printing a menue we assume"""

    print("...Welcome to the Menue....................")
    print("...........................................")
    print("...Press 1 to start Pah Tum TUI Mode.......")
    print("...Press 2 to start Pah Tum GUI PvP Mode...")
    print("...Press 3 to start Pah Tum GUI AI Mode....")
    print("...Press 4 to see the manual...............")
    print("...Press 5 to exit.........................")
    print("...........................................")
    print("...........................................")



def main():
    while(True):
            menue()
            inp = ""
            inp = input()
            if (inp == "1"):
                game = class_controller.SnakeGame()
                inp = ""
            elif (inp == "5"):
                sys.exit()
            else:
                print("Wrong Input. Choose a number between 1 and 5, please\n")


if __name__ == '__main__':
    main()
