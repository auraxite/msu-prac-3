from math import comb

def pastri(n, filler):
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(str(comb(i, j)))
        triangle.append(filler.join(row))

    width = len(triangle[-1])
    center = []
    for line in triangle:
        empty = width - len(line)
        left = empty // 2
        right = empty - left
        center.append(filler * left + line + filler * right)

    return '\n'.join(center)

# print(pastri(7, '_'))
# print(pastri(8, '_'))