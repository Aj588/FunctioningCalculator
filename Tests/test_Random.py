import unittest
from Random.Random import Random
from Statistics.Statistics import Statistics


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.random = Random()
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.random, Random)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.random, Random)

    # Test Random -------------------------------------------------------------
    def test_random_int_seed(self):
        testdata = self.random.Random_int_nums(1, 100, 5, 5)
        mean = self.statistics.mean(testdata)
        self.assertEqual(mean, 48.2)

    def test_random_int(self):
        testdata = self.random.Random_int_nums(1, 100, 5, None)
        testdata2 = self.random.Random_int_nums(1, 100, 5, None)
        mean = self.statistics.mean(testdata)
        mean2 = self.statistics.mean(testdata2)
        self.assertNotEqual(mean, mean2)

    def test_random_float_seed(self):
        testdata = self.random.Random_float_nums(1.0, 100.0, 5, 3)
        testdata2 = self.random.Random_float_nums(1.0, 100.0, 5, 3)
        mean = self.statistics.mean(testdata)
        mean2 = self.statistics.mean(testdata2)
        self.assertAlmostEqual(mean, mean2)

    def test_random_float(self):
        testdata = self.random.Random_float_nums(1.0, 100.0, 5, None)
        testdata2 = self.random.Random_float_nums(1.0, 100.0, 5, None)
        mean = self.statistics.mean(testdata)
        mean2 = self.statistics.mean(testdata2)
        self.assertNotEqual(mean, mean2)



if __name__ == '__main__':
    unittest.main()