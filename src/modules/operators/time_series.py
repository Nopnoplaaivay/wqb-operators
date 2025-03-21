import numpy as np
import pandas as pd

class TimeSeriesOperators:
    @classmethod
    def ts_sum(cls, x: pd.DataFrame, days: int):
        stocks = x.columns[1:]

        summed_df = x.copy()
        summed_df[stocks] = x[stocks].rolling(window=days, min_periods=1).sum()

        return summed_df
    
    @classmethod
    def ts_mean(cls, x: pd.DataFrame, days: int):
        stocks = x.columns[1:]

        mean_df = x.copy()
        mean_df[stocks] = x[stocks].rolling(window=days, min_periods=1).mean()

        return mean_df