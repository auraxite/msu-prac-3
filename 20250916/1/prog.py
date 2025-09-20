A = '-'
B = '-'
C = '-'

n = int(input())

if n % 25 == 0:
    if n % 2 == 0:
        A = '+'
    else:
        B = '+'

if n % 8 == 0:
    C = '+'

print('A', A, 'B', B, 'C', C)