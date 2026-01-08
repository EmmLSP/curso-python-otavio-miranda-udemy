"""
Exercicio 004
Desenvolva um programa que leia quatro valores
pelo teclado e guarde-os em uma tupla. No final,
mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posicao foi digitado o primeiro valor 3.
C) Quais foram os numeros pares.
"""

numeros = (int(input('Digite um numero: ')),
    int(input('Digite outro numero: ')),
    int(input('Digite mais um numero: ')),
    int(input('Digite o ultimo numero: ')))

print(f'Voce digitou os valores: {numeros}')

if numeros.count(9) == 1:
    print(f'O valor 9 apareceu {numeros.count(9)} vez')
elif numeros.count(9) > 1:
    print(f'O valor 9 apareceu {numeros.count(9)} vezes')
else:
    print(f'O valor 9 apareceu {numeros.count(9)} vezes')

if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1}ª posicao')
else:
    print('O numero 3 nao foi digitado em nenhuma posicao')

for pos, num in enumerate(numeros):
    if num == 3:
        print(f'O valor 3 apareceu na {pos + 1}ª posicao')
        break

if 3 not in numeros:
    print('O numero 3 nao foi digitado em nenhuma posicao')

cont_pares = 0
pares = ''
for numero in numeros:
    if numero % 2 == 0:
        pares += f'{numero} '
        cont_pares += 1

if cont_pares > 0:
    print(f'Os valores pares digitados foram {pares}')
else:
    print(f'Não apareceu em nenhum posicao um valor par')
