"""
Exercicio 11
Faca um programa que calcule a area de um quadrado,
em seguida mostre o dobro desta area para o usuario.
"""

lado_str = input('Digite a medida de lado do quadrado: ')
lado = int(lado_str)
# Area = lado * lado
area_quadr = lado * lado
print(f'A area do quadrado de lado {lado} é igual a {area_quadr} unidades²')
print(f'O dobro de {area_quadr} unidades² é igual a {area_quadr * 2} unidades²')
