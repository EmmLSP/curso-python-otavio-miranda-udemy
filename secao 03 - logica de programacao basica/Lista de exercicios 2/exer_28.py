"""
Exercicio 28
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

par_impar = False
resultado = numero % 2 == 0
if resultado is True:
    par_impar = True
if par_impar is True:
    print(F'O numero {numero} é PAR')
else:
    print(f'O numero {numero} é IMPAR')
