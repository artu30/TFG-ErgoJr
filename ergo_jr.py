from pypot.creatures import PoppyErgoJr

poppy = PoppyErgoJr(camera='dummy')

poppy.m1.compliant = False
poppy.m2.compliant = False
poppy.m3.compliant = False

poppy.m1.moving_speed = 250
poppy.m2.moving_speed = 250
poppy.m3.moving_speed = 250

print(poppy.m3.present_position)

poppy.m1.goal_position = 0
poppy.m2.goal_position = 0
poppy.m3.goal_position = 0