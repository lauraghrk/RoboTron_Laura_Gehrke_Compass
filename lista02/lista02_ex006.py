#6-Faça com que o programa printe apenas os primeiros dados dentro de edicao_atual, fase_atual, rodada_atual usando o JSON 2.

import json

def retorna_json():
    with open("JSON2.json", encoding="utf-8") as json_normal:
        json_manipulavel = json.load(json_normal)
        return json_manipulavel

campeonato = retorna_json()

print(campeonato["edicao_atual"]["edicao_id"])
print(campeonato["fase_atual"]["fase_id"])
print(campeonato["rodada_atual"]["nome"])