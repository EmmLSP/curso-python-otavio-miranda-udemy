"""
Exercicio 10
Faca um programa que peca o raio de um circulo,
calcule e mostre a sua area.
"""

from math import pi, pow

raio_str = input('Digite o raio de um circulo: ')
raio = float(raio_str)
# Area = PI * raio * raio
area = pi * pow(raio, 2)
print(f'A area é aproximadamente {area:.2f} unidades²')
