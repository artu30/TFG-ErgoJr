from pypot.creatures import PoppyErgoJr
import time

poppy = PoppyErgoJr(camera='dummy')

for _ in range(3):
    poppy.m3.goto_position(30, 0.5, wait=True)
    poppy.m3.goto_position(-30, 0.5, wait=True)