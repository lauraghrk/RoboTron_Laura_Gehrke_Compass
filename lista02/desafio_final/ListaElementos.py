#Crie uma “aplicação” em loop que tenha uma opção para:

#A)listar todos os elementos da tabela, porém mostrando apenas uma propriedade do elemento. Ex: listar todos os nomes dos elementos na tabela.

#B) Listar todos os dados de determinado elemento, buscando através do seu símbolo.

#C) Listar todos os dados de todos os elementos inseridos.

import pandas as pd
tabela = pd.read_csv("tabela_periodica.csv", encoding="UTF-8", sep=",")

def seleciona_propriedade(prop):
    propriedade = tabela[prop]
    return propriedade

def seleciona_elemento(elem):
    elemento = tabela[tabela["Simbolo"] == elem]
    return elemento

def lista_tudo():
    return tabela

opcao = 0
while opcao != 4:
    print("Opções:\n 1- listar uma propriedade de todos os elementos.\n 2- listar todas as propriedades de um elemento.\n 3- listar todos os dados da tabela.\n 4- sair.")
    opcao = int(input("Digite sua opção: "))

    if opcao == 1:
        prop = input("Digite a propriedade que deseja ver: ")
        print(seleciona_propriedade(prop))
    elif opcao == 2:
        elem = input("Digite o símbolo do elemento que deseja ver: ")
        print(seleciona_elemento(elem))
    elif opcao == 3:
        print(lista_tudo())
    elif opcao == 4:
        exit()