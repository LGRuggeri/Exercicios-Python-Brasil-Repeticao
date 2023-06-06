#Faça um programa que leia e valide as seguintes informações:
#1. Nome: maior que 3 caracteres;
#2. Idade: entre 0 e 150;
#3. Salário: maior que zero;
#4. Sexo: 'f' ou 'm';
#5. Estado Civil: 's', 'c', 'v', 'd';


nome_usuario= input('Digite o nome do usuário:')
while len(nome_usuario) <= 3:
     nome_usuario= input('O nome digitado possui menos que 3 caracter, digite novamente:')
     
idade_usuario= (int(input('Digite a idade do usuário:')))
while idade_usuario < 0 or idade_usuario > 150: 
    idade_usuario= (int(input('A idade do usuário deve ser entre 0 e 150 anos, digite novamente:')))
        
salario_usuario= (float(input('digite o salário do usuário:')))
while salario_usuario <= 0:
    salario_usuario= (float(input('Salário digitado zerado, digite novamente:')))
    
sexo_usuario= input('Digite o sexo do usuário F-(Feminino) ou M-(Masculino):')
while sexo_usuario != 'f' and sexo_usuario != 'm':
    sexo_usuario= input('Sexo digitado errado, digite o sexo do usuário F-(Feminino) ou M-(Masculino):')
    
estado_civil_usuario= input('Digite o estado civil do usuário S-(Solteiro), C-(Casado), V-(Viuvo), D-(Divorciado)')
while estado_civil_usuario != 's' and estado_civil_usuario != 'c' and estado_civil_usuario != 'v' and estado_civil_usuario and 'd':
    estado_civil_usuario= input('Estado civil digitado errado, digite o estado civil do usuário S-(Solteiro), C-(Casado), V-(Viuvo), D-(Divorciado)')   
    
else:
    print(f'O nome do usuário é {nome_usuario} sua idade {idade_usuario}, o salário de {nome_usuario} é {salario_usuario}, seu sexo é {sexo_usuario} e o seu estado civil é {estado_civil_usuario}')
