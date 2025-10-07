from math import sin

def scale(a, b, A, B, x):
    return (x - a) * (B - A) / (b - a) + A

W, H = eval(input())
A, B = eval(input())
screen = [['.']*W for _ in range(H)]
for line in range(0, W):
    x = scale(0, W - 1, A, B, line)
    y = sin(x)
    k = round(scale(-1, 1, 0, H - 1, y))
    screen[H - k - 1][line] = '*'
screen = '\n'.join(''.join(line) for line in screen)
print(screen)