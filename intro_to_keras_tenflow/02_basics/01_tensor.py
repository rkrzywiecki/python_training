import numpy as np


scalar = 3
print(scalar)
print(type(scalar))

scalar = 3.0
print(scalar)
print(type(scalar))

vector = np.array([2, 4, -6, 5])
print(vector)
print(type(vector))
print(f"Rozmiar vectora: {vector.shape}")
print(f"Typ danych vectora: {vector.dtype}")
print(f"Rząd: {vector.ndim}")
print(f"Długość: {len(vector)}")


# macierz
array = np.array([[2, 6, 3], [5, -3, 4]])

print(array)
print(type(array))
print(f"Rozmiar macierzy: {array.shape}")
print(f"Typ danych macierzy: {array.dtype}")
print(f"Rząd: {array.ndim}")
print(f"Dlugosc: {len(array)}")

# Tensor
tensor = np.array([])
