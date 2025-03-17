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

    trigger_trade_x = close.copy() # close price
    trigger_trade_y = TS.ts_mean(x=close, days=5) # 10-day moving average
    trigger_exit_y = TS.ts_mean(x=close, days=5) # 10-day moving average

    trigger_trade_exp_matrix = LG.greater_equal(x=trigger_trade_x, y=trigger_trade_y)
    # alpha_exp_matrix = CS.rank(x=TS.ts_sum(x=close, days=10))
    alpha_exp_matrix = close.copy()
    trigger_exit_exp_matrix = LG.less_equal(x=close, y=trigger_exit_y)

    trade_df = TF.trade_when(x=trigger_trade_exp_matrix, y=alpha_exp_matrix, z=trigger_exit_exp_matrix)
    print(trade_df)

def test_tradewhen():
    df = pd.read_csv('test_tradewhen.csv')
    df = TF.test_trade_when(df)

    # thay đổi lại thứ tự các cột
    cols = df.columns.tolist()
    columns = ['time', 'close', 'tradewhen', 'x1', 'y1', 'z1']
    df = df[columns]

    print(df)


if __name__ == "__main__":
    test_alpha()
    test_tradewhen()