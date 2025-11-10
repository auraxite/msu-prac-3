class E1(Exception):
    pass

class E2(Exception):
    pass

class E3(E2):
    pass

for err in [Exception(), E1(), E2(), E3()]:
    try:
        raise err
    except E3:
        print('E3')
    except E2:
        print('E2')
    except E1:
        print('E1')
    except Exception:
        print('E')