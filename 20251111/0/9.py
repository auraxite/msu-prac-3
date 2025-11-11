class C:
    def __init__(self):
        self._var = 100500

    @property
    def age(self):
        if self._var == 42:
            print('secret value!')
            return -1
        return self._var
    
    @age.setter
    def age(self, value):
        self._var = value
        if value < 128:
            self._var = value
            return
        raise ValueError("Too old!")
    
c = C()
c.age = 1