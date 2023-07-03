# 18. Faça um programa que, dado um conjunto de N números, 
# determine o menor valor, o maior valor e a soma dos valores.

lista_num=[]
count=0

rept= int(input('Digite quantos número deseja digitar: '))
while rept != count:
    num= int(input('Digite os números inteiros: '))
    
    lista_num.append(num)
    count+=1
    menor=min(lista_num)
    maior=max(lista_num)
    soma=sum(lista_num) 


print(menor)
print(maior)
print(soma)
