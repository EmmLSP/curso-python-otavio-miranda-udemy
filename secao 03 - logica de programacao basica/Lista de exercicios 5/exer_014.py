"""
Exercicio 014
Crie um programa onde o usuario possa digitar sete
valores numericos e cadastre-os em uma lista unica
que mantenha separados os valores pares e impares.
No final, mostre os valores pares e impares em
ordem crescente.
"""

numeros = [[], []]
for c in range(1, 8):
    num = int(input(f'Digite o {c}o. valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print('-=' * 30)
print(numeros)
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores impares digitados foram: {numeros[1]}')
