#6-Construa um programa que receba uma valor inteiro maior que 2 em uma variavel x e apresenta os impares entre 0 e x.

x = int(input("Insira um valor maior que 2: "))
impares = []

if x<=2:
    print("INVÁLIDO")
else:
    for i in range(0, x+1):
        if i%2 == 1:
            impares.insert(i, i)
    print(impares)