"""
Exercicio 004
Refacao o DESAFIO da tabuado, mostrando a tabuada de um 
numero que o usuario escolher, so que agora utilizando
um laco for.
"""

num = int(input('Digite um numero para ver sua tabuada: '))
print(f'Tabuada de: {num}')
print('-' * 15)
for c in range(1, 11):
    print(f'{num} x {c:2} = {num*c:2}')
print('-' * 15)
