"""
Exercicio 21
Faca um programa que leia 2 numeros e em seguida
pergunte ao usuario qual operacao ele deseja realizar.
O resultado da operacao deve ser acompanhado de uma
frase que diga se o numero é:
- par ou impar
- positivo ou negativo
- inteiro ou decimal
"""

from math import floor

print('-' * 30)
print('(+) soma    | (-) subtracao')
print('(/) divisao | (*) multiplicacao')
print('-' * 30)
oper = input('Digite qual operacao deseja realizar? ')
if oper in '+-*/':
    num1 = int(input('Digite o primeiro numero: '))
    num2 = int(input('Digite o segundo numero: '))
    if oper == '+':
        result = num1 + num2
    elif oper == '-':
        result = num1 - num2
    elif oper == '/':
        result = num1 / num2
    elif oper == '*':
        result = num1 * num2
    print('-' * 30)
    print(f'{num1} {oper} {num2} = {result}')
    print('O resultado é ', end='')
    if result % 2 == 0:
        print('PAR')
    else:
        print('IMPAR')
    print('O resultado é ', end='')
    if result >= 0:
        print('POSITIVO')
    else:
        print('NEGATIVO')
    print('O resultado é ', end='')
    if '.' in str(result):
        print('Decimal')
    else:
        print('Inteiro')
    print('-' * 30)
else:
    print('Operacao invalida!')
