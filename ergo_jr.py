import numpy as np
import matplotlib.pyplot as plt
from pypot.creatures import PoppyErgoJr

poppy = PoppyErgoJr(camera='dummy')

poppy.rest_posture.start()

[m.present_position for m in poppy.motors]