"""
Exercicio 010
Faca um programa que leia o peso de cinco
pessoas. No final, mostre qual foi o maior 
e o menor peso lidos.
"""

pesos = []
maior_peso = menor_peso = 0
pesos_string = maior_peso_lido = menor_peso_lido = ''
for p in range(1, 6):
    peso = float(input(f'Peso da {p}° pessoa: (Kg) '))
    pesos.append(peso)
    if p == 1:
        maior_peso = menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

for p in range(len(pesos)):
    if pesos[p] == maior_peso:
        pesos_string += f'\033[1;32m{pesos[p]}\033[m '
    elif pesos[p] == menor_peso:
        pesos_string += f'\033[1;31m{pesos[p]}\033[m '
    else:
        pesos_string += f'\033[1;33m{pesos[p]}\033[m '

print('\nVetor de pesos:\n[', end='')
for c in range(len(pesos)):
    if c < len(pesos) - 1:
        print(f'{pesos[c]}, ', end='')
    else:
        print(f'{pesos[c]}]\n')

print(f'Pesos: {pesos_string}')
for peso in pesos:
    if peso == menor_peso:
        menor_peso_lido = f'O menor peso lido foi de {f'\033[1;31m{peso}\033[m'} Kg'
    if peso == maior_peso:
        maior_peso_lido = f'O maior peso lido foi de {f'\033[1;32m{peso}\033[m'} Kg'

print(maior_peso_lido)
print(menor_peso_lido)
