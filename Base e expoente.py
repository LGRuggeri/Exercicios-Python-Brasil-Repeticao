"""Faça um programa que peça dois números, base e expoente, 
calcule e mostre o primeiro número elevado ao segundo número. 
Não utilize a função de potência da linguagem."""

base= int(input('Digite o número que será a base: '))
expoente= int(input('Digite o número que será o expoente: '))

base_expoente= base ** expoente

print(f'A base {base} pelo expoente {expoente} da o resultado de {base_expoente} ')
