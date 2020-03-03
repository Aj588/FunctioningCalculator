from Calculator.Calculator import Calculator
from StatisticsOps.mean import Mean

from Random.random_Op import Random_num;

class Statistics(Calculator):

    def mean(self, data):
        self.Result = Mean(data)
        return self.Result