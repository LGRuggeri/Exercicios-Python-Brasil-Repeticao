# 27. Faça um programa que calcule o número médio de alunos por turma. 
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
# As turmas não podem ter mais de 40 alunos.

turmas = int(input("Quantas turmas? : "))
alunos_turmas = []
turma = 1

for i in range(turmas):
    print("turma ", turma)
    alunos = int(input("Alunos na turma : "))
    while alunos > 40:
        print("As turmas não podem ter mais de 40 alunos!")
        alunos = int(input("Digite a quantidade de alunos por turma: "))
    turma += 1
    alunos_turmas.append(alunos)

media = sum(alunos_turmas) / len(alunos_turmas)
print("A media e igual a: ", media)