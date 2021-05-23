from pypot.creatures import PoppyErgoJr
import time

poppy = PoppyErgoJr(camera='dummy')

for m in poppy.motors:
    m.compliant = False
    m.goal_position = 0