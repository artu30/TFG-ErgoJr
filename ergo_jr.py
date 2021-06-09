import time
import argparse
from pypot.creatures import PoppyErgoJr

def getchar():
   #Returns a single character from standard input
   import tty, termios, sys
   fd = sys.stdin.fileno()
   old_settings = termios.tcgetattr(fd)
   try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
   finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
   return ch

def InitializeErgoJr(poppy):
    poppy.m1.compliant = False
    poppy.m2.compliant = False
    poppy.m3.compliant = False

    poppy.m1.moving_speed = 200
    poppy.m2.moving_speed = 200
    poppy.m3.moving_speed = 200

def executeExample(poppy):
    poppy.m1.goal_position = 10
    poppy.m2.goal_position = 10
    poppy.m3.goal_position = 10
    poppy.m4.goal_position = 10
    poppy.m5.goal_position = 10
    poppy.m6.goal_position = 10

def BackToRestPosture(poppy):
    poppy.m1.goal_position = 0
    poppy.m2.goal_position = 0
    poppy.m3.goal_position = 0
    poppy.m4.goal_position = 0
    poppy.m5.goal_position = 0
    poppy.m6.goal_position = 0

print("Write a character")

while 1:
    ch = getchar()
    if ch.strip() == '':
        print('bye!')
        break
    else:
        print('Writting . . .')

        poppy = PoppyErgoJr(camera='dummy')

        InitializeErgoJr(poppy)

        executeExample(poppy)
        time.sleep(4)
        
        BackToRestPosture(poppy)
        time.sleep(4)
        break



