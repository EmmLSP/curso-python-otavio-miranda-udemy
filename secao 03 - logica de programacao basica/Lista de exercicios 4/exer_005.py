"""
Exercicio 005
Desenvolva um programa que leia seis numeros
inteiros e mostre a soma apenas daqueles que
forem pares. Se o valor digitado for impar,
desconsidere-o.
"""

soma = 0
numeros = ''
for c in range(1, 7):
    num = int(input(f'Digite {c} valor: '))
    if num % 2 == 0:
        soma += num
        numeros += f'\033[1;32m{num}\033[m '
    else:
        numeros += f'{num} '

print(f'Numeros: {numeros}')
print(f'Soma dos numeros pares: {soma}')
