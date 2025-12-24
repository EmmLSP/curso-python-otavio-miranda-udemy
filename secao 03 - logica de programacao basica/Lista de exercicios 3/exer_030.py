"""
Exercicio 030
O Sr. Manoel Joaquim acaba de adquirir uma panificadora
e pretende implantar a metodologia da tabelinha, que ja
é um sucesso na sua loja de R$1.99. Voce foi contratado
para desenvolver o programa que monta a tabela de precos
de paes, de 1 ate 50 paes, a partir do preco do pao
informado pelo usuario, conforme exemplo abaixo:

Preco do pao: R$ 0.18
Panificadora Pao de Ontem - Tabela de Precos
1 - R$ 0.18
2 - R$ 0.36
...
50 - R$ 9.00
"""

preco_pao = float(input('Digite o preco do pao: R$ '))

print(f'Preco do pao: R${preco_pao:.2f}')
print('-' * 45)
print('Panificadora Pao de Ontem - Tabela de Precos')
print('-' * 45)
for itens in range(1, 51):
    print(f'{itens:2} - R${preco_pao * itens:5.2f}')
print('-' * 45)
