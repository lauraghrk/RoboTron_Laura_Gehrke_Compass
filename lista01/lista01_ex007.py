#7-Crie um programa que contêm uma função que receba dois parâmetros inteiros e retorna a média dos dois valores.

def calcula_media(v1, v2):
    return (v1+v2)/2

valor1 = int(input("Insira o primeiro valor: "))
valor2 = int(input("Insira o segundo valor: "))

print(calcula_media(valor1, valor2))