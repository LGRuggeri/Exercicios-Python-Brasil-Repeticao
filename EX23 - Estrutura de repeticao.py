# 23. Faça um programa que mostre todos os primos entre 1 e N sendo N 
# um número inteiro fornecido pelo usuário. O programa deverá mostrar também 
# o número de divisões que ele executou para encontrar os números primos.
# Serão avaliados o funcionamento, o estilo e o 
# número de testes (divisões) executados.

lista_primo=[]
divisoes=0

num_primo= int(input('Digite um número: '))

for i in range(num_primo + 1):
    if i % 2 == 1 and i != 2:
        lista_primo.append(i)
        divisoes += 1
    else:
        divisoes += 1
print(f'Números primos: {lista_primo} ')
print(f'Número de divisões: {divisoes}')