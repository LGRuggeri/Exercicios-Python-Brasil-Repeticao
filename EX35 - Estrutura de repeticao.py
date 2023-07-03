# 35. Encontrar números primos é uma tarefa difícil. 
# Faça um programa que gera uma lista dos números primos existentes entre 1 
# e um número inteiro informado pelo usuário.

lista_primo=[]

num_primo= int(input('Digite um número inteiro: '))

for i in range(num_primo + 1):
    if i%2 ==1 and i!=2:
        lista_primo.append(i)
    
print(f'Os números primos até {num_primo} são: {lista_primo}')        