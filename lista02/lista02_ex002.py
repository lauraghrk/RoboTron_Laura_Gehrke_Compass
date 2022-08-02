#2-Pegue o arquivo JSON 1 e printe apenas o nome do time vencedor no terminal.

import json

def retorna_json():
    with open("lista02\JSON1.json", encoding="utf-8") as json_normal:
        json_manipulavel = json.load(json_normal)
        return json_manipulavel

partida = retorna_json()

placar_mandante = partida["copa-do-brasil"][0]["placar_mandante"]
placar_visitante = partida["copa-do-brasil"][0]["placar_visitante"]

if placar_mandante > placar_visitante:
    print(partida["copa-do-brasil"][0]["time_mandante"]["nome_popular"])
elif placar_mandante < placar_visitante:
    print(partida["copa-do-brasil"][0]["time_visitante"]["nome_popular"])
else:
    print("A partida terminou empatada.")

#Auxílio do Paulo na daily sobre como determinar o time vencedor.