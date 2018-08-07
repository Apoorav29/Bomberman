#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import termios
import fcntl
import time
from wall import Wall
from bomberman import Bomberman
from person import Person
from bricks import Brick
from enemy import Enemy
import numpy as np
from random import *
from blessings import Terminal


def getch():
    fd = sys.stdin.fileno()
    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)
    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
    try:
        while 1:
            try:
                c = sys.stdin.read(1)
                break
            except IOError:
                pass
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
    return c
qflag = 0
level = 1
while level <= 3:
    t = Terminal()
    bx = 0
    by = 0
    planted = False
    SCORE = 0
    flag = 0
    arr = [[' ' for i in range(76)] for y in range(38)]
    wall1 = Wall()
    arr = wall1.buildwall(arr)     # populate the array with the wall.
    bricks = Brick(t.cyan('/'))
    arr = bricks.place(arr)       # populate the array with the bricks.
    bomber = Bomberman(t.green('B'))
    num = randint(3*level, 4*level)
    enarr = []
    var = False
    for i in range(num):
        enarr.append(Enemy(t.red('E')))         # enarr is populated with all the enemies.
    arr = bomber.spawn(arr)             # bomberman is spawned.
    for i in range(0, num):
        arr = enarr[i].randspawn(arr)           # all the enemies are randomly spawned.
    if level == 1:
        lives = 3
    print t.blue('SCORE :- '), SCORE, t.blue('LIVES :- '), lives, t.blue('LEVEL :- '), level, t.yellow('\t\tBOMBERMAN\n')
    for i in range(38):
        print ''.join(arr[i])
    while lives:        # loop terminates when user has no lives left.
        flag = 0
        time.sleep(.2)
        char = getch()          # get the input from the user.
        if char == 'q':         # 'q' terminates the game.
            qflag = 1
            break
        elif char != 'b':
            arr = bomber.move(arr, char)
            # time.sleep()
            for i in range(num):
                arr = enarr[i].move(arr)
                if enarr[i].killed():
                    flag = 1
        elif char == 'b':
            bx = bomber.locatex()           # bomber's location is tracked.
            by = bomber.locatey()
            # for i in range(bx, bx + 2):
            #     for y in range(by, by + 4):
            #         arr[i][y] = t.black('O')
            count = 3
            while count > 0:    # loop runs until the bomb explodes.
                char = getch()  # get input for bomber's movement.
                count -= 1    # number of frames elapsed decreased by one.
                for i in range(bx, bx + 2):
                    for y in range(by, by + 4):
                        arr[i][y] = t.yellow(str(count))
                if char == 'q':
                    qflag = 1
                    break
                elif char != 'b':
                    arr = bomber.move(arr, char)
                    for i in range(num):
                        arr = enarr[i].move(arr)
                        if enarr[i].killed():  # indicates bomber killed?
                            bomber.setkilled()
                            flag=1
                            break
                    # if flag==1:

                print t.blue('SCORE :- '), SCORE, t.blue('LIVES :- '), lives, t.blue('LEVEL :- '), level, t.yellow('\t\tBOMBERMAN\n')
                for i in range(38):
                    print ''.join(arr[i])
                time.sleep(.2)
                if flag == 1:
                    for i in range(bx, bx + 2):
                        for y in range(by, by + 4):
                            arr[i][y] = ' '
                    break
            if qflag == 1:            # if the user terminates by pessing 'q'.
                break
            if flag == 0:
                if arr[bx][by + 4] == t.cyan('/'):
                    SCORE += 20
                if arr[bx][by - 4] == t.cyan('/'):
                    SCORE += 20
                if arr[bx - 2][by] == t.cyan('/'):
                    SCORE += 20
                if arr[bx + 2][by] == t.cyan('/'):
                    SCORE += 20
                if arr[bx][by + 4] == t.red('E'):
                    SCORE += 100
                if arr[bx][by - 4] == t.red('E'):
                    SCORE += 100
                if arr[bx - 2][by] == t.red('E'):
                    SCORE += 100
                if arr[bx + 2][by] == t.red('E'):
                    SCORE += 100
                for i in range(bx - 2, bx + 4):
                    for y in range(by, by + 4):
                        if arr[i][y] != 'X':
                            if arr[i][y] == t.green('B'):
                                flag = 1
                            arr[i][y] = t.magenta('e')
                for i in range(bx, bx + 2):
                    for y in range(by - 4, by + 8):
                        if arr[i][y] != 'X':
                            if arr[i][y] == t.green('B'):
                                flag = 1
                            arr[i][y] = t.magenta('e')
            print t.blue('SCORE :- '), SCORE, t.blue('LIVES :- '), lives, t.blue('LEVEL :- '), level, t.yellow('\t\tBOMBERMAN\n')
            for i in range(38):
                print ''.join(arr[i])
            # if flag ==1:
            #     break
            time.sleep(.5)
            for i in range(bx - 2, bx + 4):
                for y in range(by - 4, by + 8):
                    if arr[i][y] == t.magenta('e'):
                        arr[i][y] = ' '
        countdead=0
        for i in range(num):
            temp = enarr[i].getalive()
            if temp == 0:
                countdead += 1
        if countdead == num:
            print t.blue('SCORE :- '), SCORE, t.blue('LIVES :- '), lives, t.blue('LEVEL :- '), level, t.yellow('\t\tBOMBERMAN\n')
            for i in range(38):
                print ''.join(arr[i])
            break
        if flag == 1:
            lives -= 1
            bomber = Bomberman(t.green('B'))
            arr = bomber.spawn(arr)
            flag = 0
            for i in range(num):
                enarr[i].resetkilled()
        print t.blue('SCORE :- '), SCORE, t.blue('LIVES :- '), lives, t.blue('LEVEL :- '), level, t.yellow('\t\tBOMBERMAN\n')
        for i in range(38):
            print ''.join(arr[i])
        if qflag == 1:
            break
    if qflag == 1:
        break
    if lives > 0:
        level += 1
    else:
        break
