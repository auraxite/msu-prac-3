def multicall(times):
    def decorator(fun):
        def newfun(*args):
            return [fun(*args) for i in range(times)]
        return newfun
    return decorator

@multicall(5)
def simplefun(N):
    return N*2+1

print(*simplefun(4))