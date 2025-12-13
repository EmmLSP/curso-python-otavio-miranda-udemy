"""
Exercicio 26
Faca um programa que leia o comprimento do cateto 
oposto e do cateto adjacente  de um triangulo retangulo, 
calcule e mostre o comprimento da hipotenusa.
"""

from math import hypot, sqrt, pow

cat_op_str = input('Comprimento do cateto oposto: ')
cat_op = float(cat_op_str)
cat_ad_str = input('Comprimento do cateto adjacente: ')
cat_ad = float(cat_ad_str)
print(f'A hipotenusa vai medir {hypot(cat_op, cat_ad):.2f}')
print(f'A hipotenusa vai medir {(cat_op ** 2 + cat_ad ** 2) ** (1/2):.2f}')
print(f'A hipotenusa vai medir {sqrt(pow(cat_op, 2) + pow(cat_ad, 2)):.2f}')
