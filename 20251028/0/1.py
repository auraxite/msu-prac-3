class Rectangle:
    rectcnt = 0

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1; self.y1 = y1
        self.x2 = x2; self.y2 = y2
        self.__class__.rectcnt += 1
        self.__setattr__(f"rect_{self.__class__.rectcnt}", self.__class__.rectcnt)

    def __abs__(self):
        return abs((self.x2 - self.x1) * (self.y2 - self.y1))

    def __str__(self):
        return f"({self.x1},{self.y1})({self.x1},{self.y2})({self.x2},{self.y2})({self.x2},{self.y1})"
    
    def __lt__(self, obj):
        return abs(self) < abs(obj)
    
    def __eq__(self, obj):
        return abs(self) == abs(obj)
    
    def __mul__(self, num):
        return (self.__class__(
            x1 = self.x1 * num, y1 = self.y1 * num,
            x2 = self.x2 * num, y2 = self.y2 * num
        ))
    __rmul__ = __mul__

    '''
    def __getitem__(self, i):
        arr = [(self.x1, self.y1), (self.x1, self.y2), (self.x2, self.y2), (self.x2, self.y1)]
        return arr[i % 4]
    '''

    def __bool__(self):
        return abs(self) > 0
    
    def __del__(self):
        self.rectcnt -= 1
        print("GONE (forever)")

r1 = Rectangle(1,2,3,4)
r2 = Rectangle(5,2,1,0)
print(r1 * 5)
print(r1)
print(r1[2])