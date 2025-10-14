from collections import Counter
from timeit import Timer

def counter_f(str: str) -> Counter:
    c = Counter(str.split())
    return c

def setdefault_f(str: str) -> Counter:
    d = {}
    for w in str.split():
        d[w] = d.setdefault(w, 0) + 1
    return d

str = input()

timer_counter = Timer("c = counter_f(str)", globals=globals())
res = timer_counter.autorange()
print('c:', res)

timer_setdefault = Timer("d = setdefault_f(str)", globals=globals())
res = timer_setdefault.autorange()
print('d:', res)
