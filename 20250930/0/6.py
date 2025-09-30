def f_parent(a, b):
    def f_child(x):
        return a*x + b
    return f_child

def gen_adders(n):
    adders = []
    for i in range(n):
        def fun(x):
            return x + i
        adders.append(fun)
    return adders