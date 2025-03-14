import numpy as np
import pandas as pd

class CrossSectionalOperators:
    @classmethod
    def rank(cls, x: pd.DataFrame):
        stocks = x.columns[1:]
        stocks_num = len(stocks)

        ranked_df = x.copy()
        ranked_df[stocks] = (ranked_df[stocks].rank(axis=1, method="dense") - 1) / (stocks_num - 1) 
        ranked_df[stocks] = ranked_df[stocks] 

        return ranked_df
