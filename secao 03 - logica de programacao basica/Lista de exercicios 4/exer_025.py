"""
Exercicio 025
Crie um programa que leia o nome e o preco de
varios produtos. O programa devera perguntar
se o usuario vai continuar.
No final, mostre:

A) Qual é o total gasto na compra
B) Quantos produtos custam mais de R$1000.00
C) Qual é o nome do produto mais barato
"""

from time import sleep
from os import system

print('-' * 30)
print(f'{'LOJA SUPER BARATAO':^30}')
print('-' * 30)

total = maior_1000 = preco_barato = 0
prod_barato = ''
while True:
    while True:
        produto = input('Nome do produto: ')
        if len(produto) < 3:
            print('Nome produto precisa ter 3 caracteres')
            continue
        break
    
    while True:
        preco = input('Preco: R$ ')
        try:
            preco = float(preco)
            if preco < 0:
                print('Preco precisa ser maior que zero')
                continue
            break
        except:
            print('Digite um numero')

    if preco > 1000:
        maior_1000 += 1

    if total == 0:
        preco_barato = preco
        prod_barato = produto
    else:
        if preco < preco_barato:
            preco_barato = preco
            prod_barato = produto

    total += preco

    while True:
        resp = input('Quer continuar? [S/N] ').lower()
        if resp == 's' or resp == 'n':
            break
        print('Resposta invalida! Digite \'S\' ou \'N\'')

    if resp == 'n':
        system('cls')
        print('\nEncerrando...')
        sleep(1)
        break

    print('-' * 30)

print(f'{' FIM DO PROGRAMA ':-^50}')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {maior_1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {prod_barato.lower()}, que custa R${preco_barato:.2f}')
