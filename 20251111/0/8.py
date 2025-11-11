class C:
    counter = 0

    def __get__(self, obj, cls):
        return self.__class__.counter
    
    def __set__(self, obj, val):
        self.__class__.counter = val

c = C()
print(c.counter)

d = C()
print(d.counter)

del c
print(d.counter)
