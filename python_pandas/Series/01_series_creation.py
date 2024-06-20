import pandas as pd
import numpy as np
from sqlalchemy import column

# Example 1
s = pd.Series(4)

# Example 2
s_def = pd.Series(data=[21, 34, 54], index=["adam", "tomek", "pawel"], name="age")

# %% Example 3
A = np.random.randn(10)
s = pd.Series(A)

# %%
print(s)
# %%
stocks = {"Apple": "USA", "CD Project": "Poland", "Amazon": "USA"}
series = pd.Series(stocks, name="country")

# %% Example 6
stocks_price = {"Apple": 196, "CD Project": 215, "Amazon": 1877}
stocks_price_series = pd.Series(stocks_price, name="Price")
stocks_price_series_array = stocks_price_series.values

# %%
