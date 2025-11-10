class A:
    v = 1

class B(A):
    v = 2

b = B()
print(b.v)
b.v = 3
print(b.v)