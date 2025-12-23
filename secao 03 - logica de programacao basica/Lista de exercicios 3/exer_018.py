"""
Exercicio 018
Faca um programa que, dado um conjunto de N numeros,
determine o menor valor, o maior valor e a soma dos
valores.
"""

numeros = int(input('Digite a quantidade de numeros: '))
numeros_str = ''
menor = maior = soma = 0
for n in range(numeros):
    num = int(input(f'Digite o {n + 1}° numero: '))
    soma += num
    numeros_str += f'{num} '
    if n == 0:
        menor = maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print('-' * 30)
print(f'numeros: {numeros_str}')
print(f'Soma dos numeros: {soma}')
print(f'Maior numero: {maior}')
print(f'Menor numero: {menor}')
