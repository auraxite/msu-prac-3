class dump(type):
    def __new__(mcls, name, bases, d):
        new_d = {}

        for attr, val in d.items():
            if callable(val):
                def wrap(func_name, func):
                    def wrapper(self, *args, **kwargs):
                        print(f"{func_name}: {args}, {kwargs}")
                        return func(self, *args, **kwargs)
                    return wrapper
                new_d[attr] = wrap(attr, val)
            else:
                new_d[attr] = val

        return super().__new__(mcls, name, bases, new_d)

import sys
exec(sys.stdin.read())