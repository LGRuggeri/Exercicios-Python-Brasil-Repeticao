"""Desenvolva um gerador de tabuada, capaz de gerar a tabuada de 
qualquer número inteiro entre 1 a 10. 
O usuário deve informar de qual numero ele deseja ver a tabuada"""

num_tabuada= int(input('Digite de 1 a 10 de qual número deseja a tabuada:'))

if num_tabuada >= 1 and num_tabuada <= 10:
    for i in range(10):
        i += 1
        valores_tabuada= i * num_tabuada
        print(f'Você digitou o número {num_tabuada} os valores da tabuada do número é {i} x {num_tabuada} = {valores_tabuada} ')
