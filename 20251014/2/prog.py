from math import *

funcs = {}
lines_c = 0

while True:
    line = input()
    lines_c += 1

    if line.startswith(':'):
        s = line[1:].strip()
        name, *rest = s.split(maxsplit=1)
        if not rest:
            continue
        rest = rest[0]
        words = rest.split()
        if len(words) > 1:
            *params, expr = words
        else:
            params, expr = [], words[0]
        if '(' in rest and ')' in rest and '"' in rest:
            expr = rest[rest.find('('):]
        funcs[name] = (params, expr)

    elif not line.startswith('quit'):
        words = line.split(maxsplit=1)
        name = words[0]
        args = words[1] if len(words) > 1 else ''
        params, expr = funcs[name]
        args = args.split() if len(params) != 1 else [args]

        local = {}
        for param, arg in zip(params, args):
            val = arg.strip()
            if val and (val[0] == val[-1]) and val[0] in ('"', "'"):
                val = val[1:-1]
            else:
                try:
                    val = float(val)
                    if val.is_integer():
                        val = int(val)
                except ValueError:
                    pass
            local[param] = val

        res = eval(expr, globals(), local)
        if isinstance(res, float) and res.is_integer():
            res = int(res)
        print(res)

    else:
        res = line.split(maxsplit=1)[1].strip()
        if (res[0] == res[-1]) and res[0] in ('"', "'"):
            res = res[1:-1]
        print(res.format(len(funcs) + 1, lines_c))
        break
