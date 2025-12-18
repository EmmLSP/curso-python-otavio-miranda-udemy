"""
Exercicio 33
Desenvolva um programa que leia o comprimento
de tres retas e diga ao usuario se elas podem
ou nao formar um triangulo.
"""

print('-=-' * 15)
print(f'{'Analisador de Triangulos':^45}')
print('-=-' * 15)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
print('Os segmentos acima ', end='')
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('PODEM FORMAR um triangulo')
else:
    print('NÃO PODEM formar um triangulo')
