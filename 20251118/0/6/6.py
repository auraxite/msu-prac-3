import pickle

class SerCls:
    def __init__(self, lst = [], dct = {}, num = 0, st = ""):
        self.lst = lst
        self.dct = dct
        self.num = num
        self.st = st

ser = SerCls(['a', 'b', 'c'], {'1': 1, '2': 2}, 1, 'a')
tmp = pickle.dumps(ser)
print(tmp)
del ser
ser1 = pickle.loads(tmp)
print(ser1, ser1.lst, ser1.dct, ser1.num, ser1.st)

tmp = pickle.dumps(SerCls)
del SerCls
SerCls = pickle.loads(tmp)
ser2 = SerCls(['a', 'b', 'c'], {'1': 1, '2': 2}, 1, 'a')
print(ser2, ser2.__dir__)