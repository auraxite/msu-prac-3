class A:
    def fun(*args):
        print(f'1: {args}')
        
        @classmethod
        def cfun(*args):
            print(f'2: {args}')

        @staticmethod
        def sfun(*args):
            print(f'3: {args}')