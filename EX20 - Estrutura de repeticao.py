# 20. Altere o programa de cálculo do fatorial, 
# permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial 
# a números inteiros positivos e menores que 16.

import math
count = 0

rept = int(input('Digite a quantiade de número que deseja digitar: '))
while rept != count:
    numero = int(input("Digite um número: "))
    while numero // 1 != numero or numero < 0 or 0 or numero > 16:
        numero = int(input('Você digitou um número fora do intervalo, digite novamente: '))

    print("Fatorial do número digitado: ", math.factorial(numero))
    count += 1