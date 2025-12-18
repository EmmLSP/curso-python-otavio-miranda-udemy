"""
Exercicio 23
Um posto esta vendendo combustiveis com a seguinte
tabela de descontos:
--------------------------------------------------
1. Alcool
- ate 20 litros, desconto de 3% por litro
- acima de 20 litros, desconto de 5% por litro
2. Gasolina
- ate 20 litros, desconto de 4% por litro
- acima de 20 litros, desconto de 6% por litro
--------------------------------------------------
Escreva um algoritmo que leia o numero de litros 
vendidos, o tipo de combustivel (codificado da 
seguinte forma: A-alcool, G-gasolina), calcule e 
imprima o valor a ser pago pelo cliente sabendo-se 
que o preco do litro da gasolina eR$ 2.50 e o preco 
do litro do alcool é R$ 1.90.
"""

qtd_litros = int(input('Digite a quantidade de litros vendido: '))
tipo_comb = input('Digite o tipo de combustivel [A-alcool - G-gasolina]: ').upper()

preco_gasolina = 2.50
preco_alcool = 1.90

desconto = 0
total = 0
if tipo_comb == 'A':
    if qtd_litros <= 20:
        desconto = 3
    else:
        desconto = 5
    total = qtd_litros * preco_alcool
elif tipo_comb == 'G':
    if qtd_litros <= 20:
        desconto = 4
    else:
        desconto = 6
    total = qtd_litros * preco_gasolina

total_pagar = total - (total * desconto / 100)
print(f'O valor sem desconto: R$ {total:.2f}')
print(f'O valor sem desconto: R$ {total_pagar:.2f}')
