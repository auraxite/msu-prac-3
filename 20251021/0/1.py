def gen(n):
    s = 0
    c = 0
    while c <= n:
        yield (s := s + 1 / (c := c + 1) / c)

print(list(gen(5)))