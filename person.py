from random import *
import numpy as np
from blessings import Terminal

t = Terminal()


class Person:
    __xl = 0  # encapsulation to create a private variable
    __yl = 0  # encapsulation to create a private variab;e
    __killed = 0  # encapsulation to create a private variable

    def __init__(self, char):
        self.char = char   # character assignment

    def spawn(self, arr):
        self.__xl = 2  # modify the private variable ,i.e, location of person
        self.__yl = 4
        for i in range(2, 4):
            for y in range(4, 8):
                arr[i][y] = self.char
        return arr

    def move(self, arr, char):
        # char is the input given by user to move person class instance
        idx1 = self.__xl
        idx2 = self.__yl
        if self.__killed == 0:
            for i in range(idx1, idx1+2):
                for y in range(idx2, idx2+4):
                    if arr[i][y] != t.yellow(str(2)):
                        arr[i][y] = ' '

            if (char == 'w'):
                if (arr[idx1 - 2][idx2] == ' '):
                    idx1 -= 2
            elif (char == 's'):
                if (arr[idx1 + 2][idx2] == ' '):
                    idx1 += 2
            elif (char == 'a'):
                if (arr[idx1][idx2 - 4] == ' '):
                    idx2 -= 4
            elif (char == 'd'):
                if (arr[idx1][idx2 + 4] == ' '):
                    idx2 += 4
            for i in range(idx1, idx1 + 2):
                for y in range(idx2, idx2 + 4):
                    arr[i][y] = self.char
            self.__xl = idx1
            self.__yl = idx2
        return arr

    def locatex(self):  # function to get x co-ordinate of person's location
        return self.__xl

    def locatey(self):  # function to get y co-ordinate of person's location
        return self.__yl

    def setkilled(self):
        self.__killed = 1-self.__killed
        return
