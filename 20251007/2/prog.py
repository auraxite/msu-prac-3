import math

def scale(a, b, A, B, i): # переводит число i из диапазона [a, b] в диапазон [A, B]
    if b == a:
        return (A + B) / 2
    return (i - a) * (B - A) / (b - a) + A

W, H, A, B, expr = input().split()
W, H, A, B = int(W), int(H), float(A), float(B)

xs = [scale(0, W - 1, A, B, i) for i in range(W)]
ys = [eval(expr, {'x': x, '__builtins__': None, **math.__dict__}) for x in xs]
ymin, ymax = min(ys), max(ys)

screen = [[' ' for _ in range(W)] for _ in range(H)]
for col in range(W):
    y = ys[col]
    row = round(scale(ymin, ymax, H - 1, 0, y))
    if 0 <= row < H:
        screen[row][col] = '*'

print('\n'.join(''.join(row) for row in screen))
