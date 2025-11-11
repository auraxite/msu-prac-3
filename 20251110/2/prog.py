class InputError(Exception):
    pass

class NoTriangle(Exception):
    pass

def calcTriangleArea(s):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(s)
    except:
        raise InputError
    else:
        a = abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2
        if a == 0:
            raise NoTriangle
        return f'{a:.2f}'

while True:
    try:
        print(calcTriangleArea(input()))
    except InputError:
        print('Invalid input')
    except NoTriangle:
        print('Not a triangle')
    else:
        break