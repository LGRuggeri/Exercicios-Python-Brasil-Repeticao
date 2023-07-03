# 33. O Departamento Estadual de Meteorologia lhe contratou para desenvolver um 
# programa que leia um conjunto indeterminado de temperaturas, e informe ao 
# final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

continuar=1
temperaturas=[]

while continuar != 0:
    temperatura= float(input('Digite a temperatura: '))
    temperaturas.append(temperatura)
    continuar= int(input('Você deseja informar mais temperaturas? 1-Sim ou 0-Não:  '))
    if continuar ==0:
        print(f'A temperatura mínima é: {min(temperaturas)}')
        print(f'A temperatura máxima é: {max(temperaturas)}')
        