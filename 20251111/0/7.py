class Dsc:
    def __get__(self, obj, cls):
        print(obj.__class__, cls)
        return obj._value
    def __set__(self, obj, value):
        obj._value = value
    def __delete__(self, obj):
        obj._value = None

class A:
    a = Dsc()
    x = 100500
    def __init__(self, name):
        self.a = name
    def __str__(self):
        return f'<{self.data}>'
    
b = A('qwe')

print(Dsc)
print(A)

a_obj = A()
a_obj.a = 123
