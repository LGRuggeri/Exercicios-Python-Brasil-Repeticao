"""Altere o programa anterior permitindo ao usuário informar 
as populações e as taxas de crescimento iniciais. 
Valide a entrada e permita repetir a operação."""


while True: 
                         
    pop_A= float(input('Digite a quantidade populacional de A:'))
    pop_B= float(input('Digite a quantidade populacional de B:'))
    anos= 0
    taxa_crescmentoA= float(input('Digite a taxa de crescimento populacional de A:'))
    taxa_crescmentoB= float(input('Digite a taxa de crescimento populacional de B:'))

    while pop_A < pop_B:
        pop_A+= round((pop_A * taxa_crescmentoA)/100)
        pop_B+= round((pop_B * taxa_crescmentoB)/100)
        anos= anos + 1
    
    print(f'Será necessário {anos} anos para a população A passar ou igualar a população B.')
    print(f'populaçãoA possui {pop_A} habitantes')
    print(f'populaçãoB possui {pop_B} habitantes')
   
         
    
    
    
    
    
    
    
    
    
    
