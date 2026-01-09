"""
Exercicio 005
Crie um programa que tenha uma tupla unica com nomes 
de produtos e seus respectivos precos, na sequencia.
No final, mostre uma listagem de precos, organizando
os dados em forma tabular.
"""

listagem = ('Lapis', 1.75, 'borracha', 2.00, 'caderno', 15.90, 
    'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
    'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-' * 40)
print(f'{'LISTAGEM DE PRECOS':^40}')
print('-' * 40)
for pos, item in enumerate(listagem):
    if pos % 2 == 0:
        print(f'{item:.<30}', end='')
    else:
        print(f'R${item:7.2f}')
print('-' * 40)
