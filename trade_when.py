import numpy as np
import pandas as pd

"""
Example: 
    trade_when(volume >= ts_sum(volume, 5) / 5, rank(-returns), abs(returns) > 0.1)
"""

