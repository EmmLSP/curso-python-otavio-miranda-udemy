"""
Exercicio 23
Faca um programa para uma loja de tintas. O programa devera 
pedir o tamanho em metros quadrados da area a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para 3 metros 
quadrados e que a tinta é vendida em latas de 18 litros, que 
custam R$ 80.00. Informe ao usuario a quantidade de latas de 
tinta a serem compradas e o preco total.
"""

metros_str = input('Digite o tamanho em metros da area a ser pintada: ')
metros = float(metros_str)
area = metros ** 2
qtd_tinta = area / 3
qtd_latas = qtd_tinta / 18
total_pago = qtd_latas * 80
print(f'A area a ser pintada é de {area:.2f} metros²')
print(f'A quantidade de tinta a ser usada é de {qtd_tinta:.2f} litros')
print(f'A quantidade de latas a serem compradas é de {qtd_latas:.2f} latas')
print(f'O total a ser pago é R${total_pago:.2f}')
