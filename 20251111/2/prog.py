class Num:
    def __get__(self, obj, cls):
        try:
            return obj._val
        except:
            return 0

    def __set__(self, obj, val):
        try:
            obj._val = val.real
        except:
            obj._val = len(val)

import sys
exec(sys.stdin.read())