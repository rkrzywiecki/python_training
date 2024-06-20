from tabnanny import verbose
from turtle import color
from matplotlib import units
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow.keras.datasets.mnist import load_data
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, Dropout

import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

np.set_printoptions(precision=12, suppress=True, linewidth=120)
print(tf.__version__)

(X_train, y_train), (X_test, y_test) = load_data()
print(f"X_train shape {X_train.shape}")
print(f"y_train shape {y_train.shape}")
print(f"X_test shape {X_test.shape}")
print(f"y_test shape {y_test.shape}")

print(X_train[0])

print(X_train[0].shape)

X_train = X_train / 255
X_test = X_test / 255

# plt.imshow(X_train[0], cmap='gray_r')
# plt.axis("off")
# plt.figure(figsize=(13, 13))
# for i in range(1, 11):
#     plt.subplot(1, 10, i)
#     plt.axis("off")
#     plt.imshow(X_train[i - 1], cmap="gray_r")
#     plt.title(y_train[i - 1], color="black", fontsize=16)
# plt.show()

model = Sequential()
model.add(Flatten(input_shape=(28, 28)))
model.add(Dense(units=128, activation="relu"))
model.add(Dropout(0.2))
model.add(Dense(units=10, activation="softmax"))

model.compile(
    optimizers="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
)

model.summary()

history = model.fit(X_train, y_train, epochs=15)

model.evaluate(X_test, y_test, verbose=2)

metrics = pd.DataFrame(history.history)
fig = make_subplots(rows=2, cols=1)
fig.add_trace(go.Scatter(y=metrics["loss"], name="loss"), row=1, col=1)
fig.add_trace(go.Scatter(y=metrics["accuracy"], name="accuracy"), row=2, col=1)
fig.update_layout(width=800)

y_pred = model.predict_classes(X_test)
pred = pd.concat(
    [
        pd.DataFrame(y_test, columns=["y_test"]),
        pd.DataFrame(y_pred, columns=["y_pred"]),
    ],
    axis=1,
)
pred.head(10)
misclassified = pred[pred["y_test"] != pred["y_pred"]]
misclassified.index[:10]
plt.figure(figsize=(13, 13))
for i, j in zip(range(1, 11), misclassified.index[:10]):
    plt.subplot(1, 10, i)
    plt.axis("off")
    plt.imshow(X_test[j], cmap="gray_r")
    plt.title(
        "y_test: " + str(y_test[j]) + "\n" + "y_pred: " + str(y_pred[j]),
        color="black",
        fontsize=12,
    )
plt.show()
