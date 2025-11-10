A = type(
    'A', (),
    {
        'a': 1,
        '__b' : 2
    }
)
print(A, dir(A))

B = type(
    'B', (A,), 
    {
        'a': 3,
    }
)
print(B, dir(B))

print(A.a, A.__b, B.__a)