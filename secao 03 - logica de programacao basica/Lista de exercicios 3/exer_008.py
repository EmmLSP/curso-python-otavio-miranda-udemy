"""
Exercicio 008
Faca um programa que leia 5 numeros e informe a
soma e a media dos numeros.
"""

soma = media = 0
numeros = range(0, 5)
numeros_str = ''
for numero in numeros:
    num = int(input(f'Digite o {numero + 1} numero: '))
    soma += num
    numeros_str += str(num) + ' '
media = soma / len(numeros)

print('numeros: ', end='')
for numero in numeros_str:
    print(numero, end='')
print()

print(f'Soma = {soma}')
print(f'Media = {media:.1f}')
