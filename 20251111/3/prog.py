class Vowel:
    answer = 42
    __slots__ = ['a', 'e', 'i', 'o', 'u', 'y', 'full']

    def __init__(self, **kwargs):
        super().__setattr__("full", False)
        for key, val in kwargs.items():
            setattr(self, key, val)
        self.check_full()

    def __str__(self):
        res = []
        for c in "aeiouy":
            if hasattr(self, c):
                res.append(f"{c}: {getattr(self, c)}")
        return ", ".join(res)

    def __setattr__(self, name, val):
        if name != "full":
            super().__setattr__(name, val)
            if name in "aeiouy":
                self.check_full()

    def check_full(self):
        super().__setattr__("full", all(hasattr(self, c) for c in "aeiouy"))

import sys
exec(sys.stdin.read())