from decimal import Decimal
from fractions import Fraction

def multiplier1(x, y, type):
    if type == float:
        return x * y
    elif type == Decimal:
        return Decimal(x) * Decimal(y)
    elif type == Fraction:
        return Fraction(x) * Fraction(y)

def multiplier2(x, y, Type):
    return Type(x) * Type(y)

print(multiplier1(0.1, 0.2, float))
print(multiplier1(Decimal('0.1'), Decimal('0.2'), Decimal))
print(multiplier1(Fraction('1/3'), Fraction('3/5'), Fraction))
print(multiplier2(0.1, 0.2, float))
print(multiplier2(Decimal('0.1'), Decimal('0.2'), Decimal))
print(multiplier2(Fraction('1/3'), Fraction('3/5'), Fraction))