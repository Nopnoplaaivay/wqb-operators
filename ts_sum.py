import numpy as np
import pandas as pd


def ts_sum(x, days=5):
    matrix = x.drop(columns=["time"]).values  # Remove 'time' column
    summed_df = np.zeros(matrix.shape)
    stocks = x.columns[1:]

    for idx, stock in enumerate(stocks):
        rolling_sum = x[stock].rolling(window=days).sum().values
        summed_df[:, idx] = rolling_sum

    summed_df = pd.DataFrame(summed_df, columns=stocks)
    summed_df.insert(0, "time", x["time"])
    return summed_df


data = pd.read_csv('close_price.csv')
sum_data = ts_sum(data)
print(sum_data)