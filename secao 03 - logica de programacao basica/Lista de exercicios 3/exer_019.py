"""
Exercicio 019
Altere o programa anterior para que ele aceite apenas
numeros entre 0 e 1000.
"""

while True:
    numero = int(input('Digite a quantidade de numeros: '))
    if 0 < numero <= 1000:
        break
    print('Entrada invalida! Digite numeros no intervalo entre 1 e 1000')

maior = menor = soma = 0
numeros_str = ''
for n in range(numero):
    num = int(input(f'Digite o {n + 1} numero: '))
    soma += num
    numeros_str += f'{num} '
    if n == 0:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print(f'Numeros: {numeros_str}')
print(f'Soma dos numeros: {soma}')
print(f'Maior numero: {maior}')
print(f'Menor numero: {menor}')
