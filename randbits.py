from random import sample

def randbits(p, n):
    if not (1 <= n <= p):
        return 0

    bits = sample(range(0, p), n)
    x = 0
    for b in bits:
        x |= 1 << b
    return x

# print(*[randbits(6, i) for i in range(1, 10)])