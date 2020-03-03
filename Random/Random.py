from Random.random_Op import *

class Random:
    Result = 0

    def Random_int_nums(self, a, b, c, d):
        self.Result = Random_num.random_int_generator(a, b, c, seed_num=d)
        return self.Result


    def Random_float_nums(self, a, b, c, d):
        self.Result = Random_num.random_float_generator(a, b, c, seed_num=d)
        return self.Result