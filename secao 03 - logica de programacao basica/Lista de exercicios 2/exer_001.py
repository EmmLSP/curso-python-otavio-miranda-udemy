"""
Exercicio 001
Faca um programa que peca dois numeros e imprima 
o maior deles.
"""

try:
    num1_str = input('Digite um numero: ')
    num1 = int(num1_str)
    num2_str = input('Digite outro numero: ')
    num2 = int(num2_str)
    if num1_str and num2_str:
        if num1 > num2:
            print(f'O {num1=} é maior')
        elif num2 > num1:
            print(f'O {num2=} é maior')
        else:
            print(f'{num1=} == {num2=}')
except:
    print('Por favor, digite dois numeros inteiros')


num1_str = input('Digite um numero: ')
num2_str = input('Digite outro numero: ')
if num1_str and num2_str:
    num1 = int(num1_str)
    num2 = int(num2_str)
    if num1 > num2:
        print(f'O {num1=} é maior')
    elif num2 > num1:
        print(f'O {num2=} é maior')
    else:
        print(f'{num1=} == {num2=}')
else:
    print('Por favor, digite dois numeros inteiros')
