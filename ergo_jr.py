from pypot.creatures import PoppyErgoJr

poppy = PoppyErgoJr(camera='dummy')

poppy.m1.compliant = False
poppy.m2.compliant = False
poppy.m3.compliant = False

print(poppy.m3.present_position)

poppy.m1.goal_position = 10
poppy.m2.goal_position = 20
poppy.m3.goal_position = 30