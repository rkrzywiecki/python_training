import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = "./data/amzn_us_d.csv"
df = pd.read_csv(path, index_col=0)

close = df["Zamkniecie"]

close = close["2010-01-01":]

# %% plotting the results
close.plot(title="Wykres notowan spolki Amazon", logy=True)
plt.savefig("./charts/close.png")
# %% export to csv

close.to_csv("./data/close_amzn.csv", header=["close"])

# %%
