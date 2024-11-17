import random
import plotly.express as px

rozmiar_probki = 31
liczba_probek = 1000
wartosc_x = [
    (sum([random.uniform(0.0, 1.0) for i in range(rozmiar_probki)]) / rozmiar_probki)
    for _ in range(liczba_probek)
]
wartosc_y = [1 for _ in range(liczba_probek)]

px.histogram(x=wartosc_x, y=wartosc_y, nbins=20).show()
