# 25. Faça um programa que peça para n pessoas a sua idade, 
# ao final o programa devera verificar se a média de idade da turma varia entre 0 e 
# 25, 26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, 
# conforme a média calculada.

lista_turma=[]

num_pessoas= int(input('Digite a quantidade de pessoas que possuem na turma: '))

for i in range(num_pessoas):
    idade_pessoas= int(input('Digite a idade das pessoas na turma: '))
    lista_turma.append(idade_pessoas)
    
soma= sum(lista_turma)
media= soma/num_pessoas

if media <= 25:
    print(f'A média de idade da turma é: {media}, sua turma é jovem.')
elif media > 25 and media <= 60:
    print(f'A média de idade da turma é: {media}, sua turma é adulta.')
else:
    print(f'A média de idade da turma é: {media}, sua turma é idosa.')