from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction


class Calculator:
    Result = 0

    def __init__(self):
        pass

    def Sum(self, a, b):
        self.Result = Addition.sum(a, b)
        return self.Result

    def Difference(self, a, b):
        self.Result = Subtraction.difference(a, b)
        return self.Result

    '''
    def multiplication(self, a, b):
        return a * b

    def squared(self, a):
        return a * a 
    
    def squareRoot(self, a):
        import math
        return (math.sqrt(a))
    '''

