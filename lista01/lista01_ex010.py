#10-Crie um programa que recebe uma lista com três frutas e compare com uma lista com os valores ["maça", "banana", "pera"].

lista = ["maçã", "banana", "pera"]
frutas = []
for i in range(0, 3):
    frutas.insert(i, input("Insira uma fruta: "))

if set(frutas) == set(lista):
    print("As listas são iguais")
else:
    print("As listas não são iguais.")

#Referência do uso de set(): https://www.delftstack.com/pt/howto/python/compare-lists-python/#:~:text=Use%20o%20set%20para%20comparar%20listas%20em%20Python,-O%20Set%20%C3%A9&text=Podemos%20converter%20diretamente%20uma%20lista,e%20compar%C3%A1%2Dlos%20por%20igualdade.&text=Tamb%C3%A9m%20podemos%20descobrir%20os%20elementos,a%20interse%C3%A7%C3%A3o%20de%20dois%20conjuntos.