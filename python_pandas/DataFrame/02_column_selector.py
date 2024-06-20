import pandas as pd
import numpy as np


# %%
df = pd.read_csv("./data/aapl_us_d.csv", index_col=0)
df.columns = ["Open", "High", "Low", "Close", "Volume"]
# %%
print(df.columns)
# %%
open_price = df["Open"]
# %%
df.iloc[10:20]
# %%
df.iloc[:, :2]
# %%
df.iloc[:, :]
# %%
df["Daily Change"] = df["Close"] / df["Close"].shift(1) - 1
# %%
df["Daily Change"].max()
# %%
