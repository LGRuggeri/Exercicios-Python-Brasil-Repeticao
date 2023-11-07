# 49. Faça um programa que mostre os n termos da Série a seguir:
# S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
# Imprima no final a soma da série.

s_termos= []
s1_termos= []
    
n_termos= int(input('Digite a quantide de termos para calcular: '))

n=1
m=1
for i in range(n_termos):
    s= n
    s1= m
    s_termos.append(s)
    s1_termos.append(s1)
    print(s,'/',s1,'+')
    n+=1
    m+=2
soma= sum(s_termos)
soma1= sum(s1_termos)
soma_total= soma + soma1
print('Divesão dos termos: ',soma/soma1)
print('Valor final dos termos: ', soma,'/',soma1)
print('Soma total dos termos: ', soma_total)