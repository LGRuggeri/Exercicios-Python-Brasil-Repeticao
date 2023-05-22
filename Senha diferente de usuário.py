#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
#mostrando uma mensagem de erro e voltando a pedir as informações.

nome_usuario= input('Digite o nome do usuário:')
senha_usuario= input('Digite a senha do usuário:')

if nome_usuario == senha_usuario:
    print('Nome de usuário não pode ser igual a senha, por favor digitar novamente a senha!!')
    senha_usuario= input('Digite novamente a senha:')
    
print(f'O usuário digitado foi {nome_usuario} e a senha {senha_usuario}')
