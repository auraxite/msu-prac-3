def istype(typ):
    def decor(*args):
        if any(not isinstance(arg, int) for arg in args):
            raise TypeError("All args must be {typ}")
        return fun(*args)
    return decor

@istype(int)
def fun(a, b):
    return a*2 + b