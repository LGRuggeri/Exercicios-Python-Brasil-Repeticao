"""Faça um programa que peça 10 números inteiros, calcule e mostre a 
quantidade de números pares e a quantidade de números impares."""

numeros= []
par= 0
impar= 0

for impar_par in range(10):
    impar_par= int(input('Digite 10 números:'))
    numeros.append(impar_par)
    if impar_par %2 ==0:
        par += 1
        print(f'O número {impar_par} é par')
    else:
        impar += 1
        print(f'O número {impar_par} é ímpar')
 
 
print(f'Os numeros digitados foram {numeros} no total foram {par} pares e {impar} impares')
    
