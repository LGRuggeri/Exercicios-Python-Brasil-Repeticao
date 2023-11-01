# 43. Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
# Considere que o cliente deve informar quando o pedido deve ser encerrado.
# O cardápio de uma lanchonete é o seguinte:

# Especificação - Código - Preço

# Cachorro Quente - 100 - R$ 1,20
# Bauru Simples - 101 - R$ 1,30
# Bauru com ovo - 102 - R$ 1,50
# Hambúrguer - 103 - R$ 1,20
# Cheeseburguer - 104 - R$ 1,30
# Refrigerante - 105 - R$ 1,00

saida=0
lista_item= []
lista_quantidade= []
valor_cod100= 1.20
valor_cod101= 1.30
valor_cod102= 1.50
valor_cod103= 1.20
valor_cod104= 1.30
valor_cod105= 1.00
preco100= 0
preco101= 0
preco102= 0
preco103= 0
preco104= 0
preco105= 0

while saida == 0:
    info_cardapio= print(' Especificação      Código    Preço')
    cardapio= print(' Cachorro Quente  -  100   -  R$ 1,20\n',
                'Bauru Simples    -  101   -  R$ 1,30\n',
                'Bauru com ovo    -  102   -  R$ 1,50\n',
                'Hambúrguer       -  103   -  R$ 1,20\n',
                'Cheeseburguer    -  104   -  R$ 1,30\n',
                'Refrigerante     -  105   -  R$ 1,00')
    item_pedido= int(input('Digite o código do item desejado: '))
    lista_item.append(item_pedido)
    print(lista_item)
    quantidade_pedido= int(input('Digite a quantidade: '))
    lista_quantidade.append(quantidade_pedido)
    print(lista_quantidade)
    saida= int(input('Deseja pedir algo mais? 0 - Sim e 1 - Não: '))

for i, item in enumerate(lista_item):
    if item == 100:
        item = 'Cachorro Quente'
        preco100= valor_cod100 * lista_quantidade[i]
        print(f'Você comprou {lista_quantidade[i]}', item, 'e ficou no valor de R$',"%.2f" % preco100)
    if item == 101:
        item = 'Bauru Simples'
        preco101= valor_cod101 * lista_quantidade[i]
        print(f'Você comprou {lista_quantidade[i]}', item, 'e ficou no valor de R$',"%.2f" % preco101)
    if item == 102:
        item = 'Bauru com ovo'  
        preco102= valor_cod102 * lista_quantidade[i]
        print(f'Você comprou {lista_quantidade[i]}', item, 'e ficou no valor de R$',"%.2f" % preco102)
    if item == 103:
        item = 'Hambúrguer'
        preco103= valor_cod103 * lista_quantidade[i]
        print(f'Você comprou {lista_quantidade[i]}', item, 'e ficou no valor de R$',"%.2f" % preco103)
    if item == 104:
        item = 'Cheeseburguer'
        preco104= valor_cod104 * lista_quantidade[i]
        print(f'Você comprou {lista_quantidade[i]}', item, 'e ficou no valor de R$',"%.2f" % preco104)
    if item == 105:
        item = 'Refrigerante'
        preco105= valor_cod105 * lista_quantidade[i]
        print(f'Você comprou {lista_quantidade[i]}', item, 'e ficou no valor de R$',"%.2f" % preco105)
        
soma_total= preco100 + preco101 + preco102 + preco103 + preco104 + preco105
print('O valor total do seu pedido é R$', "%.2f" % soma_total)    