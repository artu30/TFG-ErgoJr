from pypot.creatures import PoppyErgoJr

poppy = PoppyErgoJr(camera='dummy')

poppy.rest_posture.start()
poppy.m1.goal_position = -20