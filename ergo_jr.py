from pypot.creatures import PoppyErgoJr
import time

poppy = PoppyErgoJr(camera='dummy')

for m in poppy.motors:
    print(m.present_position)