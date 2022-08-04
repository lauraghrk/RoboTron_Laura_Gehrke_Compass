#10-Usando Pandas, procure por um dado específico (da sua escolha) e printe somente o mesmo utilizando o CSV.

import pandas as pd

filmes = pd.read_csv('CSV.csv', encoding="utf-8", sep=",")

#Nome do ator de "Forrest Gump"
print(filmes.loc[67, ["Name"]])