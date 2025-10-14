from string import ascii_uppercase, ascii_lowercase
import timeit

def count_chars(in1: str) -> tuple[int, int]:
    upper = set()
    lower = set()
    for ch in str:
        if ch in ascii_uppercase:
            upper.add(ch)
        elif ch in ascii_lowercase:
            lower.add(ch)
    return (len(upper), len(lower))

str = input()

timer = timeit.Timer("upper, lower = count_chars(str)", globals=globals())
res = timer.autorange()
print(res)