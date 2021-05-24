from pypot.creatures import PoppyErgoJr

poppy = PoppyErgoJr(camera='dummy')

poppy.m3.compliant = False
poppy.m1.goal_position = -20
poppy.m2.goal_position = -30
poppy.m3.goal_position = -30
poppy.m4.goal_position = -30