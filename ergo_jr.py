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

server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

advertise_service( server_sock, "AquaPiServer",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ]
                    )

while True:
    server_sock.listen(1)
    print ("Waiting for connection on RFCOMM channel %d", port)

    client_sock = server_sock.accept()
    
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

    try:
        data = client_sock.recv(1024)

        operaciones[data[0].decode("utf-8")]()

        BackToRestPosture(poppy)

    except IOError:
	    pass

    except KeyboardInterrupt:
        print ("disconnected")
        client_sock.close()
        server_sock.close()
        print ("all done")
        break