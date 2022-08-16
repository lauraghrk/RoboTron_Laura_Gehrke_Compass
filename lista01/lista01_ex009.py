#9-Crie um programa que recebe 15 valores e armazena em uma lista, e no final da execução mostre os valores da lista do último para o primeiro.

lista = []

for i in range(0, 15):
    lista.insert(i, int(input("Digite um valor: ")))

lista.reverse()
print(lista)

# Referência sobre o reverse(): https://cursos.alura.com.br/forum/topico-inverter-a-ordem-de-uma-lista-125197