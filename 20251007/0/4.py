from math import sin

W, H = eval(input())
A, B = eval(input())
for line in range(0, H):
    x = A + line * (B - A) / H
    y = sin(x)
    k = round((y + 1) * W / 2)
    print(' '*k, '*')