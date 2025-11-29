class sole(type):
    def __new__(metacls, name, parents, namespace):
        cnt = 0
        if len(parents) > 1:
            raise TypeError("Cannot have more than one parent")
        return super().__new__(metacls, name, parents, namespace)
class E(metaclass=sole): pass
class C: pass
class A(C, E): pass