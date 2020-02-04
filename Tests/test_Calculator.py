import unittest

from Calculator.Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_calculator_return_sum(self):
        calculator = Calculator()
        result = calculator.Sum(1, 2)
        self.assertEqual(3, result)

    def test_calculator_return_difference(self):
        calculator = Calculator()
        result = calculator.Difference(1, 2)
        self.assertEqual(-1, result)

    def test_calculator_access_difference_result(self):
        calculator = Calculator()
        calculator.Difference(1, 2)
        self.assertEqual(-1, calculator.Result)

    def test_calculator_access_sum_result(self):
        calculator = Calculator()
        calculator.Sum(1, 2)
        self.assertEqual(3, calculator.Result)

    def test_multiple_calculators(self):
        calculator1 = Calculator()
        calculator2 = Calculator()
        calculator3 = Calculator()
        calculator3.Sum(calculator1.Sum(1, 2), calculator2.Difference(3, 4))
        self.assertEqual(2, calculator3.Result)

if __name__ == '__main__':
    unittest.main()

    '''
    def test_calculator_division(self):
        calculator = Calculator()
        result = calculator.division(6,3)
        self.assertEqual(2, result)

    def test_calculator_multiplication(self):
        calculator = Calculator()
        result = calculator.multiplication(6,3)
        self.assertEqual(18, result)

    def test_calculator_squared(self):
        calculator = Calculator()
        result = calculator.squared(6)
        self.assertEqual(36, result)
    
    def test_calculator_squareRoot(self):
    calculator = Calculator()
    result = calculator.squared(2)
    self.assertEqual(4, result)
'''

