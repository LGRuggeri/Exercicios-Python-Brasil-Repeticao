# 37. Uma academia deseja fazer um senso entre seus clientes para descobrir o 
# mais alto, o mais baixo, o mais gordo e o mais magro, para isto você deve 
# fazer um programa que pergunte a cada um dos clientes da academia seu código, 
# sua altura e seu peso. O final da digitação de dados deve ser dada quando o 
# usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser 
# informados os códigos e valores do cliente mais alto, do mais baixo, 
# do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes.

cod_clientes = []
altura_clientes = []
peso_clientes = []
n_cliente = 1
codigo = True

while codigo != 0:
    print('\nCliente n° ', n_cliente)
    codigo = int(input('Digite o código: '))
    if codigo == 0:
        break
    else:
        altura = float(input('Digite a altura: '))
        peso = float(input('Digite o peso: '))
        cod_clientes.append(codigo)
        altura_clientes.append(altura)
        peso_clientes.append(peso)
        n_cliente += 1

cod_magro = peso_clientes.index(min(peso_clientes))
peso_magro = peso_clientes.index(min(peso_clientes))
altura_magro= peso_clientes.index(min(peso_clientes))
cod_gordo = peso_clientes.index(max(peso_clientes))
peso_gordo = peso_clientes.index(max(peso_clientes))
altura_gordo = peso_clientes.index(max(peso_clientes))
cod_alto = altura_clientes.index(max(altura_clientes))
peso_alto = altura_clientes.index(max(altura_clientes))
altura_alto = altura_clientes.index(max(altura_clientes))
cod_baixo = altura_clientes.index(min(altura_clientes))
peso_baixo = altura_clientes.index(min(altura_clientes))
altura_baixo = altura_clientes.index(min(altura_clientes))


print('\n' * 2)
print(f'Código do mais magro:{cod_clientes[cod_magro]}, seu peso {peso_clientes[peso_magro]} e sua altura {altura_clientes[altura_magro]}')
print(f'Código do mais gordo:{cod_clientes[cod_gordo]}, seu peso {peso_clientes[peso_gordo]} e sua altura {altura_clientes[altura_gordo]}')
print(f'Código do mais alto:{cod_clientes[cod_alto]}, seu peso {peso_clientes[peso_alto]} e sua altura {altura_clientes[altura_alto]}')
print(f'Código do mais baixo:{cod_clientes[cod_baixo]}, seu peso {peso_clientes[peso_baixo]} e sua altura {altura_clientes[altura_baixo]}')
print(f'Média de altura: {sum(altura_clientes) / len(altura_clientes)}')
print(f'Média de peso: {sum(peso_clientes) / len(peso_clientes)}')