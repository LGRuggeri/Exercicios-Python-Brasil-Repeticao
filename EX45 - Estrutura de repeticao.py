# 45. Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, 
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
# 10 - A

# Após concluir isto você poderia incrementar o programa permitindo que o professor digite 
# o gabarito da prova antes dos alunos usarem o programa.

gabarito= ['A','B','C','D','E','E','D','C','B','A']
resposta_aluno= []
respostas_corretas= []
perguntas = 0
contador_pergunta= 0

while contador_pergunta <=1:
    perguntas+=1
    gabarito_aluno= input(f'Aluno digite a resposta da {perguntas} pergunta: ')
    resposta_aluno.append(gabarito_aluno)
    contador_pergunta+=1


for j, resposta in enumerate(resposta_aluno):
    for i, gabarito in enumerate(gabarito):
        if resposta == gabarito:
            respostas_corretas.append(resposta)
            print(respostas_corretas)
