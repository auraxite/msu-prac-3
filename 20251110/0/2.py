class A:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        return self.__class__(self.val + other.val)
    def __str__(self):
        return f"<{self.val}>"
    
a = A(3)
print(a)

class B(A):
    def __str__(self):
        return f">{self.val}<"
    
b = B(4)
print(b)
c = a + b
print(c)
print(a + B(10))