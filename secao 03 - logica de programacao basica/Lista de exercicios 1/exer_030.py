"""
Exercicio 30
Crie um programa que leia o nome completo de
uma pessoa e mostre:

- O nome com todas as letras maisculas
- O nome com todas as letras minusculas
- Quantas letras ao todo (sem condierar espacos)
- Quantas letras tem o primeiro nome
"""

nome = input('Digite seu nome completo: ').strip() # elimina espacos nas extremidades
dividido = nome.split()
qtd_letras = len(''.join(dividido))
print('Analizando seu nome...')
print(f'Seu nome em maisculas é {nome.upper()} ')
print(f'Seu nome em minusculas é {nome.lower()}')
print(f'Seu nome tem ao todo {qtd_letras} letras')
print(f'Seu nome tem ao todo {len(nome) - nome.count(' ')} letras')
print(f'Seu primeiro nome é {dividido[0]} e ele tem {len(dividido[0])} letras')
print(f'Seu primeiro nome é {dividido[0]} e ele tem {nome.find(' ')} letras')
