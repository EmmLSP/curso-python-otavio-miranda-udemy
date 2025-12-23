"""
Exercicio 014
Faca um programa que peca 10 numeros inteiros,
calcule e mostre a quantidade de numeros pares
e a quantidade de numeros impares.
"""

from random import randint

pares_impares = ''
pares = impares = 0
for n in range(1, 11):
    num = int(input(f'Digite o {n}° numero: '))
    # num = randint(1, 20)
    if num % 2 == 0:
        pares_impares += f'\033[1;32m{num} \033[m'
        pares += 1
    else:
        pares_impares += f'\033[1;33m{num} \033[m'
        impares += 1

print(f'Pares e Impares: {pares_impares}')
print(f'PARES = {pares}')
print(f'ÍMPARES = {impares}')
