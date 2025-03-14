import numpy as np
import pandas as pd

from src.modules.operators import (
    CrossSectionalOperators as cs, 
    TimeSeriesOperators as ts,
    TransformationalOperators as tf,
    GroupOperators as gp,
    ArithmeticOperators as ar,
    LogicalOperators as lg
)

def test_alpha():
    raw_data = pd.read_csv('close_price.csv')

    print("===== TimeSeriesOperators =====")
    ts_sum_matrix = ts.ts_sum(x=raw_data, days=10)
    # print(ts_sum_matrix)


    print("===== CrossSectionalOperators =====")
    ranked_data = cs.rank(x=raw_data)
    print(ranked_data)

    # test division
    print("===== ArithmeticOperators =====")
    # divided_data = ar.divide(x=ranked_data, y=ranked_data)
    # print(divided_data)

    # test logical operators
    print("===== LogicalOperators =====")
    compared_data = lg.equal(x=raw_data, y=raw_data)
    print(compared_data)

    # test combine alpha rank(ts_sum(close, 10))
    result_matrix = cs.rank(x=ts.ts_sum(x=raw_data, days=10))
    print(result_matrix)




test_alpha()