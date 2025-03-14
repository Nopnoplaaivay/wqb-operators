import numpy as np
import pandas as pd

from src.modules.operators import CrossSectionalOps, TimeSeriesOps

def test_alpha():
    data = pd.read_csv('close_price.csv')

    # ts_sum
    ts_sum_data = TimeSeriesOps.ts_sum(data)
    print("ts_sum_data")
    print(ts_sum_data)

    # rank
    print("ranked_data")
    ranked_data = CrossSectionalOps.rank(ts_sum_data)
    print(ranked_data)

test_alpha()