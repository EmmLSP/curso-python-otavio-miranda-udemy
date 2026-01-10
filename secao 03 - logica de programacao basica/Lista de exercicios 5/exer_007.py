"""
Exercicio 007
Faca um programa que leia 5 valores numericos e
guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor
digitado e as suas respectivas posicoes na lista.
"""

lista_num = list()
for pos in range(0, 5):
    lista_num.append(int(input(f'Digite um valor para a Posicao {pos}: ')))

maior = menor = 0
for pos, valor in enumerate(lista_num):
    if pos == 0:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

# version 1
print('-=' * 30)
print(f'Voce digitou os valores {lista_num}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for pos, valor in enumerate(lista_num):
    if valor == max(lista_num):
        print(f'{pos}... ', end='')
print()

print(f'O menor valor digitado foi {menor} nas posições ', end='')
for pos, valor in enumerate(lista_num):
    if valor == min(lista_num):
        print(f'{pos}... ', end='')
print()

# version 2
print('-=' * 30)
print(f'Voce digitou os valores {lista_num}')
print(f'O maior valor digitado foi {max(lista_num)} nas posições ', end='')
for pos, valor in enumerate(lista_num):
    if valor == max(lista_num):
        print(f'{pos}... ', end='')
print()

print(f'O menor valor digitado foi {min(lista_num)} nas posições ', end='')
for pos, valor in enumerate(lista_num):
    if valor == min(lista_num):
        print(f'{pos}... ', end='')
print()
