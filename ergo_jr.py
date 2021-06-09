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

def executeExample():
    poppy = PoppyErgoJr(camera='dummy')

    poppy.m1.compliant = False
    poppy.m2.compliant = False
    poppy.m3.compliant = False

    poppy.m1.moving_speed = 250
    poppy.m2.moving_speed = 250
    poppy.m3.moving_speed = 250

    poppy.m1.goal_position = 10
    poppy.m2.goal_position = 10
    poppy.m3.goal_position = 10


print("Write a character")

while 1:
    ch = getchar()
    if ch.strip() == '':
        print('bye!')
        break
    else:
        executeExample()
        time.sleep(6)
        break



