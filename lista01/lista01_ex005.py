#5-Construa um programa que recebe 20 valores para X e no final apresenta a média aritmética dos valores pares digitados

x = []

for i in range(0, 20):
    x.insert(i, int(input("Insira um valor: ")))

soma_pares = 0
conta_pares = 0

for i in range(0, len(x)):
    if x[i]%2 != 1:
        soma_pares = soma_pares + x[i]
        conta_pares = conta_pares + 1

media_pares = soma_pares/conta_pares

print("Média dos valores pares: " + str(media_pares))

# Referência sobre vetores: https://pt.stackoverflow.com/questions/217223/guardar-dados-dentro-de-um-vetor-com-loop-em-python#:~:text=Para%20voc%C3%AA%20armazenar%20os%20valores,o%20while%20ou%20o%20for%20.&text=Observe%20o%20funcionamento%20do%20algoritmo,comuns%20na%20hora%20da%20digita%C3%A7%C3%A3o.