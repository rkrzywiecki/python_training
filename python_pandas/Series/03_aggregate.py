import pandas as pd
import numpy as np


# %%
np.random.seed(0)
s = pd.Series(np.random.randn(20))

# %%
minimum = s.min()
# %%
maximum = s.max()
# %%
suma = s.aggregate(sum)
# %%
stats = s.aggregate(["min", "max", "sum", "mean"])
# %%
