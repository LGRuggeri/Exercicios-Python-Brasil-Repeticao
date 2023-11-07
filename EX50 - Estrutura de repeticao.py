# 50. Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

h= 1
n=1

n_termos= int(input('Digite o números de termos para ser calculado: '))

for i in range(n_termos):
    print(f'Valor do {i+1} termo: ', h,'/',n)
    n+=1

