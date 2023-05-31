#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo 
#compreendido por eles.

def inteiros_Intervalo():
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    intervalo = []
    if n1 > n2:
        for i in range(n2, n1):
            i= i + 1
            intervalo.append(i)
          
    elif n2 > n1:
        for i in range(n1, n2):
            i= i + 1
            intervalo.append(i)
            
    else:
        print('Os números digitados são iguais')
     
    soma= sum(intervalo) 
    print(f'Os números digitados são {n1} e {n2}.')
    print(f'Os números inteiros que estão no intervalo compreendido por eles são {intervalo}.')
    print(soma)
    print(intervalo)
        
inteiros_Intervalo()
