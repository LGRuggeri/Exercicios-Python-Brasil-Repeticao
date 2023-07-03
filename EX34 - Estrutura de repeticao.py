# 34. Os números primos possuem várias aplicações dentro da Computação, 
# por exemplo na Criptografia. Um número primo é aquele que é divisível apenas 
# por um e por ele mesmo. Faça um programa que peça um número inteiro e determine 
# se ele é ou não um número primo.


num_primo= int(input('Digite um número inteiro: '))

resultado_primo = num_primo%2

if resultado_primo ==1 or num_primo==2:
    print(f'O {num_primo} é primo')
else:
    print(f'O {num_primo} não é primo')
    
    