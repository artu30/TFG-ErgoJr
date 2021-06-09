from pypot.creatures import PoppyErgoJr

poppy = PoppyErgoJr(camera='dummy')

poppy.m1.compliant = True
poppy.m2.compliant = True
poppy.m3.compliant = True

print(poppy.m3.current_position)

poppy.m1.goal_position = 10
poppy.m2.goal_position = 20
poppy.m3.goal_position = 30