class A:
    def __init__(self, val):
        self.val = val

class B(A):
    def __init__(self, val):
        print("Do it, A")
        super().__init__(val)
        print(f"<{self.val}>")

b = B(456)