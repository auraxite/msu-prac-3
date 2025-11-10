def div(a, b, eps):
    if abs(b) < eps:
        raise ZeroDivisionError
    else:
        return a / b
    
print(div(1, 100, 0.1))
print(div(1, 0.01, 0.1))