"""
Exercicio 33
Crie um programa que leia o nome de uma pessoa 
e diga de ela tem "SILVA" no nome.
"""

nome = input('Qual é seu nome completo? ').strip()
print(f'Seu nome tem Silva? {'SILVA' in nome.upper()}')
