def objcount(cls):

    original_init = getattr(cls, "__init__", None)
    original_del  = getattr(cls, "__del__", None)

    cls.counter = 0

    def __init__(self, *args, **kwargs):
        cls.counter += 1
        if original_init is not None:
            original_init(self, *args, **kwargs)

    def __del__(self):
        cls.counter -= 1
        if original_del is not None:
            original_del(self)

    cls.__init__ = __init__
    cls.__del__  = __del__

    return cls

import sys
exec(sys.stdin.read())