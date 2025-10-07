from decimal import Decimal
from fractions import Fraction

def esum(N, one):
    e = one
    cur = one
    for i in range(1, N+1):
        cur *= i
        e += one / cur
    return e

print(esum(100, Decimal('1')))