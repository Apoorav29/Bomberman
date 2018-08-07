from random import *
import numpy as np

class Brick:
    def __init__(self,char):        # function to assign character to the bricks.
        self.char=char

    def place(self,arr):  # function to place all the bricks in the game matrix.
        num = randint(18,25)
        count=0
        while count<num : # num contains the total number of bricks to be placed
            xl = randint(2,35)
            yl = randint(4,71)
            if (arr[xl][yl]==' '):
                for j in range(xl-(xl%2),xl+2-(xl%2)):
                    for k in range(yl-(yl%4),yl+4-(yl%4)):
                        arr[j][k]=self.char
                count+=1
        return arr  # modified array is returned to the driver program.
