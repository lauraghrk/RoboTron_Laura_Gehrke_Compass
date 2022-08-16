#8-Abra o arquivo CSV com pandas e guarde em uma variável de sua escolha e printe o conteúdo no terminal.

import pandas as pd

filmes = pd.read_csv('CSV.csv', encoding="utf-8", sep=",")

print(filmes)