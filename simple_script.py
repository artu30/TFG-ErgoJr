import time
import argparse
import os
import glob
import time
import RPi.GPIO as GPIO
import socket
from bluetooth import *
from character_library import *
from pypot.creatures import PoppyErgoJr

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

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
    poppy.m2.goal_position = 0
    poppy.m3.goal_position = 0
    poppy.m4.goal_position = 0
    poppy.m5.goal_position = 0
    poppy.m6.goal_position = 0
    time.sleep(1)

poppy = PoppyErgoJr(camera='dummy')

InitializeErgoJr(poppy)
BackToRestPosture(poppy)