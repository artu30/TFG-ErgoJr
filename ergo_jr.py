from pypot.creatures import PoppyErgoJr

poppy = PoppyErgoJr(camera='dummy')

for m in poppy.motors:
    m.compliant = False
    print(m.name)