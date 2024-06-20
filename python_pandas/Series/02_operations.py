import pandas as pd
import numpy as np

np.random.seed(0)

A = np.random.randint(0, 10, 10)

series = pd.Series(A, name="los")

# %% attributes
series.dtype
series.iloc[3]
series.iloc[-1]
series.index
series.name
series.shape

# %%
array_A = series.values
# %%
N = np.random.randn(10)
M = np.random.randn(10)
series_N = pd.Series(N)
series_M = pd.Series(M)

# %%
series_N.abs()
# %%
series_N.add(series_M)
# %%
series.drop_duplicates()
# %%
series[4] = np.nan
# %%
series.dropna()
# %%
series.idxmax()
# %%
series.idxmin()
# %%
series.count()
# %%
series.sum()

# %%
series_N.cumsum()
# %%
series.std()
# %%
series.describe()
# %%
hist_data = pd.Series(np.random.randn(10000))
hist_data.hist(bins=80)
# %%
hist_data.nlargest(3)
# %%
