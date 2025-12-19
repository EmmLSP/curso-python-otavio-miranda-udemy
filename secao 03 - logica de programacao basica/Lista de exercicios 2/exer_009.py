"""
Exercicio 009
Faca um programa que leia tres numeros e mostre-os
em ordem decrescente.
"""

from random import randint

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))

# num1 = randint(1, 20)
# num2 = randint(1, 20)
# num3 = randint(1, 20)

print('Numeros Aletorios:')
print(f'{num1}, {num2}, {num3}')

print('Ordem Decrescente:')
if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
        print(f'{num1}, {num2}, {num3}')
    else:
        print(f'{num1}, {num3}, {num2}')
elif num2 >= num1 and num2 >= num3:
    if num1 >= num3:
        print(f'{num2}, {num1}, {num3}')
    else:
        print(f'{num2}, {num3}, {num1}')
else:
    if num1 >= num2:
        print(f'{num3}, {num1}, {num2}')
    else:
        print(f'{num3}, {num2}, {num1}')
