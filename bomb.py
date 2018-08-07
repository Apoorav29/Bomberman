from time import sleep
from random import *


class Bomb:
    def __init__(self, char):   # defines the character of bomb
        self.char = char

    def planted(self, xl, yl, arr):
        # function which plants the bomb and displays it on the board.
        for i in range(xl - (xl % 2), xl + 2 - (xl % 2)):
            for j in range(yl - (yl % 4), yl + 4 - (yl % 4)):
                arr[i][j] = self.char
        return arr
