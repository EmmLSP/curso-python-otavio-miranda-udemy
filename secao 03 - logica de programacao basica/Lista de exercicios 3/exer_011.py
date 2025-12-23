"""
Exercicio 011
Altere o programa anterior para mostrar no final
a soma dos numeros.
"""

start = int(input('Digite o inicio da contagem: '))
end = int(input('Digite o final da contagem: '))

print(f'Numeros que estao no intervalo entre {start} e {end}:')

soma = 0
for num in range(start + 1, end):
    soma += num
    if num < end - 1:
        print(f'{num} + ', end='')
    else:
        print(f'{num} = {soma}')
