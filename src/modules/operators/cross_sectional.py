import numpy as np
import pandas as pd

class CrossSectionalOps:
    @classmethod
    def rank(cls, x):
        stocks = x.columns[1:]  # Lấy tên cột, bỏ 'time'
        
        matrix = x[stocks].to_numpy()  # Chuyển sang np.ndarray (bỏ time)
        ranked_matrix = np.argsort(np.argsort(matrix, axis=1), axis=1) / (len(stocks) - 1)

        ranked_df = pd.DataFrame(ranked_matrix, columns=stocks)
        ranked_df.insert(0, "time", x["time"])  # Thêm lại 'time'

        return ranked_df
    
        x = x.reset_index(drop=True) 
        matrix = x.drop(columns=["time"]).values  # Remove 'time' column
        ranked_matrix = np.zeros(matrix.shape)
        len_stocks = matrix.shape[1]
        stocks = x.columns[1:]

        for i in range(len(matrix)):
            ranked_matrix[i] = np.argsort(np.argsort(matrix[i])) / (len_stocks - 1)  # Double argsort to get ranks

        ranked_df = pd.DataFrame(ranked_matrix, columns=stocks)
        ranked_df.insert(0, "time", x["time"])
        return ranked_df