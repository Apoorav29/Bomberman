import numpy as np


class Wall:
    def __init__(self):
        return

    def buildwall(self, arr):  # encapsulation principle.
        row1 = [0, 1, 36, 37]
        col1 = [0, 1, 2, 3, 72, 73, 74, 75]
        for i in col1:  # loop to populate the array with the wall
            for row in arr:
                row[i] = 'X'
        for i in row1:
            for y in range(76):
                arr[i][y] = 'X'
        for i in range(0, 38):
            if ((i % 4) // 2 == 0):
                for y in range(4, 76):
                    if ((y % 8) // 4 == 0):
                        arr[i][y] = 'X'
                    elif ((y % 8) // 4 == 1):
                        y += 4
                        continue
            else:
                i += 2
        return arr
