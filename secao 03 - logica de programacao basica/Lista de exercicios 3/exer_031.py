"""
Exercicio 031
O Sr. Manoel Joaquim expandiu seus negocios para alem dos negocios 
de R$1.99 e agora possui uma loja de conveniencias. Faca um programa 
que implemente uma caixa registradora rudimentar. O programa devera
receber um numero desconhecido de valores referentes aos precos das 
mercadorias. Um valor zero deve ser informado pelo operador para indicar 
o final da compra. O programa deve entao mostrar o total da compra e 
perguntar o valor em dinheiro que o cliente forneceu, para entao calcular
e mostrar o valor do troco. Apos esta operacao, o programa devera voltar 
ao ponto inicial, para registrar a proxima compra. 
A saida deve ser conforme o exemplo abaixo:

Lojas Tabajara
-------------------
Produto 1: R$  2.20
Produto 2: R$  5.80
Produto 3: R$  0.00
Total    : R$  9.00
Dinheiro : R$ 20.00
Troco    : R$ 11.00
-------------------
"""

from time import sleep
from os import system

total_geral = 0
while True:
    qtd_prod = int(input('Informe a quantidade de produtos: '))

    total = 0
    ticket = '\nLojas Tabajara\n'
    ticket += '-' * 20 + '\n'

    for itens in range(1, qtd_prod+1):
        preco = float(input(f'Digite o preco do produto {itens}: '))
        total += preco   
        ticket += f'Produto {itens}: R${preco:6.2f}\n'
    
    print(f'Total  : R${total:6.2f}')
    ticket += f'Total    : R${total:6.2f}\n'
    dinheiro_pagar = float(input('Digite o valor em dinheiro para pagar: R$ '))
    troco = total - dinheiro_pagar
    ticket += f'Troco    : R${troco:6.2f}\n'
    ticket += f'Dinheiro : R${total:6.2f}\n'
    ticket += f'-' * 30 + '\n'
    total_geral += total

    system('cls')
    print(ticket)

    while True:
        resp = input('Quer continuar? [S]im [N]ao: ').upper()
        if resp == 'S' or resp == 'N':
            break
        print('Entrada invalida! Digite \'S\' ou \'N\'')

    if resp == 'N':
        print('\nFinalizando compra...\n')
        sleep(1)
        break
    else:
        print('Proximo compra...')
        sleep(1)
        system('cls')

print('<<< FIM DAS COMPRAS >>>')
