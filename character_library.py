import time
from pypot.creatures import PoppyErgoJr

class CharacterLibrary:
   def __init__(self, poppy):
      self.poppy = poppy

   def PencilUp(self):
      self.poppy.m2.goal_position = -10
      time.sleep(0.1)
      self.poppy.m3.goal_position = 30
      time.sleep(0.5)
      self.poppy.m5.goal_position = -110
      time.sleep(0.1)
      self.poppy.m6.goal_position = -30
      time.sleep(1)
      self.poppy.m1.goal_position = 0
      self.poppy.m2.goal_position = 0
      self.poppy.m3.goal_position = 0
      self.poppy.m4.goal_position = 0
      self.poppy.m5.goal_position = 0
      self.poppy.m6.goal_position = 0
      time.sleep(2)

   def CenterInitPos(self):
      self.poppy.m1.goal_position = 0
      time.sleep(0.5)
      self.poppy.m5.goal_position = -100
      time.sleep(0.5)
      self.poppy.m3.goal_position = 100
      time.sleep(2)

   def LeftInitPos(self):
      self.poppy.m1.goal_position = 5
      time.sleep(0.5)
      self.poppy.m5.goal_position = -90
      time.sleep(0.5)
      self.poppy.m3.goal_position = 90
      time.sleep(2)

   def RightInitPos(self):
      self.poppy.m1.goal_position = -5
      time.sleep(0.5)
      self.poppy.m5.goal_position = -90
      time.sleep(0.5)
      self.poppy.m3.goal_position = 90
      time.sleep(2)

   def GoUp(self):
      self.poppy.m2.goal_position = 10
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      time.sleep(2)

   def CenterUpPos(self):
      self.poppy.m5.goal_position = -75
      time.sleep(0.5)
      self.poppy.m3.goal_position = 75
      time.sleep(2)
      self.poppy.m2.goal_position = 15
      time.sleep(1)

   def WriteA(self):
      self.LeftInitPos()

      self.poppy.m1.goal_position = 0
      self.poppy.m2.goal_position = 30
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      time.sleep(2)
      self.poppy.m1.goal_position = -5
      self.poppy.m2.goal_position = 0
      self.poppy.m5.goal_position = -90
      self.poppy.m3.goal_position = 90
      time.sleep(2)

      self.PencilUp()

      self.CenterInitPos()

      self.poppy.m1.goal_position = 6
      time.sleep(0.5)
      self.poppy.m1.goal_position = -6
      time.sleep(0.5)

      self.PencilUp()

   def WriteB(self):
      self.CenterInitPos()

      self.GoUp()

      self.poppy.m1.goal_position = -8
      time.sleep(2)

      self.poppy.m2.goal_position = 5
      self.poppy.m5.goal_position = -75
      self.poppy.m3.goal_position = 75
      time.sleep(2)

      self.poppy.m1.goal_position = 0
      time.sleep(2)

      self.poppy.m1.goal_position = -10
      time.sleep(2)

      self.poppy.m2.goal_position = 0
      self.poppy.m5.goal_position = -90
      self.poppy.m3.goal_position = 90
      time.sleep(2)

      self.poppy.m1.goal_position = 0
      time.sleep(2)

      self.PencilUp()

   def WriteC(self):
      self.RightInitPos()

      self.poppy.m1.goal_position = 0
      time.sleep(2)

      self.GoUp()

      self.poppy.m1.goal_position = -5
      time.sleep(2)

      self.PencilUp()

   def WriteD(self):
      self.CenterInitPos()

      self.GoUp()

      self.poppy.m1.goal_position = -10
      self.poppy.m2.goal_position = 15
      self.poppy.m5.goal_position = -75
      self.poppy.m3.goal_position = 75
      time.sleep(2)

      self.poppy.m1.goal_position = 6
      self.poppy.m2.goal_position = 0
      self.poppy.m5.goal_position = -90
      self.poppy.m3.goal_position = 90
      time.sleep(2)

      self.PencilUp()

   def WriteE(self):
      self.RightInitPos()

      self.poppy.m1.goal_position = 0
      time.sleep(2)

      self.GoUp()

      self.poppy.m1.goal_position = -5
      time.sleep(2)

      self.PencilUp()

      self.CenterInitPos()

      self.poppy.m1.goal_position = -6
      time.sleep(0.5)

      self.PencilUp()

   def WriteF(self):
      self.poppy.m1.goal_position = 5
      self.poppy.m5.goal_position = -90
      time.sleep(0.5)
      self.poppy.m3.goal_position = 90
      time.sleep(2)

      self.poppy.m1.moving_speed = 40
      self.poppy.m2.moving_speed = 40
      self.poppy.m3.moving_speed = 40
      self.poppy.m5.moving_speed = 40

      self.poppy.m2.goal_position = 30
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      time.sleep(2)

      self.poppy.m1.moving_speed = 100
      self.poppy.m2.moving_speed = 100
      self.poppy.m3.moving_speed = 100
      self.poppy.m5.moving_speed = 100

      self.poppy.m3.goal_position = 0
      time.sleep(0.5)
      self.poppy.m5.goal_position = 0
      time.sleep(0.5)
      self.poppy.m1.goal_position = 0
      time.sleep(0.5)
      self.poppy.m2.goal_position = 0
      time.sleep(0.5)

      self.poppy.m6.goal_position = -15
      time.sleep(1)
      self.poppy.m1.goal_position = 0
      time.sleep(0.5)
      self.poppy.m5.goal_position = -100
      time.sleep(0.5)
      self.poppy.m3.goal_position = 100
      time.sleep(0.5)
      self.poppy.m1.goal_position = -6
      time.sleep(0.5)

   def WriteG(self):
      self.poppy.m1.goal_position = -5
      self.poppy.m2.goal_position = 15
      time.sleep(0.5)
      self.poppy.m5.goal_position = -75
      time.sleep(0.5)
      self.poppy.m3.goal_position = 75
      time.sleep(2)

      self.poppy.m5.goal_position = -90
      time.sleep(0.5)
      self.poppy.m3.goal_position = 90
      time.sleep(2)

      self.poppy.m2.moving_speed = 40
      self.poppy.m3.moving_speed = 40
      self.poppy.m5.moving_speed = 40

      self.poppy.m1.goal_position = 5
      time.sleep(2)

      self.poppy.m2.goal_position = 30
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      time.sleep(2)

      self.poppy.m1.goal_position = -5
      time.sleep(2)

   def WriteH(self):
      self.poppy.m1.goal_position = 5
      time.sleep(0.5)
      self.poppy.m5.goal_position = -90
      time.sleep(0.5)
      self.poppy.m3.goal_position = 90
      time.sleep(0.5)

      self.poppy.m1.moving_speed = 40
      self.poppy.m2.moving_speed = 40
      self.poppy.m3.moving_speed = 40
      self.poppy.m5.moving_speed = 40

      self.poppy.m2.goal_position = 30
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      time.sleep(1)

      self.poppy.m3.goal_position = 0
      time.sleep(0.5)
      self.poppy.m5.goal_position = 0
      time.sleep(0.5)
      self.poppy.m2.goal_position = 0
      time.sleep(0.5)

      self.poppy.m1.goal_position = -5
      time.sleep(0.5)
      self.poppy.m5.goal_position = -90
      time.sleep(0.5)
      self.poppy.m3.goal_position = 90
      time.sleep(0.5)

      self.poppy.m2.goal_position = 30
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      time.sleep(1)

      self.poppy.m3.goal_position = 0
      time.sleep(0.5)
      self.poppy.m5.goal_position = 0
      time.sleep(0.5)
      self.poppy.m2.goal_position = 0
      time.sleep(0.5)

      self.poppy.m6.goal_position = -15
      time.sleep(1)
      self.poppy.m1.goal_position = 0
      time.sleep(0.5)
      self.poppy.m5.goal_position = -100
      time.sleep(0.5)
      self.poppy.m3.goal_position = 100
      time.sleep(0.5)
      self.poppy.m1.goal_position = 6
      time.sleep(0.5)
      self.poppy.m1.goal_position = -6
      time.sleep(0.5)

   def WriteI(self):
      self.poppy.m1.goal_position = 0
      self.poppy.m5.goal_position = -90
      time.sleep(0.5)
      self.poppy.m3.goal_position = 90
      time.sleep(2)

      self.poppy.m2.moving_speed = 40
      self.poppy.m3.moving_speed = 40
      self.poppy.m5.moving_speed = 40

      self.poppy.m2.goal_position = 30
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      time.sleep(2)

   def WriteJ(self):
      self.poppy.m1.goal_position = 5
      time.sleep(0.5)
      self.poppy.m5.goal_position = -90
      time.sleep(0.5)
      self.poppy.m3.goal_position = 90
      time.sleep(0.5)

      self.poppy.m1.moving_speed = 40
      self.poppy.m2.moving_speed = 40
      self.poppy.m3.moving_speed = 40
      self.poppy.m5.moving_speed = 40

      self.poppy.m1.goal_position = -5
      time.sleep(2)

      self.poppy.m2.goal_position = 30
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      time.sleep(2)

   def WriteK(self):
      self.poppy.m1.goal_position = 0
      self.poppy.m5.goal_position = -90
      time.sleep(0.5)
      self.poppy.m3.goal_position = 90
      time.sleep(2)

      self.poppy.m1.moving_speed = 40
      self.poppy.m2.moving_speed = 40
      self.poppy.m3.moving_speed = 40
      self.poppy.m5.moving_speed = 40

      self.poppy.m2.goal_position = 30
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      time.sleep(2)

      self.poppy.m2.goal_position = 15
      self.poppy.m5.goal_position = -75
      self.poppy.m3.goal_position = 75
      time.sleep(2)

      self.poppy.m1.goal_position = -5
      self.poppy.m2.goal_position = 30
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      time.sleep(2)

      self.poppy.m1.goal_position = 0
      self.poppy.m2.goal_position = 15
      self.poppy.m5.goal_position = -75
      self.poppy.m3.goal_position = 75
      time.sleep(2)

      self.poppy.m1.goal_position = -5
      self.poppy.m2.goal_position = 0
      self.poppy.m5.goal_position = -90
      self.poppy.m3.goal_position = 90
      time.sleep(2)
      
   def WriteL(self):
      self.poppy.m1.goal_position = -5
      time.sleep(0.5)
      self.poppy.m5.goal_position = -90
      time.sleep(0.5)
      self.poppy.m3.goal_position = 90
      time.sleep(0.5)

      self.poppy.m1.moving_speed = 40
      self.poppy.m2.moving_speed = 40
      self.poppy.m3.moving_speed = 40
      self.poppy.m5.moving_speed = 40

      self.poppy.m1.goal_position = 5
      time.sleep(2)
      
      self.poppy.m2.goal_position = 30
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      time.sleep(2)

   def WriteM(self):
      self.poppy.m1.goal_position = 5
      time.sleep(0.5)
      self.poppy.m5.goal_position = -90
      time.sleep(0.5)
      self.poppy.m3.goal_position = 90
      time.sleep(0.5)

      self.poppy.m1.moving_speed = 40
      self.poppy.m2.moving_speed = 40
      self.poppy.m3.moving_speed = 40
      self.poppy.m5.moving_speed = 40

      self.poppy.m2.goal_position = 30
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      time.sleep(2)

      self.poppy.m1.goal_position = 0
      self.poppy.m2.goal_position = 15
      self.poppy.m5.goal_position = -75
      self.poppy.m3.goal_position = 75
      time.sleep(2)

      self.poppy.m1.moving_speed = 100
      self.poppy.m2.moving_speed = 100
      self.poppy.m3.moving_speed = 100
      self.poppy.m5.moving_speed = 100

      self.poppy.m1.goal_position = -5
      self.poppy.m2.goal_position = 30
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      time.sleep(2)

      self.poppy.m2.goal_position = 0
      self.poppy.m5.goal_position = -90
      self.poppy.m3.goal_position = 90
      time.sleep(2)

   def WriteN(self):
      self.poppy.m1.goal_position = 5
      time.sleep(0.5)
      self.poppy.m5.goal_position = -90
      time.sleep(0.5)
      self.poppy.m3.goal_position = 90
      time.sleep(0.5)

      self.poppy.m1.moving_speed = 40
      self.poppy.m2.moving_speed = 40
      self.poppy.m3.moving_speed = 40
      self.poppy.m5.moving_speed = 40

      self.poppy.m2.goal_position = 30
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      time.sleep(2)

      self.poppy.m1.goal_position = -5
      self.poppy.m2.goal_position = 0
      self.poppy.m5.goal_position = -90
      self.poppy.m3.goal_position = 90
      time.sleep(2)

      self.poppy.m2.goal_position = 30
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      time.sleep(2)

   def WriteO(self):
      self.poppy.m1.goal_position = -5
      self.poppy.m5.goal_position = -90
      time.sleep(0.5)
      self.poppy.m3.goal_position = 90
      time.sleep(2)

      self.poppy.m2.moving_speed = 40
      self.poppy.m3.moving_speed = 40
      self.poppy.m5.moving_speed = 40

      self.poppy.m1.goal_position = 5
      time.sleep(2)

      self.poppy.m2.goal_position = 30
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      time.sleep(2)

      self.poppy.m1.goal_position = -5
      time.sleep(2)

      self.poppy.m5.goal_position = -90
      time.sleep(2)
      self.poppy.m3.goal_position = 90
      time.sleep(2)

   def WriteP(self):
      self.poppy.m1.goal_position = 0
      self.poppy.m5.goal_position = -90
      time.sleep(0.5)
      self.poppy.m3.goal_position = 90
      time.sleep(2)

      self.poppy.m2.moving_speed = 40
      self.poppy.m3.moving_speed = 40
      self.poppy.m5.moving_speed = 40

      self.poppy.m2.goal_position = 30
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      time.sleep(2)

      self.poppy.m1.goal_position = -10
      time.sleep(2)

      self.poppy.m2.goal_position = 15
      self.poppy.m5.goal_position = -75
      self.poppy.m3.goal_position = 75
      time.sleep(2)

      self.poppy.m1.goal_position = 5
      time.sleep(2)

   def WriteQ(self):
      self.poppy.m1.goal_position = -5
      self.poppy.m5.goal_position = -90
      time.sleep(0.5)
      self.poppy.m3.goal_position = 90
      time.sleep(2)

      self.poppy.m2.moving_speed = 40
      self.poppy.m3.moving_speed = 40
      self.poppy.m5.moving_speed = 40

      self.poppy.m1.goal_position = 5
      time.sleep(2)

      self.poppy.m2.goal_position = 30
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      time.sleep(2)

      self.poppy.m1.goal_position = -5
      time.sleep(2)

      self.poppy.m5.goal_position = -90
      self.poppy.m3.goal_position = 90
      time.sleep(2)

      self.poppy.m1.moving_speed = 40
      self.poppy.m2.moving_speed = 40
      self.poppy.m3.moving_speed = 40
      self.poppy.m5.moving_speed = 40

      self.poppy.m1.goal_position = 0
      self.poppy.m2.goal_position = 15
      self.poppy.m5.goal_position = -75
      self.poppy.m3.goal_position = 75
      time.sleep(2)

      self.poppy.m1.goal_position = -10
      self.poppy.m2.goal_position = -15
      self.poppy.m5.goal_position = -105
      self.poppy.m3.goal_position = 105
      time.sleep(2)

   def WriteR(self):
      self.poppy.m1.goal_position = 0
      self.poppy.m5.goal_position = -90
      time.sleep(0.5)
      self.poppy.m3.goal_position = 90
      time.sleep(2)

      self.poppy.m2.moving_speed = 40
      self.poppy.m3.moving_speed = 40
      self.poppy.m5.moving_speed = 40

      self.poppy.m2.goal_position = 30
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      time.sleep(2)

      self.poppy.m1.goal_position = -10
      time.sleep(2)

      self.poppy.m2.goal_position = 15
      self.poppy.m5.goal_position = -75
      self.poppy.m3.goal_position = 75
      time.sleep(2)

      self.poppy.m1.goal_position = 5
      time.sleep(2)

      self.poppy.m1.goal_position = -10
      time.sleep(2)

   def WriteS(self):
      self.poppy.m1.goal_position = 5
      time.sleep(0.5)
      self.poppy.m5.goal_position = -90
      time.sleep(0.5)
      self.poppy.m3.goal_position = 90
      time.sleep(0.5)

      self.poppy.m2.moving_speed = 40
      self.poppy.m3.moving_speed = 40
      self.poppy.m5.moving_speed = 40

      self.poppy.m1.goal_position = -5
      time.sleep(2)

      self.poppy.m2.goal_position = 15
      self.poppy.m5.goal_position = -75
      self.poppy.m3.goal_position = 75
      time.sleep(2)

      self.poppy.m1.goal_position = 5
      time.sleep(2)

      self.poppy.m2.goal_position = 30
      self.poppy.m5.goal_position = -90
      self.poppy.m3.goal_position = 90
      time.sleep(2)

      self.poppy.m1.goal_position = -5
      time.sleep(2)

   def WriteT(self):
      self.poppy.m1.goal_position = 0
      self.poppy.m5.goal_position = -90
      time.sleep(0.5)
      self.poppy.m3.goal_position = 90
      time.sleep(2)

      self.poppy.m2.moving_speed = 40
      self.poppy.m3.moving_speed = 40
      self.poppy.m5.moving_speed = 40

      self.poppy.m2.goal_position = 30
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      time.sleep(2)

      self.poppy.m1.goal_position = -10
      time.sleep(1)
      self.poppy.m1.goal_position = 10
      time.sleep(1)

   def WriteU(self):
      self.poppy.m1.goal_position = 5
      time.sleep(0.5)
      self.poppy.m5.goal_position = -60
      time.sleep(0.5)
      self.poppy.m3.goal_position = 60
      time.sleep(0.5)
      self.poppy.m2.goal_position = 30
      time.sleep(0.5)

      self.poppy.m2.moving_speed = 40
      self.poppy.m3.moving_speed = 40
      self.poppy.m5.moving_speed = 40
      
      self.poppy.m5.goal_position = -90
      self.poppy.m3.goal_position = 90
      self.poppy.m2.goal_position = 0
      time.sleep(2)

      self.poppy.m1.goal_position = 5
      time.sleep(2)

      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      self.poppy.m2.goal_position = 30
      time.sleep(2)

   def WriteV(self):
      self.poppy.m1.goal_position = 5
      time.sleep(0.5)
      self.poppy.m5.goal_position = -60
      time.sleep(0.5)
      self.poppy.m3.goal_position = 60
      time.sleep(0.5)
      self.poppy.m2.goal_position = 30
      time.sleep(0.5)

      self.poppy.m1.moving_speed = 40
      self.poppy.m2.moving_speed = 40
      self.poppy.m3.moving_speed = 40
      self.poppy.m5.moving_speed = 40

      self.poppy.m1.goal_position = 0
      self.poppy.m5.goal_position = -90
      self.poppy.m3.goal_position = 90
      self.poppy.m2.goal_position = 0
      time.sleep(2)

      self.poppy.m1.goal_position = -5
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      self.poppy.m2.goal_position = 30
      time.sleep(2)

   def WriteW(self):
      self.poppy.m1.goal_position = 10
      time.sleep(0.5)
      self.poppy.m5.goal_position = -60
      time.sleep(0.5)
      self.poppy.m3.goal_position = 60
      time.sleep(0.5)
      self.poppy.m2.goal_position = 30
      time.sleep(0.5)

      self.poppy.m1.moving_speed = 40
      self.poppy.m2.moving_speed = 40
      self.poppy.m3.moving_speed = 40
      self.poppy.m5.moving_speed = 40

      self.poppy.m1.goal_position = 5
      self.poppy.m5.goal_position = -90
      self.poppy.m3.goal_position = 90
      self.poppy.m2.goal_position = 0
      time.sleep(2)

      self.poppy.m1.goal_position = 0
      self.poppy.m5.goal_position = -75
      self.poppy.m3.goal_position = 75
      self.poppy.m2.goal_position = 15
      time.sleep(2)

      self.poppy.m1.goal_position = -5
      self.poppy.m5.goal_position = -90
      self.poppy.m3.goal_position = 90
      self.poppy.m2.goal_position = 0
      time.sleep(2)
      
      self.poppy.m1.goal_position = -10
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      self.poppy.m2.goal_position = 30
      time.sleep(2)

   def WriteX(self):
      self.poppy.m1.goal_position = 5
      time.sleep(0.5)
      self.poppy.m5.goal_position = -90
      time.sleep(0.5)
      self.poppy.m3.goal_position = 90
      time.sleep(0.5)

      self.poppy.m1.moving_speed = 40
      self.poppy.m2.moving_speed = 40
      self.poppy.m3.moving_speed = 40
      self.poppy.m5.moving_speed = 40

      self.poppy.m1.goal_position = -5
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      self.poppy.m2.goal_position = 30
      time.sleep(2)

      self.poppy.m3.goal_position = 0
      time.sleep(0.5)
      self.poppy.m5.goal_position = 0
      time.sleep(0.5)
      self.poppy.m1.goal_position = 0
      time.sleep(0.5)
      self.poppy.m2.goal_position = 0
      time.sleep(0.5)

      self.poppy.m2.moving_speed = 100
      self.poppy.m3.moving_speed = 100
      self.poppy.m5.moving_speed = 100
      
      self.poppy.m1.goal_position = -5
      time.sleep(0.5)
      self.poppy.m5.goal_position = -90
      time.sleep(0.5)
      self.poppy.m3.goal_position = 90
      time.sleep(0.5)

      self.poppy.m1.moving_speed = 40
      self.poppy.m2.moving_speed = 40
      self.poppy.m3.moving_speed = 40
      self.poppy.m5.moving_speed = 40

      self.poppy.m1.goal_position = 5
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      self.poppy.m2.goal_position = 30
      time.sleep(2)

   def WriteY(self):
      self.poppy.m1.goal_position = 0
      time.sleep(0.5)
      self.poppy.m5.goal_position = -90
      time.sleep(0.5)
      self.poppy.m3.goal_position = 90
      time.sleep(0.5)

      self.poppy.m2.moving_speed = 40
      self.poppy.m3.moving_speed = 40
      self.poppy.m5.moving_speed = 40

      self.poppy.m5.goal_position = -75
      self.poppy.m3.goal_position = 75
      self.poppy.m2.goal_position = 15
      time.sleep(2)

      self.poppy.m1.moving_speed = 40
      self.poppy.m2.moving_speed = 40
      self.poppy.m3.moving_speed = 40
      self.poppy.m5.moving_speed = 40

      self.poppy.m1.goal_position = 5
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      self.poppy.m2.goal_position = 30
      time.sleep(2)

      self.poppy.m1.goal_position = 0
      self.poppy.m5.goal_position = -75
      self.poppy.m3.goal_position = 75
      self.poppy.m2.goal_position = 15
      time.sleep(2)

      self.poppy.m1.goal_position = -5
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      self.poppy.m2.goal_position = 30
      time.sleep(2)

   def WriteZ(self):
      self.poppy.m1.goal_position = -5
      time.sleep(0.5)
      self.poppy.m5.goal_position = -90
      time.sleep(0.5)
      self.poppy.m3.goal_position = 90
      time.sleep(0.5)

      self.poppy.m2.moving_speed = 40
      self.poppy.m3.moving_speed = 40
      self.poppy.m5.moving_speed = 40

      self.poppy.m1.goal_position = 5
      time.sleep(2)

      self.poppy.m1.moving_speed = 40
      self.poppy.m2.moving_speed = 40
      self.poppy.m3.moving_speed = 40
      self.poppy.m5.moving_speed = 40

      self.poppy.m1.goal_position = -5
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      self.poppy.m2.goal_position = 30
      time.sleep(2)

      self.poppy.m1.moving_speed = 100

      self.poppy.m1.goal_position = 5
      time.sleep(2)