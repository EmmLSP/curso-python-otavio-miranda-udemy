"""
Exercicio 013
Faca um programa que leia nome e peso de varias
pessoas, guardando tudo em uma lista. No final,
mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""

pessoa = list()
pessoas = list()
maior_peso = menor_peso = 0
while True:
    pessoa.append(input('Nome: '))
    pessoa.append(float(input('Peso: ')))
    if len(pessoas) == 0: # quando for a 1ª pessoa
        maior_peso = menor_peso = pessoa[1]
    else:
        if pessoa[1] > maior_peso:
            maior_peso = pessoa[1]
        if pessoa[1] < menor_peso:
            menor_peso = pessoa[1]
    pessoas.append(pessoa[:]) # copia de pessoa em pessoas
    pessoa.clear()
    while True:
        resp = input('Quer continuar? [S/N] ').upper()
        if resp in 'SN':
            break
        print('Entrada invalida! Digite \'S\' ou \'N\'')
    if resp == 'N':
        break

""" 
for c in range(len(pessoas)):
    if c == 0:
        maior_peso = menor_peso = pessoas[c][1]
    else:
        if pessoas[c][1] > maior_peso:
            maior_peso = pessoas[c][1]
        if pessoas[c][1] < menor_peso:
            menor_peso = pessoas[c][1] 
"""

print('-=' * 30)
print(f'Ao todo, voce cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior_peso:.1f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior_peso:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor_peso:.1f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor_peso:
        print(f'[{p[0]}] ', end='')
print()
