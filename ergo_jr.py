from pypot.creatures import PoppyErgoJr
import time

poppy = PoppyErgoJr(camera='dummy')

for m in poppy.motors:
    m.compliant = True

poppy.goto_position({'m1': 0.,
                'm2': -60.,
                'm3': 55.,
                'm4': 0.,
                'm5': -55.,
                'm6': 60.}, 2., wait=True)