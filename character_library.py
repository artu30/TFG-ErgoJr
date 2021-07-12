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
      self.poppy.m5.goal_position = -110
      time.sleep(0.5)
      self.poppy.m3.goal_position = 110
      time.sleep(2)

   def LeftInitPos(self):
      self.poppy.m1.goal_position = 2
      time.sleep(0.5)
      self.poppy.m5.goal_position = -110
      time.sleep(0.5)
      self.poppy.m3.goal_position = 110
      time.sleep(2)

   def LeftCenterPos(self):
      self.poppy.m1.goal_position = 2
      time.sleep(0.5)
      self.poppy.m5.goal_position = -78
      time.sleep(0.5)
      self.poppy.m3.goal_position = 78
      time.sleep(2)

   def LeftTopPos(self):
      self.poppy.m1.goal_position = -2
      time.sleep(0.5)
      self.poppy.m2.goal_position = 10
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      time.sleep(2)

   def RightInitPos(self):
      self.poppy.m1.goal_position = -2
      time.sleep(0.5)
      self.poppy.m5.goal_position = -110
      time.sleep(0.5)
      self.poppy.m3.goal_position = 110
      time.sleep(2)

   def RightCenterPos(self):
      self.poppy.m1.goal_position = 2
      time.sleep(0.5)
      self.poppy.m5.goal_position = -78
      time.sleep(0.5)
      self.poppy.m3.goal_position = 78
      time.sleep(2)

   def RightTopPos(self):
      self.poppy.m1.goal_position = 2
      time.sleep(0.5)
      self.poppy.m2.goal_position = 10
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      time.sleep(2)

   def GoUp(self):
      self.poppy.m2.goal_position = 8
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      time.sleep(2)

   def GoDown(self):
      self.poppy.m2.goal_position = 0
      self.poppy.m5.goal_position = -110
      self.poppy.m3.goal_position = 110
      time.sleep(2)

   def CenterUpPos(self):
      self.poppy.m1.goal_position = 0
      time.sleep(0.5)
      self.poppy.m5.goal_position = -78
      time.sleep(0.5)
      self.poppy.m3.goal_position = 78
      time.sleep(2)

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

      self.CenterUpPos()

      self.poppy.m1.goal_position = 4
      time.sleep(0.5)
      self.poppy.m1.goal_position = -4
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

      self.poppy.m1.goal_position = 3
      time.sleep(2)

      self.GoUp()

      self.poppy.m1.goal_position = -5
      time.sleep(2)

      self.PencilUp()

   def WriteD(self):
      self.CenterInitPos()

      self.GoUp()

      self.poppy.m1.goal_position = -8
      self.poppy.m2.goal_position = 10
      self.poppy.m5.goal_position = -75
      self.poppy.m3.goal_position = 75
      time.sleep(2)

      self.poppy.m1.goal_position = 5
      self.poppy.m2.goal_position = 0
      self.poppy.m5.goal_position = -90
      self.poppy.m3.goal_position = 90
      time.sleep(2)

      self.PencilUp()

   def WriteE(self):
      self.RightInitPos()

      self.poppy.m1.goal_position = 3
      time.sleep(2)

      self.GoUp()

      self.poppy.m1.goal_position = -5
      time.sleep(2)

      self.PencilUp()

      self.CenterUpPos()

      self.poppy.m1.goal_position = -3
      time.sleep(0.5)

      self.poppy.m1.goal_position = 2
      time.sleep(0.5)

      self.PencilUp()

   def WriteF(self):
      self.CenterInitPos()

      self.GoUp()

      self.poppy.m1.goal_position = -8
      time.sleep(2)

      self.PencilUp()

      self.CenterUpPos()

      self.poppy.m1.goal_position = -5
      time.sleep(0.5)

      self.poppy.m1.goal_position = 0
      time.sleep(0.5)

      self.PencilUp()

   def WriteG(self):
      self.CenterUpPos()
      
      self.poppy.m1.goal_position = -3
      time.sleep(2)

      self.RightInitPos()

      self.poppy.m1.goal_position = 3
      time.sleep(2)

      self.GoUp()

      self.poppy.m1.goal_position = -5
      time.sleep(2)

      self.PencilUp()

   def WriteH(self):
      self.LeftInitPos()

      self.GoUp()

      self.PencilUp()

      self.RightInitPos()

      self.GoUp()

      self.PencilUp()

      self.CenterUpPos()

      self.poppy.m1.goal_position = -3
      time.sleep(0.5)

      self.poppy.m1.goal_position = 1
      time.sleep(0.5)

      self.PencilUp()

   def WriteI(self):
      self.CenterInitPos()

      self.GoUp()

      self.PencilUp()

   def WriteJ(self):
      self.LeftInitPos()

      self.poppy.m1.goal_position = -2
      time.sleep(2)

      self.GoUp()

      self.PencilUp()

   def WriteK(self):
      self.CenterInitPos()

      self.GoUp()

      self.PencilUp()

      self.CenterUpPos()

      self.poppy.m1.goal_position = -4
      self.poppy.m2.goal_position = 10
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      time.sleep(2)

      self.PencilUp()

      self.CenterUpPos()

      self.poppy.m1.goal_position = -4
      self.poppy.m2.goal_position = 0
      self.poppy.m5.goal_position = -90
      self.poppy.m3.goal_position = 90
      time.sleep(2)
      
   def WriteL(self):
      self.RightInitPos()

      self.poppy.m1.goal_position = 2
      time.sleep(2)

      self.GoUp()

      self.PencilUp()

   def WriteM(self):
      self.LeftInitPos()

      self.GoUp()

      self.poppy.m1.goal_position = 0
      self.poppy.m2.goal_position = 0
      self.poppy.m5.goal_position = -110
      self.poppy.m3.goal_position = 110
      time.sleep(2)
      
      self.GoUp()

      self.poppy.m1.goal_position = 4
      self.poppy.m2.goal_position = 0
      self.poppy.m5.goal_position = -110
      self.poppy.m3.goal_position = 110
      time.sleep(2)

      self.PencilUp()

   def WriteN(self):
      self.LeftInitPos()

      self.GoUp()

      self.poppy.m1.goal_position = 0
      self.poppy.m2.goal_position = 0
      self.poppy.m5.goal_position = -110
      self.poppy.m3.goal_position = 110
      time.sleep(2)
      
      self.GoUp()

      self.PencilUp()

   def WriteO(self):
      self.RightInitPos()

      self.poppy.m1.goal_position = 3
      self.poppy.m5.goal_position = -90
      self.poppy.m3.goal_position = 90
      time.sleep(2)

      self.GoUp()

      self.poppy.m1.goal_position = -3
      time.sleep(2)
      self.poppy.m5.goal_position = -100
      self.poppy.m3.goal_position = 100
      time.sleep(2)

      self.GoDown()

      self.PencilUp()

   def WriteP(self):
      self.CenterInitPos()

      self.GoUp()

      self.poppy.m1.goal_position = -5
      time.sleep(2)

      self.poppy.m2.goal_position = 2
      self.poppy.m5.goal_position = -75
      self.poppy.m3.goal_position = 75
      time.sleep(2)

      self.poppy.m1.goal_position = 3
      time.sleep(2)

      self.PencilUp()

   def WriteQ(self):
      self.RightInitPos()

      self.poppy.m1.goal_position = 3
      self.poppy.m5.goal_position = -90
      self.poppy.m3.goal_position = 90
      time.sleep(2)

      self.GoUp()

      self.poppy.m1.goal_position = -3
      time.sleep(2)
      self.poppy.m5.goal_position = -100
      self.poppy.m3.goal_position = 100
      time.sleep(2)

      self.GoDown()

      self.PencilUp()

      self.CenterUpPos()

      self.poppy.m1.goal_position = -4
      self.poppy.m5.goal_position = -110
      self.poppy.m3.goal_position = 110
      time.sleep(2)

      self.PencilUp()

   def WriteR(self):
      self.CenterInitPos()

      self.GoUp()

      self.poppy.m1.goal_position = -5
      time.sleep(2)

      self.poppy.m2.goal_position = 2
      self.poppy.m5.goal_position = -75
      self.poppy.m3.goal_position = 75
      time.sleep(2)

      self.poppy.m1.goal_position = 3
      time.sleep(2)

      self.PencilUp()

      self.CenterUpPos()

      self.poppy.m1.goal_position = -4
      self.poppy.m5.goal_position = -110
      self.poppy.m3.goal_position = 110
      time.sleep(2)

      self.PencilUp()

   def WriteS(self):
      self.LeftInitPos()

      self.poppy.m1.goal_position = -1
      time.sleep(2)

      self.poppy.m5.goal_position = -72
      self.poppy.m3.goal_position = 72
      time.sleep(2)

      self.poppy.m1.goal_position = 4
      time.sleep(2)

      self.GoUp()

      self.poppy.m1.goal_position = -3
      time.sleep(2)

      self.PencilUp()

   def WriteT(self):
      self.CenterInitPos()

      self.GoUp()

      self.poppy.m1.goal_position = 4
      time.sleep(0.5)
      self.poppy.m1.goal_position = -4
      time.sleep(0.5)

      self.PencilUp()

   def WriteU(self):
      self.LeftTopPos()

      self.GoDown()

      self.poppy.m1.goal_position = 3
      time.sleep(2)

      self.GoUp()

      self.PencilUp()

   def WriteV(self):
      self.LeftTopPos()

      self.poppy.m1.goal_position = 0
      self.poppy.m2.goal_position = 0
      self.poppy.m5.goal_position = -110
      self.poppy.m3.goal_position = 110
      time.sleep(2)

      self.RightTopPos()

      self.PencilUp()

   def WriteW(self):
      self.LeftTopPos()

      self.GoDown()

      self.poppy.m1.goal_position = 0
      self.poppy.m2.goal_position = 10
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      time.sleep(2)
      
      self.GoDown()

      self.poppy.m1.goal_position = 4
      self.poppy.m2.goal_position = 10
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      time.sleep(2)

      self.PencilUp()

   def WriteX(self):
      self.LeftInitPos()

      self.poppy.m1.goal_position = -4
      self.poppy.m2.goal_position = 10
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      time.sleep(2)

      self.PencilUp()

      self.RightInitPos()

      self.poppy.m1.goal_position = 4
      self.poppy.m2.goal_position = 10
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      time.sleep(2)

      self.PencilUp()

   def WriteY(self):
      self.LeftTopPos()

      self.poppy.m1.goal_position = 0
      self.poppy.m2.goal_position = 0
      self.poppy.m5.goal_position = -75
      self.poppy.m3.goal_position = 75
      time.sleep(2)

      self.RightTopPos()

      self.PencilUp()

      self.CenterUpPos()

      self.GoDown()

      self.PencilUp()

   def WriteZ(self):
      self.RightInitPos()

      self.poppy.m1.goal_position = 2

      self.poppy.m1.goal_position = -3
      self.poppy.m2.goal_position = 10
      self.poppy.m5.goal_position = -60
      self.poppy.m3.goal_position = 60
      time.sleep(2)

      self.poppy.m1.goal_position = 4
      time.sleep(2)

      self.PencilUp()