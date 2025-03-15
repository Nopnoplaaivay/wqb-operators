import numpy as np
import pandas as pd

class TransformationalOperators:

    @classmethod
    def trade_when(cls, x: pd.DataFrame, y: pd.DataFrame, z: pd.DataFrame):
        stocks = x.columns[1:]
        merged_df = pd.merge(x, y, on='time', how='outer').merge(z, on='time', how='outer')
        merged_df = merged_df.rename(columns={col: col + "_z" for col in stocks})

        for i in range(len(merged_df)):
            last_trade = 0.0
            for stock in stocks:
                if merged_df.loc[i, stock + '_z']:
                    merged_df.loc[i, stock + '_tradewhen'] = 0.0
                    last_trade = 0.0
                else:
                    if merged_df.loc[i, stock + '_x']:
                        merged_df.loc[i, stock + '_tradewhen'] = merged_df.loc[i, stock + '_y']
                        last_trade = merged_df.loc[i, stock + '_y']
                    else:
                        merged_df.loc[i, stock + '_tradewhen'] = last_trade

        # stock = "VCB"
        # merged_df = merged_df[["time", stock + "_tradewhen", stock + "_x", stock + "_y", stock + "_z"]]
        return merged_df
    
    @classmethod
    def test_trade_when(cls, df: pd.DataFrame):
        last_trade = 0.0
        for i in range(len(df)):
            if df.loc[i, "z1"]:
                df.loc[i, "tradewhen"] = 0.0
                last_trade = 0.0
            else:
                if df.loc[i, "x1"]:
                    df.loc[i, "tradewhen"] = df.loc[i, "y1"]
                    last_trade = df.loc[i, "y1"]
                else:
                    df.loc[i, "tradewhen"] = last_trade
        return df
