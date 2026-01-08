"""
Exercicio 04
Faca um programa que leia algo pelo teclado e mostre 
na tela o seu tipo primitivo e todas asinformações
possiveis sobre ele.
"""

algo = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(algo)}')
print(f'É um numero? {algo.isnumeric()}')
print(f'É alfabetico? {algo.isalpha()}')
print(f'É alfanumerico? {algo.isalnum()}')
print(f'Esta em maisculas? {algo.isupper()}')
print(f'Esta em minusculas? {algo.islower()}')
print(f'Esta capitalizada? {algo.istitle()}')
