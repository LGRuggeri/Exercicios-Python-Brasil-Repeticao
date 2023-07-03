# 19. Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

lista_num=[]
count=0

rept= int(input('Digite quantos número deseja digitar: '))
while rept != count:
    num= int(input('Digite um número inteiro entre 0 e 1000: '))
    
    while num > 1000 or num < 0:
        num= int(input('Você digitou um número fora do intervalo, digite novamente: '))
        
        
    lista_num.append(num)
    count+=1
    menor=min(lista_num)
    maior=max(lista_num)
    soma=sum(lista_num)    

print(menor)
print(maior)
print(soma)