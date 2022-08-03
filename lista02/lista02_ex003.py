#3-Do JSON 1 Guarde apenas o Nome do Estádio, o Placar e o Status do jogo dentro de variáveis e mostre-as.

import json

def retorna_json():
    with open("JSON1.json", encoding="utf-8") as json_normal:
        json_manipulavel = json.load(json_normal)
        return json_manipulavel

partida = retorna_json()

nome_estadio = partida["copa-do-brasil"][0]["estadio"]["nome_popular"]
placar = partida["copa-do-brasil"][0]["placar"]
status = partida["copa-do-brasil"][0]["status"]

print("Nome do estádio: " + nome_estadio)
print("Placar: " + placar)
print("Status da partida: " + status)