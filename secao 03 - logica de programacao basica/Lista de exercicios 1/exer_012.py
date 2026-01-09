"""
Exercicio 12
Crie um programa que leia quanto dinheiro uma pessoa tem 
na cardeira e mostre quantos dolares ela pode comprar.

Considere US$1.00 = R$3.27 
"""

dinheiro_str = input('Quanto dinheiro voce tem na carteira? R$ ') 
dinheiro_real = float(dinheiro_str)
dolar = dinheiro_real / 3.27
real = dolar * 3.27
print(f'Com R${dinheiro_real:.2f} voce pode comprar USD{dolar:.2f}')
print(f'Com USD{dolar:.2f} voce pode comprar R${real:.2f}')
