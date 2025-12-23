"""
Exercicio 010
Faca um programa que receba dois numeros inteiros
e gere os numeros inteiros que estao no intervalo
compreendido entre eles.
"""

start = int(input('Digite o inicio da contagem: '))
end = int(input('Digite o final da contagem: '))

print(f'Numeros que estao no intervalo entre {start} e {end}:')

for num in range(start+1, end):
    print(f'{num} ', end='')
