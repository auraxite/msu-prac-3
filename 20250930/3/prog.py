from math import *

def Calc(s: str, t: str, u: str):
    def F(x):
        new_x = eval(s)
        new_y = eval(t)
        x, y = new_x, new_y
        return eval(u)
    return F

stu = eval('(' + input() + ')')
F = Calc(*stu)
print(F(eval(input())))

'''
F = Calc("x", "2*x+1", "x/y")
print(F(100))

F = Calc("sin(x)**2", "cos(x)**2", "x+y")
print(F(123))

cos = lambda x: -x
sin = lambda x: x/2
print(F(123))

F = Calc("len(x)", "max(x)", "x+y")
print(F((1,2,34,56,12,3,1,7)))
'''