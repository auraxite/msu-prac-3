def walk2d():
    (x, y) = yield (0, 0)
    while (x, y):
        # не понял

gen = walk2d()
gen.send((1,0))
gen.send((0,1))
gen.send((-1,0))
gen.send((0,-1))