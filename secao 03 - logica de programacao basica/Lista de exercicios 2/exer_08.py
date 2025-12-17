"""
Exercicio 08
Faca um programa que pergunte o preco de tres produtos
e informe qual produto voce deve comprar sabendo que a 
decisao e sempre pelo mais barato.
"""

preco1 = float(input('Digite o preco do produto 1: R$ '))
preco2 = float(input('Digite o preco do produto 2: R$ '))
preco3 = float(input('Digite o preco do produto 3: R$ '))
prod_mais_barato = ''
if preco1 <= preco2 and preco1 <= preco2:
    prod_mais_barato += f'Compre o produto 1 e mais barato\n'
    prod_mais_barato += f'Preco do produto 1: R$ {preco1:.2f}\n'
elif preco2 <= preco1 and preco2 <= preco3:
    prod_mais_barato += f'Compre o produto 2 e mais barato\n'
    prod_mais_barato += f'Preco do produto 2: R$ {preco2:.2f}\n'
else:
    prod_mais_barato += f'Compre o produto 3 e mais barato\n'
    prod_mais_barato += f'Preco do produto 3: R$ {preco3:.2f}\n'
print('-' * 30)
print(prod_mais_barato)
