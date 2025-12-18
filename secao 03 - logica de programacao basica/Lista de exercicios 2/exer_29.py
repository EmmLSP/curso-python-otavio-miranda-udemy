"""
Exercicio 29
Desenvolva um programa que pergunte a distancia de
uma viagem em km. Calcule o preco da passagem, 
cobrando R$0.50 por km para viagens de ate 200 km
e R$0.45 para viagens acima de 200 km.
"""

distancia = int(input('Qual é a distancia da sua viagem? '))
preco_km = 0
print(f'Voce esta prestes a comecar uma viagem de {distancia:.1f}km.')
if distancia <= 200:
    preco_km = 0.5
else:
    preco_km = 0.45
total_pagar = distancia * preco_km
print(f'E o preco da sua passagem sera de R${total_pagar:.2f}')
