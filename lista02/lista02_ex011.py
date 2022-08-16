#11-Printe o nome do Ator que ganhou o Oscar em 1993.

import pandas as pd

filmes = pd.read_csv('CSV.csv', encoding="utf-8", sep=",")

oscar93 = filmes[filmes["Year"] == 1993]

print(oscar93["Name"])