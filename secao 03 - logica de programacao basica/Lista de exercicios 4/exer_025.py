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
total = maior_1000 = menor_preco = cont = 0
prod_barato = ''
while True:
    while True:
        produto = input(f'Nome do produto {cont + 1}: ').strip()
        if len(produto) < 3:
            print('Nome produto precisa ter 3 caracteres')
            continue
        break
    
    while True:
        preco = input('Preco: R$ ')
        try:
            preco = float(preco)
            if preco <= 0:
                print('Preco do produto precisa ser maior que 0')
                continue
            break
        except:
            print('Entrada invalida! Digite um numero.')

    if preco > 1000:
        maior_1000 += 1

    # simplificando codigo comentando abaixo
    if cont == 0 or preco < menor_preco:
        menor_preco = preco
        prod_barato = produto

    # if cont == 0:
    #     menor_preco = preco
    #     prod_barato = produto
    # else:
    #     if preco < menor_preco:
    #     menor_preco = preco
    #         prod_barato = produto

    total += preco
    cont += 1

    while True:
        resp = input('Quer continuar? [S/N] ').strip().lower()[0]
        if resp == 's' or resp == 'n':
            break
        print('Entrada invalida! Digite \'S\' ou \'N\'')

    if resp == 'n':
        system('cls')
        print('\nEncerrando...')
        sleep(1)
        break

    print('-' * 30)

print(f'{' FIM DO PROGRAMA ':-^50}')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {maior_1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {prod_barato.lower()}, que custa R${menor_preco:.2f}')
