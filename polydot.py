def info(dots, dot):
    dots = list(dots)
    n = len(dots)

    # --- 1. Периметр ---
    # пары последовательных точек + замыкание многоугольника
    pairs = zip(dots, dots[1:] + dots[:1])
    perim = sum(((x2 - x1)**2 + (y2 - y1)**2) ** 0.5 for (x1, y1), (x2, y2) in pairs)

    # --- 2. Проверка выпуклости ---
    crosses = []
    triples = zip(dots, dots[1:] + dots[:1], dots[2:] + dots[:2])
    for (x1, y1), (x2, y2), (x3, y3) in triples:
        cross = (x2 - x1)*(y3 - y2) - (y2 - y1)*(x3 - x2)
        if abs(cross) > 1e-12:
            crosses.append(cross > 0)
    convex = all(crosses) or not any(crosses)

    # --- 3. Проверка принадлежности точки ---
    x, y = dot
    inside = False
    edges = zip(dots, dots[1:] + dots[:1])
    for (x1, y1), (x2, y2) in edges:
        if (y1 > y) != (y2 > y):
            x_int = (x2 - x1) * (y - y1) / (y2 - y1 + 1e-18) + x1
            if x < x_int:
                inside = not inside
        dx, dy = x2 - x1, y2 - y1
        if abs((x - x1)*dy - (y - y1)*dx) < 1e-9:
            if min(x1, x2) - 1e-9 <= x <= max(x1, x2) + 1e-9 and \
               min(y1, y2) - 1e-9 <= y <= max(y1, y2) + 1e-9:
                inside = True
                break

    return perim, convex, inside

