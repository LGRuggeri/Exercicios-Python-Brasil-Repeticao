# 24. Faça um programa que calcule o mostre a média aritmética de N notas.

list_num=[]

num= int(input('Digite quantos notas deseja a média aritmética: '))

for i in range(num):
    notas= int(input('Digite a nota do aluno: '))
    list_num.append(notas)
    
    
soma= sum(list_num)
media= soma/num
print(f'A média do aluno é: {media} ')