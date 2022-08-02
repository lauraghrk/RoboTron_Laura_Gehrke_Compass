#5-Guarde o arquivo JSON 2 nomeando-o como campeonato em uma variável e printe todos os seus dados.

import json

def retorna_json():
    with open("lista02\JSON2.json", encoding="utf-8") as json_normal:
        json_manipulavel = json.load(json_normal)
        return json_manipulavel

campeonato = retorna_json()

print(campeonato)