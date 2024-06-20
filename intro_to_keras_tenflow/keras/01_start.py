import tensorflow as tf
import numpy as np
import pandas as pd
import plotly.express as px
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense

from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.activations import linear

var = tf.__version__
model = Sequential()
model.add(Dense(units=8, activation='relu', input_shape=(10,), ))
model.add(Dense(units=1, activation='sigmoid'))
model.summary()

# random_data = sorted(np.random.randn(200))
# data = pd.DataFrame({'data': random_data, 'linear': linear(random_data)})
# data.head()

# px.line(data, x='data', y='linear', width=800, range_y=[-2, 2])
