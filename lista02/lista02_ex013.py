#13-Crie mais uma coluna em tempo de execução juntando os dados movie e year.

import pandas as pd

filmes = pd.read_csv('CSV.csv', encoding="utf-8", sep=",")

filmes["filme_ano"] = filmes["Movie"] + " - " + filmes["Year"].map(str)

print(filmes["filme_ano"])

#Dica do Pedro na mentoria sobre o uso de .map(str)