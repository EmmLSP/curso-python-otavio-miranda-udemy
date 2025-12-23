"""
Exercicio 007
Faca um programa que leia 5 numeros e informe o
maior numero.
"""

maior = 0
numeros = ''
for numero in range(5):
    num = int(input(f'Digite o {numero + 1} numero: '))
    numeros += f'{num} '
    if numero == 0:
        maior = num
    elif num > maior:
        maior = num

print(f'O maior numero digitado foi: {maior}')
