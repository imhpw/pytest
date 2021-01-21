class Calc:

    def add(self,a:int,b:int)->int:
        return a + b

    def div(self,a,b):
        if b==0:
            return 'zero is not allowed'
        else:
            return a / b