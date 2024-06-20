import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import math
np.set_printoptions(precision=6)

#%%
def max_relu(x):
    return max(x, 0.0)

for i in [-10., -5., 0., 5., 10.]:
    print(max_relu(i))
# %%
data = np.random.randn(50)
data = sorted(data)
data
# %%
max_relu_data = np.array([max_relu(x) for x in data])
max_relu_data
# %%
df = pd.DataFrame({'data': data, 'max_relu_data': max_relu_data})
df.head()

# %%
px.line(df, x='data', y='max_relu_data', width=700, height=400, title='ReLU Function')
# %%
def sigmoid(x):
    return 1/(1+np.exp(-x))
for i in [-5., -3., -1., 0., 1., 3., 5.]:
    print(sigmoid(i))
# %%
data = 3 * np.random.randn(50)
data = sorted(data)
data
# %%
sigmoid_data = [sigmoid(i) for i in sorted(data)]
sigmoid_data
# %%
