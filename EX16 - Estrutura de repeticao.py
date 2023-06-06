"""A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
Faça um programa que gere a série até que o valor seja maior que 500"""

numero = 1
numero_anterior = 0


while numero < 1000:
        print(numero)
        aux = numero
        numero += numero_anterior
        numero_anterior = aux
        if numero >= 800:
            break
    
    

