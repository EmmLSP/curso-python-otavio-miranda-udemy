"""
Exercicio 043
O cardapio de uma lanchonete é o seguinte:
Especificacao     Codigo   Preço
-----------------------------------
Cachorro Quente   100      R$ 1,20
Bauru Simples     101      R$ 1,30
Bauru com ovo     102      R$ 1,50
Hamburguer        103      R$ 1,20
Cheeseburguer     104      R$ 1,30
Refrigerante      105      R$ 1,00
-----------------------------------
Faca um programa que leia o codigo dos itens pedidos 
e as quantidades desejadas. Calcule e mostre o valor 
a ser pago por item (preco * quatidade) e o total
geral do pedido. Considere que o cliente deve informar
quando o pedido deve ser encerrado.
"""

from os import system
from time import sleep

cardapio = 'Especificacao     Codigo   Preço\n' \
'-----------------------------------\n' \
'Cachorro Quente   100      R$ 1,20\n' \
'Bauru Simples     101      R$ 1,30\n' \
'Bauru com ovo     102      R$ 1,50\n' \
'Hamburguer        103      R$ 1,20\n' \
'Cheeseburguer     104      R$ 1,30\n' \
'Refrigerante      105      R$ 1,00\n' \
'-----------------------------------'

pedido = f'\n{'Quantidade / item':<26}{'Total R$':<8}\n' \
'-----------------------------------\n'

valor_total = 0
while True:
    print(cardapio)
    codigo = int(input('Digite o codigo do seu pedido: '))

    if codigo < 100 or codigo > 105:
        system('cls')
        print('\033[31mCodigo invalido!\033[m\nDigite no intervalo entre 100 e 105')
        print('-' * 35)
        continue
    else:
        print(f'\033[32mCodigo valido!\033[m')

    while True:
        quantidade = int(input('Digite a quantidade de seu pedido: '))
        if quantidade < 1:
            print('Quantidade precisa ser pelo menos i item')
            continue
        break

    if codigo == 100:
        total = quantidade * 1.2
        pedido += f'{quantidade} Cachorro Quente         R${total:6.2f}\n'
    elif codigo == 101:
        total = quantidade * 1.3
        pedido += f'{quantidade} Bauru Simples           R${total:6.2f}\n'
    elif codigo == 102:
        total = quantidade * 1.5
        pedido += f'{quantidade} Bauru com ovo           R${total:6.2f}\n'
    elif codigo == 103:
        total = quantidade * 1.2
        pedido += f'{quantidade} Hamburger               R${total:6.2f}\n'
    elif codigo == 104:
        total = quantidade * 1.3
        pedido += f'{quantidade} Cheeseburguer           R${total:6.2f}\n'
    elif codigo == 105:
        total = quantidade * 1
        pedido += f'{quantidade} Refrigerante            R${total:6.2f}\n'

    valor_total += total

    print(f'{'\nTotal do pedido':<26}R${valor_total:6.2f}')
    print('-' * 35)

    sair = False
    while not sair:
        resp = input('Quer continuar pedindo? (S)im ou (N)ao: ').lower()
        if resp in 'sn':
            system('cls')
            break
        print('Entrada invalida! Digite \'S\' ou \'N\'')

    if resp == 'n':
        pedido += '-----------------------------------\n'
        pedido += f'{'Total a ser pago':<26}R${valor_total:6.2f}\n'
        pedido += '-----------------------------------\n'
        print('Processando pedido...')
        sleep(1)
        break

print(pedido)
