# 26. Numa eleição existem três candidatos. Faça um programa que peça o número total 
# de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos 
# de cada candidato.

votacao=[]

eleitores= int(input('Digite a quantidade de eleitores: '))
for i in range(eleitores):
    votos= int(input('Digite o número do canditato que deseja de 1 há 3: '))
    votacao.append(votos)
    canditato1=votacao.count(1) 
    canditato2=votacao.count(2)  
    canditato3=votacao.count(3)  
    
    
print(f'O canditato 1 recebeu {canditato1} votos')
print(f'O canditato 2 recebeu {canditato2} votos')
print(f'O canditato 3 recebeu {canditato3} votos')