import unittest

from MathOperations.addition import Addition
from MathOperations.division import Division
from MathOperations.exponentiation import Exponentiation
from MathOperations.multiplication import Multiplication
from MathOperations.subtraction import Subtraction
from MathOperations.root import Root
from MathOperations.log import Log


class MyTestCase(unittest.TestCase):

    def test_MathOperations_Addition(self):
        self.assertEqual(3, Addition.sum(1,2))

    def test_calculator_subtraction(self):
        self.assertEqual(-1, Subtraction.difference(1,2))

    def test_MathOperations_sum_list(self):
        valueList = [1,2,3,4,5,6]
        self.assertEqual(21, Addition.sum(valueList))

    def test_MathOperations_multiplication(self):
        self.assertEqual(6, Multiplication.product(3,2))

    def test_MathOperations_division(self):
        self.assertEqual(3, Division.fraction(9,3))

    def test_MathOperations_exponentiation(self):
        self.assertEqual(8, Exponentiation.power(2,3))

    def test_MathOperations_root(self):
        self.assertEqual(13, Root.root(169, 2))

    def test_MathOperations_logarthim(self):
        self.assertEqual(0, Log.logarithm(10,1))


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

