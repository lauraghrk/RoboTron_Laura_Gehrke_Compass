#8-Crie um programa que lê 1 valor inteiro para X. Se o valor for par, calcular o fatorial de x em uma função e apresentar o resultado fora da função. Se o valor for impar, apresentar em uma função a tabuada de 1 a 10 de X.

from math import factorial

def fatorial(x):
    return factorial(x)

def tabuada(x):
    for i in range(1, 11):
        print(i*x)

x = int(input("Digite um valor inteiro: "))
if x%2 == 0:
    print(fatorial(x))
else:
    tabuada(x)

#Referência sobre fatorial: https://www.delftstack.com/pt/howto/python/python-factorial/#:~:text=Isso%20pode%20ser%20feito%20usando,n%C3%BAmero%20cujo%20fatorial%20deseja%20calcular.