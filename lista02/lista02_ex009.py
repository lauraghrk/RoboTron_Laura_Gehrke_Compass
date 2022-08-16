#9-Usando Pandas, leia apenas os dados da coluna Age do CSV.

import pandas as pd

idades = pd.read_csv('CSV.csv', encoding="utf-8", sep=",", usecols=["Age"])

print(idades)