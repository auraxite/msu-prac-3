def fib(m, n):
    a, b = 0, 1
    for i in range(m + n):
        if i >= m:
            yield b
        a, b = b, a + b

import sys
exec(sys.stdin.read())