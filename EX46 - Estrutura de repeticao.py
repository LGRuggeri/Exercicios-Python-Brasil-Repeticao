# 46. Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
# No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. 
# O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que 
# receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a 
# média dos saltos conforme a descrição acima informada 
# (retirar o melhor e o pior salto e depois calcular a média). 
# Faça uso de uma lista para armazenar os saltos. 
# Os saltos são informados na ordem da execução, portanto não são ordenados. 
# O programa deve ser encerrado quando não for informado o nome do atleta. 
# A saída do programa deve ser conforme o exemplo abaixo:

# Atleta: Rodrigo Curvêllo
# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m
# Melhor salto: 6.5 m
# Pior salto: 5.3 m
# Média dos demais saltos: 5.9 m
# Resultado final:
# Rodrigo Curvêllo: 5.9 m

nome_atleta= True

while nome_atleta != '':
    lista_saltos= []
    nome_atleta= input('Digite o nome do atleta: ')
    if nome_atleta == '':
        break
    else:
        for i in range(4):
            saltos_atleta= float(input(f'Digite a distancia do {i+1} salto do atleta {nome_atleta}: '))
            lista_saltos.append(saltos_atleta)
        print(lista_saltos)
        print('Atleta: ',nome_atleta)
        n_salto= 1
        count= 0
        for i in range(4):
            print(n_salto, 'Salto:', lista_saltos[count], 'm')
            count+=1
            n_salto+=1   
        print(f'O melhor salto de {nome_atleta} foi: {max(lista_saltos)}')
        print(f'O pior salto de {nome_atleta} foi: {min(lista_saltos)}')
            
        lista_saltos.remove(max(lista_saltos))
        lista_saltos.remove(min(lista_saltos))
        media_saltos= sum(lista_saltos)/len(lista_saltos)  
        print('Média dos demais Saltos: "%.2f" m' % media_saltos)  
        print('Resultado final: \n ',f'{nome_atleta}:','"%.2f" m' % media_saltos) 
        print('Digite o nome do próximo Atleta ou deixe em branco para encerrar o programa!!!')