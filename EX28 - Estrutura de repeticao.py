# 28. Faça um programa que calcule o valor total investido por um colecionador em sua 
# coleção de CDs e o valor médio gasto em cada um deles. 
# O usuário deverá informar a quantidade de CDs e o valor pago em cada um.

cd= 1
cont=0
valores_cds=[]

qtd_cds= int(input('Quantos CDS foram comprados?: '))

for i in range(qtd_cds):
    print('CD', cd)
    valor_pago= float(input('Qual o valor pago no CD: '))
    while cont==qtd_cds:
        valor_pago= float(input('Qual o valor pago no CD: '))
    cd+=1
    cont+=1
    valores_cds.append(valor_pago)
    
media_pago= round(sum(valores_cds) / len(valores_cds))
print(f'A média de valor pago por CD foi de {media_pago}')
        
                      