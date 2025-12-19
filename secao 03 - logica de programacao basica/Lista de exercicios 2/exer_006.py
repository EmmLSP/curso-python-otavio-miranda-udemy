"""
Exercicio 006
Faca um programa que leia tres numeros e 
mostre o maior deles.
"""

from random import randint

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))

# num1 = randint(1, 20)
# num2 = randint(1, 20)
# num3 = randint(1, 20)

print(f'[{num1}, {num2}, {num3}]')

if num1 >= num2 and num1 >= num3:
    print(f'O maior numero é {num1=}')
elif num2 >= num1 and num2 >= num3:
    print(f'O maior numero é {num2=}')
else:
    print(f'O maior numero é {num3=}')
