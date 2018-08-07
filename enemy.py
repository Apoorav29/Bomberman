from random import *
from person import Person
from wall import Wall
from blessings import Terminal


t = Terminal()


class Enemy(Person):         # Inheritence of Person class in the Enemy class.
    __xl = 0          # encapsulation to create private variable
    __yl = 0          # private variable holding the location of enemy
    __killf = 0             # encapsulation to create private variable
    __alive = 1

    def __init__(self, char):
        Person.__init__(self, char)

    def randspawn(self, arr):        # function to spawn the enemy.
        num = randint(5, 8)
        count = 0
        while count < 1:
            xl = randint(2, 35)
            yl = randint(4, 71)
            if (arr[xl][yl] == ' '):
                self.__xl = xl - (xl % 2)
                self.__yl = yl - (yl % 4)
                for j in range(xl - (xl % 2), xl + 2 - (xl % 2)):
                    for k in range(yl - (yl % 4), yl + 4 - (yl % 4)):
                        arr[j][k] = t.red('E')
                count += 1
        return arr

    def move(self, arr):
        # Polymorphism, both person and enemy moved by the function"move".
        idx1 = self.__xl
        idx2 = self.__yl
        if arr[idx1][idx2] != t.red('E'):
            self.__alive = 0
        else:
            for i in range(idx1, idx1 + 2):
                for y in range(idx2, idx2 + 4):
                    arr[i][y] = ' '
            count = 0
            while True:  # loop moves enemy and check if the bomber is killed.
                flag = 0
                num = randint(1, 4)
                if (num == 1 and (arr[idx1 - 2][idx2] == ' ' or
                   arr[idx1 - 2][idx2] == t.green('B'))):
                    if arr[idx1 - 2][idx2] == t.green('B'):
                        self.__killf = 1
                    flag = 1
                    idx1 -= 2
                elif (num == 2 and (arr[idx1 + 2][idx2] == ' ' or
                      arr[idx1 + 2][idx2] == t.green('B'))):
                    if arr[idx1 + 2][idx2] == t.green('B'):
                        self.__killf = 1
                    flag = 1
                    idx1 += 2
                elif (num == 3 and (arr[idx1][idx2 - 4] == ' ' or
                      arr[idx1][idx2 - 4] == t.green('B'))):
                    if arr[idx1][idx2 - 4] == t.green('B'):
                        self.__killf = 1
                    flag = 1
                    idx2 -= 4
                elif (num == 4 and (arr[idx1][idx2 + 4] == ' ' or
                      arr[idx1][idx2 + 4] == t.green('B'))):
                    if arr[idx1][idx2 + 4] == t.green('B'):
                        self.__killf = 1
                    flag = 1
                    idx2 += 4
                count += 1
                if flag == 1:
                    break
                if count > 4:
                    break
            self.__xl = idx1
            self.__yl = idx2
            for i in range(idx1, idx1 + 2):
                for y in range(idx2, idx2 + 4):
                    arr[i][y] = self.char
        return arr

    def killed(self):   # function checks if the bomberman has been killed.
        if self.__killf == 1:
            return True
        return False

    def resetkilled(self):  # function to reset the killf value
        self.__killf = 0
        return

    def resetalive(self):   # function resets the __alive valu.
        self.__alive = 0
        return

    def getalive(self):
        return self.__alive
