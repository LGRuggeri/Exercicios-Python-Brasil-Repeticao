#Faça um programa que leia 5 números e informe o maior número.

print(max([int(input(f"Informe um número na posição {x}: ")) for x in range(5)]))
