
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from utils.decorators import log_function, time_execution
from utils.iterators import DatasetIterator
from utils.generators import data_generator
from utils.mixins import BaseProcessor, LoggerMixin

class Stats:
    def __init__(self,val):
        self.val=val
    def __add__(self,other):
        return Stats(self.val+other.val)

class DataProcessor(BaseProcessor, LoggerMixin):

    def __init__(self,path):
        if path.endswith(".csv"):
          self.df = pd.read_csv(path)
        elif path.endswith(".json"):
          self.df = pd.read_json(path)

    @log_function
    def load_data(self):
        self.log("Data loaded")

    @time_execution
    def compute(self):
        stats={}

        for _ in DatasetIterator(self.df.values): pass
        for _ in data_generator([1,2,3]): pass

        a=Stats(10); b=Stats(20); c=a+b

        numeric_df = self.df.select_dtypes(include=[np.number])

        for col in numeric_df.columns:
         stats[col] = {
        "mean": float(np.mean(numeric_df[col])),
        "median": float(np.median(numeric_df[col]))
    }
        self.log(f"Processing numeric columns: {list(numeric_df.columns)}")

        self.df.plot()
        plt.savefig("static/chart.png")
        plt.clf()

        self.df.hist()
        plt.savefig("static/hist.png")
        plt.clf()

        return stats

    def process(self):
        self.load_data()
        return self.compute()
