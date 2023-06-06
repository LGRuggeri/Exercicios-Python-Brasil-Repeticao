"""A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o n-ésimo termo."""


numero = 1
numero_anterior = 0

termos_fibonacci= int(input('Digite quantas termos quer gerar de Fibonacci: '))
for _ in range(termos_fibonacci):
    print(numero)
    aux = numero
    numero += numero_anterior
    numero_anterior = aux
    
          
print(f'A quantidade de termos gerados foram {termos_fibonacci}')
