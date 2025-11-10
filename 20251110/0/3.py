C = type(
    'CC', (), 
    {
        'a': 213, 
        '__str__': lambda self: f'{self.__class__.__name__}'
    }
)
print(C)

A = type(
    'A', (),
    {
        '__init__': lambda self, v: setattr(self, 'Q-Q!', v),
        '__str__': lambda self: self.v
    }
)
