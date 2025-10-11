from decimal import Decimal, getcontext
from fractions import Fraction

getcontext().prec = 6969

x1, y1, x2, y2, x3, y3 = [Fraction(el.strip()) for el in input().split(',')]

s = Fraction(1, 2) * abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))

res = Decimal(s.numerator) / Decimal(s.denominator)

print(format(res, 'f'))