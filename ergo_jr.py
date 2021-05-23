import logging, sys
from pypot.creatures import PoppyErgoJr
import time

logging.basicConfig(stream=sys.stderr, level="DEBUG")

poppy = PoppyErgoJr(camera='dummy')

poppy.m3.compliant = False
poppy.m3.goal_position = 0

for _ in range(3):
    poppy.m3.goal_position = 30
    time.sleep(0.5)
    poppy.m3.goal_position = -30
    time.sleep(0.5)