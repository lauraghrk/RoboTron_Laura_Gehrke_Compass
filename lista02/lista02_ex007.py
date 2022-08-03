#7-Percorra o JSON 2, utilizando o loop FOR e printe suas chaves principais.

import json

def retorna_json():
    with open("JSON2.json", encoding="utf-8") as json_normal:
        json_manipulavel = json.load(json_normal)
        return json_manipulavel

campeonato = retorna_json()

for chave in campeonato.keys():
    print(chave)

#Referência uso .keys(): https://iaexpert.academy/2019/09/12/dicionarios-em-python/