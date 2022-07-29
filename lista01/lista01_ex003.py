#3-Construa um programa que recebe dois valores, soma esses valores e apresenta se o resultado é par ou impar

valor1 = int(input("Insira o valor 1: "))
valor2 = int(input("Insira o valor 2: "))

soma = valor1 + valor2

if soma%2 != 1:
    print("A soma é par!")
else:
    print("A soma é ímpar!")