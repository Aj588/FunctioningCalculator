import unittest

from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction


class MyTestCase(unittest.TestCase):

    def test_MathOperations_Addition(self):
        self.assertEqual(3, Addition.sum(1,2))

    def test_calculator_subtraction(self):
        self.assertEqual(-1, Subtraction.difference(1,2))

    def test_MathOperations_sum_list(self):
        valueList = [1,2,3,4,5,6]
        self.assertEqual(21, Addition.sum(valueList))

if __name__ == '__main__':

    '''
    def test_calculator_division(self):
        result = calculator.division(6,3)
        self.assertEquals(2, result)

    def test_calculator_multiplication(self):
        result = calculator.multiplication(6,3)
        self.assertEquals(18, result)

    def test_calculator_squared(self):
        result = calculator.squared(6)
        self.assertEquals(36, result)
    '''

