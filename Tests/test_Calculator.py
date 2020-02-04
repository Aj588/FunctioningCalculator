import unittest

from Calculator.Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_calculator_addition(self):
        calculator = Calculator()
        result = calculator.addition(1,2)
        self.assertEquals(3, result)

    def test_calculator_subtraction(self):
        calculator = Calculator()
        result = calculator.subtraction(1, 2)
        self.assertEquals(-1, result)

    def test_calculator_division(self):
        calculator = Calculator()
        result = calculator.division(6,3)
        self.assertEquals(2, result)

    def test_calculator_multiplication(self):
        calculator = Calculator()
        result = calculator.multiplication(6,3)
        self.assertEquals(18, result)

    def test_calculator_squared(self):
        calculator = Calculator()
        result = calculator.squared(6)
        self.assertEquals(36, result)

    def test_calculator_sqrt(self):
        calculator = Calculator()
        result = calculator.sqrt(9)
        self.assertEquals(3, result)

if __name__ == '__main__':
    unittest.main()