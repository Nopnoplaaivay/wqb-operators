import numpy as np
import pandas as pd

class ArithmeticOperators:
    @classmethod
    def divide(cls, x: pd.DataFrame, y: pd.DataFrame):
        stocks = x.columns[1:]
        divided_df = x.copy()
        divided_df[stocks] = x[stocks] / y[stocks]
        return divided_df