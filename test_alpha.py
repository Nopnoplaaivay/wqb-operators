import numpy as np
import pandas as pd

from src.modules.operators import (
    CrossSectionalOperators as CS, 
    TimeSeriesOperators as TS,
    TransformationalOperators as TF,
    GroupOperators as GP,
    ArithmeticOperators as AR,
    LogicalOperators as LG
)

def test_alpha():
    close = pd.read_csv('close_price.csv')

    # ts_sum_matrix = ts.ts_sum(x=raw_data, days=10)
    # print(ts_sum_matrix)

    # ranked_data = cs.rank(x=raw_data)
    # print(ranked_data)

    # test division
    # divided_data = ar.divide(x=ranked_data, y=ranked_data)
    # print(divided_data)

    # test logical operators
    # compared_data = lg.equal(x=raw_data, y=raw_data)
    # print(compared_data)

    # test combine alpha rank(ts_sum(close, 10))
    # result_matrix = cs.rank(x=ts.ts_sum(x=raw_data, days=10))
    # print(result_matrix)

    trigger_trade_exp_matrix = LG.greater_than(x=close, y=TS.ts_mean(x=close, days=10))
    print(trigger_trade_exp_matrix)

    alpha_exp_matrix = CS.rank(x=close)
    print(alpha_exp_matrix)

    m_one_matrix = close.copy()
    m_one_matrix.iloc[:, 1:] = -1

    trigger_exit_exp_matrix = LG.less_than(x=close, y=TS.ts_mean(x=close, days=10))
    print(trigger_exit_exp_matrix)

test_alpha()