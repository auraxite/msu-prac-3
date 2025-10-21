import itertools

def raw():
    s = 0
    for i in itertools.count(1):
        s += 1 / i ** 2
        yield s

print(*itertools.islice(itertools.dropwhile(lambda x: x < 1.6, raw()), 10))