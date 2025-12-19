"""
Exercicio 024
Uma fruteira esta vendendo frutas com a seguinte tabela
de precos:
1. Ate 5kg
- Morango - R$ 2.50 por Kg
- Maca    - R$ 1.80 por Kg
2. Acima de 5kg
- Morango - R$ 2.20 por Kg
- Maca    - R$ 1.50 por Kg
Se o cliente comprar mais de 8kg em frutas ou o valor total
da compra ultrapassar R$ 25.00, recebera um desconto de 10%
sobre este total. Escreva um algoritmo para ler a quantidade
(em Kg) de morangos e a quantidade (em Kg) de macas adquiridas
e escreva o valor a ser pago pelo cliente.    
"""

qtd_kg_morangos = float(input('Digite a quantidade em Kg de morangos: '))
qtd_kg_macas = float(input('Digite a quantidade em Kg de macas: '))

preco_morango = 0
preco_maca = 0

if qtd_kg_morangos <= 5:
    preco_morango = 2.5
else:
    preco_morango = 2.2

if qtd_kg_macas <= 5:
    preco_maca = 1.8
else:
    preco_maca = 1.5

total_morango = qtd_kg_morangos * preco_morango
total_maca = qtd_kg_macas * preco_maca
total_frutas = total_morango + total_maca

print('-' * 40)
print(f'Quantidade de morangos       {qtd_kg_morangos:6} Kg')
print(f'Quantidade de macas          {qtd_kg_macas:6} Kg')
print(f'Total em Kg das frutas       {qtd_kg_morangos + qtd_kg_macas:6} Kg')
print(f'Valor total das frutas        R$ {total_frutas:5.2f}')
print('-' * 40)

valor_total = total_frutas

msg = 'Valor sem desconto'
if (qtd_kg_morangos + qtd_kg_macas) > 8 or valor_total > 25:
    valor_total -= (valor_total * 10 / 100)
    msg = 'Voce recebeu um desconto de 10%'

print(f'Valor total a pagar           R$ {valor_total:5.2f}')
print('-' * 40)
print(msg)
print('-' * 40)
