# 38. Um funcionário de uma empresa recebe aumento salarial anualmente 
# Sabe-se que:

# Esse funcionário foi contratado em 1995, com salário inicial de 
# R$ 1.000,00;
# Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# A partir de 1997 (inclusive), os aumentos salariais sempre 
# correspondem ao dobro do percentual do ano anterior. 
# Faça um programa que determine o salário atual desse funcionário. 
# Após concluir isto, altere o programa permitindo que o usuário digite 
# o salário inicial do funcionário.

sal_init= 1000
perc_aumento= 1.5

ano_atual= int(input('Digite o ano atual: '))
salario= int(input('Digite o salario do funcionario: '))


for i in range(1996, ano_atual + 1):
    perc_aumento = perc_aumento * 2
    salario_atual = sal_init + (sal_init * (perc_aumento / 100))
    print('Salario em', i, " = %.2f " % salario_atual)
    
print('###################################################') 

for i in range(1996, ano_atual + 1):
    perc_aumento = perc_aumento * 2
    salario_atual = salario + (salario * (perc_aumento / 100))
    print('Salario em', i, " = %.2f " % salario_atual)  