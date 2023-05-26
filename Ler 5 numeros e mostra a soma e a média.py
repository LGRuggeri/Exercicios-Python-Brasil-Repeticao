#Faça um programa que leia 5 números e informe a soma e a média dos números.

def main():
    soma = 0
    media = 0
    for i in range(5):
        n = int(input('Digite um número: '))
        soma += n
        media = soma / 5
        print(media)
        print(soma)
    return

main()
       