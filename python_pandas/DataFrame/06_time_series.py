import pandas as pd
import numpy as np


# %%
index = pd.date_range("01-01-2019", periods=10000)
df = pd.DataFrame(np.random.randn(10000), index=index)

# %%
df_cumsum = df.cumsum()
# %%
df_cumsum.plot(kind="line")
# %%
3 ** 3
# %%
27 *= 2
# %%
m = 3 ** 3
m = *= 2
# %%
