# 32. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo 
# usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:

# Fatorial de: 5

# 5! = 5 . 4 . 3 . 2 . 1 = 120

from math import prod

fatores=[]
fatorando=0

num_fat= int(input('Digite o número que deseja fatorar: '))
while fatorando != num_fat:
    fatorando+=1
    fatores.append(fatorando)
    
print(f'O resultado fatorial de {num_fat} é {round(prod(fatores))}.')   