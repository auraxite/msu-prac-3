rec = []
while line := input().strip():
    x, y, dx, dy, ch = line.split()
    rec.append((int(x), int(y), int(dx), int(dy), ch))

xs, ys = [], []
for x, y, dx, dy, ch in rec:
    if dx == 0 or dy == 0:
        continue

    if dx > 0:
        x1, x2 = x, x + dx - 1
    else:
        x1, x2 = x + dx, x - 1

    if dy > 0:
        y1, y2 = y, y + dy - 1
    else:
        y1, y2 = y + dy, y - 1

    xs += [x1, x2]
    ys += [y1, y2]

xmin, xmax = min(xs), max(xs)
ymin, ymax = min(ys), max(ys)

w = xmax - xmin + 1
h = ymax - ymin + 1

grid = [['.' for _ in range(w)] for _ in range(h)]

for x, y, dx, dy, ch in rec:
    if dx == 0 or dy == 0:
        continue

    if dx > 0:
        x1, x2 = x, x + dx - 1
    else:
        x1, x2 = x + dx, x - 1

    if dy > 0:
        y1, y2 = y, y + dy - 1
    else:
        y1, y2 = y + dy, y - 1

    for y3 in range(y1, y2 + 1):
        for x3 in range(x1, x2 + 1):
            grid[y3 - ymin][x3 - xmin] = ch

for row in grid:
    print(''.join(row))
