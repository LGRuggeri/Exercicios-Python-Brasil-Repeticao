# 36. Desenvolva um programa que faça a tabuada de um número qualquer inteiro 
# que será digitado pelo usuário, mas a tabuada não deve necessariamente 
# iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados 
# também pelo usuário, conforme exemplo abaixo:

# Montar a tabuada de: 5
# Começar por: 4
# Terminar em: 7
# Vou montar a tabuada de 5 começando em 4 e terminando em 7:

# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35
# Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

cont=0


tabuada= int(input('Digite a tabuada de qual número deseja: '))
comeco_tabuada= int(input('Digite por qual número deseja começar a tabuada: '))
fim_tabuada= int(input('Digite por qual número deseja terminar a tabuada: '))

while fim_tabuada < comeco_tabuada:
    print('Você digitou o final menor que o começo da tabuada, Favor digitar novamente')
    fim_tabuada= int(input('Digite por qual número deseja terminar a tabuada: '))
    
cont = comeco_tabuada    
    
for i in range(comeco_tabuada,fim_tabuada + 1):
    print(f'A tabuada do {tabuada} de {comeco_tabuada} até {fim_tabuada} é {tabuada} X {cont} = {tabuada * cont}')
    cont+=1
    
    