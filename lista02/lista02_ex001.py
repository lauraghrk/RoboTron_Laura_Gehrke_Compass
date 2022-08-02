#1-Baixe o arquivo do link JSON 1, abra ele no vsCode com Python nomeando-o como partida guarde em uma variável e printe o JSON inteiro no terminal.

import json

def retorna_json():
    with open("lista02\JSON1.json", encoding="utf-8") as json_normal:
        json_manipulavel = json.load(json_normal)
        return json_manipulavel

partida = retorna_json()

print(partida)

#Referência: material da trilha RoboTron da Compass.