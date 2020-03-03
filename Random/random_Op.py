from numpy.random import seed
from numpy.random import randint
from numpy.random import uniform

class Random_num:
    @staticmethod
    def random_int_generator(low, high, num, seed_num = randint(1,100)):
        if seed_num != 5:
            data = randint(low, high, num)
            return data
        seed(seed_num)
        data = randint(low, high, num)
        return data

    @staticmethod
    def random_float_generator(low, high, num, seed_num = randint(1,100)):
        seed(seed_num)
        data = uniform(low, high, num)
        return data