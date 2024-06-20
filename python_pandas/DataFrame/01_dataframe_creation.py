import pandas as pd
import numpy as np

# %%
df = pd.DataFrame(data=[12, 34, 23])

# %%
df = pd.DataFrame(
    data=[[12, 34, 32], [53, 23, 74]],
    index=["first", "second"],
    columns=["col1", "col2", "col3"],
)

# %%
df = pd.DataFrame(
    data=[[12, 34, 32], [53, 23, 74], [3134, 435, 23]],
    index=["first", "second", "third"],
    columns=["col1", "col2", "col3"],
)

# %%
d = {"one": pd.Series([1, 2, 3]), "two": pd.Series([4, 5, 6])}
df = pd.DataFrame(d)

# %%
