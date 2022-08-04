#14-Printe todos os nomes e as idades dos atores que ganharam o oscar de 1987 até 1999.

import pandas as pd

filmes = pd.read_csv('CSV.csv', encoding="utf-8", sep=",")

anos_selecionados = filmes[(filmes["Year"] >= 1987) & (filmes["Year"] <= 1999)]

print(anos_selecionados.loc[:, ["Name", "Age"]])

#Referência uso do .loc: https://www.delftstack.com/pt/howto/python-pandas/select-multiple-columns-pandas/