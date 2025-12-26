"""
Exercicio 005
Desenvolva um programa que leia seis numeros
inteiros e mostre a soma apenas daqueles que
forem pares. Se o valor digitado for impar,
desconsidere-o.
"""

soma = cont_pares = 0
num_pares = ''
for c in range(1, 7):
    num = int(input(f'Digite o {c} valor: '))
    if num % 2 == 0:
        soma += num
        num_pares += f'\033[1;32m{num}\033[m '
        cont_pares += 1

print(f'Numeros PARES: {num_pares}')
print(f'Voce informou {cont_pares} numeros PARES e a soma foi {soma}')
