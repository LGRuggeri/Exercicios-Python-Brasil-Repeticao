# 45. Desenvolver um programa para verificar a nota do aluno em uma prova com 3 questões, 
# o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito 
# da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). 
# Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema.
# Após todos os alunos terem respondido informar:

# Maior e Menor Acerto;
# Total de Alunos que utilizaram o sistema;
# A Média das Notas da Turma.
# Gabarito da Prova:

# 01 - A
# 02 - B
# 03 - C
# 04 - D
# 05 - E
# 06 - E
# 07 - D
# 08 - C
# 09 - B
# 3 - A

# Após concluir isto você poderia incrementar o programa permitindo que o professor digite 
# o gabarito da prova antes dos alunos usarem o programa.

gabarito= []
resposta_aluno= []
notas_tiradas= []
total_alunos_sistema= 0


for i in range(3):
    print('Professor digite as respostas do gabarito!')
    gabarito_professor= input(f'resposta da {i+1} pergunta: ')
    gabarito_professor_maiuscula= gabarito_professor.upper()
    gabarito.append(gabarito_professor_maiuscula)
    

numero_aluno= 1
continuar= True
while continuar != 'n':
    print(f'Bem vindo aluno n° {numero_aluno}: ')
    resposta_aluno.clear()
    for i in range(3):
        gabarito_aluno= input(f'Aluno digite a resposta da {i+1} pergunta: ')
        gabarito_aluno_maiuscula= gabarito_aluno.upper()
        resposta_aluno.append(gabarito_aluno_maiuscula)  
    nota= 0
    for i in range(3):
        if resposta_aluno[i] == gabarito[i]:
            nota+=1
    notas_tiradas.append(nota)
    continuar= input('Outro aluno irá realizar a prova? s-SIM ou n-NÃO: ')
    numero_aluno+=1

print(f'A maior nota tirada foi: {max(notas_tiradas)}')
print(f'A menor nota tirada foi: {min(notas_tiradas)}')
print(f'O total de alunos que realizaram a prova foi: {len(notas_tiradas)}')
print(f'A média de nota da turma foi de: {sum(notas_tiradas)/len(notas_tiradas)}')
print(f'Gabarito da prova: {gabarito}')