"""
Exercicio 25
O hipermercado Tabajara esta com uma promocao de carnes que
é imperdivel. Confira:
-----------------------------------
1. Ate 5Kg
- File duplo - R$ 4.90 por Kg
- Alcatra    - R$ 5.90 por Kg
- Picanha    - R$ 6.90 por Kg
2. Acima de 5Kg
- File duplo - R$ 5.80 por Kg
- Alcatra    - R$ 6.80 por Kg
- Picanha    - R$ 7.80 por Kg
-----------------------------------
Para atender a todos os clientes, cada cliente podera levar
apenas um dos tipos de carne da promocao, porem nao ha limites
para a quantidade de carne por cliente. Se a compra for feita
no cartao Tabajara o cliente recebera ainda um desconto de 5%
sobre o total da compra. Escreva um programa que peca o tipo e
a quantidade de carne comprada pelo usuario e gere um cupom
fiscal, contendo as informações da compra:
tipo e quantidade de carne, preco total, tipo de pagamento,
valor do desconto e valor a pagar.
"""

print('-' * 20)
print('''Cod  Tipo de Carne:
[1]  File Duplo
[2]  Alcatra
[3]  Picanha''')
print('-' * 20)

tipo_carne = input('Digite o tipo de carne comprada: ')

if tipo_carne.isdigit():
    gera_cupom = True
    qtd_carne = float(input('Digite a quantidade de carne: Kg '))
    
    preco_carne = 0
    if tipo_carne == '1':
        tipo_carne = 'File Duplo'
        if qtd_carne <= 5:
            preco_carne = 4.90
        else:
            preco_carne = 5.80
    elif tipo_carne == '2':
        tipo_carne = 'Alcatra'
        if qtd_carne <= 5:
            preco_carne = 5.90
        else:
            preco_carne = 6.80 
    elif tipo_carne == '3':
        tipo_carne = 'Picanha'
        if qtd_carne <= 5:
            preco_carne = 6.90
        else:
            preco_carne = 7.80 
    else:
        gera_cupom = False

    total = qtd_carne * preco_carne
    
    preco_total = 0
    valor_desc = 0

    if gera_cupom is True:
        tipo_pag = input('Digite o tipo de pagamento? [C]artao ou [D]inheiro: ').upper()
        if tipo_pag == 'C':
            tipo_pag = 'Cartao'
            valor_desc = (total * 5) / 100
            total -= valor_desc # pagamento com cartao, desconto de 5%
            preco_total = total
        elif tipo_pag == 'D':
            tipo_pag = 'Dinheiro'
            preco_total = total # pagamento com dinheiro, sem desconto
        else:
            gera_cupom = False

    if gera_cupom is True:
        print('-' * 40)
        print(f'{'CUPOM FISCAL DA COMPRA':^38}')
        print('-' * 40)
        print(f'Tipo de carne..............: {tipo_carne}')
        print(f'Quanidade de carne.........: {qtd_carne} Kg')
        print(f'Tipo de pagamento..........: {tipo_pag}')
        print(f'Valor do desconto..........: R${valor_desc:6.2f}')
        print(f'Valor total a pagar........: R${preco_total:6.2f}')
        print('-' * 40)
    else:
        print('Programa encerrado com entrada invalida!')
else:
    print('Codigo precisa ser um numero')
