from fractions import Fraction

def is_solution(s, w, dA, cA, dB, cB):
    A = sum(cA[i] * s ** (dA - i) for i in range(dA + 1))
    B = sum(cB[i] * s ** (dB - i) for i in range(dB + 1))
    return (B != 0) and (A / B == w)

inp = [x.strip() for x in input().split(',')]
s, w = map(Fraction, inp[:2])
dA = int(inp[2])
cA = list(map(Fraction, inp[3:3 + dA + 1]))
dB = int(inp[3 + dA + 1])
cB = list(map(Fraction, inp[4 + dA + 1:]))

print(is_solution(s, w, dA, cA, dB, cB))