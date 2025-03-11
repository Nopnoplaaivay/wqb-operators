import numpy as np
import pandas as pd


def rank(x):
    matrix = x.drop(columns=["time"]).values  # Remove 'time' column
    ranked_matrix = np.zeros(matrix.shape)
    len_stocks = matrix.shape[1]
    stocks = x.columns[1:]

    for i in range(len(matrix)):
        ranked_matrix[i] = np.argsort(matrix[i]) / (len_stocks - 1)  # Double argsort to get ranks

    ranked_df = pd.DataFrame(ranked_matrix, columns=stocks)
    ranked_df.insert(0, "time", x["time"])
    return ranked_df


data = pd.read_csv('close_price.csv')
ranked_df = rank(data)
print(ranked_df)