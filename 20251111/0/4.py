class istype:
    def __init__(self, type):
        class decor:
            def __init__(self, f):
                self.f = f
            
            def __call__(*args):
                for arg in args:
                    if not isinstance(arg, type):
                        raise TypeError("err")
                return self.f(*args)
        
        self.type = type
        self.decor = decor

