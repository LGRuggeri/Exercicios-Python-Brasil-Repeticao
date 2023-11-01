#41. Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: 
#valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
#Os juros e a quantidade de parcelas seguem a tabela abaixo:
#Quantidade de Parcelas % de Juros sobre o valor inicial da dívida


juros= 0
juros1= 0.10
juros2= 0.15
juros3= 0.20
juros4= 0.25
parcerlamento= 1
parcerlamento1= 3
parcerlamento2= 6
parcerlamento3= 9
parcerlamento4= 12

valor_divida= float(input('Digite o valor da Dívida: '))

cobranca_A= int(valor_divida*juros)
cobranca_B= int(valor_divida*juros1)
cobranca_C= int(valor_divida*juros2)
cobranca_D= int(valor_divida*juros3)
cobranca_E= int(valor_divida*juros4)

dados_cobranca= print('Valor da Dívida - Valor dos Juros - Quantidade de Parcelas - Valor da Parcela')
pagamento_A= print('R$',valor_divida,'      -       ',cobranca_A,'        -       ',parcerlamento,'      -       ','R$',((valor_divida+cobranca_A)/parcerlamento))
pagamento_A= print('R$',valor_divida+cobranca_B,'      -       ',cobranca_B,'      -       ',parcerlamento1,'      -       ','R$',"%.2f" % ((valor_divida+cobranca_B)/parcerlamento1))
pagamento_A= print('R$',valor_divida+cobranca_C,'      -       ',cobranca_C,'      -       ',parcerlamento2,'      -       ','R$',"%.2f" % ((valor_divida+cobranca_C)/parcerlamento2))
pagamento_A= print('R$',valor_divida+cobranca_D,'      -       ',cobranca_D,'      -       ',parcerlamento3,'      -       ','R$',"%.2f" %((valor_divida+cobranca_D)/parcerlamento3))
pagamento_A= print('R$',valor_divida+cobranca_E,'      -       ',cobranca_E,'      -       ',parcerlamento4,'     -       ','R$',"%.2f" %((valor_divida+cobranca_E)/parcerlamento4))