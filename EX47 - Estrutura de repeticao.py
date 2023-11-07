# 47. Em uma competição de ginástica, cada atleta recebe votos de sete jurados. 
# A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. 
# Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo
# atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada 
# (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). 
# As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme 
# o exemplo abaixo:

# Atleta: Aparecido Parente
# Nota: 9.9
# Nota: 7.5
# Nota: 9.5
# Nota: 8.5
# Nota: 9.0
# Nota: 8.5
# Nota: 9.7

# Resultado final:
# Atleta: Aparecido Parente
# Melhor nota: 9.9
# Pior nota: 7.5
# Média: 9,04

notas_jurados= []
count= 0

nome_atleta= input('Digite o nome do atleta: ')
for i in range(7):
    nota_jurado= float(input(f'{i+1} Jurado digite sua nota: '))
    notas_jurados.append(nota_jurado)

print('Atleta:', nome_atleta)
for i in range(7):
    print('Nota:', notas_jurados[count])
    count+=1
    
print('Resultado final:', '\nAtleta:', nome_atleta,'\nMelhor nota:', max(notas_jurados), '\nPior nota:', min(notas_jurados))
notas_jurados.remove(max(notas_jurados))
notas_jurados.remove(min(notas_jurados))
print('Média:', sum(notas_jurados)/len(notas_jurados))