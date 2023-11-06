# 44. Em uma eleição presidencial existem quatro candidatos. 
# Os votos são informados por meio de código. 
# Os códigos utilizados são:

# 1 , 2, 3, 4 - Votos para os respectivos candidatos
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:

# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. 
# Para finalizar o conjunto de votos tem-se o valor zero.

import itertools

candidatos= []
votos_candidato1= []
votos_candidato2= []
votos_candidato3= []
votos_candidato4= []
votos_nulos= []
votos_branco= []
soma_votos= []
contador= 0
votos_contador= 0
canditado_voto_zerado= []

while contador <=3:
    candidato= input('Digite o nome do candidato: ')
    candidatos.append(candidato)
    contador+=1
  
print('Os canditatos disponíveis para votação são: ')
for i, candidato in enumerate(candidatos,1):
    print(i,'-',candidato)

print('Para votação NULA ou BRANCO digite: ')    
print('5 - nulo\n6 - brancos')

while votos_contador <=10:    
    votos= int(input('Selecione o número do voto conforme o seu candidato: '))
    if votos == 1:
        votos_candidato1.append(votos)
    elif votos == 2:
        votos_candidato2.append(votos)
    elif votos == 3:
        votos_candidato3.append(votos)
    elif votos == 4:
        votos_candidato4.append(votos)
    elif votos == 5:
        votos_nulos.append(votos)
    elif votos == 6:
        votos_branco.append(votos)
    else:
        print('Número digitado não confere com nenhum dos candidatos, por favor digitar novamente!!! ')
    votos_contador+=1

junta_votos= [votos_candidato1,votos_candidato2,votos_candidato3,votos_candidato4,votos_nulos,votos_branco]
soma_votos= list(itertools.chain(*junta_votos))

for i,candidato in enumerate(candidatos,1):
    if i == 1:
        candidato1= candidato
        print(f'O candidato {candidato1} teve um total de {len(votos_candidato1)} voto(s)')   
    if i == 2:
        candidato2= candidato
        print(f'O candidato {candidato2} teve um total de {len(votos_candidato2)} voto(s)')   
    if i == 3:
        candidato3= candidato
        print(f'O candidato {candidato3} teve um total de {len(votos_candidato3)} voto(s)')   
    if i == 4:
        candidato4= candidato
        print(f'O candidato {candidato4} teve um total de {len(votos_candidato4)} voto(s)')
        
print(f'Os votos nulos teve um total de {len(votos_nulos)} voto(s)')
print(f'Os votos em branco teve um total de {len(votos_branco)} voto(s)')   

percentagem_votos_nulos= (len(votos_nulos)/len(soma_votos))* 100
percentagem_votos_brancos= (len(votos_branco)/len(soma_votos))* 100
print(f'A percentagem de votos nulos é', "%.2f" % percentagem_votos_nulos)
print(f'A percentagem de votos nulos é', "%.2f" % percentagem_votos_brancos)

for i, candidato in enumerate(candidatos,1):
    if len(votos_candidato1) == 0 and i == 1:
        canditado_voto_zerado.append(candidato)
    elif len(votos_candidato2) == 0 and i == 2:
        canditado_voto_zerado.append(candidato)
    elif len(votos_candidato3) == 0 and i == 3:
        canditado_voto_zerado.append(candidato)
    elif len(votos_candidato4) == 0 and i == 4:
        canditado_voto_zerado.append(candidato)

print(f'O conjunto de votos zerados são: {canditado_voto_zerado}')