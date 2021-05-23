import numpy as np
from pypot.creatures import PoppyErgoJr

poppy = PoppyErgoJr(camera='dummy')

poppy.rest_posture.start()

[m.present_position for m in poppy.motors]