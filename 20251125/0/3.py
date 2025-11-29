class Doubleton(type):
    _instance_1 = None
    _instance_2 = None
    _queue = 0
    def __call__(cls, *args, **kw):
        if cls._queue:
            if cls._instance_1 is None:
                cls._instance_1 = super().__call__(*args, **kw)
            cls._queue = 0
            return cls._instance_1
        else:
            if cls._instance_2 is None:
                 cls._instance_2 = super().__call__(*args, **kw)
            cls._queue = 1
            return cls._instance_2

class S(metaclass=Doubleton):
    A = 3
s, t, q = S(), S(), S()
s.newfield = 100500
t.newfield = 5
print(f"{s.newfield=}, {t.newfield=}, {q.newfield=}")
print(f"{s is t=}")