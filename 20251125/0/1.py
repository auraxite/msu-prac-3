import inspect

class A:
    a: int = 5

    def __init__(self, val):
        if not isinstance(val, inspect.get_annotations(self.__class__)["a"]):
            raise TypeError
        self.a =  val