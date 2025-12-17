"""
Exercicio 20
Faca um programa que peca um numero e informe se o
numero e inteiro ou decimal. Dica utilize funcao de
arredondamento.
"""

numero = input('Digite um numero: ')
num = 0
if numero.isdigit():
    num = int(numero)
elif numero.replace('.', '').isdigit():
    num = float(numero)
else:
    print('Nao é um numero')

if numero.isdigit() or numero.replace('.', '').isdigit():
    print(f'O numero {numero} é do tipo {type(num)}')
