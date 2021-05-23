from pypot.creatures import PoppyErgoJr

poppy = PoppyErgoJr(camera='dummy')

for m in poppy.motors:
    m.compliant = False
    m.goto_position(30, 0.5, wait=True)