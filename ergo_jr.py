from pypot.creatures import PoppyErgoJr
from .poppy_ergo_jr import PoppyErgoJr

poppy = PoppyErgoJr(camera='dummy')

poppy.m1.compliant = False
poppy.m2.compliant = False
poppy.m3.compliant = False
poppy.m4.compliant = False
poppy.m5.compliant = False
poppy.m6.compliant = False

poppy.m1.goal_position = 10
poppy.m2.goal_position = 20
poppy.m3.goal_position = 30