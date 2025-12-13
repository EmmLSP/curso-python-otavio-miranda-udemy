"""
Exercicio 18
Escreva um programa que pergunte a quantidade de km percorridos 
por um carro alugado e a quantidade de dias pelos quais ele foi 
alugado. Calcule o preco apagar, sabendo que o carro custa R$60 
por dia e R$0.15 por km rodado.
"""

dias_str = input('Quantos dias alugados? ')
dias = int(dias_str)
km_rodados_str = input('Quantos km rodados? ')
km_rodados = int(km_rodados_str)
preco_pagar = (dias * 60) + (km_rodados * 0.15)
print(f'O total a pagar é de R${preco_pagar:.2f}')
