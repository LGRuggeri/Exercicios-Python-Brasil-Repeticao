#Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

valor_valido= (float(input('Digite uma nota entre zero e dez:')))

while valor_valido > 10:
   valor_valido= (float(input('Digite uma nota entre zero e dez:')))
    
print(f'A nota digitada foi {valor_valido}')
    
    