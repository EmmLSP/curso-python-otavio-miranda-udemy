"""
Exercicio 026
Crie um programa que simule o funcionamento de um
caixa eletronico. No inicio, pergunte ao usuario
qual sera o valor a ser sacado (numero inteiro) e
o programa vai informar quantas cedulas de cada
valor serao entregues.

Obs.: Considere que o caixa possui cedulas de
R$50.00, R$20.00, R$10.00 e R$1.00.
"""

print('=' * 35)
print(f'{'BANCO CEV':^30}')
print('=' * 35)

valor = int(input('Qual valor voce quer sacar? R$ '))
total = valor
ced_atual = 200
total_ced = 0
while True:
    if total >= ced_atual:
        total -= ced_atual
        total_ced += 1
    else:
        if total_ced > 0:
            print(f'Total de {total_ced:02} cédulas de R${ced_atual:7.2f}')
        if ced_atual == 200:
            ced_atual = 100
        elif ced_atual == 100:
            ced_atual = 50
        elif ced_atual == 50:
            ced_atual = 20
        elif ced_atual == 20:
            ced_atual = 10
        elif ced_atual == 10:
            ced_atual = 5
        elif ced_atual == 5:
            ced_atual = 1
        total_ced = 0
        if total == 0:
            break

print('=' * 35)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
