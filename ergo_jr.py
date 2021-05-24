try:
    from pypot.creatures import PoppyErgoJr
    poppy = PoppyErgoJr(camera='dummy')
except Exception,e:
    print "could not create poppy object"
    print e

for m in poppy.motors:
    m.compliant = False
    m.goal_position = 0.0