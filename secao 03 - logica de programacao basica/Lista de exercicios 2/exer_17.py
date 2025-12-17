"""
Exercicio 17
Faca um programa que leia um numero inteiro menor que 1000
e imprima a quantidade de centenas, dezenas e unidades do
mesmo.

Ex:326 = 3 centenas, 2 dezenas e 6 unidades
"""

numero = int(input('Digite um numero menor que 1000: '))
if 100 <= numero < 1000: 
    unidade = numero % 10 // 1
    dezena = numero % 100 // 10
    centena = numero % 1000 // 100
    print(f'{numero} = {centena} centenas, {dezena} dezenas e {unidade} unidades')
else:
    print('Numero maior ou igual a 100 e menor que 1000')
