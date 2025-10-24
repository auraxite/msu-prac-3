from itertools import tee, islice

def slide(seq, n):
    seq = iter(seq)
    while True:
        seq, window = tee(seq)
        win = list(islice(window, n))
        if not win:
            break
        yield from win
        next(seq, None)

import sys
exec(sys.stdin.read())