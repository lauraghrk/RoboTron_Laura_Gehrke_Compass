#4-No JSON 1 printe todas as chaves e valores do time visitante.

import json

def retorna_json():
    with open("JSON1.json", encoding="utf-8") as json_normal:
        json_manipulavel = json.load(json_normal)
        return json_manipulavel

partida = retorna_json()

print(partida["copa-do-brasil"][0]["time_visitante"])