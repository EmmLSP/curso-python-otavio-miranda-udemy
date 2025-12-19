"""
Exercicio 040
Refaca o DESAFIO DOS 035 dos triangulos, 
acrescentando o recurso de mostrar que 
tipo de triangulo sera formado:

- Equilatero: todos os lados iguais
- Isosceles: dois lados iguais
- Escaleno: todos os lados diferentes 
"""

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('Os segmentos acima FORMAM um triangulo ', end='')
    if r1 == r2 and r1 == r3 and r2 == r3:
        print(' EQUILATERO')
    if (r1 == r2 and r1 != r3) or \
        (r1 == r3 and r1 != r2) or \
        (r2 == r3 and r2 != r1):
        print('ISOSCELES')
    if r1 != r2 and r1 != r3 and r2 != r3:
        print('ESCALENO')
else:
    print('Os segmentos acima NÃO FORMAM um triangulo')

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('Os segmentos acima FORMAM um triangulo ', end='')
    if r1 == r2 and r1 == r3 and r2 == r3:
        print(' EQUILATERO')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('ISOSCELES')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('ESCALENO')
else:
    print('Os segmentos acima NÃO FORMAM um triangulo')
