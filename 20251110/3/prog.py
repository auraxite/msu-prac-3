class Undead(Exception):
    pass

class Skeleton(Undead):
    pass

class Zombie(Undead):
    pass

class Ghoul(Undead):
    pass

def necro(a):
    r = a % 3
    if r == 0:
        raise Skeleton
    if r == 1:
        raise Zombie
    raise Ghoul

x, y = eval(input())
for n in range(x, y):
    try:
        necro(n)
    except Skeleton:
        print("Skeleton")
    except Zombie:
        print("Zombie")
    except Undead:
        print("Generic Undead")