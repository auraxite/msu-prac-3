def itercalc():
    stack = []
    cmd = yield
    while True:
        if cmd == "?":
            if stack:
                yield stack[-1]
            else:
                print("Insufficient stack")
                yield None
        else:
            try:
                n = int(cmd)
                stack.append(n)
                yield None
            except Exception:
                if cmd in {"+", "-", "*", "/"}:
                    if len(stack) < 2:
                        print("Insufficient stack")
                        yield None
                    else:
                        b = stack.pop()
                        a = stack.pop()
                        if cmd == "+":
                            stack.append(a + b)
                        elif cmd == "-":
                            stack.append(a - b)
                        elif cmd == "*":
                            stack.append(a * b)
                        elif cmd == "/":
                            if b == 0:
                                print("Zero division")
                                stack.extend([a, b])
                            else:
                                stack.append(a // b)
                        yield None
                elif cmd is None:
                    break
                else:
                    print("Unknown command")
                    yield None
        cmd = yield


# передаём список команд напрямую
calc = itercalc()
next(calc)
for cmd in ["?", "3", "-2", "-", "what", "5", "*", "2", "/", "?"]:
    res = calc.send(cmd)
    if res is not None:
        print(res)
