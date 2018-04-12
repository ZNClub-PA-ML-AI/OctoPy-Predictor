
import pandas as pd

class DataGatherer(object):
    """docstring for DataGatherer"""
    def __init__(self, arg):
        super(DataGatherer, self).__init__()
        self.arg = arg

    def read(self, path):
        return pd.read_csv(path)