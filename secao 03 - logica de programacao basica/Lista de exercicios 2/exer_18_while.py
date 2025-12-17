"""
Exercicio 18
Faca um programa para um caixa eletronico. O programa devera
perguntar ao usuario o valor do saque e depois informar quantas
notas de cada valor serao fornecidas. As notas disponiveis serao
as de 1, 5, 10, 50, 100 reais. O valor minimo é de 10 reais e o
maximo de 600 reais. O programa nao deve se preocupar com a
quantidade de notas existentes na maquina.

Ex 1: Para sacar a quantia de 256 reais, o programa fornece duas
notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1.
Ex 2: Para sacar a quantia de 399 reais, o programa fornece tres
notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e
quatro notas de 1.
"""

"""
saque = 50
valor = 100
notas = 0
enquanto verdadeiro
    se saque >= 100 (valor)
        saque -= 100 (valor)
        notas += 1
    senao
        se notas > 0
            escreva({notas} notas de R${valor:.2f})
        se valor == 100 (valor)
            valor = 50
        se senao valor == 50
            valor = 10
        se senao valor == 10
            valor = 5
        se senao valor == 5
            valor = 1
        notas = 0
        se saque == 0
            break
    senao
        escreva('Valor minimo de saque 10')
"""

valor = 100
notas = 0
sair = False
while True:
    saque = int(input('Digitre o valor do saque: R$ '))
    if 10 <= saque <= 600:
        while not sair:
            if saque >= valor:
                saque -= valor
                notas += 1
            else:
                if notas > 0:
                    print(f'{notas} notas de R${valor:7.2f}')
                if valor == 100:
                    valor = 50
                elif valor == 50:
                    valor = 10
                elif valor == 10:
                    valor = 5
                elif valor == 5:
                    valor = 1
                notas = 0
                if saque == 0:
                   sair = True
    if sair is True:
        break
    else:
        print('Valor minimo de saque de 10 e maximo de 600')
