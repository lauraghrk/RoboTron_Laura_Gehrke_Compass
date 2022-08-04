#12-Printe somente o nome dos atores que ganharam o Oscar em 1991 e 2016.

import pandas as pd

filmes = pd.read_csv('CSV.csv', encoding="utf-8", sep=",")

anos = filmes[(filmes["Year"] == 1991) | (filmes["Year"] == 2016)]

print(anos["Name"])