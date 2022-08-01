#10-Crie um programa que recebe uma lista com três frutas e compare com uma lista com os valores ["maça", "banana", "pera"].

lista = ["maçã", "banana", "pera"]
frutas = []
for i in range(0, 3):
    frutas.insert(i, input("Insira uma fruta: "))

if frutas == lista:
    print("As listas são iguais")
else:
    print("As listas não são iguais.")
