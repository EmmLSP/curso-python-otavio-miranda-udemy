"""
Exercicio 028
Crie um programa que leia um numero inteiro
e mostre na tela se ele é PAR ou ÍMPAR.
"""

numero = int(input('Me diga um numero qualquer: '))

if numero % 2 == 0:
    print(f'O numero {numero} é PAR')
else:
    print(f'O numero {numero} é IMPAR')

print(f'O numero {numero} é ', end='')
print('PAR' if numero % 2 == 0 else 'IMPAR')

resultado = numero % 2
if resultado == 0:
    print(F'O numero {numero} é PAR')
else:
    print(f'O numero {numero} é IMPAR')
