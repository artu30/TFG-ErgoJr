import time
from pypot.creatures import PoppyErgoJr

class CharacterLibrary:
    def __init__(self, poppy):
        self.poppy = poppy

    def WriteA(self):
         self.poppy.m1.goal_position = 30
         time.sleep(1)
         self.poppy.m3.goal_position = 30
         time.sleep(1)
         self.poppy.m1.moving_speed = 20
        
    def WriteB(self):
       print ("B")

    def WriteC(self):
       print ("C")

    def WriteD(self):
       print ("D")

    def WriteE(self):
       print ("E")

    def WriteF(self):
       print ("F")

    def WriteG(self):
       print ("G")

    def WriteH(self):
       print ("H")

    def WriteI(self):
       print ("I")

    def WriteJ(self):
       print ("J")

    def WriteK(self):
       print ("K")

    def WriteL(self):
       print ("L")

    def WriteM(self):
       print ("M")

    def WriteN(self):
       print ("N")

    def WriteO(self):
       print ("O")

    def WriteP(self):
       print ("P")

    def WriteQ(self):
       print ("Q")

    def WriteR(self):
       print ("R")

    def WriteS(self):
       print ("S")

    def WriteT(self):
       print ("T")

    def WriteU(self):
       print ("U")

    def WriteV(self):
       print ("V")

    def WriteW(self):
       print ("W")

    def WriteX(self):
       print ("X")

    def WriteY(self):
       print ("Y")

    def WriteZ(self):
       print ("Z")