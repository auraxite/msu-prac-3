from collections import UserString

class DivStr(UserString):
    def __init__(self, s=''):
        super().__init__(s)
    
    def __floordiv__(self, k):
        m = len(self) // k
        return (self[i*m:(i+1)*m] for i in range(k))
    
    def __mod__(self, k):
        return self[(len(self)//k)*k:]
    
import sys
exec(sys.stdin.read())