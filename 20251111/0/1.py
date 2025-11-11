def genf(f):
    def decor(*args):
        print(">", *args)
        res = f(*args)
        print("<", res)
        return res
    return newfun

def fun(a,b):
    return a*2+b

print(fun(2,3))
