from itertools import starmap, product

starmap(str.__add__, product("abcdefgh", "12345678"))