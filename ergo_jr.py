from pypot.creatures import PoppyErgoJr

poppy = PoppyErgoJr(camera='dummy')

poppy.m1.compliant = False
poppy.m2.compliant = False
poppy.m3.compliant = False

poppy.m1.goal_position = 0
poppy.m2.goal_position = 0
poppy.m3.goal_position = 0