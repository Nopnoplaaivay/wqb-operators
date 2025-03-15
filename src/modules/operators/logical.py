import numpy as np
import pandas as pd

class LogicalOperators:
    @classmethod
    def greater_than(cls, x: pd.DataFrame, y: pd.DataFrame):
        stocks = x.columns[1:]
        compared_df = x.copy()
        compared_df[stocks] = x[stocks] > y[stocks]
        return compared_df
    
    @classmethod
    def greater_equal(cls, x: pd.DataFrame, y: pd.DataFrame):
        stocks = x.columns[1:]
        compared_df = x.copy()
        compared_df[stocks] = x[stocks] >= y[stocks]
        return compared_df
    
    @classmethod
    def less_than(cls, x: pd.DataFrame, y: pd.DataFrame):
        stocks = x.columns[1:]
        compared_df = x.copy()
        compared_df[stocks] = x[stocks] < y[stocks]
        return compared_df
    
    @classmethod
    def less_equal(cls, x: pd.DataFrame, y: pd.DataFrame):
        stocks = x.columns[1:]
        compared_df = x.copy()
        compared_df[stocks] = x[stocks] <= y[stocks]
        return compared_df

    @classmethod
    def equal(cls, x: pd.DataFrame, y: pd.DataFrame):
        stocks = x.columns[1:]
        compared_df = x.copy()
        compared_df[stocks] = x[stocks] == y[stocks]
        return compared_df