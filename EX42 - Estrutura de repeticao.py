# 42. Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos 
# deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. 
# A entrada de dados deverá terminar quando for lido um número negativo.

lista_positivos= []
numeros_positivos= 0
numero_0_a_25= 0
numero_26_a_50= 0
numero_51_a_75= 0
numero_76_a_100= 0

while numeros_positivos >= 0:
    numeros_positivos= int(input('Digite o número positivo desejado ou negativo para encerrar: '))
    lista_positivos.append(numeros_positivos)
    

for numero in lista_positivos:
        if 0 <= numero <= 25:
            numero_0_a_25+=1   
for numero in lista_positivos:
        if 26 <= numero <= 50:
            numero_26_a_50+=1   
for numero in lista_positivos:
        if 51 <= numero <= 75:
            numero_51_a_75+=1   
for numero in lista_positivos:
        if 76 <= numero <= 100:
            numero_76_a_100+=1   

            
               
print(numero_0_a_25) 
print(numero_26_a_50) 
print(numero_51_a_75) 
print(numero_76_a_100) 