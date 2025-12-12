"""
Exercicio 06
Crie um algoritmo que leia um numero e mostre
o seu dobro, triplo e raiz quadrada.
"""

from math import sqrt

numero = input('Digite um numero: ')
dobro = int(numero) * 2
triplo = int(numero) * 3
raiz_q = sqrt(int(numero))
print(f'O dobro {numero} vale {dobro}')
print(f'O triplo {numero} vale {triplo}')
print(f'A raiz quadrada de {numero} é igual a {raiz_q:.2f}')
