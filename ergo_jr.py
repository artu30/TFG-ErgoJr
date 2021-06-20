import time
import argparse
from character_library import *
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
    poppy.m4.compliant = False
    poppy.m5.compliant = False
    poppy.m6.compliant = False

    poppy.m1.moving_speed = 100
    poppy.m2.moving_speed = 100
    poppy.m3.moving_speed = 100
    poppy.m4.moving_speed = 100
    poppy.m5.moving_speed = 100
    poppy.m6.moving_speed = 100

def BackToRestPosture(poppy):
    poppy.m3.goal_position = 0
    time.sleep(1)
    poppy.m2.goal_position = 0
    poppy.m3.goal_position = 0
    poppy.m4.goal_position = 0
    poppy.m5.goal_position = 0
    poppy.m6.goal_position = 0
    time.sleep(1)

print("Write a character")

while 1:
    ch = getchar()
    if ch.strip() == '':
        print('bye!')
        break
    else:
        print('Writting . . .')

        poppy = PoppyErgoJr(camera='dummy')

        CharacterManager = CharacterLibrary(poppy)

        operaciones = { 
        'a': CharacterManager.WriteA, 
        'b': CharacterManager.WriteB, 
        'c': CharacterManager.WriteC, 
        'd': CharacterManager.WriteD,
        'e': CharacterManager.WriteE, 
        'f': CharacterManager.WriteF, 
        'g': CharacterManager.WriteG, 
        'h': CharacterManager.WriteH,
        'i': CharacterManager.WriteI, 
        'j': CharacterManager.WriteJ, 
        'k': CharacterManager.WriteQ, 
        'l': CharacterManager.WriteL,
        'm': CharacterManager.WriteM, 
        'n': CharacterManager.WriteN, 
        'o': CharacterManager.WriteO, 
        'p': CharacterManager.WriteP,
        'q': CharacterManager.WriteQ, 
        'r': CharacterManager.WriteR, 
        's': CharacterManager.WriteS, 
        't': CharacterManager.WriteT,
        'u': CharacterManager.WriteU, 
        'v': CharacterManager.WriteV, 
        'w': CharacterManager.WriteW, 
        'x': CharacterManager.WriteX,
        'y': CharacterManager.WriteY, 
        'z': CharacterManager.WriteZ
        }

        InitializeErgoJr(poppy)
        BackToRestPosture(poppy)
        
        operaciones[ch]()
        time.sleep(2)

        BackToRestPosture(poppy)
        time.sleep(4)
        break



