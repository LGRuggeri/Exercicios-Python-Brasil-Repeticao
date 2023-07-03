# 17. Faça um programa que calcule o fatorial de um número inteiro 
# fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

fat_num= int(input('Digite o número inteiro que deseja calcular o fatorial: '))

resultado=1
count=1

while count <= fat_num:
    resultado *= count
    count += 1

print(resultado)