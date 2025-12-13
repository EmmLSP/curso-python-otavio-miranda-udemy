"""
Exercicio 32
Crie um programa que leia o nome de uma
cidade e diga se ela começa ou nao com o
nome "SANTO".
"""

cidade = input('Em que cidade voce nasceu? ').upper().strip()
dividido = cidade.split()
print('SANTO' == dividido[0])
