import numpy as np
import pandas as pd

class TimeSeriesOps:
    @classmethod
    def ts_sum(cls, x, days=5):
        stocks = x.columns[1:]

        summed_df = x.copy()
        summed_df[stocks] = x[stocks].rolling(window=days, min_periods=1).sum()

        return summed_df