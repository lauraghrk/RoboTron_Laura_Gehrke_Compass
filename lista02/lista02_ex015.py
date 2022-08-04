#15-Mostre todos os filmes menos o “The Revenant”.

import pandas as pd

filmes = pd.read_csv('CSV.csv', encoding="utf-8", sep=",")

print(filmes[filmes["Movie"] != "The Revenant"])