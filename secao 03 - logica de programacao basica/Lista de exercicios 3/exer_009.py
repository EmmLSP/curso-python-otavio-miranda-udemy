"""
Exercicio 009
Faca um programa que imprima na tela apenas os
numeros impares entre 1 e 50.
"""

print('Numeros inpares de 1 a 50:')
for num in range(1, 50, 2):
    print(f'{num} ', end='')
print()

print('Numeros inpares de 1 a 50:')
for num in range(50):
    if num % 2 != 0:
        print(f'{num} ', end='')
print()

print('Numeros inpares de 1 a 50:')
for num in range(50):
    if num % 2 == 1:
        print(f'{num} ', end='')
print()

print('Numeros inpares de 1 a 50:')
for num in range(50):
    if num % 2 == 0:
        continue
    print(f'{num} ', end='')
print()
