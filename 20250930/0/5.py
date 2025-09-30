from math import sin, cos, tan

def MINF(*f_args):
    def fun(x=0.5):
        return min([f(x) for f in f_args])
    return fun

print(MINF(sin,cos,tan))

g = MINF(sin, cos, tan, lambda x: x**2)
print(g.__closure__[0].cell_contents[0])

