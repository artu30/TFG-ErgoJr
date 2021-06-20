import time
from pypot.creatures import PoppyErgoJr

class CharacterLibrary:
   def __init__(self, poppy):
      self.poppy = poppy

   def WriteA(self):
      self.poppy.m1.moving_speed = 40
      self.poppy.m2.moving_speed = 40
      self.poppy.m3.moving_speed = 40
      self.poppy.m5.moving_speed = 40
      self.poppy.m4.moving_speed = 40
      
      self.poppy.m1.goal_position = 0
      self.poppy.m2.goal_position = 30
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      time.sleep(1)
      self.poppy.m1.goal_position = -5
      self.poppy.m2.goal_position = 0
      self.poppy.m5.goal_position = -90
      self.poppy.m3.goal_position = 90
      time.sleep(1)

      self.poppy.m1.moving_speed = 100
      self.poppy.m2.moving_speed = 100
      self.poppy.m3.moving_speed = 100
      self.poppy.m5.moving_speed = 100
      self.poppy.m4.moving_speed = 100

      self.poppy.m3.goal_position = 0
      time.sleep(0.5)
      self.poppy.m2.goal_position = 0
      self.poppy.m3.goal_position = 0
      self.poppy.m4.goal_position = 0
      self.poppy.m5.goal_position = 0
      self.poppy.m6.goal_position = 0
      time.sleep(1)

      self.poppy.m6.goal_position = -15
      time.sleep(1)
      self.poppy.m1.goal_position = 0
      self.poppy.m5.goal_position = -90
      self.poppy.m3.goal_position = 105
      self.poppy.m6.moving_speed = 40
      time.sleep(2)
      self.poppy.m4.goal_position = 10
      time.sleep(1)
      self.poppy.m4.goal_position = -10
      time.sleep(1)

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